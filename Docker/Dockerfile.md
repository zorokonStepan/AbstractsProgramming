```
    https://habr.com/ru/articles/694872/
    ENV PYTHONDONTWRITEBYTECODE 1
    ENV PYTHONUNBUFFERED 1
    
    PYTHONUNBUFFERED отвечает за отключение буферизации вывода (output). То есть непустое значение данной 
    переменной среды гарантирует, что мы можем видеть выходные данные нашего приложения в режиме реального времени.
    
    PYTHONDONTWRITEBYTECODE означает, что Python не будет пытаться создавать файлы .pyc
```
