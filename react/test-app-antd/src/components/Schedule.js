import { TimePicker, Space, Typography } from 'antd';
import moment from 'moment';
import React, { useState } from 'react';

// Colors:
// Teal:        #4ec9b0
// Light Blue:  #9cdcfe
// Grey:        #1e1e1e
// Dark Grey:   #0e0e0e

function printData(){
    console.log("Time Selected!")
}

//TODO get current schedule(json) from backend at page load and update ui
let desired_json = {"motor1" : {
    "schedule": {
        "Monday"    :   ["01:00", "08:00"],
        "Tuesday"   :   ["02:00", "09:00"],
        "Wednesday" :   ["03:00", "10:00"],
        "Thursday"  :   ["04:00", "11:00"],
        "Friday"    :   ["05:00", "12:00"],
        "Saturday"  :   ["06:00", "13:00"],
        "Sunday"    :   ["07:00", "14:00"]
    },
    "startAngle" : 0,
    "endAngle" : 360,
    "time" : 30
}}

function DayOfTheWeek({scheduleData,motor,day,setScheduleData}){
    // console.log(scheduleData)
    // console.log(motor)
    // console.log(moment(scheduleData[motor].schedule))

    const [startTime, setStartTime] = useState(moment(scheduleData[motor].schedule[day][0], 'HH:mm'));
    const [endTime, setEndTime] = useState(moment(scheduleData[motor].schedule[day][1], 'HH:mm'));
    // const [startTime, setStartTime] = useState(moment('00:00', 'HH:mm'));
    // const [endTime, setEndTime] = useState(moment("00:00", 'HH:mm'));

    const setOpenTime = (time, timeString) => {
        setStartTime(timeString)
        
        const timeslice = [timeString, scheduleData[motor].schedule[day][1]]
        let newSchedule = scheduleData
        newSchedule[motor].schedule[day] = timeslice
        setScheduleData(newSchedule)
    };
    const setCloseTime = (time, timeString) => {
        setEndTime(timeString)
        const timeslice = [desired_json[motor].schedule[day][0], timeString]
        let newSchedule = scheduleData
        newSchedule[motor].schedule[day] = timeslice
        setScheduleData(newSchedule)
    };
    // function printData(){
    //     //create json
    //     console.log()

    //     //send json
    //     fetch(`http://192.168.0.14:8000/sendschedule?steps=${stepValue}`, {
    //         method: "POST",
    //         mode: "cors",
    //     })
    //     .then(response => response.json())
    //     .then(data => console.log(data));
    //     setStepValue(0);
    // }
    return(
        <Space direction='vertical' align='center' size="small" style={
            {padding: '1fr', color: "#4ec9b0"}
            }>
            <Typography style={{color:"#4ec9b0"}}>{day}</Typography>
            <TimePicker onChange={setOpenTime} defaultValue={startTime} className="openTime custom-hover" format="HH:mm" placeholder='Open Time'/>
            <TimePicker onChange={setCloseTime} defaultValue={endTime} className="closeTime custom-hover" format="HH:mm" placeholder='Close Time'/>
        </Space>
    )
}

function Schedule({scheduleData, setScheduleData, motor}){
    return(
        <Space style={{padding: '1fr'}}>
            <Space direction='Horizontal' align='center' size="small" >
                <DayOfTheWeek scheduleData={scheduleData} setScheduleData={setScheduleData} motor={motor} day="Monday"/>
                <DayOfTheWeek scheduleData={scheduleData} setScheduleData={setScheduleData} motor={motor} day="Tuesday" />
                <DayOfTheWeek scheduleData={scheduleData} setScheduleData={setScheduleData} motor={motor} day="Wednesday" />
                <DayOfTheWeek scheduleData={scheduleData} setScheduleData={setScheduleData} motor={motor} day="Thursday" />
                <DayOfTheWeek scheduleData={scheduleData} setScheduleData={setScheduleData} motor={motor} day="Friday" />
                <DayOfTheWeek scheduleData={scheduleData} setScheduleData={setScheduleData} motor={motor} day="Saturday" />
                <DayOfTheWeek scheduleData={scheduleData} setScheduleData={setScheduleData} motor={motor} day="Sunday" />
            </Space>
        </Space>
    )
}

export default Schedule