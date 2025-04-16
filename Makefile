.DEFAULT_GOAL := help

run: ## Run the application using uvicorn with provided arguments or default
	poetry run uvicorn main:app --host 0.0.0.0 --port 8000 --reload --env-file .local.env

install: ## Install the dependency using poetry
	@echo "Installing dependency $(LIBRARY)"
	poetry add $(LIBRARY)

uninstall: ## Install the dependency using poetry
	@echo "Uninstalling dependency $(LIBRARY)"
	poetry remove $(LIBRARY)

makemigrations: ## Create migrations
	poetry run alembic revision --autogenerate

migrate: ## Migrate migrations
	poetry run alembic upgrade head

help: ## Show this help message
	@echo "Usage: make [command]"
	@echo ""
	@echo "Commands:"
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?##"}; {printf "  %-20s %s\n", $$1, $$2}'

