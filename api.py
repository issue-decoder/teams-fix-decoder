from fastapi import FastAPI
from pydantic import BaseModel

from src.parser import parse_fix, summarize_fix

app = FastAPI()


class FixRequest(BaseModel):
    message: str


@app.post("/decode")
def decode_fix(req: FixRequest):
    parsed = parse_fix(req.message)
    summary = summarize_fix(parsed)

    return {
        "parsed": parsed,
        "summary": summary
    }
