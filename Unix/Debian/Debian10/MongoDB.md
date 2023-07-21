### установка Mongo Monolith
```
    https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-debian/
    
    mason 20.07.2023
    
    1. apt-get update
    2. apt-get upgrade
    3. apt-get install gnupg curl
    4. curl -fsSL https://pgp.mongodb.com/server-6.0.asc | gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg --dearmor
    5. echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg ] http://repo.mongodb.org/apt/debian buster/mongodb-org/6.0 main" | tee /etc/apt/sources.list.d/mongodb-org-6.0.list
    6. apt-get update
    7. apt-get install -y mongodb-org
    8. systemctl start mongod
    9. systemctl status mongod
```

### Настройка удаленного доступа
```
    https://www.youtube.com/watch?v=zZnVG_GpcbM
    
    mongosh
    
    > use admin  выбрал БД admin
    switched to db admin
    
    db.createUser(
            {
                user: "stepan",
                pwd:  "*************",
                roles: [ { role: "root", db: "admin" } ]
            }
        )
        
    - настройка конфигурации сервера БД
    nano /etc/mongod.conf
    
    port: указать порт
    bindIp: внешний ip adress server 
    
    отключаем ананимную авторизацию на нашем сервере:
    #noauth=false -> noauth=false 
    
    перезагружаем приложение
    sudo systemctl restart mongod
    
    sudo systemctl status mongod  
```

### установка Mongo Docker
```
    https://cpab.ru/kak-zapustit-mongodb-v-kontejnere-docker-cloudsavvy-it/

    docker pull mongodb/mongodb-community-server
    
    docker run -d -p 38000:27017 --name chat-mongo -v chat-mongo-data:/data/db -e MONGODB_INITDB_ROOT_USERNAME="example-user" -e MONGODB_INITDB_ROOT_PASSWORD="example-pass" mongodb/mongodb-community-server:latest
    
    # docker run -d -p 38000:27017 --name chat-mongo -v chat-mongo-data:/data/db -v /etc/chatmongo.conf:/etc/mongod.conf mongodb/mongodb-community-server:latest --config /etc/mongod.conf
    
    docker container ls
    
    docker exec -it chat-mongo
```
