### создание и запуск миграций
```
    alembic revision --autogenerate -m "message"
    alembic upgrade head
```

### откатить последнюю миграцию
```
    alembic downgrade head-1
```