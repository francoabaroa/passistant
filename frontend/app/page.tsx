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

const AppBar: React.FC = () => {
  return (
    <div className="p-4 bg-white shadow-md">
      <div className="max-w-7xl mx-auto px-2 sm:px-6 lg:px-8">
        <div className="relative flex items-center justify-between h-16">
          <div className="flex items-center px-2 lg:px-0 xl:w-1/4">
            <div className="flex items-center lg:hidden">
              {/* Mobile menu button */}
              <button className="p-2 rounded-md inline-flex items-center justify-center text-gray-400 hover:text-gray-500 hover:bg-gray-100 focus:outline-none">
                {/* Icon when menu is closed. */}
                <svg className="block h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
                </svg>
              </button>
            </div>
            <div className="hidden lg:block lg:ml-10">
              <a href="#" className="text-2xl font-bold text-gray-700">smilo</a> {/* replace "AppName" with your app name */}
            </div>
          </div>
          <div className="hidden lg:block lg:w-3/4">
            <div className="flex justify-end">
              <a href="#" className="px-3 py-2 text-sm font-medium text-gray-500 hover:text-gray-700">Home</a>
              <a href="#" className="px-3 py-2 text-sm font-medium text-gray-500 hover:text-gray-700">Reminders</a>
              <a href="#" className="px-3 py-2 text-sm font-medium text-gray-500 hover:text-gray-700">Lists</a>
              <a href="#" className="px-3 py-2 text-sm font-medium text-gray-500 hover:text-gray-700">Calendar</a>
              <a href="#" className="px-3 py-2 text-sm font-medium text-gray-500 hover:text-gray-700">Settings</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
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
