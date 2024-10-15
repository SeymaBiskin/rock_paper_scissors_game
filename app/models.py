from sqlalchemy import Column, Integer, String
from app.db import Base

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    player1 = Column(String, index=True)
    player2 = Column(String, index=True)
    player1_score = Column(Integer, default=0)
    player2_score = Column(Integer, default=0)
