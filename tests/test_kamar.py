import pytest
from kamar import Kamar


# Test status awal dari kamar
def test_status_default_kamar(kamar):
    assert kamar.status == "Tersedia"


# Test untuk perubahan status kamar
def test_ubah_status_kamar(kamar):
    kamar.ubah_status("Dipesan")
    assert kamar.status == "Dipesan"


# Test exception


def test_ubah_status_tidak_valid(kamar):
    with pytest.raises(ValueError):
        kamar.ubah_status("Rusak")
