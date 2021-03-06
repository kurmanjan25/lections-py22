GIT - распределенная система контроля версий 
Это система для отслеживания и введения истории изменений ваших файлов или проекта.
Репозиторий - это хранилище ваших файлов, которые вы отслеживаете при помощи гита и изменений.
Команды GIT: 
1. git init - она создает новый гит репозиторий локально на вашем пк, создаст она в той директории, где вы запускаете эту команду.
2. git add - когда мы создаём и изменяем файлы, то при помощи этой команды мы загружаем все изменения в промежуточное место хранения.
gid add <file_name>
git add . -> все в текущей директории
3. git commit - как только мы достигаем определенного момента в разработке, то мы тогда сохраняем и комментируем все наши изменения в репозитории. Т.е. иными словами это фиксация изменений в репо.
git commit -m '<comments>'
4 git remote add- это команда для того, чтобы связать ваш локальный репозиторий с удаленным репозиторием )репо в гитхабе)
 git remote add <название подключения> <ссылка на репозиторий>
git remote add origin <url>
5. git push - после коммита изменений при помощи этой команды мы отправляем изменения в файлах на удаленный репозиторий.
git push <origin> <название ветки (main)>
git push origin main
----------------------------------------------------------------------------------------------------------------------------------------------
1. git init
2. git branch -M main (переименовываем главную ветку с master на main)
3. git add .
4. git commit -m 'comment' (все добавлено в локальный репо)
5. git remote add origin <url>
6. git push origin main
---------------------------------------------------------------------------------------------------------------------------------------------
git add .
git commit -m 'comment'
git push origin main

