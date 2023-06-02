import Link from 'next/link';

export default function NotFound() {
  return (
    <div className="text-center mt-10">
      <h2>Not Found</h2>
      <p>
      <Link href="/">Go Home</Link>
      </p>
    </div>
  );
}