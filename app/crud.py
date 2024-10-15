from sqlalchemy.orm import Session
from app import models, schemas

def create_game(db: Session, game: schemas.GameCreate):
    db_game = models.Game(player1=game.player1, player2=game.player2)
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game

def get_game_by_id(db: Session, game_id: int):
    return db.query(models.Game).filter(models.Game.id == game_id).first()

def update_game(db: Session, game: models.Game):
    db.commit()
    db.refresh(game)
    return game
