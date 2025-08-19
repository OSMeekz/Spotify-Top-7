#from app import create_app 
#assumes we have a file tited app.py(or module)


#app = create_app()
#this is calling a fucntion (Create App) that doesnt exist
#if __name__ == "__main__":
 #   app.run(debug=True)
from flask import Flask 

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port =6060)