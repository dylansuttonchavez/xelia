from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {
        "request": request,
        "show_nav": False
    })

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "show_nav": True
    })

@app.get("/contacts", response_class=HTMLResponse)
async def contacts(request: Request):
    return templates.TemplateResponse("contacts.html", {
        "request": request,
        "show_nav": True
    })

@app.get("/campaigns", response_class=HTMLResponse)
async def campaigns(request: Request):
    return templates.TemplateResponse("campaigns.html", {
        "request": request,
        "show_nav": True
    })

@app.get("/messages", response_class=HTMLResponse)
async def messages(request: Request):
    return templates.TemplateResponse("messages.html", {
        "request": request,
        "show_nav": True
    })

@app.get("/settings", response_class=HTMLResponse)
async def settings(request: Request):
    return templates.TemplateResponse("settings.html", {
        "request": request,
        "show_nav": True
    })

# python -m uvicorn main:app --reload