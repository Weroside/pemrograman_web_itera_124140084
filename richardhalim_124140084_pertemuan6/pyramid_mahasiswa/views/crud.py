from pyramid.httpexceptions import HTTPBadRequest, HTTPNotFound
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError


def error(cls, pesan):
    return cls(json_body={"error": pesan})


def baca_data(request, teks, angka, wajib):
    try:
        data = request.json_body
    except ValueError:
        raise error(HTTPBadRequest, "Isi permintaan harus berupa JSON.")
    if not isinstance(data, dict):
        raise error(HTTPBadRequest, "Isi JSON harus berupa objek.")
    hasil = {}
    for key in (*teks, *angka):
        if key not in data:
            if wajib:
                raise error(HTTPBadRequest, f"{key} wajib diisi.")
            continue
        nilai = data[key]
        if key in teks:
            if not isinstance(nilai, str) or not nilai.strip():
                raise error(HTTPBadRequest, f"{key} harus berupa teks.")
            hasil[key] = nilai.strip()
        else:
            if type(nilai) is not int or not 0 < nilai <= 2147483647:
                raise error(HTTPBadRequest, f"{key} harus integer positif.")
            hasil[key] = nilai
    if not hasil:
        raise error(HTTPBadRequest, "Tidak ada kolom yang dapat diperbarui.")
    return hasil


def buat_handlers(model, teks, angka=()):
    def ambil(db, request):
        try:
            item_id = int(request.matchdict["id"])
        except ValueError:
            item_id = 0
        item = db.get(model, item_id) if 0 < item_id <= 2147483647 else None
        if item is None:
            raise error(HTTPNotFound, "Data tidak ditemukan.")
        return item

    def daftar(request):
        with request.registry.sessions() as db:
            return [item.to_dict() for item in
                    db.scalars(select(model).order_by(model.id))]

    def detail(request):
        with request.registry.sessions() as db:
            return ambil(db, request).to_dict()

    def simpan(request, baru):
        try:
            with request.registry.sessions.begin() as db:
                data = baca_data(request, teks, angka, wajib=baru)
                if baru:
                    item = model(**data)
                    db.add(item)
                else:
                    item = ambil(db, request)
                    for key, nilai in data.items():
                        setattr(item, key, nilai)
                db.flush()
                return item.to_dict()
        except IntegrityError:
            raise error(HTTPBadRequest, f"{teks[0]} sudah digunakan.")

    def tambah(request):
        return simpan(request, baru=True)

    def ubah(request):
        return simpan(request, baru=False)

    def hapus(request):
        with request.registry.sessions.begin() as db:
            db.delete(ambil(db, request))
        return {"pesan": "Data berhasil dihapus."}

    return dict(daftar=daftar, detail=detail, tambah=tambah, ubah=ubah,
                hapus=hapus)
