from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.post("/update_schedule")
def update_schedule(schedule_data: dict):
    print("Updating schedule...")
    print(schedule_data)
    # schedule = open("Schedule.json", "w")
    # schedule.write(json.dumps(schedule_data))
    # schedule.close()
    # refresh_schedule(motor1, motor2, motor3)


@app.post("/sendsteps")
def sendsteps(steps: int):
    # Printing steps to console
    print(f"Steps set to {steps}")
    return {"Steps": steps}