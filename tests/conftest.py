import pytest
from datetime import date

from kamar import Kamar
from pelanggan import Pelanggan
from reservasi import Reservasi
from hotel import Hotel


@pytest.fixture
def kamar():
    return Kamar(101, "Deluxe", 50000)


@pytest.fixture
def pelanggan():
    return Pelanggan("Budi", 8123456789)


@pytest.fixture
def reservasi_valid(kamar, pelanggan):
    return Reservasi(pelanggan, kamar, date(2025, 1, 10), date(2025, 2, 10))


@pytest.fixture
def hotel():
    return Hotel("Hotel Nusantara")
