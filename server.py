from flask import Flask
import asyncio

app = Flask(__name__)


@app.route("/hello")
async def hello():
    await asyncio.sleep(30)
    return {"message": "minelo 30s"}


@app.route("/hello2")
async def hello2():
    return {"message": "Hello, World!"}


if __name__ == "__main__":
    app.run()
