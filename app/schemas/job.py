from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, field_validator


class JobBase(BaseModel):
    title: str
    company: str
    location: Optional[str] = None
    url: Optional[str] = None
    raw_description: Optional[str] = None


class JobCreate(JobBase):
    title: str
    company: str

    @field_validator("title", "company")
    @classmethod
    def must_not_be_blank(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Field must not be blank")
        return v.strip()


class JobUpdate(BaseModel):
    title: Optional[str] = None
    company: Optional[str] = None
    location: Optional[str] = None
    url: Optional[str] = None
    raw_description: Optional[str] = None

    @field_validator("title", "company", mode="before")
    @classmethod
    def must_not_be_blank(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and not v.strip():
            raise ValueError("Field must not be blank")
        return v.strip() if v else v


class JobRead(JobBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None