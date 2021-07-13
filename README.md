# Instructions

## Frontend

```
cd app
```

### Project setup

```
yarn install
```

### Compiles and hot-reloads for development

```
yarn dev
```

## Backend

Before continue install Task [https://taskfile.dev/#/installation] and Poetry [https://python-poetry.org/docs/#installation]

```
brew install go-task/tap/go-task
```

```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

```
cd backend
```

### Init environment

```
task init_env
```

### Install dependencies

```
task install_dependencies
```

### Run server

```
task run
```

### Run tests

```
task tests
```
