from ..models import Matakuliah
from .crud import buat_handlers

handlers = buat_handlers(Matakuliah, ("kode_mk", "nama_mk"),
                        ("sks", "semester"))
