```
    git init .  # . - текущая директория. создать базу данных git, т.е. репозиторий
    
    git status
    
    git add * OR git add .  # добавить все файлы в коммит из дирректории
    git add path/file       # добавить определенные файлы 
    
    git commit -m "message"
    
    git log             # история всех коммитов
    git log -number     # вывести число последних коммитов
    git log -number -p  # вывести с анализом изменений
    
    git checkout -- filename.py  # убрать изменения в файле
    
    git diff --staged  # разница в коде, то что запишится в коммит, после команды git add
    
    git push origin
    
    -------------------------------------------------------------------------------------------------------------------
    
    git remote -v  # link для общения с гитом
        PS D:\Stepan\GitProjects\AbstractsProgramming> git remote -v
        origin  https://github.com/zorokonStepan/AbstractsProgramming.git (fetch)
        origin  https://github.com/zorokonStepan/AbstractsProgramming.git (push)
        
    CHANGE HTTPS -> SSH:
        
        git remote set-url origin git@github..(ssh-url)

    
```