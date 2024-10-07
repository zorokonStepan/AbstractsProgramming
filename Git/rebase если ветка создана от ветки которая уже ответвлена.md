```
     !!! 
     git checkout master 
     git pull 
     git checkout branch
     
     git rebase --onto master
     git push --force-with-lease
```

## Эльнар
```
    git pull 
    
    Нужно актуализировать ветку на которую будет перебазироваться ветка
    
    https://selectel.ru/blog/tutorials/how-to-rebase-commits-and-branches/
    
    откатиться:
    git reset --hard origin/update_versions_python_and_libs
    
    git rebase --onto origin/update_versions_python_and_libs update_versions_python_and_libs
        
    git rebase --onto origin/update_versions_python_and_libs-куда перебазироваться [update_versions_python_and_libs - локальная ветка или хэш коммита к которому прицепиться]
    
    смотреть результат по графу
    
    --onto куда перебазироваться, обязательно origin/...
    следующий параметр куда прицепиться, хэш коммита или локальная ветка
    следующий параметр с какой ветки перебазироваться. если находишься в этой ветке то указывать этот параметр не нужно  
```