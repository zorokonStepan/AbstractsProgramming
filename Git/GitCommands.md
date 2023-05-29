Ресурсы:
https://habr.com/ru/company/ruvds/blog/599929/#17

### настроить GIT для обхода: LF will be replaced by CRLF the next time Git touches it
git config --global core.safecrlf false 

### Обновить код на локальной машине из удаленного репозитория
https://techrocks.ru/2021/04/09/how-to-use-git-part-3/#updating-our-local

```
git fetch - Для запроса новой информации. 
Теперь наш локальный репозиторий знает о наличии новых коммитов, но мы пока ничего с ними не делали.
Запуск git fetch ничего не меняет в наших файлах. Мы просто загрузили из удаленного репозитория новую информацию о его статусе.
```
```
git pull — это, собственно, сокращенная форма запуска двух команд: git fetch, за которой сразу идет git merge.
```

```
https://stackoverflow.com/questions/1443210/updating-a-local-repository-with-changes-from-a-github-repository
git pull origin main
```




### **Создать новый репозиторий из командной строки**
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