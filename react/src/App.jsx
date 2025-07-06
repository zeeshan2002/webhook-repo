import React, { useEffect, useState } from 'react';
import axios from 'axios';
import EventList from './components/EventList';

const API_URL = 'http://127.0.0.1:5000/events';

function App() {
  const [events, setEvents] = useState([]);
  const [loading, setLoading] = useState(true);

  const fetchEvents = async () => {
    try {
      const res = await axios.get(API_URL);
      console.log("res: ", res.data)
      setEvents(res.data);
    } catch (err) {
      setEvents([]);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchEvents();
    const interval = setInterval(fetchEvents, 15000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="min-h-screen flex flex-col items-center p-6 bg-gray-50">
      <h1 className="text-2xl font-bold mb-6">Repository Activity Feed</h1>
      <div className="w-full max-w-xl">
        <EventList events={events} loading={loading} />
      </div>
    </div>
  );
}

export default App; 