class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.kelas_diambil = []

    def ambil_kelas(self, kelas):
        self.kelas_diambil.append(kelas)
        kelas.tambah_mahasiswa(self)
        print(f"{self.nama} telah mengambil kelas {kelas.mata_kuliah.nama} yang diajar oleh {kelas.dosen.nama}")

class MataKuliah:
    def __init__(self, nama, kode):
        self.nama = nama
        self.kode = kode

class Dosen:
    def __init__(self, nama):
        self.nama = nama
        self.kelas_ajar = []

    def tambah_kelas(self, kelas):
        self.kelas_ajar.append(kelas)
        kelas.set_dosen(self)
        print(f"{self.nama} mengajar kelas {kelas.mata_kuliah.nama}")

class Kelas:
    def __init__(self, mata_kuliah):
        self.mata_kuliah = mata_kuliah
        self.dosen = None
        self.mahasiswa = []

    def set_dosen(self, dosen):
        self.dosen = dosen

    def tambah_mahasiswa(self, mahasiswa):
        self.mahasiswa.append(mahasiswa)

mahasiswa1 = Mahasiswa("Anastasia Citra Negara", "2255061017")
mahasiswa2 = Mahasiswa("Al Fatih Naufaldo", "2215061092")

matakuliah1 = MataKuliah("Pemrograman Berorientasi Objek", "PBO123")
matakuliah2 = MataKuliah("Kecerdasan Buatan", "AI123")

dosen1 = Dosen("Pak Puput")
dosen2 = Dosen("Pak Puput")

kelas1 = Kelas(matakuliah1)
kelas2 = Kelas(matakuliah2)
print ("")

dosen1.tambah_kelas(kelas1)
dosen2.tambah_kelas(kelas2)
print(" ")

mahasiswa1.ambil_kelas(kelas1)
mahasiswa2.ambil_kelas(kelas2)
print ("")
