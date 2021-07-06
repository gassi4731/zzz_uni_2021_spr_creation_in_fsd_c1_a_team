from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()
# staticのディレクトリにあるファイルを / でアクセスできるようにする．
app.mount("/", StaticFiles(directory="static", html=True), name="static")
