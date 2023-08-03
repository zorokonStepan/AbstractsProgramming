### install
```
    sudo apt update
    sudo apt install redis-server
    
    redis-server -v
    
    sudo nano /etc/redis/redis.conf
        supervised systemd
        
    sudo systemctl restart redis-server    
```

### Connect to Redis Server
```  
    redis-cli info
    redis-cli info stats
    redis-cli info server     

    redis-cli
        ping
        
        set test "It's working!"
        get test
        
        exit
```

### Managing the Redis Service
```
    sudo systemctl start redis-server
    sudo systemctl stop redis-server
    
    sudo systemctl enable redis-server
    sudo systemctl disable redis-server
    
    sudo systemctl status redis-server
```

### Work with DB
```
    https://pacificsky.ru/cache/redis/112-redis-poluchit-vse-dannye-iz-bd.html
    
    redis-cli
        
    Теперь для просмотра списка БД(ключей) нужно выполнить данную команду:
    info keyspace
    
    Для перехода в интересующую БД необходимо выполнить команду
    select имя_бд например 3
    
    Теперь для получения списка всех данных из данной бд необходимо выполнить данную команду:
    keys *
    
    Проверка срока действия ключа в секундах
    ttl key_melon
    
    Проверка срока действия ключа в милисекундах
    pttl key_melon
```