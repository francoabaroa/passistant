'use client';

import { useEffect, useState } from 'react'
import AppBar from './components/AppBar';

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

type ListItem = {
  id: number;
  name: string;
  quantity: string;
  completed: boolean;
  favorited: boolean;
};

type List = {
  id: number;
  name: string;
  original_text: string;
  due_date: string | null;
  type: string | null;
  archived: boolean;
  member_id: number;
  list_items: ListItem[];
};

export default function Home() {
  const [reminders, setReminders] = useState<Reminder[]>([]);
  const [lists, setLists] = useState<List[]>([]);
  const [expandedListId, setExpandedListId] = useState<number | null>(null);

  useEffect(() => {
    fetch("http://localhost:5000/api/reminders")
      .then(res => res.json())
      .then(data => setReminders(data));

    fetch("http://localhost:5000/api/lists")
      .then(res => res.json())
      .then(data => setLists(data));
  }, []);

  const toggleListItems = (listId: number) => {
    setExpandedListId(listId !== expandedListId ? listId : null);
  };

  return (
    <>
      <AppBar />
      <main className="flex flex-col items-center justify-between p-24 min-h-screen">
        <div className="z-10 max-w-5xl w-full items-start justify-between font-mono text-sm flex">
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
          <div className="mt-10">
            <h1 className="mb-3 text-2xl font-semibold">Lists</h1>
            {lists.map(list => (
              <div key={list.id} className="border p-2 rounded my-2">
                <h2 className="font-bold" style={{ fontSize: '1.5em', paddingBottom: '10px' }}>{list.name}</h2>
                <p className="pb-2"><b>Type:</b> {list.type}</p>
                <p className="pb-2"><b>Original Text:</b> {list.original_text}</p>
                <p className="pb-2"><b>Due Date:</b> {list.due_date}</p>
                <h4 className="cursor-pointer flex items-center" onClick={() => toggleListItems(list.id)}>
                  List Items:
                  {expandedListId === list.id ?
                    <span style={{ transform: 'rotate(90deg)', fontSize: '32px' }}>➤</span> :
                    <span style={{ fontSize: '32px' }}>➤</span>
                  }
                </h4>
                {expandedListId === list.id && list.list_items.map(item => (
                  <div key={item.id} className="border p-3 rounded my-2">
                    <p><b>Name:</b> {item.name}</p>
                    <p><b>Quantity:</b> {item.quantity}</p>
                  </div>
                ))}
              </div>
            ))}
          </div>
        </div>
      </main>
    </>
  );
}
