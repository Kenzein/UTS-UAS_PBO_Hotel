class Kamar:
    def __init__(self, nomor, tipe, harga_per_malam):
        self.nomor = nomor
        self.tipe = tipe
        self.harga = harga_per_malam
        self.status = "Tersedia"

    def ubah_status(self, status_baru):
        status_valid = ["Tersedia", "Dipesan", "Terisi"]
        if status_baru not in status_valid:
            raise ValueError(
                f"Status {status_baru} tidak valid. Gunakan {status_valid}"
            )
        self.status = status_baru

    def __str__(self):
        return f"Kamar {self.nomor} ({self.tipe}) - Rp{self.harga:,}/malam - Status: {self.status}"
