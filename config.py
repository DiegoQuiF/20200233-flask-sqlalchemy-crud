from dotenv import load_dotenv
import os

load_dotenv()

#OBTIENE LOS DATOS DEL ARCHIVO DE CONFIGURACIÓN '.env' PARA LA CONEXIÓN
user=os.environ["USER"]
password=os.environ["PASSWORD"]
host=os.environ["HOST"]
database=os.environ["DATABASE"]
server=os.environ["SERVER"]

#CREA LA LÍNEA DE CONEXIÓN
DATABASE_CONNECTION_URI=f'{server}://{user}:{password}@{host}/{database}'
