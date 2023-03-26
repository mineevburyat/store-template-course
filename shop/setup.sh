#! /sh/bash
pip install requirements.txt
python manage.py migrate
python manage.py collectstatic
python loaddate catalog/fixture/category.json
python loaddate catalog/fixture/product.json
python gen_secret.py
