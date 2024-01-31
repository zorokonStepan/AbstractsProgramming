```
    https://habr.com/ru/articles/755036/
    https://sendel.ru/posts/https-to-ssh-on-github/#что-необходимо
    
    1. Генерация ключей в директории .ssh
        open GitBash 
        ssh-keygen -t ed25519 -b 4096
        Enter
        Enter
        Enter
    
    2. Добавление публичного ключа в профиль на GitHub/GitLab
    
    3. Активация private ключа
        
        3.1. Предварительно:
            1. Установить PuTTY
            2. Установить переменную окружения GIT_SSH C:\Program Files\PuTTY\plink.exe
            3. С помощью PuTTYgen сгенерировать private.ppk ключ из приватного ключа.
        
        3.2. Добавить в Pageant private.ppk

    
    
```