import { useState, useMemo } from "react";
import { useBooks } from "../context/BookContext";
import { Form } from "../components/BookForm";
import { BookFilter } from "../components/BookFilter";
export function Home() {
  const { books, add, update, remove } = useBooks(),
    [q, setQ] = useState(""),
    [status, setStatus] = useState("all"),
    [show, setShow] = useState(false),
    [editing, setEditing] = useState(null);
  const filtered = useMemo(
    () =>
      books.filter(
        (b) =>
          (b.title + " " + b.author)
            .toLowerCase()
            .includes(q.trim().toLowerCase()) &&
          (status === "all" || b.status === status),
      ),
    [books, q, status],
  );
  return (
    <>
      <section className="hero">
        <small>PERPUSTAKAAN PRIBADI</small>
        <h1>
          Koleksi buku,
          <br />
          <em>cerita yang bertumbuh.</em>
        </h1>
        <p>Richard Halim · NIM 124140084</p>
      </section>
      <section>
        <div className="heading">
          <h2>Daftar buku</h2>
          <button
            className="primary"
            onClick={() => {
              setEditing(null);
              setShow(!show);
            }}
          >
            + Tambah buku
          </button>
        </div>
        {show && (
          <Form
            onSave={(b) => {
              add(b);
              setShow(false);
            }}
          />
        )}
        {editing && (
          <Form
            key={editing.id}
            initial={editing}
            onSave={(b) => {
              update(editing.id, b);
              setEditing(null);
            }}
            onCancel={() => setEditing(null)}
          />
        )}
        <BookFilter
          query={q}
          onQueryChange={setQ}
          status={status}
          onStatusChange={setStatus}
          count={filtered.length}
        />
        <div className="list">
          {filtered.map((b) => (
            <article className="book" key={b.id}>
              <div className="cover">{b.title[0]}</div>
              <div className="bookbody">
                <small>
                  {{ milik: "MILIK", baca: "BACA", beli: "BELI" }[b.status]}{" "}
                  {b.year && " · " + b.year}
                </small>
                <h3>{b.title}</h3>
                <p>oleh {b.author}</p>
                <label>
                  Status{" "}
                  <select
                    aria-label={"Status " + b.title}
                    value={b.status}
                    onChange={(e) => update(b.id, { status: e.target.value })}
                  >
                    <option value="milik">Milik</option>
                    <option value="baca">Baca</option>
                    <option value="beli">Beli</option>
                  </select>
                </label>
                <div className="actions">
                  <button
                    onClick={() => {
                      setEditing(b);
                      setShow(false);
                    }}
                  >
                    Edit
                  </button>
                  <button
                    className="danger"
                    onClick={() => {
                      if (confirm("Hapus buku " + b.title + "?")) remove(b.id);
                    }}
                  >
                    Hapus
                  </button>
                </div>
              </div>
            </article>
          ))}
        </div>
        {!filtered.length && (
          <p className="empty">
            Tidak ada buku yang cocok. Ubah filter atau tambahkan buku.
          </p>
        )}
      </section>
    </>
  );
}

Home.propTypes = {};
