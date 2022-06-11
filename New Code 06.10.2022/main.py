import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from stepper import Stepper
from scheduling import refresh_schedule


motor1, motor2, motor3 = None, None, None


# Configure motors and GPIOs.
motor1 = Stepper(enable_pin = 7, step_pin = 5, dir_pin = 3)
# Motor 2 has no directional control. Bad PCB design.
motor2 = Stepper(enable_pin = 13, step_pin = 15, dir_pin = 16)
motor3 = Stepper(enable_pin = 23, step_pin = 27, dir_pin = 29)

# Load default/existing schedule from saved json.
refresh_schedule(motor1, motor2, motor3)

app = FastAPI()

origins = ["*"]
app.add_middleware( 
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/alive")
def alive():
    print("I am alive!")
    return {"alive": True}

@app.post("/update_schedule")
def update_schedule(schedule_data: dict):
    print("Updating schedule...")
    schedule = open("Schedule.json", "w")
    schedule.write(json.dumps(schedule_data))
    schedule.close()
    refresh_schedule(motor1, motor2, motor3)


@app.post("/sendsteps")
def sendsteps(steps: int):
    # Printing steps to console
    print(f"Steps set to {steps}")
    return {"Steps": steps}


while True:
    schedule.run_pending()
    time.sleep(1)