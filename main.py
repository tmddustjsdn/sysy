from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# 정적 파일을 제공하기 위해 StaticFiles 클래스를 사용하여 디렉토리를 설정합니다.
app.mount("/static", StaticFiles(directory="self"), name="static")

# Jinja2Templates를 사용하여 템플릿을 설정합니다.
templates = Jinja2Templates(directory="self")

# index.html을 렌더링하는 라우터를 추가합니다.
@app.get("/")
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# kkk.js 파일을 제공하는 라우터를 추가합니다.
@app.get("/kkk.js")
async def read_kkk_js():
    return FileResponse("self/kkk.js", media_type="application/javascript")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
