import './App.css';
import Schedule from './components/Schedule';
import LiveInfo from './components/LiveInfo';
import Config from './components/Config';

// Colors:
// Teal:        #4ec9b0
// Light Blue:  #9cdcfe
// Grey:        #1e1e1e
// Dark Grey:   #0e0e0e


function App() {
  return (
<div className="container">
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

  <div className="config1">
    <Config/>
  </div>
  <div className="config2">
    <Config/>
  </div>
  <div className="config3">
    <Config/>
  </div>
</div>
  );
}

export default App;
