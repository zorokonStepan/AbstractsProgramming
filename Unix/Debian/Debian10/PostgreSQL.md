https://losst.pro/ustanovka-postgresql-v-debian-10

### Установка postgresql 11 в Debian 10
```
    apt-get update
    apt-get upgrade
    apt install postgresql-11 postgresql-client-11
```

### Проверка установки:
```
    pg_isready
    systemctl status postgresql
```    

### Полезные команды:
```
    systemctl start postgresql
    systemctl restart postgresql
    systemctl stop postgresql
    systemctl reload postgresql
```

### Пароль учетной записи пользователя Postgres
```
    Учетная запись пользователя системы Postgres не защищена паролем, для ее защиты вы можете создать пароль с помощью утилиты passwd.
    
    passwd postgres
```

### Пароль super-пользователя Postgres
```
    Кроме того, роль Postgres (или, если угодно, суперпользователь базы данных) по умолчанию не защищена. 
    Вам также необходимо защитить ее паролем. Теперь переключитесь на учетную запись пользователя системы 
    postgres и роль postgres (не забудьте установить надежный и безопасный пароль), как показано ниже.
    
    su - postgres
    psql -c "ALTER USER postgres WITH PASSWORD 'новый_пароль';"   
```

### Настроить аутентификацию по паролю md5 для аутентификации клиента
```
    nano /etc/postgresql/11/main/pg_hba.conf
    systemctl restart postgresql
```

### Создание новой базы данных и роли базы данных/пользователя в PostgreSQL
```
    su - postgres
    psql
    CREATE DATABASE test_chat;
    CREATE USER stepan PASSWORD 'новый_пароль';
```

### Чтобы подключиться к test_db от имени пользователя test_user, выполните:
```
    psql -d test_chat -U stepan
```

### настроить удаленное подключение к PostgreSQL
https://www.dmosk.ru/miniinstruktions.php?mini=pgsql-remote

```
    посмотрим путь расположения конфигурационного файла postgresql.conf:
    # su - postgres -c "psql -c 'SHOW config_file;'"
    
    Теперь открываем на редактирование основной файл конфигурации PostgreSQL:
    # nano /db/pgsql/postgresql.conf
    change:  
        listen_addresses 
        port
        
    открываем на редактирование следующий конфигурационный файл:
    # nano /db/pgsql/pg_hba.conf    
    и внизу добавляем следующую строку:
    host     all     all     192.168.0.10/32     password
    
    Чтобы изменения вступили в силу, перезапускаем службу postgresql:
    # systemctl restart postgresql  
```

### PSQL in Docker
```
    docker run --name chat-postgresql -p 9777:5432 -v /root/psql-test-chat/data:/var/lib/postgresql/data -e POSTGRES_USER="stepan" -e POSTGRES_PASSWORD="987&654" -e POSTGRES_DB="test_chat" -d postgres:11.2
    docker exec -it chat-postgresql bash    
```






