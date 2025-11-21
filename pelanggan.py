import uuid


class Pelanggan:
    def __init__(self, nama, kontak):
        self.id_pelanggan = str(uuid.uuid4())
        self.nama = nama
        self.kontak = kontak

    def __str__(self):
        return f"{self.nama} (ID: {self.id_pelanggan[:6]})"
