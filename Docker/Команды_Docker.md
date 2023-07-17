https://tretyakov.net/post/shpargalka-po-komandam-docker/
https://routerus.com/how-to-remove-docker-images-containers-volumes-and-networks/

```
    docker build  - собрать образ
    docker run    - запустить контейнер
    docker stop   - остановить контейнер
    docker commit - сохранить контейнер в качестве образа
    docker tag    - присвоить тег образу 
    docker rm     - удалить контейнер(ы)
    docker rmi    - удалить образ(ы)
    docker pull   - скачать образ с DockerHub
    docker exec   - выполнить команды внутри контейнера
```

```
    sudo service docker restart - перезапуск
    service docker status -       проверка работы
    
```

### работа с образами Docker
```
    docker images                     - вывести все образы docker
    docker image ls                   - вывести все образы docker 
    docker image rm image_id image_id - удалить образы
```

### работа с контейнерами Docker
```
    docker ps -a                 - выводит список всех контейнеров и информацию о них
    docker ps                    - выводит список всех запущенных контейнеров и информацию о них    
    docker ps -f "status=exited" - выводит список всех остановленных контейнеров и информацию о них
    docker ps -a -q              - выводит только id всех контейнеров
    
    docker container ls -a                                - получить список всех контейнеров 
    
    docker container rm id_container_1 ... id_container_N - удалить контейнер(ы)
    docker container prune                                - удалить все остановленные контейнеры
```

### работа с volumes Docker
```
    docker volume ls         - выводит список всех volume docker
    docker volume create имя - создать docker volume    
```

### docker commands
```
    docker build .                   # . - это путь к Dockerfile
    docker tag 66c76cea05bb todoapp  # переименование образа по id в имя_тега=todoapp
```


### запуск контейнера docker
```
    docker run -i -t -p 8000:8000 --name example1 todoapp
        -i 
        -t
        -p 8000:8000  # перенаправляет порт контейнера 8000 в порт 8000 на хост-компьютере
        --name        # присваивает контейнеру уникальное имя
        todoapp       # это образ
```
```
    docker run -d -i -p 1234:1234 --name daemon ubuntu:14.04 nc -l 1234
        -d      # запускает контейнер в качестве демона
        -i      # дает этому контейнеру возможность взаимодействовать с вашим сеансом Telnet
        -p      # вы «публикуете» порт 1234 из контейнера на хост
        --name  # позволяет присвоить контейнеру имя, чтобы вы могли обратиться к нему позже
        В конце вы запускаете простой прослушивающий эхо-сервер на порту 1234 с помощью netcat (nc).
```

### docker run--restart
```
    docker run -d --restart=no                      # Не перезапускать при выходе контейнера
    docker run -d --restart=always                  # Всегда перезапускать при выходе контейнера
    docker run -d --restart=unless-stopped          # Всегда перезагружать, но помнить о явной остановке
    docker run -d --restart=on-failure[:max-retry]  # Перезапускать только в случае сбоя
```

### флаги docker run
```
    -p host_port: container_port   # пробросить порты
    -d                             # запустить контейнер в фоне
    --rm                           # удалить сразу после остановки
    -e TZ=Europe/Moscow            # переменная окружения
    -v abspath_host:abspath_docker # прикрутить папку к docker container
    -v name_volume:abspath_docker  # прикрутить volume к docker container
```

### флаги docker build
```
    -t  # tag // название образа 
```

```
    docker build . -t my-image
    docker build -t my-image pathDockerfile
    docker run --rm my-image
    docker run -t -i my-image /bin/bash
    
    docker run --rm --name web -p 8080:8080 web-hello
    docker run --rm --name web -p 8080:8080 -v name_volume:/user/src/app/folder web-hello
```

