import { TimePicker, Space, Switch, Input, Progress } from 'antd';
import moment from 'moment';
import './App.css';

// logo Header
// motor1
// motor2
// motor3

// const onChange = (checked: boolean) => {
//   console.log(`switch to ${checked}`);
// };

function App() {
  return (
<div className="container">
    <div className="logo">Logo</div>
    <div className="header">Header</div>
    <div className="motor1">
      <Space direction='vertical' align='center' size="large">
        <Switch className><div className="switch-label">Motor 1</div></Switch>
        <Input stepsInput1 className="input-label" placeholder="0" />
        <Progress className="potRotation1" type="dashboard" percent={50} showInfo={false} size='small' />
      </Space>
    </div>

    <div className="motor2">
      <Space direction='vertical' align='center' size="large">
        <Switch className><div className="switch-label">Motor 1</div></Switch>
        <Input stepsInput1 className="input-label" placeholder="0" />
        <Progress className="potRotation1" type="dashboard" percent={50} showInfo={false} />
      </Space>
    </div>
    
    <div className="motor3">
      <Space direction='vertical' align='center' size="large">
        <Switch className><div className="switch-label">Motor 1</div></Switch>
        <Input stepsInput1 className="input-label" placeholder="0" />
        <Progress className="potRotation1" type="dashboard" percent={50} showInfo={false} />
      </Space>
    </div>
</div>
  );
}

export default App;
