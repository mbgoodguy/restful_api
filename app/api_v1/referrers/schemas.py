# pydantic models
from pydantic import BaseModel, EmailStr, ConfigDict


class ReferrerBase(BaseModel):
    username: str
    email: EmailStr


class Referrer(ReferrerBase):
    model_config = ConfigDict(from_attributes=True)  # берем св-ва из атрибутов

    id: int = None


class ReferrerCreate(ReferrerBase):
    pass
