from .views import mahasiswa, matakuliah
from .views.default import beranda


def includeme(config):
    config.add_route("beranda", "/")
    config.add_view(beranda, route_name="beranda", renderer="json")
    for nama, views in (("mahasiswa", mahasiswa), ("matakuliah", matakuliah)):
        for aksi, method, suffix in (
            ("daftar", "GET", ""),
            ("detail", "GET", "/{id}"),
            ("tambah", "POST", ""),
            ("ubah", "PUT", "/{id}"),
            ("hapus", "DELETE", "/{id}"),
        ):
            route = f"{nama}_{aksi}"
            config.add_route(route, f"/api/{nama}{suffix}",
                             request_method=method)
            config.add_view(views.handlers[aksi], route_name=route,
                            renderer="json")
