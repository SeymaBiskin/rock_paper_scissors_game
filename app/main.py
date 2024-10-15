from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.db import engine, SessionLocal
from app.game_logic import determine_winner

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Rock Paper Scissors API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/game/start", response_model=schemas.Game)
def start_game(game: schemas.GameCreate, db: Session = Depends(get_db)):
    return crud.create_game(db=db, game=game)

@app.post("/game/play", response_model=schemas.GameResult)
def play_turn(play_data: schemas.PlayTurn, db: Session = Depends(get_db)):
    game = crud.get_game_by_id(db=db, game_id=play_data.game_id)
    
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")

    result = determine_winner(play_data.player1_choice, play_data.player2_choice)
    
    game.player1_score += 1 if result == 1 else 0
    game.player2_score += 1 if result == -1 else 0
    crud.update_game(db=db, game=game)
    
    return {"game_id": game.id, "winner": result, "player1_score": game.player1_score, "player2_score": game.player2_score}

@app.get("/game/{game_id}", response_model=schemas.Game)
def get_game(game_id: int, db: Session = Depends(get_db)):
    game = crud.get_game_by_id(db=db, game_id=game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    return game
