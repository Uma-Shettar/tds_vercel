from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Query
from typing import List
import json
import os

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load student marks from JSON on startup
marks_file = os.path.join(os.path.dirname(__file__), '..', 'marks.json')
with open(marks_file) as f:
    data = json.load(f)

# Create a dictionary for quick lookup
marks_dict = {student['name']: student['marks'] for student in data}

@app.get("/api")
def get_marks(name: List[str] = Query([])):
    results = [marks_dict.get(n, None) for n in name]
    return {"marks": results}
