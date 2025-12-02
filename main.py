from kamar import Kamar
from pelanggan import Pelanggan
from reservasi import Reservasi
from hotel import Hotel
from exceptions import HotelError, InputError
from datetime import datetime
from layanan import (
    LayananLaundry,
    LayananRoomService,
    LayananSewaMobil,
)

hotel = Hotel("Hotel Nusantara")


def menu():
    while True:
        hotel.tampilkan_semua_kamar()
        print(f"Sistem Manajemen: ")
        print("1. Tambah Kamar Baru")
        print("2. Buat Reservasi")
        print("3. Tampilkan Semua Reservasi")
        print("4. Layanan Tambahan")
        print("5. Check-In")
        print("6. Check-Out")
        print("7. Histori Tagihan")
        print("8. Keluar dari Sistem")
        try:
            pilihan = int(input("Pilih menu: "))
        except InputError:
            print("Input harus angka!")
            continue
        # Pilihan 1: Tambah Kamar Baru
        if pilihan == 1:
            nomor = int(input("Nomor Kamar: "))
            tipe = input("Tipe Kamar: ")
            harga = int(input("Harga per malam: "))
            kamar = Kamar(nomor, tipe, harga)
            hotel.tambah_kamar(kamar)
            print("\nKamar berhasil ditambahkan.")
        # Pilihan 2: Membuat reservasi
        elif pilihan == 2:
            try:
                nama = str(input("Nama pelanggan: "))
                kontak = int(input("Kontak pelanggan: "))
                pelanggan = Pelanggan(nama, kontak)
                hotel.tampilkan_semua_kamar()
                nomor_kamar = int(input("\nNomor kamar yang ingin dipesan: "))
                kamar_dipilih = next(
                    (k for k in hotel.kamar_list if k.nomor == nomor_kamar), None
                )
                if not kamar_dipilih:
                    print("\nKamar tidak ditemukan")
                    continue
                while True:
                    try:
                        check_in = datetime.strptime(
                            input("Tanggal Check-In (YYYY-MM-DD): "), "%Y-%m-%d"
                        ).date()
                        check_out = datetime.strptime(
                            input("Tanggal Check-Out (YYYY-MM-DD): "), "%Y-%m-%d"
                        ).date()
                    except ValueError:
                        print(
                            f"\nFormat tanggal salah! Gunakan YYYY-MM-DD (contoh: 2025-11-19)"
                        )
                        continue
                    break
                reservasi = Reservasi(pelanggan, kamar_dipilih, check_in, check_out)
                hotel.tambah_reservasi(reservasi)
                print("\nReservasi berhasil dibuat!")
                print(reservasi)
            except HotelError as e:
                print(f"[Error] {e}")
        # Pilihan 3:Menampilkan semua reservasi
        elif pilihan == 3:
            if not hotel.reservasi_list:
                print("\nBelum ada reservasi")
            else:
                print("\nMenelusuri reservasi satu per satu: ")
                for reservasi in hotel.reservasi_iterator():
                    print(reservasi)
        # Pilihan 4: Menambah layanan tambahan
        elif pilihan == 4:
            if not hotel.reservasi_list:
                print("\nBelum ada reservasi")
                continue
            for i, r in enumerate(hotel.reservasi_list):
                print(f"{i+1}. {r.pelanggan.nama} - Kamar {r.kamar.nomor}")
            idx = int(input("Pilih nomor reservasi: ")) - 1
            reservasi = hotel.reservasi_list[idx]
            print("\nPilih layanan")
            print("1. Laundry")
            print("2. Room Service")
            print("3. Sewa Mobil")
            jenis = int(input("Pilih: "))

            if jenis == 1:
                jumlah = int(input("Jumlah Pakaian: "))
                reservasi.tambah_layanan(LayananLaundry(jumlah))
            elif jenis == 2:
                menu = input("Menu: ")
                harga = int(input("Harga: "))
                reservasi.tambah_layanan(LayananRoomService(menu, harga))
            elif jenis == 3:
                tipe = input("Jenis Mobil (sedan/pickup): ")
                hari = int(input("Durasi Penyewaan (hari): "))
                reservasi.tambah_layanan(LayananSewaMobil(tipe, hari))
            reservasi.tampilkan_tagihan()
        # Pilihan 5: Check-In
        elif pilihan == 5:
            if not hotel.reservasi_list:
                print("\nBelum ada reservasi")
                continue
            for i, r in enumerate(hotel.reservasi_list):
                print(f"{i+1}. {r.pelanggan.nama} - Kamar {r.kamar.nomor} [{r.status}]")
            idx = int(input("Pilih nomor reservasi untuk check-in: ")) - 1
            reservasi = hotel.reservasi_list[idx]
            reservasi.check_in()
        # Pilihan 6: Check-Out
        elif pilihan == 6:
            if not hotel.reservasi_list:
                print("\nBelum ada reservasi.")
                continue
            for i, r in enumerate(hotel.reservasi_list):
                print(f"{i+1}. {r.pelanggan.nama} - Kamar {r.kamar.nomor} [{r.status}]")
            idx = int(input("Pilih nomor reservasi untuk check-out: ")) - 1
            reservasi = hotel.reservasi_list[idx]
            reservasi.check_out()
        # Pilihan 7: Menampilkan histori pelanggan
        elif pilihan == 7:
            if not hotel.reservasi_list:
                print("\nBelum ada histori pelanggan")
                continue
            for i, r in enumerate(hotel.reservasi_list):
                print(f"{i+1}. {r.pelanggan.nama} - Kamar {r.kamar.nomor}")
            idx = int(input("Pilih nomor reservasi: ")) - 1
            reservasi = hotel.reservasi_list[idx]
            reservasi.tampilkan_tagihan()
        # Pilihan 8: Exit Program
        elif pilihan == 8:
            print("\nTerima kasih! Program selesai.")
            break
        else:
            print("\nPilihan tidak valid, coba lagi")


if __name__ == "__main__":
    menu()
