# db models

import datetime

from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Referrer(Base):
    __tablename__ = "referrers"

    id = Column(Integer, primary_key=True, index=True)
    referral_code = Column(String, index=True, nullable=True)
    referral_code_created = Column(DateTime, default=datetime.datetime.now())
    referral_code_expire = Column(DateTime)
    email = Column(String, nullable=True)

    referral = relationship("Referral", uselist=False, back_populates="referrer")


class Referral(Base):
    __tablename__ = "referrals"

    id = Column(Integer, primary_key=True, index=True)
    referral_code = Column(String, index=True, nullable=False)
    referrer_id = Column(Integer, ForeignKey("referrers.id"), nullable=False)
    referred_email = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    referrer = relationship("Referrer", back_populates="referral")
