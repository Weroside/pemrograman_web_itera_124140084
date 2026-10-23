import React from "react";
import { beforeEach, expect, it, vi } from "vitest";
import { fireEvent, render, screen, within } from "@testing-library/react";
import { MemoryRouter } from "react-router-dom";
import { App, Form, Provider } from "./App";
const key = "richardhalim-124140084-books";
const records = [
  {
    id: "a",
    title: "Laut Bercerita",
    author: "Leila",
    status: "milik",
    year: 2017,
  },
  {
    id: "b",
    title: "Filosofi Teras",
    author: "Henry",
    status: "baca",
    year: 2018,
  },
  {
    id: "c",
    title: "Bumi Manusia",
    author: "Pramoedya",
    status: "beli",
    year: 1980,
  },
];
function openApp() {
  return render(
    <MemoryRouter>
      <Provider>
        <App />
      </Provider>
    </MemoryRouter>,
  );
}
function card(title) {
  return screen.getByRole("heading", { name: title }).closest("article");
}
beforeEach(() => {
  vi.restoreAllMocks();
  window.localStorage.clear();
  window.localStorage.setItem(key, JSON.stringify(records));
});
it("menampilkan data tersimpan", () => {
  openApp();
  expect(screen.getAllByRole("heading", { level: 3 })).toHaveLength(3);
});
it("menambah buku dan menyimpannya", () => {
  openApp();
  fireEvent.click(screen.getByRole("button", { name: "+ Tambah buku" }));
  fireEvent.change(screen.getByLabelText("Judul buku"), {
    target: { value: "Dune" },
  });
  fireEvent.change(screen.getByLabelText("Penulis"), {
    target: { value: "Frank Herbert" },
  });
  fireEvent.click(
    screen.getByRole("button", { name: "Tambah buku", exact: true }),
  );
  expect(card("Dune")).toBeInTheDocument();
  expect(JSON.parse(window.localStorage.getItem(key))).toHaveLength(4);
});
it("menolak isian kosong", () => {
  const save = vi.fn();
  render(<Form onSave={save} />);
  fireEvent.click(screen.getByRole("button", { name: "Tambah buku" }));
  expect(screen.getByRole("alert")).toHaveTextContent("wajib diisi");
  expect(save).not.toHaveBeenCalled();
});
it("menolak tahun yang tidak valid", () => {
  const save = vi.fn();
  render(<Form onSave={save} />);
  fireEvent.change(screen.getByLabelText("Judul buku"), {
    target: { value: "Dune" },
  });
  fireEvent.change(screen.getByLabelText("Penulis"), {
    target: { value: "Frank" },
  });
  fireEvent.change(screen.getByLabelText("Tahun terbit"), {
    target: { value: "3000" },
  });
  fireEvent.click(screen.getByRole("button", { name: "Tambah buku" }));
  expect(screen.getByRole("alert")).toHaveTextContent(
    "Tahun terbit tidak valid",
  );
  expect(save).not.toHaveBeenCalled();
});
it("mengedit judul", () => {
  openApp();
  fireEvent.click(
    within(card("Laut Bercerita")).getByRole("button", { name: "Edit" }),
  );
  fireEvent.change(screen.getByLabelText("Judul buku"), {
    target: { value: "Laut Edisi Baru" },
  });
  fireEvent.click(screen.getByRole("button", { name: "Simpan perubahan" }));
  expect(card("Laut Edisi Baru")).toBeInTheDocument();
});
it("mengganti isian ketika beralih buku yang diedit", () => {
  openApp();
  fireEvent.click(
    within(card("Laut Bercerita")).getByRole("button", { name: "Edit" }),
  );
  fireEvent.click(
    within(card("Filosofi Teras")).getByRole("button", { name: "Edit" }),
  );
  expect(screen.getByLabelText("Judul buku")).toHaveValue("Filosofi Teras");
});
it("menghapus setelah konfirmasi", () => {
  vi.spyOn(window, "confirm").mockReturnValue(true);
  openApp();
  fireEvent.click(
    within(card("Laut Bercerita")).getByRole("button", { name: "Hapus" }),
  );
  expect(
    screen.queryByRole("heading", { name: "Laut Bercerita" }),
  ).not.toBeInTheDocument();
  expect(JSON.parse(window.localStorage.getItem(key))).toHaveLength(2);
});
it("membatalkan penghapusan", () => {
  vi.spyOn(window, "confirm").mockReturnValue(false);
  openApp();
  fireEvent.click(
    within(card("Laut Bercerita")).getByRole("button", { name: "Hapus" }),
  );
  expect(card("Laut Bercerita")).toBeInTheDocument();
});
it("mencari judul dan nama penulis", () => {
  openApp();
  const search = screen.getByLabelText("Cari judul atau penulis");
  fireEvent.change(search, { target: { value: "LAUT" } });
  expect(screen.getAllByRole("heading", { level: 3 })).toHaveLength(1);
  fireEvent.change(search, { target: { value: "henry" } });
  expect(card("Filosofi Teras")).toBeInTheDocument();
});
it("memfilter status dan menampilkan hasil kosong", () => {
  openApp();
  fireEvent.change(screen.getByLabelText("Filter status"), {
    target: { value: "beli" },
  });
  expect(screen.getAllByRole("heading", { level: 3 })).toHaveLength(1);
  expect(card("Bumi Manusia")).toBeInTheDocument();
  fireEvent.change(screen.getByLabelText("Cari judul atau penulis"), {
    target: { value: "tidak ada" },
  });
  expect(screen.getByText(/Tidak ada buku yang cocok/)).toBeInTheDocument();
});
it("memperbarui status dan statistik melalui navigasi", () => {
  openApp();
  fireEvent.change(screen.getByLabelText("Status Laut Bercerita"), {
    target: { value: "baca" },
  });
  fireEvent.click(screen.getByRole("link", { name: "Statistik" }));
  expect(
    screen.getByRole("heading", { name: "Statistik koleksi" }),
  ).toBeInTheDocument();
  expect(screen.getByText("Baca").closest("article")).toHaveTextContent("2");
});
it("memulihkan data yang rusak", () => {
  window.localStorage.setItem(key, "{rusak");
  openApp();
  expect(card("Laut Bercerita")).toBeInTheDocument();
});
it("memberi pesan jika penyimpanan gagal", () => {
  vi.spyOn(Storage.prototype, "setItem").mockImplementation(() => {
    throw new Error("penuh");
  });
  openApp();
  expect(screen.getByRole("alert")).toHaveTextContent(
    "Data belum dapat disimpan",
  );
});
