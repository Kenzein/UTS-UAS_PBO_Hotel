class KamarIterator:
    def __init__(self, kamar_list):
        self._kamar_list = kamar_list
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._kamar_list):
            kamar = self._kamar_list[self._index]
            self._index += 1
            return kamar
        raise StopIteration


class ReservasiIterator:
    def __init__(self, reservasi_list):
        self._reservasi_list = reservasi_list
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._reservasi_list):
            reservasi = self._reservasi_list[self._index]
            self._index += 1
            return reservasi
        raise StopIteration
