from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()

# Mounting static files
app.mount("/static", StaticFiles(directory="test/self"), name="static")

# Templates setting
templates = Jinja2Templates(directory="test/self")

# Serve the index.html
@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Serve a file directly for testing
@app.get("/file")
async def get_file():
    return FileResponse("test/self/index.html")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
