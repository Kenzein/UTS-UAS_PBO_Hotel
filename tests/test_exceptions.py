from exceptions import (
    HotelError,
    InputError,
    TanggalTidakValidError,
    KamarTidakTersediaError,
)


def test_exception():
    assert issubclass(InputError, HotelError)
    assert issubclass(TanggalTidakValidError, HotelError)
    assert issubclass(KamarTidakTersediaError, HotelError)
