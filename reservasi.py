import uuid
from datetime import datetime
from exceptions import KamarTidakTersediaError, TanggalTidakValidError
from layanan import LayananTambahan


class Reservasi:
    def __init__(self, pelanggan, kamar, check_in, check_out):
        if check_out <= check_in:
            raise TanggalTidakValidError("Tanggal check-out harus setelah check-in!")
        if kamar.status != "Tersedia":
            raise KamarTidakTersediaError(f"Kamar {kamar.nomor} tidak tersedia!")

        self.id_reservasi = str(uuid.uuid4())[:8]
        self.pelanggan = pelanggan
        self.kamar = kamar
        self.tgl_check_in = check_in
        self.tgl_check_out = check_out
        self.durasi_malam = (check_out - check_in).days
        self.biaya_kamar = kamar.harga * self.durasi_malam
        self.biaya_tambahan = 0
        self.total_tagihan = self.biaya_kamar
        self.layanan_tambahan = []
        self.status = "Dipesan"

        kamar.ubah_status("Dipesan")

    def check_in(self):
        if self.status != "Dipesan":
            print("Reservasi tidak dapat check-in. Sudah terisi atau selesai.")
            return
        self.status = "Terisi"
        self.kamar.ubah_status("Terisi")
        print(
            f"Pelanggan {self.pelanggan.nama} telah check-in ke kamar {self.kamar.nomor}."
        )

    def check_out(self):
        if self.status != "Terisi":
            print("Check-out hanya bisa dilakukan jika kamar sedang terisi.")
            return
        self.status = "Selesai"
        self.kamar.ubah_status("Tersedia")
        print(f"Check-out berhasil. Kamar {self.kamar.nomor} kini tersedia kembali.")

    # Layanan Tambahan ke reservasi pelanggan
    def tambah_layanan(self, layanan: LayananTambahan):
        self.layanan_tambahan.append(layanan)
        biaya = layanan.hitung_biaya()
        self.biaya_tambahan += biaya
        self.total_tagihan = self.biaya_kamar + self.biaya_tambahan
        print(f"Layanan {layanan.nama} ditambahkan (Rp{biaya:,.0f})")

    def tampilkan_tagihan(self):
        print(f"\n=== RINCIAN TAGIHAN - {self.pelanggan.nama} ===")
        print(f"Durasi: {self.durasi_malam} malam x Rp{self.kamar.harga:,.0f}")
        print(f"Subtotal kamar : Rp{self.biaya_kamar:,.0f}")

        if self.layanan_tambahan:
            print("\nLayanan Tambahan:")
            for l in self.layanan_tambahan:
                print(" -", l)
            print(f"Total biaya tambahan : Rp{self.biaya_tambahan:,.0f}")

        print(f"\nTOTAL TAGIHAN AKHIR : Rp{self.total_tagihan:,.0f}")
        print(f"Status: {self.status}")

    def __str__(self):
        return (
            f"Reservasi {self.id_reservasi} | {self.pelanggan.nama} | "
            f"Kamar {self.kamar.nomor} ({self.kamar.tipe}) | "
            f"{self.durasi_malam} malam | Total: Rp{self.total_tagihan:,.0f}"
        )
