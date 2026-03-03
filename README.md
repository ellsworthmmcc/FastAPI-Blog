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
