from pydantic import BaseModel


class ParsedJobData(BaseModel):
    skills: list[str]
    seniority: str
    salary_min: int | None = None
    salary_max: int | None = None
    remote: bool = False