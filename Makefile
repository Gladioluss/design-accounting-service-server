#!/usr/bin/make

include .env

run-docker-compose:
	docker compose -f docker-compose.yaml up -d --build

stop-docker-compose:
	docker compose -f docker-compose.yaml down

run-database:
	docker compose -f docker-compose.yaml up -d db

stop-database:
	docker compose -f docker-compose.yaml down db

yoyo-init:
	yoyo init --database postgresql+psycopg://$(DATABASE_USER):$(DATABASE_PASSWORD)@$(DATABASE_HOST):$(DATABASE_PORT)/$(DATABASE_NAME) migrations

run-app:
	uvicorn src.main:app --reload --port $(APP_PORT)

	
lint:
	ruff check src