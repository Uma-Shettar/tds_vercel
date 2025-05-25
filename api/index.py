from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load marks data
with open("marks.json") as f:
    student_marks = json.load(f)

@app.get("/api")
def get_marks(name: List[str] = []):
    result = [student_marks.get(n, None) for n in name]
    return {"marks": result}
