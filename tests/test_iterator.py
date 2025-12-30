def test_kamar_iterator(hotel):
    iterator = hotel.kamar_iterator()
    kamar = next(iterator)
    assert kamar.nomor == 101


def test_reservasi_iterator(hotel, reservasi_valid):
    hotel.tambah_reservasi(reservasi_valid)
    iterator = hotel.reservasi_iterator()
    hasil = list(iterator)
    assert reservasi_valid in hasil
