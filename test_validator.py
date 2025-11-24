# test_validator.py
from validator import cek_password

def test_password_pendek():
    assert cek_password("12345") == "Lemah"
    assert cek_password("pendek") == "Lemah"

def test_password_sedang():
    # Panjang cukup, tapi tidak ada angka
    assert cek_password("kopihitam") == "Sedang"
    assert cek_password("indonesia") == "Sedang"

def test_password_kuat():
    # Panjang cukup DAN ada angka
    assert cek_password("kopi1234") == "Kuat"
    assert cek_password("p4ssw0rd") == "Kuat"