import { useState } from "react";
import PropTypes from "prop-types";
export function Form({ initial, onSave, onCancel }) {
  const [form, setForm] = useState(
      initial || { title: "", author: "", year: "", status: "milik" },
    ),
    [error, setError] = useState("");
  function submit(e) {
    e.preventDefault();
    if (!form.title.trim() || !form.author.trim()) {
      setError("Judul dan penulis wajib diisi.");
      return;
    }
    if (
      form.year &&
      (!Number.isInteger(Number(form.year)) ||
        Number(form.year) < 0 ||
        Number(form.year) > new Date().getFullYear())
    ) {
      setError("Tahun terbit tidak valid.");
      return;
    }
    onSave({
      ...form,
      title: form.title.trim(),
      author: form.author.trim(),
      year: form.year ? Number(form.year) : null,
    });
    if (!initial) setForm({ title: "", author: "", year: "", status: "milik" });
    setError("");
  }
  return (
    <form className="panel form" onSubmit={submit} noValidate>
      <div className="fields">
        <label>
          Judul buku
          <input
            required
            maxLength="120"
            aria-invalid={!!error && !form.title.trim()}
            value={form.title}
            onChange={(e) => setForm({ ...form, title: e.target.value })}
          />
        </label>
        <label>
          Penulis
          <input
            required
            value={form.author}
            onChange={(e) => setForm({ ...form, author: e.target.value })}
          />
        </label>
        <label>
          Tahun terbit
          <input
            type="number"
            min="0"
            max={new Date().getFullYear()}
            value={form.year || ""}
            onChange={(e) => setForm({ ...form, year: e.target.value })}
          />
        </label>
        <label>
          Status
          <select
            value={form.status}
            onChange={(e) => setForm({ ...form, status: e.target.value })}
          >
            <option value="milik">Milik</option>
            <option value="baca">Baca</option>
            <option value="beli">Beli</option>
          </select>
        </label>
      </div>
      {error && (
        <p role="alert" className="form-error">
          {error}
        </p>
      )}
      <button className="primary">
        {initial ? "Simpan perubahan" : "Tambah buku"}
      </button>
      {onCancel && (
        <button type="button" onClick={onCancel}>
          Batal
        </button>
      )}
    </form>
  );
}

Form.propTypes = {
  initial: PropTypes.shape({
    id: PropTypes.string,
    title: PropTypes.string.isRequired,
    author: PropTypes.string.isRequired,
    status: PropTypes.oneOf(["milik", "baca", "beli"]).isRequired,
    year: PropTypes.number,
  }),
  onSave: PropTypes.func.isRequired,
  onCancel: PropTypes.func,
};
