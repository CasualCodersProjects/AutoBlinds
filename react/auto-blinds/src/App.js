import './App.css';
import Schedule from './components/Schedule';
import LiveInfo from './components/LiveInfo';
import React from 'react'
// logo Header
// motor1
// motor2
// motor3

// const onChange = (checked: boolean) => {
//   console.log(`switch to ${checked}`);
// };

function App() {
  document.body.classList.add("dark");
  return (
<div className="container">
  <div className="logo">Logo</div>  
  <div className="header">Header</div>
  <div className="schedule1">
    <Schedule/>
  </div>
  <div className="schedule2">
    <Schedule/>
  </div>
  <div className="schedule3">
    <Schedule/>
  </div>
  <div className="motor1">
    <LiveInfo name="Motor1 Enable"/>
  </div>
  <div className="motor2">
    <LiveInfo name="Motor2 Enable"/>
  </div>
  <div className="motor3">
    <LiveInfo name="Motor3 Enable"/>
  </div>

</div>
  );
}

export default App;
