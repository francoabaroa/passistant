export default function NotFound() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-md w-full">
        <div className="text-center">
          <h2 className="mt-2 text-4xl font-extrabold text-gray-900">
            Page Not Found
          </h2>
          <p className="mt-2 text-base text-gray-500">Sorry, we couldn’t find the page you’re looking for.</p>
          <div className="mt-6">
            <div className="hidden lg:block lg:ml-10">
              <a href="/" className="text-base font-medium text-indigo-600 hover:text-indigo-500">Go back home<span aria-hidden="true"> &rarr;</span></a>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}