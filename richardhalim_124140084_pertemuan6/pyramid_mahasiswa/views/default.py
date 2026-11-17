def beranda(request):
    return {"api": "Data akademik", "endpoint": [
        "/api/mahasiswa", "/api/matakuliah",
    ]}
