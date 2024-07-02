# specialoffer
## How to launch
1. install sqlite3 database
2. git clone this repo
3. use vscode open this project
4. open vscode terminal
   1. `python3 -m venv virtual`
   2. `source virtual/bin/activate` (virtual/Scripts/activate -Win)
   3. `pip install django`
   4. `python manage.py makemigrations`
   5. `python manage.py migrate`
   6. `python manage.py runserver`
   7.  check url `http://127.0.0.1:8000/`
   8. `python craw.py` wating for a moment until finished
   9. `python manage.py runserver` then login and you can see the results

