#! python
from django.core.management.utils import get_random_secret_key
import manage
manage
with open('.env', 'rw') as f:
    f.write(f"SECRET_KEY={get_random_secret_key()}")
    f.write(f"DEBUG=False")
    f.write(f"PG_HOST=localhost")
    f.write(f"PG_PORT=localhost")
    f.write(f"PG_HOST=localhost")
    f.write(f"PG_HOST=localhost")
    f.write(f"PG_HOST=localhost")
 PG_HOST = env('')
    PG_PORT = env('PG_PORT')
    PG_DBNAME = env('PG_DBNAME')
    PG_USER = env('PG_USER')
    PG_PASS = env('PG_PASS')