from ..models import Mahasiswa
from .crud import buat_handlers

handlers = buat_handlers(Mahasiswa, ("nim", "nama", "jurusan"))
