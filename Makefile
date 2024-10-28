.PHONY: build down delete_volume ruserver manage bash test apps

PREFIX ?=
FLAGS ?= --rm
DOCKER_SERVICE ?= backend

DOCKER_COMPOSE_FLAGS := ${PREFIX} docker compose

setup:
	cp .env.sample .env

stop:
	$(DOCKER_COMPOSE_FLAGS) stop $(filter-out $@,$(MAKECMDGOALS))

build:
	$(DOCKER_COMPOSE_FLAGS) build --no-cache

down:
	$(DOCKER_COMPOSE_FLAGS) down

delete_volume:
	$(DOCKER_COMPOSE_FLAGS) down -v

runserver:
	$(DOCKER_COMPOSE_FLAGS) run ${FLAGS} -it --service-ports ${DOCKER_SERVICE} sh -c "python manage.py runserver 0.0.0.0:8000"

manage:
	$(DOCKER_COMPOSE_FLAGS) run ${FLAGS} ${DOCKER_SERVICE} python manage.py $(filter-out $@,$(MAKECMDGOALS))

bash:
	$(DOCKER_COMPOSE_FLAGS) run ${FLAGS} -it ${DOCKER_SERVICE} $(filter-out $@,$(MAKECMDGOALS)) /bin/sh

%:
	@:
