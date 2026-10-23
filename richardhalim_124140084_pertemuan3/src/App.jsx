import { NavLink, Route, Routes } from "react-router-dom";
import { useBooks } from "./context/BookContext";
import { Home } from "./pages/Home";
import { Stats } from "./pages/Stats";
export { Provider } from "./context/BookContext";
export { Form } from "./components/BookForm";
export function App() {
  const { books, storageError } = useBooks();
  return (
    <div className="app">
      <header>
        <NavLink to="/" className="brand">
          LEMBAR <small>PERSONAL LIBRARY</small>
        </NavLink>
        <nav>
          <NavLink to="/" end>
            Koleksi
          </NavLink>
          <NavLink to="/stats">Statistik</NavLink>
        </nav>
        <span>Richard Halim · 124140084</span>
      </header>
      <main>
        {storageError && <p role="alert">{storageError}</p>}
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/stats" element={<Stats />} />
        </Routes>
      </main>
      <footer>PAW Pertemuan 3 · {books.length} buku dalam koleksi</footer>
    </div>
  );
}

App.propTypes = {};
