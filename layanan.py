class LayananTambahan:
    def __init__(self, nama, biaya):
        self.nama = nama
        self.biaya = biaya

    def hitung_biaya(self):
        return self.biaya

    def __str__(self):
        return f"{self.nama} - Rp{self.biaya:,.0f}"


class LayananLaundry(LayananTambahan):
    def __init__(self, jumlah_pakaian):
        super().__init__("Laundry", 10000 * jumlah_pakaian)
        self.jumlah_pakaian = jumlah_pakaian

    def __str__(self):
        return f"Laundry ({self.jumlah_pakaian} pcs) - Rp{self.biaya:,.0f}"


class LayananRoomService(LayananTambahan):
    def __init__(self, menu, harga):
        super().__init__(f"Room Service - {menu}", harga)
        self.menu = menu
        self.harga = harga

    def __str__(self):
        return f"Room Service ({self.menu}) - Rp{self.biaya:,.0f}"


class LayananSewaMobil(LayananTambahan):
    def __init__(self, jenis, durasi_hari):
        biaya_per_hari = 500000 if jenis.lower() == "sedan" else 800000
        super().__init__(f"Sewa Mobil ({jenis})", biaya_per_hari * durasi_hari)
        self.jenis = jenis
        self.durasi_hari = durasi_hari

    def __str__(self):
        return (
            f"Sewa Mobil {self.jenis} ({self.durasi_hari} hari) - Rp{self.biaya:,.0f}"
        )
