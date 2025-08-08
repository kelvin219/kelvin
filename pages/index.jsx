import Link from 'next/link';

export default function Home() {
  return (
    <main>
      <h1>Welcome to Kelvin App</h1>
      <nav>
        <Link href="/demos">View Demos</Link>
      </nav>
    </main>
  );
}
