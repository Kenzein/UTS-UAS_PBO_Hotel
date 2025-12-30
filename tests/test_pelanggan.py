from pelanggan import Pelanggan


def test_pelanggan(pelanggan):
    assert pelanggan.id_pelanggan is not None


def test_str_pelanggan(pelanggan):
    hasil = str(pelanggan)
    assert "Budi" in hasil
