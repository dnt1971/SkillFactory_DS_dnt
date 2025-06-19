> git init
> git status
On branch master
No commits yet
> git add .
git commit -m "Первичный Commit"
>git status
On branch master
nothing to commit, working tree clean

Узнать Хэш коммита
>git rev-parse HEAD
7977c228ca6f3871692798775d03f10c1f45e4f6

Просмотр коммита
> git show
commit 7977c228ca6f3871692798775d03f10c1f45e4f6 (HEAD -> master)
Author: dnt <dnt_box@mail.ru>
Date:   Fri Jun 20 00:22:33 2025 +0200

    Первичный Commit

diff --git a/game.ipynb b/game.ipynb
new file mode 100644
index 0000000..d586945

Создать новую ветку (после основной ветки)
>git branch develop

> git checkout master

>git status
On branch develop
nothing to commit, working tree clean

> git branch
* develop
  master

Удалим файл из индекса
> git rm game.ру

> git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        deleted:    "game.\321\200\321\203"  

> git commit -m "Файл удален"
[master c8e38b0] Файл удален
 1 file changed, 22 deletions(-)
 delete mode 100644 "game.\321\200\321\203"
 
 > git checkout develop
 Switched to branch 'develop'
 
 Есть 3 файла

> git checkout master
 Есть 2 файла


# Переключаемся на основную ветку, которая будет принимать изменения 
> git master
> git merge develop

> Просмотр заданного коммита
git show
git show c2c09364c8678f0ff818db36e5ebc412f1d2d21f 

> Просмотр до коммита
git diff

> Отка  коммита
git revert HEAD

-----------------------

# Привязка локального репозитория к удалённому на GitHub
> git remote add SkillFactory_DS_dnt https://github.com/dnt1971/SkillFactory_DS_dnt.git
#Смотрим
>git remote
SkillFactory_DS_dnt

# Запрос списка удалённых репозиториев с URL-адресами
> git remote -v
SkillFactory_DS_dnt     https://github.com/dnt1971/SkillFactory_DS_dnt.git (fetch)
SkillFactory_DS_dnt     https://github.com/dnt1971/SkillFactory_DS_dnt.git (push) 


# Команда для первой загрузки изменений в удалённый репозиторий: текущая ветка будет связана с веткой main в удалённом репозитории origin 
Во время первой загрузки нужно использовать команду с опцией -u. Это свяжет локальную и удалённую ветки и синхронизирует их для последующих операций. Для второй и всех последующих загрузок опция -u для связанных веток не понадобится.
Свяжем локальный master с master (там ветка создастся)
 > git push -u SkillFactory_DS_dnt master  




Добавим в индекс ветки develop файл
> git add game.ру

>git status
On branch develop
nothing to commit, working tree clean


git commit -m "commit1 develop"

Откат коммита до кэша
>git reset --soft 7977c228ca6f3871692798775d03f10c1f45e4f6


