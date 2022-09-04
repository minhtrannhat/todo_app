#!/bin/bash
docker-compose build &&
docker-compose run api alembic upgrade head &&
docker-compose up -d
