#! /bin/bash
echo "I am going to run django"
cd ../backend/reasonmljobs
echo "Activate env"
source env/bin/activate
echo "python manage.py runserver $1"
python manage.py runserver $1
echo "Exit"