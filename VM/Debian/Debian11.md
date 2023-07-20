### Установка OS
```
    download image:
    https://cdimage.debian.org/cdimage/archive/11.7.0/amd64/iso-cd/
    
    installing:
    https://www.youtube.com/watch?v=QtnqV5ut9Ao&list=LL&index=1
    
    задать быстрый доступ к терминалу:
    https://g-soft.info/articles/3223/chetyre-sposoba-otkryt-terminal-v-debian/
    
    установить гостевые дополнения:
    https://infoit.com.ua/linux/kak-ustanovit-virtualbox-guest-additions-na-debian-11-debian-10/
    
    Debian 11, 12 - настройка после установки:
    https://dzen.ru/a/YwiCaenDbjRkMQuW?utm_referer=yandex.ru
    
    Получить доступ к общей папке:
    https://qa.yodo.im/t/kak-poluchit-dostup-k-obshhej-papke-v-virtualbox/684/2
    sudo adduser your_username vboxsf
```

### PyCharm
```
    https://wiki.debian.org/JetBrains
    https://infoit.com.ua/linux/kak-ustanovit-pycharm-na-debian-11/
    
    sudo apt update
    sudo apt upgrade
    sudo apt install snapd
    sudo snap install pycharm-community --classic
    
    - Run pycharm
    snap run pycharm-community
```

### Git
```
    https://setiwik.ru/kak-ustanovit-git-v-debian-11/
    
    git config --global user.email "dev1@instrument-fit.ru"
    git config --global user.name "skolodkin"
    git config --list
    cat ~/.gitconfig
    
    
    git config --global user.name "ваше имя"
    git config --global user.email email@example.com
```

### SSH
```
    chmod 0600 id_rsa
    ls -la

    установить ssh сервер: https://losst.pro/nastrojka-ssh-v-debian
    
    eval "$(ssh-agent)"
    ssh-add ~/.ssh/id_rsa
    ssh-add -l
    git clone ssh://git@git.techzone.spb.ru:9106/skolodkin/MongoVSPostgreSQL-Chat.git
    
    проверка соединения
    ssh -T git.techzone.spb.ru
```
