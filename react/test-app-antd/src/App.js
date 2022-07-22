import './App.css';
import React, {useState} from 'react';
import Schedule from './components/Schedule';
import LiveInfo from './components/LiveInfo';
import Config from './components/Config';
import useAsyncEffect from 'use-async-effect';

function App() {

  const [scheduleData, setScheduleData] = useState(null);

  useAsyncEffect(async () => {
    const resp = await fetch('http://localhost:80/get_schedule');
    const data = await resp.json()

    setScheduleData(data);
  }, [])

  async function saveScheduleDataToServer(data){
    const resp = await fetch(`http://localhost:80/update_schedule?schedule_data=${JSON.stringify(data)}`,{
      method: 'POST',
      mode: "cors",
    })
    const apidata = await resp.json()
    setScheduleData(data)
    return
  };

  return (
    <div className="container">
      <div className="motor1">
        <LiveInfo name="Motor1 Enable:" />
      </div>
      <div className="motor2">
        <LiveInfo name="Motor2 Enable:" />
      </div>
      <div className="motor3">
        <LiveInfo name="Motor3 Enable:" />
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


      <div className="schedule1">
        {scheduleData ? <Schedule scheduleData={scheduleData} setScheduleData={saveScheduleDataToServer} motor="motor1"/> : null}
      </div>
      <div className="schedule2" >
        {scheduleData ? <Schedule scheduleData={scheduleData} setScheduleData={saveScheduleDataToServer} motor="motor2"/> : null}
      </div>
      <div className="schedule3" >
        {scheduleData ? <Schedule scheduleData={scheduleData} setScheduleData={saveScheduleDataToServer} motor="motor3"/> : null}
      </div>

    </div>
  );
}

export default App;
