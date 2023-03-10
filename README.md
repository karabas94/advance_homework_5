##  Tutorial django project

--------
* Done:
  * created project
  * created the Polls app
  * wrote views and modern
  * database setup
  * created models
  * activated models
  * removed hardcodes
  * wrote tests
  * customized app’s look and feel
  * customize the admin form
  * created management command create_users
  * created management command delete_users
  * created fixtures in db.json
--------
**How to start project**
* install all from requirements.txt
* for start project write in terminal:
```
    
    $ python manage.py runserver
    
```
* for creating users write in terminal:
```
    
    $ ./manage.py create_users 4
    
```
for example created four users
* for delete users write in terminal:
```
    
    $ ./manage.py delete_users 2 4
    
```
write ID users which like delete
* for loading fixtures:
  * clear table:
```
    
    $ ./manage.py flush
    
```
  * load fixtures
```
    
    $ ./manage.py loaddata fixtures.json
    
```
* Quit the server with CONTROL-C.
--------
Project checked by flake8
