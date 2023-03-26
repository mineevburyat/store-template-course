#! /sh/bash
echo "INIT gunicorn and nginx? (Y|n):"
read I
if [ "$I" != "Y" ]
then
  exit 1
fi

echo "INSTALL REQUIREMENTS"
pip install -r requirements.txt
if [ $? -eq 0 ]
then
  echo "REQUIREMENTS INSTALLED SECCEFULL"
else
  echo "Failure!"
  exit 1
fi


echo "INSTALL DB POSTGREE? (Y|n):"
read I
if [ "$I" != "Y" ]
then
    echo "CREATE ENVIRONMENT FILE"
    python gen_env.py no_db
    if [ $? -eq 0 ]
    then
        echo "ENVIRONMENT FILE SUCCESS"
    else
        echo "Failure!"
        exit 1
    fi
    NO_DB=yes
    export NO_DB
    echo "CREATE STATIC COLLECTION"
    python manage.py collectstatic
    if [ $? -eq 0 ]
    then
        echo "STATIC COLLECTION SUCCESS"
    else
        echo "Failure!"
        exit 1
    fi
    echo "CREATE SUPER USER"
    python manage.py createsuperuser
    if [ $? -eq 0 ]
    then
        echo "SUPER USER SUCCESS"
    else
        echo "Failure!"
        exit 1
    fi
    unset NO_DB
    exit 1
fi

echo "MIGRATE SHEME TO DB"
python manage.py migrate
if [ $? -eq 0 ]
then
  echo "SHEME MIGRETE SUCCEFULL"
else
  echo "Failure!"
  exit 1
fi

echo "LOAD FIXTURE"
python loaddate catalog/fixture/category.json
if [ $? -eq 0 ]
then
  echo "FIXTURE SUCCESS"
else
  echo "Failure!"
  exit 1
fi
python loaddate catalog/fixture/product.json
if [ $? -eq 0 ]
then
  echo "FIXTURE SUCCESS"
else
  echo "Failure!"
  exit 1
fi

