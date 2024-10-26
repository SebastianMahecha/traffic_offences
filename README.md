# traffic_offences

RUN PROJECT

fastapi dev main.py

conda activate traffic_offences_env


create database traffic_offences_db;
CREATE ROLE traffic_offences_user WITH LOGIN PASSWORD '12345678';
grant all privileges on database  traffic_offences_db to traffic_offences_user;
ALTER DATABASE traffic_offences_db  OWNER TO traffic_offences_user;

psql -U traffic_offences_user -d traffic_offences_db 


pip install fastapi uvicorn sqlalchemy asyncpg



Config automigrate

pip install alembic
alembic init alembic

Modificar el archivo env.py,
agregar el target_metadata

target_metadata = SQLModel.metadata

Reemplazar las urls de la DB en offline y online
DATABASE_URL = os.getenv("DATABASE_URL")

reemplazar el connectable del online

connectable = create_engine(DATABASE_URL)

importar los modelos del proyecto 
from models import *


agregar la siguiente linea en el archivo script.py.mako

import sqlmodel # added


Crear migraciones
alembic revision --autogenerate -m "create user table"
correr migracion
alembic upgrade head