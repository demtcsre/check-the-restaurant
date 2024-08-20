from application import app
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    PORT = "5000" #os.environ.get('PORT_DEV')
    DEBUG = True #os.environ.get('FLASK_DEBUG')
    HOST = "127.0.0.1" #os.environ.get('HOST_DEV')
    app.run(host=HOST, port=PORT, debug=DEBUG)
    
if __name__ == "__main__":
    main()