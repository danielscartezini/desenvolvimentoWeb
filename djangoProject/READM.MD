**Preparando o Ambiente**
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
pip install django
django-admin --version

**Criando o Projeto**
django-admin startproject universidade
cd universidade
python manage.py runserver
http://127.0.0.1:8000

*manage.py*
python manage.py runserver
python manage.py startapp alunos
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py shell

***Criando um Aplicativo**
python manage.py startapp alunos

