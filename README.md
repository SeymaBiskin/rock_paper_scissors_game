
# Rock, Paper, Scissors API

This project implements a simple "Rock, Paper, Scissors" game using FastAPI as the backend. The game allows two players (or one player vs a computer) to compete, with the results stored in a SQLite database.

## Features
- Create a new game between two players.
- Simulate a turn of Rock, Paper, Scissors.
- Track and update scores.
- Save and retrieve game state from a database.
- OpenAPI support for API documentation.

## Prerequisites

Make sure you have the following installed on your machine:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Setup and Running the Application

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/rock-paper-scissors-api.git
    cd rock-paper-scissors-api
    ```

2. **Build the Docker image**:

    Use Docker to build the image for the FastAPI application. This step creates a Docker image for the FastAPI backend and sets up the environment.

    ```bash
    docker-compose build
    ```

3. **Run the Docker containers**:

    Once the image is built, start the application using Docker Compose:

    ```bash
    docker-compose up
    ```

4. **Apply Database Migrations**:

    The project uses Alembic for database migrations. To set up the database (SQLite), apply the migrations as follows:

    ```bash
    docker-compose exec web alembic upgrade head
    ```

    This will create the necessary tables in the SQLite database.

5. **Access the Application**:

    Once the containers are up and running, you can access the FastAPI application at:

    ```
    http://localhost:8000
    ```

## Accessing the OpenAPI Documentation

FastAPI automatically generates OpenAPI documentation for the API. You can access it via the following URLs:

```
http://localhost:8000/docs
```

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
