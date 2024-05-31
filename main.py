import sqlite3
import uvicorn
from fastapi import FastAPI

app = FastAPI()

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

@app.get("/")
async def read_all_data():
    cursor.execute("SELECT * FROM sentiment")
    data = cursor.fetchall()
    return {"data": data}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
