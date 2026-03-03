## Blog made using FastAPI

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

### How to run
```
create .env in root folder
py -c "import secrets; print(secrets.token_hex(32))"
SECRET_KEY=[insert secret key generated ^]
fastapi dev main.py
```
