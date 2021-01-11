ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
$(eval $(ARGS):;@:)
MAKEFLAGS += --silent
RUN_WEB = docker-compose run --rm -w /code web
EXEC_WEB = docker-compose exec web
RUN_BOT = docker-compose run --rm -w /code bot
EXEC_WEB = docker-compose exec bot

# HELP COMMANDS
help: ## show this help
	@echo 'usage: make [target] [option]'
	@echo ''
	@echo 'Common sequence of commands:'
	@echo '- make build [nocache]'
	@echo '- make init'
	@echo '- make run'
	@echo '- make test [unit | integration]'
	@echo '- make lint'
	@echo '- make bandit'
	@echo '- make audit'
	@echo '- make bump [major | minor | patch(default)]'
	@echo ''
	@echo 'targets:'
	@egrep '^(.+)\:\ .*##\ (.+)' ${MAKEFILE_LIST} | sed 's/:.*##/#/' | column -t -c 2 -s '#'

.PHONY : build
build: ## build application containers
ifeq ($(ARGS), nocache)
	@ docker-compose build --no-cache
else
	@ docker-compose build
endif

init: ## build containers and run fixtures
	@ make run
	@ $(EXEC) sh -c "ls apps/**/fixtures/*.json | xargs -I {} python manage.py loaddata {}"

.PHONY : run
run: ## start the application
	@ docker-compose -f ../docker-compose.yml up -d db
	@ docker-compose up -d

.PHONY : test
test: ## run the application tests
ifeq ($(ARGS), unit)
	@ $(RUN_WEB) python manage.py test tests.unit
	@ $(RUN_BOT) py.test tests.unit
else ifeq ($(ARGS), integration)
	@ $(RUN_WEB) python manage.py behave --no-capture tests.integration
else
	make test integration
	make test unit
endif

.PHONY: lint
lint: ## run linters over the code
	@ $(RUN_WEB) /bin/sh -c "isort . && black . && flake8"
	@ $(RUN_BOT) /bin/sh -c "isort . && black . && flake8"

.PHONY: bandit
bandit: ## run bandit security linter
	@ $(RUN_WEB) bandit
	@ $(RUN_BOT) bandit

.PHONY: audit
audit: build ## run package auditor
	@ $(RUN_WEB) safety check --full-report
	@ $(RUN_BOT) safety check --full-report

.PHONY: shell
shell: run ## run application's shell
	@ $(EXEC_WEB) python manage.py shell

.PHONY: bump
bump: ## increase package version
	@ $(RUN) python -m "bump" --$(ARGS)
	@ git add setup.py
	@ git commit -n -m "chore: update pkg version"
	@ git push -u
