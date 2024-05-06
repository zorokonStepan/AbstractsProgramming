### Установка PowerShell (Windows)
```
    https://python-poetry.org/docs/#installing-with-the-official-installer
    
        (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -

        poetry --version    
```

### Создание проекта
```
        poetry new my-project
    
    или
    
        poetry init: если проект уже создан
```

### Подготовка виртуального окружения
```
    https://habr.com/ru/articles/740376/
    
    По умолчанию, Poetry создает виртуальные окружения в папке {cache_dir}/virtualenvs. 
    Если вы хотите, чтобы виртуальное окружение находилось в папке проекта, можно выполнить следующую команду:
    
        poetry config virtualenvs.in-project true
    
        poetry env use python3.8  # Если python3.8 есть в PATH
        poetry env use /path/to/python  # Можно указать и полный путь
```

### Установка пакетов
```
    poetry add : в [tool.poetry.dependencies]
    
    poetry add --group dev: в [tool.poetry.group.dev.dependencies]
```

### Удаление пакетов
```
    poetry remove pendulum
    poetry remove mkdocs --group docs
```

### Commands from poetry shell
```
    poetry run python --version
```
