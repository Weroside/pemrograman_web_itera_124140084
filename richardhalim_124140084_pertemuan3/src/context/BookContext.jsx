import { createContext, useContext } from "react";
import PropTypes from "prop-types";
import { useLocalStorage } from "../hooks/useLocalStorage";
const BookContext = createContext(null),
  KEY = "richardhalim-124140084-books",
  seed = [
    {
      id: "1",
      title: "Laut Bercerita",
      author: "Leila S. Chudori",
      year: 2017,
      status: "milik",
    },
    {
      id: "2",
      title: "Filosofi Teras",
      author: "Henry Manampiring",
      year: 2018,
      status: "baca",
    },
    {
      id: "3",
      title: "Bumi Manusia",
      author: "Pramoedya Ananta Toer",
      year: 1980,
      status: "beli",
    },
  ];
export function Provider({ children }) {
  const [books, setBooks, storageError] = useLocalStorage(KEY, seed);
  const add = (book) =>
    setBooks((old) => [{ ...book, id: crypto.randomUUID() }, ...old]);
  const update = (id, changes) =>
    setBooks((old) => old.map((b) => (b.id === id ? { ...b, ...changes } : b)));
  const remove = (id) => setBooks((old) => old.filter((b) => b.id !== id));
  return (
    <BookContext.Provider value={{ books, add, update, remove, storageError }}>
      {children}
    </BookContext.Provider>
  );
}
export function useBooks() {
  // Komponen membaca dan mengubah koleksi melalui context yang sama.
  const context = useContext(BookContext);
  if (!context) throw new Error("useBooks harus digunakan di dalam Provider");
  return context;
}

Provider.propTypes = { children: PropTypes.node.isRequired };
