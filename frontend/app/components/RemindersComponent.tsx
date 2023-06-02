'use client';

import { useEffect, useState } from 'react'

type Reminder = {
  id: number;
  name: string;
  details: string;
  original_text: string;
  due_date: string | null;
  due_time: string | null;
  start_date: string | null;
  source: string | null;
  completed: boolean;
  completion_date: string | null;
  priority: string | null;
  type: string | null;
  archived: boolean;
  member_id: number;
};

export default function RemindersComponent() {
  const [reminders, setReminders] = useState<Reminder[]>([]);

  useEffect(() => {
    fetch("http://localhost:5000/api/reminders")
      .then(res => res.json())
      .then(data => setReminders(data));
  }, []);

  return (
    <div className="mt-10 mr-8">
      <h1 className="mb-3 text-2xl font-semibold">Reminders</h1>
      {reminders.map(reminder => (
        <div key={reminder.id} className="border p-2 rounded my-2">
          <h2 className="font-bold" style={{ fontSize: '1.5em', paddingBottom: '10px' }}>{reminder.name}</h2>
          <p className="pb-2"><b>Details:</b> {reminder.details}</p>
          <p className="pb-2"><b>Due Date:</b> {reminder.due_date}</p>
          <p className="pb-2"><b>Due Time:</b> {reminder.due_time}</p>
          <p className="pb-2"><b>Original Text:</b> {reminder.original_text}</p>
          <p className="pb-2"><b>Source:</b> {reminder.source}</p>
          <p className="pb-2"><b>Priority:</b> {reminder.priority}</p>
          <p className="pb-2"><b>Type:</b> {reminder.type}</p>
        </div>
      ))}
    </div>
  );
}
