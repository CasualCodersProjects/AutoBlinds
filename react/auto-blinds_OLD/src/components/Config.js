import { InputNumber, Space } from 'antd';
import React from 'react'


function Config(props){

    return(
        <Space style={{padding: '1fr'}}>
            <Space direction='vertical' align='center' size="small" >
                <Space direction='Horizontal' align='center' size="small">
                    <text>Steps: </text>
                    <InputNumber defaultValue={0}/>
                </Space>
                <Space direction='Horizontal' align='center' size="small">
                    <text>Time: </text>
                    <InputNumber defaultValue={0}/>
                </Space>
            </Space>
        </Space>
    )
}

export default Config