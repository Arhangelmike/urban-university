Домашнее задание по теме "Настраиваем СУБД postgre в django"
Задание:
Часть 1:

1) Старт работы с PostgreSQL. Скачайте и установите официальный пакет pgsql для
вашей ОС. Установите PGadmin и подключитесь к локальному серверу, создайте новую
базу данных и прикрепите скриншот выполненного задания.
2) В своем Django проекте установите драйвер psycopg2 для работы с базой PGSQL
используя менеджер пакетов pip. В файле настроек проекта выполните подключение к
базе данных:
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql',
'NAME': 'имя_базы_данных',
'USER': 'имя_пользователя',
'PASSWORD': 'пароль',
'HOST': '127.0.0.1',
'PORT': '5432',
}
}

Создайте и выполните миграции используя makemigrations и migrate. Проверьте
подключение, в базе данных должны создаться технические таблицы Django проекта.
3) Перенесите любую созданную ранее модель базы данных в PGSQL. Используйте
Джанго модели и миграции. Создайте несколько таблиц через конструктор PGadmin и
свяжите их с Джанго проектом, создав необходимые модели.


Создали пустую базу 
 ![image](https://github.com/user-attachments/assets/e6698afa-d356-4236-86d5-f4ffa159fee4)


Ставим драйвер 
 ![image](https://github.com/user-attachments/assets/4709e7c7-92ee-45a4-aa46-c70432debdff)


python manage.py makemigrations
![image](https://github.com/user-attachments/assets/55c00af0-f2dc-4e33-9eb5-5cbb778d067b)

 
python manage.py migrate
 ![image](https://github.com/user-attachments/assets/b2e3f039-df90-475d-a802-23c1419b5f09)


Добавились базы с предыдущего проекта. Но пустые.
![image](https://github.com/user-attachments/assets/b2f2ac59-2433-40f3-bd9f-6fb83e64c3a5)

 

python manage.py createsuperuser
 ![image](https://github.com/user-attachments/assets/964d800f-5ee4-4433-96b5-060afb695f20)



Создайте несколько таблиц через конструктор PGadmin и
свяжите их с Джанго проектом, создав необходимые модели.

Так как нет смысла усложнять задачу разберем как это сделать, на примере таблицы News, создадим ее клона task1_news2 в нашей базе данных и пропишем ее в модели в файл models.py как News2. И можем делать те же запросы что и для первой таблицы, ничем не будет отличаться.

Заходим в PGadmin выбираем раздел таблицы и создаем таблицу с аналогичным именем
![image](https://github.com/user-attachments/assets/5491fb32-afdf-4817-ad3f-b47bda7564bd)

![image](https://github.com/user-attachments/assets/d4d7ace7-f181-44a1-bd01-7f4ebc74aa8d)

![image](https://github.com/user-attachments/assets/bb13668a-583b-49e8-95dc-752201f63ad3)


Нажимаем Save

И добавляем в Джанго
 
![image](https://github.com/user-attachments/assets/086bc815-7a2c-4231-a660-253bc3c9a213)



Часть 2:
4) Используйте Django ORM для тестирования запросов в вашу базу данных.
Выполните команду Python manage.py shell. Импортируйте необходимые модели из вашей
базы данных и создайте не менее 4 запросов, например:
Запрос на получение всех объектов базы данных и конкретного по id.
Запрос на фильтрацию
Запрос на добавление или удаление объекта

Добавим пользователей в пустую базу 
![image](https://github.com/user-attachments/assets/85b66ab1-0a13-482a-9db1-151a05fddb51)

 
Переходим в админку
![image](https://github.com/user-attachments/assets/717fa7d7-60f8-4706-adc3-4acddf29d66f)

 
Проверяем работу с базой через админку. В таблицу News успешно внесены данные.
![image](https://github.com/user-attachments/assets/6da0a7e9-f5fa-4b63-a92b-9c7fa35ec7da)

 
После внесения данных продолжаем тестировать запросы в базу данных выведем всех пользователей, содержащих в имени User
 ![image](https://github.com/user-attachments/assets/12426f38-ab5c-4fbd-9b47-d39dae49ea60)


Импортируем модель News и также просим показать где встречается сочетание «вы же»
![image](https://github.com/user-attachments/assets/902ab802-0157-49af-84cb-ff06f7ef0460)

 

Вывести в консоль содержимое заполненных таблиц
![image](https://github.com/user-attachments/assets/e5fd8c0e-5c9b-4626-b76e-63840ea575d6)

 
Выводим сколько раз встречается пользователи, содержащие в имени User
![image](https://github.com/user-attachments/assets/3bbbbc08-a73e-41ff-97d6-936aae94cc7e)

 

