import PropTypes from "prop-types";

export function BookFilter({
  query,
  onQueryChange,
  status,
  onStatusChange,
  count,
}) {
  return (
    <div className="filters">
      <label>
        Cari judul atau penulis
        <input
          type="search"
          value={query}
          onChange={(e) => onQueryChange(e.target.value)}
          placeholder="Cari buku..."
        />
      </label>
      <label>
        Filter status
        <select value={status} onChange={(e) => onStatusChange(e.target.value)}>
          <option value="all">Semua status</option>
          <option value="milik">Milik</option>
          <option value="baca">Baca</option>
          <option value="beli">Beli</option>
        </select>
      </label>
      <span>{count} buku ditemukan</span>
    </div>
  );
}
BookFilter.propTypes = {
  query: PropTypes.string.isRequired,
  onQueryChange: PropTypes.func.isRequired,
  status: PropTypes.oneOf(["all", "milik", "baca", "beli"]).isRequired,
  onStatusChange: PropTypes.func.isRequired,
  count: PropTypes.number.isRequired,
};
