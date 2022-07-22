import { Space, InputNumber, Progress, Switch, Typography } from 'antd';
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
        <Space direction='vertical' align='center' size="middle">
            <Space direction='horizontal' align='center' size="small" >
            <Typography style={{color:"#4ec9b0"}}>{props.name}</Typography>
                <Switch defaultChecked={false} onChange={Toggle} style={{backgroundColor: "#9cdcfe"}}/>
            </Space>

            <Space direction='horizontal' align='center' size="small" >
            <Typography style={{color:"#4ec9b0"}}>Move +/-</Typography>
                <InputNumber className="custom-hover" defaultValue={0} value={stepValue} onChange={setStepValue} disabled={disabled} onPressEnter={sendSteps}/>
            </Space>

            <Progress type='dashboard' strokeWidth={15} showInfo={false} percent={50} disabled={disabled} strokeColor={"#9cdcfe"} trailColor={"#0e0e0e"}/>
        </Space>
    )
}

export default LiveInfo