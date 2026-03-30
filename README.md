## Blog made using FastAPI

<div align="center">
    <img alt="GitHub Repo Name" src="https://img.shields.io/badge/FastAPI-Blog-7209b7">
    <img alt="GitHub Author" src="https://img.shields.io/badge/Author-Ellsworth%20McCullough-006d77">
    <img alt="GitHub commit-activity" src="https://img.shields.io/github/commit-activity/t/ellsworthmmcc/FastAPI-Blog">
    <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/ellsworthmmcc/FastAPI-Blog">
    <img alt="GitHub Created At" src="https://img.shields.io/github/created-at/ellsworthmmcc/FastAPI-Blog">
    <img alt="GitHub Last Commit" src="https://img.shields.io/github/last-commit/ellsworthmmcc/FastAPI-Blog">
    <img alt="GitHub Open Issues" src="https://img.shields.io/github/issues/ellsworthmmcc/FastAPI-Blog">
    <img alt="GitHub Closed Issues" src="https://img.shields.io/github/issues-closed/ellsworthmmcc/FastAPI-Blog">
    <img alt="GitHub Open PR" src="https://img.shields.io/github/issues-pr/ellsworthmmcc/FastAPI-Blog">
    <img alt="GitHub Closed PR" src="https://img.shields.io/github/issues-pr-closed/ellsworthmmcc/FastAPI-Blog">
    <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/ellsworthmmcc/FastAPI-Blog">
</div>

### Setup
```
py -m venv venv
```
```
venv/scripts/activate
```
```
pip install -r requirements.txt
```

create .env in root folder
```
py -c "import secrets; print(secrets.token_hex(32))"
```
add following line to .env:
```
SECRET_KEY=[insert secret key generated ^]
```

### How to run
```
fastapi dev main.py
```
