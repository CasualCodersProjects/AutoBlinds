import { TimePicker, Space, Switch, Input, Progress } from 'antd';
import React from 'react'

function ControlsBlock(props) {
  return (
    <Space>
        <Space direction='vertical' align='center' size="large">
            <Switch className><div className="switch-label">Motor 1</div></Switch>
            <Input stepsInput1 className="input-label" placeholder="0" />
            <Progress className="potRotation1" type="dashboard" percent={50} showInfo={false} size='small' />
        </Space>
        <Space direction='vertical' align='center' size="large">
            <Space direction='Horizontal' align='center' size="large" >
                <TimePicker className="timePicker1" format="HH:mm" />
                <TimePicker className="timePicker1" format="HH:mm" />
                <TimePicker className="timePicker1" format="HH:mm" />
                <TimePicker className="timePicker1" format="HH:mm" />
                <TimePicker className="timePicker1" format="HH:mm" />
                <TimePicker className="timePicker1" format="HH:mm" />
                <TimePicker className="timePicker1" format="HH:mm" />
            </Space>
            <Space direction='Horizontal' align='center' size="large" >
                <TimePicker className="timePicker1" format="HH:mm" />
                <TimePicker className="timePicker1" format="HH:mm" />
                <TimePicker className="timePicker1" format="HH:mm" />
                <TimePicker className="timePicker1" format="HH:mm" />
                <TimePicker className="timePicker1" format="HH:mm" />
                <TimePicker className="timePicker1" format="HH:mm" />
                <TimePicker className="timePicker1" format="HH:mm" />
            </Space>
        </Space>
    </Space>
  )
}

export default ControlsBlock