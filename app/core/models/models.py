# db models

import datetime

from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, MetaData
from sqlalchemy.orm import relationship
from app.core.models import Base


class Referrer(Base):
    __tablename__ = "referrers"

    id: int = Column(Integer, primary_key=True, index=True)
    referral_code: str = Column(String, index=True, nullable=True)
    referral_code_created: DateTime = Column(DateTime, default=datetime.datetime.now)
    referral_code_expire: DateTime = Column(DateTime)
    email: str = Column(String, nullable=True)

    referral = relationship("Referral", uselist=False, back_populates="referrer")


class Referral(Base):
    __tablename__ = "referrals"

    id: int = Column(Integer, primary_key=True, index=True)
    referral_code: str = Column(String, index=True, nullable=False)
    referrer_id: int = Column(Integer, ForeignKey("referrers.id"), nullable=False)
    referred_email: str = Column(String, nullable=False)
    created_at: DateTime = Column(DateTime, default=datetime.datetime.utcnow)

    referrer = relationship("Referrer", back_populates="referral")
