https://syntaxerror.ru/decorators-in-javascript/

```
    # Создаём package.json с дефолтными значениями полей
    npm init -y
    
    # Устанавливаем babel-core и babel-cli
    npm i @babel/core @babel/cli -D
 
    # Устанавливаем @babel/preset-env
    npm i @babel/preset-env -D
     
    # Устанавливаем плагин для поддержки декораторов
    npm i @babel/plugin-proposal-decorators -D
     
    # Устанавливаем nodemon для перезапуска скомпилированных скриптов
    npm i nodemon -D
```
```
    После установки зависимостей нам нужно создать файл настроек babel.config.json
    
    {
        "presets": [
            ["@babel/preset-env", {
                "shippedProposals": true,
                "loose": true
            }]
        ],
        "plugins": [
            [
                "@babel/plugin-proposal-decorators",
                {
                    "decoratorsBeforeExport": true
                }
            ]
        ]
    } 
```
```
    Заключительным этапом будет настройка npm команды для запуска компиляции исходных файлов в режиме отслеживания. 
    Для этого в файле package.json есть специальный блок scripts в котором мы сможем разместить следующую команду:
    
    babel src --out-dir dist --watch
```