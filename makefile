SHELL := /bin/bash
.DEFAULT_GOAL := help
DOCKER_COMPOSE := docker-compose
DOCKER := docker exec -it snappy-app
POETRY_CMD := poetry run

.PHONY: help scaffold alembic start build stop container migration  migrate pre-commit pre-commit-install pre-commit-update pylint-generate lint test flake black isort autoflake pylint

help:
	@echo "Snappy"
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
	$(POETRY_CMD) alembic init migrations

start: ## Start all containers
	$(DOCKER_COMPOSE) up -d

build: ## Build all containers without detach
	$(DOCKER_COMPOSE) up --build

stop: ## Stop all containers
	$(DOCKER_COMPOSE) down

container: ## Enter the container
	$(DOCKER) bash

migration: ## Create a migration
	$(POETRY_CMD) alembic revision --autogenerate -m "$(message)"

migrate: ## Run migration
	$(POETRY_CMD) alembic upgrade head

pre-commit: ## Run pre-commit
	$(POETRY_CMD) pre-commit run --all-files

pre-commit-install: ## Install pre-commit
	$(POETRY_CMD) pre-commit install

pre-commit-update: ## Update pre-commit
	$(POETRY_CMD) pre-commit autoupdate

pylint-generate: ## Generate pylint file
	$(POETRY_CMD) pylint --generate-rcfile > .pylintrc

lint: flake black isort autoflake pylint ## Run all linting tools

test: ## Run Pytest inside the Docker container
	$(DOCKER) $(POETRY_CMD) pytest

flake: ## Run Flake8
	@echo "Running flake tools..."
	@$(POETRY_CMD) flake8 app

black: ## Run Black
	@echo "Running black tools..."
	@$(POETRY_CMD) black app

isort: ## Run Isort
	@echo "Running isort tools..."
	@$(POETRY_CMD) isort app

autoflake: ## Run Autoflake
	@echo "Running autoflake tools..."
	@$(POETRY_CMD) autoflake app

pylint: ## Run Pylint
	@echo "Running pylint tools..."
	@$(POETRY_CMD) pylint app --recursive=y
