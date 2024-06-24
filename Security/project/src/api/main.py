import traceback

from bson import ObjectId
import fastapi
import jwt
import requests
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi_keycloak_middleware import KeycloakConfiguration, setup_keycloak_middleware
from models import Meeting
from pymongo import MongoClient

app = FastAPI()

client = MongoClient("mongodb", 27017)
db = client["meetings_db"]
blogs = db.get_collection("meetings")


keycloak_url = "http://keycloak:8080/"
keycloak_config = KeycloakConfiguration(
    url=keycloak_url,
    realm="test",
    client_id="fastapi",
    client_secret="587NlFvGdOd2zMBbwozFksVuE3FU4dFL",
    claims=["name", "email"],
    reject_on_missing_claim=False,
)

setup_keycloak_middleware(
    app,
    keycloak_configuration=keycloak_config,
)


@app.middleware("http")
async def role_getter(request: Request, call_next):
    try:
        auth_header = request.headers["Authorization"]
    except Exception:
        return JSONResponse({"details": "Auth header missing"}, 401)

    try:
        token = auth_header.split(" ")[1]
        options = {"verify_signature": True, "verify_aud": False, "exp": True}
        public_key = requests.get(f"{keycloak_url}realms/test").json()["public_key"]
        public_key = (
            f"-----BEGIN PUBLIC KEY-----\n{public_key}\n-----END PUBLIC KEY-----"
        )
        decoded = jwt.decode(token, public_key, algorithms=["RS256"], options=options)

    except Exception:
        traceback.print_exc()
        return JSONResponse({"details": "Not authorized"}, 401)

    request.state.name = decoded["name"]
    request.state.roles = decoded["realm_access"]["roles"]

    res = await call_next(request)

    return res


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_current_user_roles(request: fastapi.Request) -> list:
    return request.state.roles


def has_role(required_role: str):
    def role_checker(roles=Depends(get_current_user_roles)):
        if required_role in roles:
            return True
        raise HTTPException(status_code=403, detail="Forbidden: Insufficient role")

    return role_checker


@app.get("/meetings")
def get_meetings():
    meetings = list(blogs.find())

    for meeting in meetings:
        meeting["id"] = str(meeting["_id"])
        meeting["_id"] = None
    return meetings


@app.post("/meetings/add")
async def add_meeting(meeting: Meeting):
    new_meeting = meeting.model_dump()
    result = blogs.insert_one(new_meeting)
    new_meeting["id"] = str(result.inserted_id)

    del new_meeting["_id"]

    return new_meeting


@app.delete("/meetings/{meeting_id}", dependencies=[Depends(has_role("admin"))])
async def delete_meeting(meeting_id: str):
    result = blogs.delete_one({"_id": ObjectId(meeting_id)})
    if result.deleted_count == 1:
        return {"message": "Meeting deleted"}
    else:
        return {"message": "Meeting not found"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5000)
