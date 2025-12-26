from __future__ import annotations

from uuid import uuid4

from fastapi import FastAPI
from pydantic import BaseModel

from agents.orchestrator import Orchestrator

app = FastAPI(title="Agentic RAG Lab")


class AskRequest(BaseModel):
    question: str


class AskResponse(BaseModel):
    answer: str
    chosen_agent: str
    evidence: list[str]
    trace_id: str
    citations: list[str]


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/ask", response_model=AskResponse)
def ask(payload: AskRequest) -> AskResponse:
    orchestrator = Orchestrator()
    chosen_agent, result = orchestrator.route_with_choice(payload.question)
    return AskResponse(
        answer=result.answer,
        chosen_agent=chosen_agent,
        evidence=result.evidence,
        trace_id=str(uuid4()),
        citations=[],
    )
