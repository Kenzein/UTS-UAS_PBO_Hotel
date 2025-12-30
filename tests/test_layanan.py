from layanan import LayananLaundry, LayananRoomService, LayananSewaMobil


def test_laundry():
    layanan = LayananLaundry(2)
    assert layanan.hitung_biaya() == 20000


def test_room_service():
    layanan = LayananRoomService("Nasi Padang", 50000)
    assert layanan.hitung_biaya() == 50000


def test_sewa_mobil():
    layanan = LayananSewaMobil("Sedan", 3)
    assert layanan.hitung_biaya() == 1500000
