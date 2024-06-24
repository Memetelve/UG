import Link from 'next/link';

export default function Nav() {
  return (
    <ul className="mt-3">
      <li className="my-1"><Link className="hover:bg-orange-500 bg-orange-700 rounded-lg p-1 mb-3" href="/">Home</Link></li>
      <li className="my-1"><Link className="hover:bg-orange-500 bg-orange-700 rounded-lg p-1 mb-3" href="/products">Meetings</Link></li>
      <li className="my-1"><Link className="hover:bg-orange-500 bg-orange-700 rounded-lg p-1 mb-3" href="/admin">Admin</Link></li>
    </ul>
  );
}
