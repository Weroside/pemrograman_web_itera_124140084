import { Link } from "react-router-dom";
import { useBooks } from "../context/BookContext";
import { StatCard } from "../components/StatCard";
export function Stats() {
  const { books } = useBooks(),
    stats = [
      ["Total buku", books.length],
      ["Milik", books.filter((b) => b.status === "milik").length],
      ["Baca", books.filter((b) => b.status === "baca").length],
      ["Beli", books.filter((b) => b.status === "beli").length],
    ];
  return (
    <section>
      <small>RINGKASAN KOLEKSI</small>
      <h2>Statistik koleksi</h2>
      <div className="stats">
        {stats.map(([t, n]) => (
          <StatCard key={t} title={t} count={n} />
        ))}
      </div>
      <Link to="/">Kembali ke koleksi</Link>
    </section>
  );
}

Stats.propTypes = {};
