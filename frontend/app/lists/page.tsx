'use client';

import ListsComponent from '../components/ListsComponent'

export default function Lists() {
  return (
    <>
      <main className="flex flex-col items-center justify-between p-24 min-h-screen">
        <div className="z-10 max-w-5xl w-full items-start justify-between font-mono text-sm flex">
          <ListsComponent />
        </div>
      </main>
    </>
  );
}