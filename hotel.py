from iterator import KamarIterator, ReservasiIterator
from kamar import Kamar
from exceptions import InputError


class Hotel:
    def __init__(self, nama):
        self.nama = nama
        self.kamar_list = [
            Kamar(101, "Deluxe", 50),
            Kamar(102, "Standar", 35),
            Kamar(103, "Deluxe", 50),
            Kamar(104, "Suite", 100),
            Kamar(105, "Presidensial", 500),
        ]
        self.reservasi_list = []

    # Bagian iterator
    def kamar_iterator(self):
        return KamarIterator(self.kamar_list)

    def reservasi_iterator(self):
        return ReservasiIterator(self.reservasi_list)

    # Fungsi Hotel
    def tambah_kamar(self, kamar):
        for n in self.kamar_list:
            if n.nomor == kamar.nomor:
                raise InputError(f"Kamar dengan nomor {kamar.nomor} sudah ada!")
        self.kamar_list.append(kamar)

    def tambah_reservasi(self, reservasi):
        self.reservasi_list.append(reservasi)

    def tampilkan_semua_kamar(self):
        print(f"\nDaftar kamar di {self.nama}:")
        print("=" * 62)
        print(
            f"|{'No Kamar':<10} | {'Tipe':<15} | {'Harga per Malam':<15} | {'Status':<10} |"
        )
        print("=" * 62)
        for kamar in self.kamar_iterator():
            harga_format = f"Rp{kamar.harga:,}"
            print(
                f"|{kamar.nomor:<10} | "
                f"{kamar.tipe:<15} | "
                f"{harga_format:<15} | "
                f"{kamar.status:<10} |"
            )
        print("=" * 62)

    def tampilkan_semua_reservasi(self):
        print(f"Daftar Reservasi di {self.nama}:")
        for i in self.reservasi_iterator():
            print("-", i)
