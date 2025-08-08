import Link from 'next/link';

const demos = ['demo1', 'demo2'];

export default function DemoList() {
  return (
    <main>
      <h1>Demos</h1>
      <nav>
        <Link href="/">Home</Link>
      </nav>
      <ul>
        {demos.map((id) => (
          <li key={id}>
            <Link href={`/demos/${id}`}>{id}</Link>
          </li>
        ))}
      </ul>
    </main>
  );
}
