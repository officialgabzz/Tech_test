# Backend
You can run using either Poetry or Docker

## Setup
1. update .env_loca file with your gpt API key

## Requiremnt
1. Docker or Poetry

## Run with Poetry
`poetry run api`

## Run with Docker
1. `docker build -t be-api . --no-cache`
2. `docker run -p 8002:8002 be-api`