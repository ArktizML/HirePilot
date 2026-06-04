from app.services.parsing_service import ParsingService


def test_parse_returns_structured_data():
    service = ParsingService()
    result = service.parse("We are looking for a Python developer...")
    assert isinstance(result.skills, list)
    assert len(result.skills) > 0
    assert result.seniority is not None