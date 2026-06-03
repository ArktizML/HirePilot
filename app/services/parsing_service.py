from app.schemas.parsing import ParsedJobData


class ParsingService:
    def parse(self, raw_description: str) -> ParsedJobData:
        """
        Parses a raw job description into structured data.
        Currently returns mock data — AI integration planned.
        """
        return ParsedJobData(
            skills=["Python", "FastAPI", "PostgreSQL"],
            seniority="mid",
            salary_min=8000,
            salary_max=14000,
            remote=True,
        )