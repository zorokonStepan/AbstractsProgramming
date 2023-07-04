```
    docker build  - собрать образ
    docker run    - запустить образ
    docker commit - сохранить контейнер в качестве образа
    docker tag    - присвоить тег образу 
```

```
    sudo service docker restart - перезапуск
    service docker status -       проверка работы
    
```

https://routerus.com/how-to-remove-docker-images-containers-volumes-and-networks/
### Удаление контейнеров Docker
```
    docker container ls -a                                - получить список всех контейнеров 
    docker container rm id_container_1 ... id_container_N - удалить контейнер(ы)
    docker container prune                                - удалить все остановленные контейнеры
```

### Удаление образов Docker
```
    docker image ls 
    docker image rm 75835a67d134 2a4cca5ac898
```

```
    docker build . -t my-image
```
