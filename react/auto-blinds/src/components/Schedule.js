import { TimePicker, Space } from 'antd';
import React from 'react'

// Colors:
// Teal:        #4ec9b0
// Light Blue:  #9cdcfe
// Grey:        #1e1e1e
// Dark Grey:   #0e0e0e

function DayOfTheWeek(props){
    return(
        <Space direction='vertical' align='center' size="small" style={
            {padding: '1fr', color: "#4ec9b0"}
            }>
            <text>{props.day}</text>
            <TimePicker className="openTime dropdown-menu" format="HH:mm" placeholder='Open Time'/>
            <TimePicker className="closeTime dropdown-menu" format="HH:mm" placeholder='Close Time'/>
        </Space>
    )
}

function Schedule(){
    return(
        <Space style={{padding: '1fr'}}>
            <Space direction='Horizontal' align='center' size="small" >
                <DayOfTheWeek day="Monday" />
                <DayOfTheWeek day="Tuesday" />
                <DayOfTheWeek day="Wednesday" />
                <DayOfTheWeek day="Thursday" />
                <DayOfTheWeek day="Friday" />
                <DayOfTheWeek day="Saturday" />
                <DayOfTheWeek day="Sunday" />
            </Space>
        </Space>
    )
}

export default Schedule