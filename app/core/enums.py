from enum import Enum


class ApplicationStatus(str, Enum):
    APPLIED = "applied"
    PHONE_SCREEN = "phone_screen"
    INTERVIEWING = "interviewing"
    TECHNICAL = "technical"
    OFFER = "offer"
    REJECTED = "rejected"
    WITHDRAWN = "withdrawn"