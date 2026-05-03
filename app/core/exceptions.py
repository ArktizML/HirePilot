class HirePilotError(Exception):
    """Base exception for all HirePilot errors."""

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)


class NotFoundError(HirePilotError):
    """Raised when a requested resource does not exist."""


class ConflictError(HirePilotError):
    """Raised when an operation conflicts with existing data."""


class ValidationError(HirePilotError):
    """Raised when business-level validation fails (beyond Pydantic)."""