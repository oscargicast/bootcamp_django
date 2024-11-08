# Bootcamp Django - Sesión 2

## Setup

```sh
make setup
make build
```

## Ejecutar migraciones

```sh
make manage migrate
```

Crea un super usuario si es necesario:

```sh
make manage createsuperuser
```

## Correr el servido de forma local

```sh
make runserver
```

> [!IMPORTANT]
> Este comando no lleva el manage.py ya que es especial
> para correr el servidor de forma local puesto que
> expone el puerto 8000.