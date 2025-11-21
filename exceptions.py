class HotelError(Exception):
    pass


class KamarTidakTersediaError(HotelError):
    pass


class TanggalTidakValidError(HotelError):
    pass


class InputError(HotelError):
    pass
