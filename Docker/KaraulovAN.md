https://medium.com/nuances-of-programming/%D0%BC%D0%BE%D1%89%D0%BD%D0%B5%D0%B9%D1%88%D0%B8%D0%B9-%D1%81%D0%BF%D0%B8%D1%81%D0%BE%D0%BA-%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4-%D0%B2-docker-b2a22747de12 - отличная статья. Но открывать надо через VPN.
https://www.youtube.com/watch?v=QF4ZF857m44 - отличный ролик по основам.

**ВАЖНО!**
Образ (image) - то, что собирается с помощью Dockerfile.
Контейнер (container) - то, что запускается на основе образа.

**Команды:**
1. Список всех запущенных контейнеров, включая завершившие внутренний процесс, но не удалившиеся (т.е. запущенные без ключа --rm в команде docker run...)
`docker ps -a`

2. Список образов, зарегистрированных в локальном реестре Docker на конкретной машине:
`docker images` или `docker images ls`

3. История построения конкретного образа
`docker history <IMAGE_ID>`

4. Текущий консольный лог контейнера
`docker logs <CONTAINER_NAME|CONTAINER ID>`

5. Полезная для дебага информация об образе/контейнере
`docker inspect <IMAGE_ID|CONTAINER ID>`

6. Показывает используемую на хосте версию клиента и сервера Docker.
`docker version`

**ВАЖНО! В командах, которые требуют указания конкретного объекта для работы (IMAGE или CONTAINER) - можно использовать как IMAGE_ID|CONATINER_ID, так и IMAGE_NAME|CONTAINER_NAME.**

**Отличие команд run и start в Docker в следующем.**
run запустит образ, и/или предварительно его извлечет из Docker Hub, если не обнаружит его в локальном реестре.
start только запустит уже имеющийся локально контейнер.

7. Извлечь образ из удаленного реестра, не запуская (после этой команды образ окажется в локальном реестре Docker):
`docker pull registry.techzone.spb.ru/kenton050`
7a. Отправить образ в удаленный реестр:
`docker push registry.techzone.spb.ru/kenton050`

**Команды для исследования volumes:**
https://docs.docker.com/engine/reference/commandline/volume_create/ - смотреть ближе к концу, там список относящихся к делу команд.
`docker volume ls` - список имеющихся вольюмов
`docker volume create my_volume_name` - создать вольюм с именем my_volume_name

8. Выполнить команду внутри контейнера:
`docker exec -ti <CONTAINER_ID> [COMMAND]`
Например, `docker exec -ti 6088b0206dce /bin/bash` - и ты получаешь командную строку внутри своего контейнера. Дальше можно исполнять любые Linux-команды, ls, cat и прочие.

9. Как найти контейнер, использующий конкретный вольюм:
`docker ps -a --filter volume=VOLUME_NAME_OR_MOUNT_POINT`

10. Удалить ненужный образ:
`docker image rm <IMAGE_ID>`

11. Если один IMAGE_ID соответствует разным тэгам (TAG) репозитория, то такой образ не удалить, сначала нужно убрать не нужный тэг:
`docker rmi <REPOSITORY_NAME/IMAGE_NAME:TAG>` (или просто <IMAGE_NAME:TAG>).

12. Инспекция вольюмов в контейнере:
`docker inspect --format="{{.Mounts}}" <CONTAINER_ID>`

13. Рестартовать контейнер:
`docker restart <CONTAINER_ID>`

14. Посмотреть открытые контейнером порты:
`docker port <CONTAINER_ID>`

15. Статистика и мониторинг контейнеров:
`docker stats <CONTAINER_ID>`

**Логгирование контейнеров**
https://docs.docker.com/config/containers/logging/configure/ - офдок.
https://sandro-keil.de/blog/logrotate-for-docker-container/ - logrotate внутри контейнера.
https://williamdurand.fr/2014/12/17/elasticsearch-logstash-kibana-with-docker/ - ELK
http://jasonwilder.com/blog/2014/03/17/docker-log-management-using-fluentd/ - fluentd
https://xakep.ru/2016/02/04/docker-utilites/ - хорошая статья. Начинается с мониторинга контейнеров, а далее про отличные плюшки.

**Docker Compose**
Начиная с современных версий (на МАСОНе, например) команды Compose пишутся без дефиса. Например, `docker compose up`. Здесь же даются команды старых версий, типа как на BARRYMORE.
https://docs.docker.com/compose/compose-file/compose-file-v3/ - офдок, начало для погружения.

**ВАЖНО**
Если нет каких-то ~~сектантских~~ особых предпочтений, все файлы типа docker-compose.yml должны находиться в подкаталогах каталога Linux - `/usr/local/bin`. Рядом с ними должны находиться файлы/каталоги, содержащие данные, необходимые для запускаемых этим docker-compose.yml-файлом контейнеров.

Подавать команды `docker-compose` надо в папке, где лежит .yml-файл.
`docker-compose start` - запустить описанное в файле yml.
`docker-compose stop` - остановить ранее запущенное этим yml-файлом. *Интересный факт: можно поменять версии образов в yml-файле, остановить, и сразу запустить снова, но уже с новыми образами (используется при замене контейнеров ФК).*
`docker-compose up` - создать все контейнеры из образов, описанных в yml-файле, и запустить. Контейнеры займут консоль, в которой ты их запустил и будут выводить консольный лог всех запущенных из этого yml-файла контейнера. Остановить их можно, нажав Ctrl+C. Это аналогично `docker-compose stop`.
`docker-compose up -d` - аналогично верхнему, но контейнеры перейдут в режим демона, освобождая твою консоль для дальнейших команд.
`docker-compose down` - остановить и/или разрушить все контейнеры, созданные из yml-файла. С самим yml-файлом все будет хорошо. Это бывает полезно для вычистки т.н. слоев контейнеров (хранятся по пути `/var/lib/docker/overlay2`).

Compose, при установке переменных окружения по умолчанию ищет файл типа .env рядом с yml-файлом. И из него берет переменные окружения для запускаемых контейнеров. Далее, подставляет их по ссылкам типа ${VARIABLE}, используемых в yml-файле.

**ВАЖНО** Для каждого yml-файла в .env-файле д.б. хотя бы переменная DOCKER_COMPOSE_PROJECT='...'! Иначе запущенные контейнеры станут "сиротками" (orphaned) и будут выключаться любой командой docker-compose stop|down и т.д.
https://docs.docker.com/compose/env-file/ - офдок
https://stackoverflow.com/questions/29377853/how-to-use-environment-variables-in-docker-compose

Статья от человека, ненавидящего Docker:
https://habr.com/ru/post/467607/ - очень по-деловому и практично.


