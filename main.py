from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

posts: list[dict] = [
    {
        "id": 1,
        "author": "Example Author",
        "title": "Examle Title",
        "content": "Example Content",
        "date_posted": "January 1, 2020",
    },
    {
        "id": 2,
        "author": "Example Author",
        "title": "Examle Title",
        "content": "Example Content",
        "date_posted": "January 1, 2020",
    },
]


@app.get("/", include_in_schema=False)
@app.get("/posts", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(request=request, name="home.html", context={"posts": posts, "title": "Home"})


@app.get("/api/posts")
def get_posts():
    return posts
