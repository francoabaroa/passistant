'use client';

import RemindersComponent from '../components/RemindersComponent'

export default function Reminders() {
  return (
    <>
      <main className="flex flex-col items-center justify-between p-24 min-h-screen">
        <div className="z-10 max-w-5xl w-full items-start justify-between font-mono text-sm flex">
          <RemindersComponent />
        </div>
      </main>
    </>
  );
}
