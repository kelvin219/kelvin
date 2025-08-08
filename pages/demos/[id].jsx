import Link from 'next/link';
import { useRouter } from 'next/router';

export default function DemoDetail() {
  const router = useRouter();
  const { id } = router.query;

  return (
    <main>
      <h1>Demo Detail</h1>
      <p>Currently viewing demo: {id}</p>
      <nav>
        <Link href="/demos">Back to Demos</Link>
      </nav>
    </main>
  );
}
