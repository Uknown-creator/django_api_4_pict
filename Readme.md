# Django API for pictures
## Установка for Yarik

1. Установи зависимости:   
``pip install -r requirements.txt``
2. Мигрируем птичек:   
``cd app && python manage.py migrate``
3. Создать админа для админки:  
``cd app && python manage.py createsuperuser``

### API это кто? Who?
Начнём с того, что это RestAPI.
В общем, есть две директории(корень не реагирует на гет запросы):

admin/,
api/, 
Ну и есть uploads, но он предназначен для картиночек. Туда уже загружены
две тестовые картиночки, можно их посмотреть в test_uploads, или же в
/uploads/*название*.png

С примерами запросов можно ознакомиться в тестах(/app/api/tests.py)

