import { InputNumber, Space, Button, Typography } from 'antd';
import React from 'react'


function Config(props){

    return(
        <Space style={{padding: '1fr'}}>
            <Space direction='vertical' align='center' size="small" >
                <Space direction='Horizontal' align='center' size="small">
                <Typography style={{color:"#4ec9b0"}}>Time (s): </Typography>
                    <InputNumber className="custom-hover" defaultValue={10*60} style={{outlineColor: "#4ec9b0"}}/>
                </Space>
                <Button type="primary" shape="round" style = {{backgroundColor: "#9cdcfe", color: "#1e1e1e", borderColor: "#1e1e1e"}}>Set Open Position</Button>
                <Button type="primary" shape="round" style = {{backgroundColor: "#9cdcfe", color: "#1e1e1e", borderColor: "#1e1e1e"}}>Set Close Position</Button>
            </Space>
        </Space>
    )
}

export default Config