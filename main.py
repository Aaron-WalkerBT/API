from fastapi import FastAPI, Request
from fastapi.params import Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import random
#import tileif as tif

def execute_config(tile_num, array):
    print(tile_num)
    print(len(array))
    if len(array) < 520:
        array = eval(array)
        #tif.setconf(tile_num, array)
        print(type(array))
        return f"32:16 Config should be sent: {array}"
    else:
        return "Config is too largee"
    
    
app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name ="static")


@app.get("/", response_class=HTMLResponse)
def get_input(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})


@app.post("/", response_class=HTMLResponse)
def post_input(request: Request, api_mode: str = Form(...)):
    print(f"API Mode ={api_mode}")
    return templates.TemplateResponse(f"mode{api_mode}.html", {"request": request})

#API Mode 0-------------------------------------------
@app.get("/mode0", response_class=HTMLResponse)
def mode0(request: Request):
    print(f"made it to mode 0!")
    return templates.TemplateResponse("mode0.html", {"request": request, "Input_Config": "", "submitted": False})

@app.post("/mode0", response_class=HTMLResponse)
def post_input(request: Request, Input_Config:str = Form(...)):
    print(f"RIS Config: {Input_Config}")
    tile_num = int(1)
    return_text = execute_config(tile_num, Input_Config)
    return templates.TemplateResponse("mode0.html", {"request": request, "Input_Config": Input_Config, "return_text": return_text, "submitted": True})


#API Mode 1-------------------------------------------
@app.get("/mode1", response_class=HTMLResponse)
def mode0(request: Request):
    print(f"made it to mode 1!")
    return templates.TemplateResponse("mode1.html",{"request":request, "dictionary": "", "submitted": False})

@app.post("/mode1", response_class=HTMLResponse)
def post_input(request: Request, dictionary:str = Form(...)):
    print(f"dictionary: {dictionary}")
    return templates.TemplateResponse("mode1.html", {"request": request, "dictionary": dictionary, "submitted": True})


#API Mode 2 -------------------------------------------
@app.get("/mode2", response_class=HTMLResponse)
def mode0(request: Request):
    print(f"made it to mode 2!")
    return templates.TemplateResponse("mode2.html",{"request":request,"mode":"Mode 2"})

@app.post("/mode2", response_class=HTMLResponse)
def post_input(request: Request, dictionary:str = Form(...)):
    print(f"dictionary: {dictionary}")
    return templates.TemplateResponse("mode2.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run(app)
    
    
#uvicorn main:app --reload     to autoreload API
