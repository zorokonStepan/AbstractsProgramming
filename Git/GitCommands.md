Ресурсы:
https://habr.com/ru/company/ruvds/blog/599929/#17

### настроить GIT для обхода: LF will be replaced by CRLF the next time Git touches it
git config --global core.safecrlf false 

### **Создать новый репозиторий из командной строки**

https://habr.com/ru/company/ruvds/blog/599929/#17

```
touch README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin ssh://git@git.techzone.spb.ru:9106/skolodkin/admin-site.git
git push -u origin master
```
### **Отправить существующий репозиторий из командной строки
```
git remote add origin ssh://git@git.techzone.spb.ru:9106/skolodkin/admin-site.git
git push -u origin master
```

###**Отменить merge
```
https://translated.turbopages.org/proxy_u/en-ru.ru.5ee50c35-645cba6b-3715bf30-
74722d776562/https/stackoverflow.com/questions/5741407/how-to-undo-a-git-merge-with-conflicts
git merge --abort
```