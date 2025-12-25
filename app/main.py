from __future__ import annotations

from uuid import uuid4

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="Agentic RAG Lab")


class AskRequest(BaseModel):
    question: str


class AskResponse(BaseModel):
    answer: str
    citations: list[str]
    trace_id: str


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/ask", response_model=AskResponse)
def ask(payload: AskRequest) -> AskResponse:
    _ = payload.question
    return AskResponse(
        answer="더미 답변",
        citations=["더미 출처 1", "더미 출처 2"],
        trace_id=str(uuid4()),
    )
