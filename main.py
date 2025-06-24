import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

def get_supabase_env():
    return {
        "SUPABASE_URL": os.getenv("SUPABASE_PROJECT_URL"),
        "SUPABASE_ANON_KEY": os.getenv("SUPABASE_ANON_PUBLIC"),
    }

@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    context = {"request": request, "show_nav": False, **get_supabase_env()}
    return templates.TemplateResponse("login.html", context)

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

@app.exception_handler(StarletteHTTPException)
async def custom_404_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        return templates.TemplateResponse("404.html", {"request": request, "show_nav": False}, status_code=404)
    return await app.default_exception_handler(request, exc)

# python -m uvicorn main:app --reload