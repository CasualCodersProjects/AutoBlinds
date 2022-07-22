import schedule
import threading
import json

# def spin_motor(enable_pin, step_pin, dir_pin, steps, direction, time):
def spin_motor_threaded(stepper, steps, time):
    job_thread = threading.Thread(target = stepper.spin_motor, args = (steps, time))
    job_thread.start()

def refresh_schedule(motor1, motor2, motor3):
    # clear schedule
    schedule.clear()
    schedule_data = json.load(open("Schedule.json"))
    
    # motor 1
    setmotor(motor1,schedule_data['motor1'])
    setmotor(motor2,schedule_data['motor2'])
    setmotor(motor3,schedule_data['motor3'])

    def setmotor(motor, schedule_data):
        for scheduled_time in schedule_data["Schedule"]["Monday"]:
            schedule.every().monday.at(scheduled_time).do(spin_motor_threaded, motor, schedule_data["steps"], schedule_data["time"])

        for scheduled_time in schedule_data["Schedule"]["Tuesday"]:
            schedule.every().tuesday.at(scheduled_time).do(spin_motor_threaded, motor, schedule_data["steps"], schedule_data["time"])

        for scheduled_time in schedule_data["Schedule"]["Wednesday"]:
            schedule.every().wednesday.at(scheduled_time).do(spin_motor_threaded, motor, schedule_data["steps"], schedule_data["time"])

        for scheduled_time in schedule_data["Schedule"]["Thursday"]:
            schedule.every().thursday.at(scheduled_time).do(spin_motor_threaded, motor, schedule_data["steps"], schedule_data["time"])

        for scheduled_time in schedule_data["Schedule"]["Friday"]:
            schedule.every().friday.at(scheduled_time).do(spin_motor_threaded, motor, schedule_data["steps"], schedule_data["time"])

        for scheduled_time in schedule_data["Schedule"]["Saturday"]:
            schedule.every().saturday.at(scheduled_time).do(spin_motor_threaded, motor, schedule_data["steps"], schedule_data["time"])

        for scheduled_time in schedule_data["Schedule"]["Sunday"]:
            schedule.every().sunday.at(scheduled_time).do(spin_motor_threaded, motor, schedule_data["steps"], schedule_data["time"])