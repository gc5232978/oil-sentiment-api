# oil-sentiment-api

Example API for the oil-sentiment repo using FastAPI.

## Description

This project shows how to setup a simple API:

## Getting Started

### Dependencies

* fastapi

### Installing

```
git clone https://github.com/gc5232978/oil-sentiment-api.git
cd oil-sentiment-api
poetry install
```

### Starting Local Server

```
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Make a request to the API
```
curl http://localhost:8000/
``` 
