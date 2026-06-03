import uvicorn
from inf.connection import init_db
from handler.handler import app

if __name__ == "__main__":
      init_db()                                    # build tables before serving
      uvicorn.run(app, host="127.0.0.1", port=8000)