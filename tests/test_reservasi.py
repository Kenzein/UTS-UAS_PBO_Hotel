import pytest
from datetime import date
from exceptions import TanggalTidakValidError, KamarTidakTersediaError


def test_reservasi_status_awal(reservasi_valid):
    assert reservasi_valid.status == "Dipesan"


def test_durasi_reservasi(reservasi_valid):
    assert reservasi_valid.durasi_malam == 31


def test_biaya_kamar(reservasi_valid):
    assert reservasi_valid.biaya_kamar == 31 * reservasi_valid.kamar.harga


def test_check_in(reservasi_valid):
    reservasi_valid.check_in()
    assert reservasi_valid.status == "Terisi"


def test_check_out(reservasi_valid):
    reservasi_valid.check_in()
    reservasi_valid.check_out()
    assert reservasi_valid.status == "Selesai"
    assert reservasi_valid.kamar.status == "Tersedia"


def test_tanggal_Tidak_valid(pelanggan, kamar):
    from reservasi import Reservasi

    with pytest.raises(TanggalTidakValidError):
        Reservasi(pelanggan, kamar, date(2025, 2, 10), date(2025, 2, 5))


def test_kamar_tidak_tersedia(pelanggan, kamar):
    from reservasi import Reservasi

    kamar.ubah_status("Terisi")
    with pytest.raises(KamarTidakTersediaError):
        Reservasi(pelanggan, kamar, date(2025, 2, 10), date(2025, 2, 15))
