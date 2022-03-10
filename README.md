# djangotestproject

### ЗАПУСК ПРОЕКТА ЧЕРЕЗ "Dockerfile"

Запустите Docker на Вашем компьютере и введите последовательно все нижеперечисленные команды:

`python3 manage.py migrate`

`pip install -r requirements.txt`

`docker build -t django-test-project -f Dockerfile .`

`gunicorn djangotestproject.wsgi:application —bind localhost:8000`

Проект запущен.

---

## СОЗДАНИЕ СУПЕРЮЗЕРА ДЛЯ ДОСТУПА К АДМИНИСТРАТИВНОЙ ПАНЕЛИ DJANGO

После ввода нижепредставленной команды нужно вести логин и пароль дважды (почту вводить необязательно):

`python3 manage.py createsuperuser`

Админка с возможностью создания, редактирования и просмотра сущностей доступна по url: http://127.0.0.1:8000/admin/

---

Регистрация новых пользователей:

http://127.0.0.1:8000/auth/users/

Получение токена:

http://127.0.0.1:8000/auth/jwt/create/
