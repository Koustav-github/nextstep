from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base import Base
from sqlalchemy.orm import relationship

class Goal(Base):

    __tablename__ = "goal"

    id = Column(Integer, primary_key=True)

    title = Column(String)

    user_id = Column(Integer, ForeignKey("user.id"))

    user = relationship("User", back_populates="goal")

    task = relationship("Task", back_populates="goal")