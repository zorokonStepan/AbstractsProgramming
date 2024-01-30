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
```