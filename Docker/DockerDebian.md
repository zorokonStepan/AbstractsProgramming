https://www.dmosk.ru/miniinstruktions.php?mini=docker-self-image
https://lumpics.ru/how-to-find-out-debian-version/

### Войдем в скачанный образ
```
    docker run -t -i name_image /bin/bash
    ...    
    exit
```

### Посмотреть версию Debian
```
    cat /etc/debian_version
```
