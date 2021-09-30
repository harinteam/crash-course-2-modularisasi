"""
Program menghitung luas segitiga
luas segitiga = alas * tinggi / 2
"""

print('>> Menghitung luas segitiga 1')
alas = 10
tinggi = 6
luas_segitiga = alas * tinggi / 2
print(f'Segitiga dengan alas = {alas} dan tinggi = {tinggi} memiliki luas {luas_segitiga}')

print('\n>> Menghitung luas segitiga 2 dengan copy paste')
alas = 20
tinggi = 2
luas_segitiga = alas * tinggi / 2
print(f'Segitiga dengan alas = {alas} dan tinggi = {tinggi} memiliki luas {luas_segitiga}')

print('\n>> Membuat fungsi hitung_luas_segitiga')
def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga


alas = 99
tinggi = 77
print(
    f"Dengan fungsi, segitiga dengan alas = {alas} dan tinggi = {tinggi} memiliki luas  {hitung_luas_segitiga(alas, tinggi)}")
print(f'Menghitung luas segitiga dengan fungsi, hasilnya {hitung_luas_segitiga(10, 6)}')
print(f'Menghitung luas segitiga dengan fungsi, hasilnya {hitung_luas_segitiga(18, 3)}')
