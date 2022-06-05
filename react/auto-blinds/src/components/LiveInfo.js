import { Space, InputNumber, Progress, Switch } from 'antd';
import React from 'react'



function LiveInfo(props){
    const [disabled, setDisabled] = React.useState(true);

    const Toggle = () => { setDisabled(!disabled); }


    return(
        <Space direction='vertical' align='center' size="middle" style={{padding: '10px'}}>
            <Space direction='horizontal' align='center' size="small" >
                <text>{props.name}</text>
                <Switch defaultChecked={false} onChange={Toggle}/>
            </Space>
            <Space direction='horizontal' align='center' size="small" >
                <text>Move +/-</text>
                <InputNumber defaultValue={0} disabled={disabled}/>
            </Space>
            <Progress type='dashboard' width={80} strokeWidth={15}
            showInfo={false} percent={50} disabled={disabled}
            strokeColor="#4ec9b0"/>


        </Space>
    )
}

export default LiveInfo