'use client';

import { useEffect, useState } from 'react'

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
  source: string | null;
  type: string | null;
  archived: boolean;
  member_id: number;
  list_items: ListItem[];
};

export default function ListsComponent() {
  const [lists, setLists] = useState<List[]>([]);
  const [expandedListId, setExpandedListId] = useState<number | null>(null);

  useEffect(() => {
    fetch("http://localhost:5000/api/lists")
      .then(res => res.json())
      .then(data => setLists(data));
  }, []);

  const toggleListItems = (listId: number) => {
    setExpandedListId(listId !== expandedListId ? listId : null);
  };

  return (
    <div className="mt-10">
      <h1 className="mb-3 text-2xl font-semibold">Lists</h1>
      {lists.map(list => (
        <div key={list.id} className="border p-2 rounded my-2">
          <h2 className="font-bold" style={{ fontSize: '1.5em', paddingBottom: '10px' }}>{list.name}</h2>
          <p className="pb-2"><b>Type:</b> {list.type}</p>
          <p className="pb-2"><b>Original Text:</b> {list.original_text}</p>
          <p className="pb-2"><b>Due Date:</b> {list.due_date}</p>
          <p className="pb-2"><b>Source:</b> {list.source}</p>
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
  );
}
