from app import app
from utils.db import db

with app.app_context():
    db.create_all()

#INICIALIZACIÓN DEL PROGRAMA
#LINK: http://127.0.0.1:5000
if __name__ == '__main__':    
    app.run(host='0.0.0.0', debug=True, port=5000)