
# Rock, Paper, Scissors API

This project implements a simple "Rock, Paper, Scissors" game using FastAPI as the backend. The game allows two players (or one player vs a computer) to compete, with the results stored in a SQLite database.

## Features
- Create a new game between two players.
- Simulate a turn of Rock, Paper, Scissors.
- Track and update scores.
- Save and retrieve game state from a database.
- OpenAPI support for API documentation.

## API Endpoints

1. **Start Game** (POST `/game/start`)
    - Request Body: 
      ```json
      {
          "player1": "Player1 Name",
          "player2": "Player2 Name or 'Computer'"
      }
      ```
    - Response: 
      ```json
      {
          "id": 1,
          "player1": "Player1 Name",
          "player2": "Player2 Name",
          "player1_score": 0,
          "player2_score": 0
      }
      ```

2. **Play Turn** (POST `/game/play`)
    - Request Body:
      ```json
      {
          "game_id": 1,
          "player1_choice": "rock",
          "player2_choice": "scissors"
      }
      ```
    - Response: 
      ```json
      {
          "game_id": 1,
          "winner": 1,
          "player1_score": 1
      }
