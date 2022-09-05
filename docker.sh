#!/bin/bash
if [[ "$1" == *"prune"* ]]; then
    echo 'Remove all containers and volumes'
    docker compose rm -vfs &&
    docker volume rm todo_postgres_data || true
  else
    echo 'Building docker containers' &&
    docker-compose build &&
    echo 'Running migrations' &&
    docker-compose run api alembic upgrade head &&
    echo 'Getting containers up' &&
    docker-compose up -d
fi
