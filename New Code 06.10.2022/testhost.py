import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]
app.add_middleware( 
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/get_schedule")
def get_schedule():
    print("Getting schedule...")
    schedule = open("Schedule.json", "r")
    schedule_data = json.load(schedule)
    schedule.close()
    return schedule_data

@app.post("/update_schedule")
def update_schedule(schedule_data):
    print("Updating schedule...")
    print(schedule_data)
    schedule = open("Schedule.json", "w")
    schedule.write(schedule_data)
    schedule.close()
    return {"Schedule": "Updated"}

@app.get("/alive")
def alive():
    print("I am alive!")
    return {"alive": True}