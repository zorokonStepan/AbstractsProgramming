Запустить в контейнере образ nginx, скачав его с удаленного репозитория
`docker run --rm -p 8080:80 --name nginx-compose nginx`

Запустить в контейнере образ nginx, скачав его с удаленного репозитория и примонтировать каталог с файлом
`docker run --rm -p 8080:80 --name nginx-compose -v $(pwd)/static-site:/usr/share/nginx/html nginx`

### Тоже самое, но с помощью Docker Compose

```
    docker-compose.yml который устанавливает NGINX(пробелы важны):
    
    services:
        nginx:
            image: nginx
            ports:
            - 8080:80
```

```
    docker-compose.yml который устанавливает NGINX с примонтированным файлом:
    
    services:
        nginx:
            image: nginx
            ports:
            - 8080:80
            volumes:
            - ./static-site:/usr/share/nginx/html
```
