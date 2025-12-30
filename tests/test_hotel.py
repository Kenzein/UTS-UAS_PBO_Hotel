import pytest
from kamar import Kamar
from exceptions import InputError


def test_hotel_kamar_awal(hotel):
    assert len(hotel.kamar_list) == 5


def test_tambah_kamar(hotel, kamar):
    kamar_baru = Kamar(200, "Amazing", 789456123)
    hotel.tambah_kamar(kamar_baru)
    assert kamar_baru in hotel.kamar_list


def test_kamar_duplikat(hotel):
    kamar_dupli = Kamar(101, "Deluxe", 50000)
    with pytest.raises(InputError):
        hotel.tambah_kamar(kamar_dupli)


def test_tambah_reservasi(hotel, reservasi_valid):
    hotel.tambah_reservasi(reservasi_valid)
    assert reservasi_valid in hotel.reservasi_list
