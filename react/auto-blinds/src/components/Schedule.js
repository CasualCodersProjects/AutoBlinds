import { TimePicker, Space } from 'antd';
import React from 'react'

function DayOfTheWeek(props){
    return(
        <Space direction='vertical' align='center' size="small" style={{padding: '1fr'}}>
            <text>{props.day}</text>
            <TimePicker className="timePicker1" format="HH:mm" />
            <TimePicker className="timePicker1" format="HH:mm" aria-label='Hello'/>
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