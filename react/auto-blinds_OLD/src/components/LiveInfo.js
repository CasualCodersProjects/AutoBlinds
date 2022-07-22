import { Space, InputNumber, Progress, Switch } from 'antd';
import React, { useState } from 'react';


// Colors:
const Teal =      '#4ec9b0';
const LightBlue = '#9cdcfe';
const Grey =      '#1e1e1e';
const DarkGrey =  '#0e0e0e';

function LiveInfo(props){
    const [disabled, setDisabled] = useState(true);
    const Toggle = () => { setDisabled(!disabled); }

    const [stepValue, setStepValue] = useState(0);
    function sendSteps(){
        fetch(`http://192.168.0.14:8000/sendsteps?steps=${stepValue}`, {
            method: "POST",
            mode: "cors",
        })
        .then(response => response.json())
        .then(data => console.log(data));
        setStepValue(0);
    }


    return(
        <Space direction='vertical' align='center' size="middle" className='LiveInfo general-theme'>
            <Space direction='horizontal' align='center' size="small" >
                <text>{props.name}</text>
                <Switch defaultChecked={false} onChange={Toggle} style={
                    {backgroundColor: LightBlue, borderColor: Teal}
                }/>
            </Space>

            <Space direction='horizontal' align='center' size="small" >
                <text>Move +/-</text>
                <InputNumber defaultValue={0} value={stepValue} onChange={setStepValue} disabled={disabled} onPressEnter={sendSteps} style={
                    {backgroundColor: DarkGrey, borderColor: Teal, color: LightBlue, accentColor: LightBlue}
                }/>
            </Space>

            <Progress type='dashboard' strokeWidth={15} showInfo={false} percent={50} disabled={disabled} strokeColor={Teal} trailColor={DarkGrey}/>
        </Space>
    )
}

export default LiveInfo