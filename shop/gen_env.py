#! python
from django.core.management.utils import get_random_secret_key
import sys
if len(sys.argv) > 1:
   arg = sys.argv[1]
s = ''
if arg == 'no_db':
   with open('.env', 'w') as f:
      f.write(f"SECRET_KEY={get_random_secret_key()}\n")
      f.write(f"DEBUG=False\n")
      f.write(f"PG_HOST=localhost\n")
      f.write(f"PG_PORT=5432\n")
      f.write(f"PG_DBNAME=dbscheme\n")
      f.write(f"PG_USER=dbuser\n")
      f.write(f"PG_PASS=pgpass\n")
      s = input('Введите ALLOWED_HOSTS через запятую без пробелов:')
      f.write(f"ALLOWED_HOSTS={s}")
else:
   with open('.env', 'w') as f:
      f.write(f"SECRET_KEY={get_random_secret_key()}\n")
      f.write(f"DEBUG=False\n")
      ip = input('Введите IP адрес или имя postgree:')
      f.write(f"PG_HOST={ip}\n")
      port = input('Введите порт postgree:')
      f.write(f"PG_PORT={port}\n")
      db_name = input('Введите название базы postgree:')
      f.write(f"PG_DBNAME={db_name}\n")
      user = input('Введите имя пользователя postgree:')
      f.write(f"PG_USER={user}\n")
      user_pass = input('Введите пароль пользователя postgree:')
      f.write(f"PG_PASS={user_pass}\n")
      s = input('Введите ALLOWED_HOSTS через запятую без пробелов:')
      f.write(f"ALLOWED_HOSTS={s}")
