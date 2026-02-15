from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base import Base
from sqlalchemy.orm import relationship



class Task(Base):

    __tablename__ = "task"

    id = Column(Integer, primary_key=True)

    title = Column(String)

    goal_id = Column(Integer, ForeignKey("goal.id"))

    goal = relationship("Goal", back_populates="task")