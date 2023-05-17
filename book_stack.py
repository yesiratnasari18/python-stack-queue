stack = []

def tambah_judul(stack, judul_baru , pengarang_baru):
    buku_baru =[judul_baru, pengarang_baru]
    stack.append(buku_baru)
    print(f"{buku_baru}, berhasil ditambahkan ke dalam stack.")

def hapus_judul_terakhir(stack):
    if len(stack) == 0:
        print("Stack kosong, tidak ada barang yang dapat dihapus.")
    else:
        judul_terakhir = stack.pop()
        print(f"{judul_terakhir} berhasil dihapus dari stack")
def tampilkan_judul_teratas(stack):
    if len(stack) == 0:
        print("Stack teratas di dalam stack adalah {judul_teratas}.")

while True:
    print("\nGudang saat ini:",stack)
    print("Menu:")
    print("1. Tambah Judul")
    print("2. Hapus Judul Terakhir")
    print("3. Tampilkan Judul Teratas")
    print("4. Keluar")

    pilihan = input("Masukan pilihan Anda (1/2/3/4):")

    if pilihan == "1":
        judul_baru = input("Masukan nama judul dan pengarang yang akan ditambahkan:")
        pengarang_baru = input("Masukan nama pengarang yang akan ditambahkan:")
        tambah_judul(stack, judul_baru, pengarang_baru)
    elif pilihan == "2":
        hapus_judul_terakhir(stack)
    elif pilihan == "3":
        tampilkan_judul_teratas(stack)
    elif pilihan == "4":
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak Valid. Silakan masukan pipihan yang benar.")
