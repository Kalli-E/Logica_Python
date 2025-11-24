python manage.py makemigrations ou python manage.py migrate -> serve para atualizar o BD após uma alteração. Não esquecer de utilizar.

.\\manage.py makemigrations > O comando \manage.py não foi encontrado, mas existe no local atual. Por padrão, o Windows PowerShell não carrega comandos do local atual. Se você confia nesse comando, digite: ".\\manage.py". Consulte "get-help about_Command_Precedence" para obter mais detalhes.

python manage.py createsuperuser -> para criar superusuário p acessar BD Web (anotar usuário e senha criados)

 py -m django startapp filme

 python manage.py runserver

 ---

Iniciar um projeto no Django:
django-admin startproject "NomeDoProjeto"

Criar um app dentro do projeto:
py -m django startapp "NomeDoApp"

Iniciar servidor:
python manage.py runserver

Criar um Superusuário:
python manage.py createsuperuser

Verificar as alterações feitas no sistema:
python manage.py makemigrations

Fazer as aterações no sistemas:
python manage.py migrate