import { useEffect, useState } from "react";

export function useLocalStorage(key, initial) {
  const [storageError, setStorageError] = useState("");
  const [value, setValue] = useState(() => {
    try {
      const saved = JSON.parse(window.localStorage.getItem(key));
      if (!Array.isArray(saved)) return initial;
      // Data versi awal menggunakan kategori membaca yang berbeda.
      const oldStatus = { unread: "milik", reading: "baca", finished: "milik" };
      return saved
        .filter(
          (book) =>
            book &&
            typeof book.id === "string" &&
            typeof book.title === "string" &&
            book.title.trim() &&
            typeof book.author === "string" &&
            book.author.trim(),
        )
        .map((book) => ({
          ...book,
          status:
            oldStatus[book.status] ||
            (["milik", "baca", "beli"].includes(book.status)
              ? book.status
              : "milik"),
        }));
    } catch {
      return initial;
    }
  });
  useEffect(() => {
    try {
      window.localStorage.setItem(key, JSON.stringify(value));
      setStorageError("");
    } catch {
      setStorageError(
        "Data belum dapat disimpan di browser. Periksa ruang penyimpanan.",
      );
    }
  }, [key, value]);
  return [value, setValue, storageError];
}
