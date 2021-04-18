from fastapi import FastAPI
app = FastAPI()


@app.get('/', tags=['index'])
def index():
    return 'test'


