from pydantic import BaseModel


class Meeting(BaseModel):
    date: str
    start: str
    end: str
    desc: str
