'use client';

export default function AppBar() {

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
              <a href="/" className="text-2xl font-bold text-gray-700">passistant</a>
            </div>
          </div>
          <div className="hidden lg:block lg:w-3/4">
            <div className="flex justify-end">
              <a href="/dashboard" className="px-3 py-2 text-sm font-medium text-gray-500 hover:text-gray-700">Dashboard</a>
              <a href="/reminders" className="px-3 py-2 text-sm font-medium text-gray-500 hover:text-gray-700">Reminders</a>
              <a href="/lists" className="px-3 py-2 text-sm font-medium text-gray-500 hover:text-gray-700">Lists</a>
              <a href="/calendar" className="px-3 py-2 text-sm font-medium text-gray-500 hover:text-gray-700">Calendar</a>
              <a href="/settings" className="px-3 py-2 text-sm font-medium text-gray-500 hover:text-gray-700">Settings</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
