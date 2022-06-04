import { TimePicker, Space, Switch, Input, Progress } from 'antd';
import moment from 'moment';
import './App.css';
import ControlsBlock from './components/ControlsBlock';

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
      <ControlsBlock/>
    </div>

    <div className="motor2">
      <ControlsBlock/>
    </div>
    
    <div className="motor3">
      <ControlsBlock/>
    </div>
</div>
  );
}

export default App;
