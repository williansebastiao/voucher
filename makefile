SHELL := /bin/bash
.DEFAULT_GOAL := help
DOCKER_COMPOSE := docker-compose
DOCKER := docker exec -it voucher_app
POETRY_CMD := poetry run

.PHONY: help scaffold alembic start build stop container migration  migrate pylint-generate lint test flake black isort autoflake pylint

help:
	@echo "Voucher"
	@echo "---------------------"
	@echo "Usage: make <command>"
	@echo ""
	@echo "Commands:"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  \033[36m%-26s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

scaffold: ## Start config to project
	@if [ ! -e .env ]; then \
		cp .env.example .env; \
	fi
	poetry update

alembic: ## Start alembic
	poetry run alembic init migrations

start: ## Start all containers
	$(DOCKER_COMPOSE) up -d

build: ## Build all containers without detach
	$(DOCKER_COMPOSE) up --build

stop: ## Stop all containers
	$(DOCKER_COMPOSE) down

container: ## Enter the container
	$(DOCKER) bash

migration: ## Create a migration
	poetry run alembic revision --autogenerate -m "$(message)"

migrate: ## Run migration
	poetry run alembic upgrade head

pylint-generate: ## Generate pylint file
	poetry run pylint --generate-rcfile > .pylintrc

lint: flake black isort autoflake pylint mypy ## Run all linting tools

test: ## Run Pytest inside the Docker container
	poetry run pytest tests

flake: ## Run Flake8
	@echo "Running flake tools..."
	poetry run flake8 app

black: ## Run Black
	@echo "Running black tools..."
	poetry run black app

isort: ## Run Isort
	@echo "Running isort tools..."
	poetry run isort app

autoflake: ## Run Autoflake
	@echo "Running autoflake tools..."
	poetry run autoflake app

pylint: ## Run Pylint
	@echo "Running pylint tools..."
	poetry run pylint app --recursive=y

mypy: ## Run Mypy
	@echo "Running mypy tools..."
	poetry run mypy app
