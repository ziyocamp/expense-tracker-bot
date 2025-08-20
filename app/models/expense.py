import enum

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum, Float
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class Category(enum.Enum):
    food = "Ovqatlanish"
    transport = "Transport"
    rent = "Ijara"
    other = "Boshqa"


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    category = Column(Enum(Category), default=Category.other)
    amount = Column(Float, nullable=False)
    note = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.now)

    # --- Relationships ---
    user = relationship("User", back_populates="expenses")

    def __repr__(self) -> str:
        return f"<Expense id={self.id} amount={self.amount}>"

