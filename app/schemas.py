from pydantic import BaseModel

class GameBase(BaseModel):
    player1: str
    player2: str

class GameCreate(GameBase):
    pass

class Game(GameBase):
    id: int
    player1_score: int
    player2_score: int

    class Config:
        orm_mode = True

class PlayTurn(BaseModel):
    game_id: int
    player1_choice: str
    player2_choice: str

class GameResult(BaseModel):
    game_id: int
    winner: int
    player1_score: int
    player2_score: int
