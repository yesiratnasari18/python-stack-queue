import random
import time

class Customer:
    def __init__(self, nama, transaksi):
        self.nama = nama
        self.transaksi = transaksi

class Queue :
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self, customer):
        self.queue.append(customer)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)
    
    def display_transaksi_berikutnya(self):
        if self.is_empty():
            print("Antrian Kosong")
        else:
            customer = self.queue[0]
            print(f"Transaksi berikutnya: {customer.transaksi} - {customer.nama}")

    def hapus_transaksi_selesai(self):
        if self.is_empty():
            print("Antrian Kosong")
        else:
            customer = self.queue.pop(0)
            print(f"Transaksi selesai: {customer.transaksi} - {customer.nama}")

queue = Queue()
while True:
    print('=======Sistem Antrian Transaksi Pelanggan============')
    print('1. Tambah Transaksi Ke Antrian')
    print('2. Tampilkan Transaksi Berikutnya')
    print('3. Hapus Transaksi Selesai')
    print('4. Keluar')

    pilihan = input("Masukan Pilihan : ")

    if pilihan == "1":
        nama = input("Masukan nama Pelanggan : ")
        transaksi = input("Masukan jenis transaksi : ")
        customer = Customer(nama, transaksi)
        queue.enqueue(customer)
        print("Transaksi berhasil ditambahkan ke antrian.")
    elif pilihan == "2":
        queue.display_transaksi_berikutnya()
    elif pilihan == "3":
        queue.hapus_transaksi_selesai()
    elif pilihan == "4":
        print("terima kasih! Program berakhir.")
        break
    else:
        print("Pilihan tiddak valid. Silakan Masukan pilihan yang benar.")