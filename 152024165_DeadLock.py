import threading
import time

# Resource (diibaratkan printer & scanner)
printer = threading.Lock()
scanner = threading.Lock()

def mahasiswa_A():
    print("Mahasiswa A mengambil PRINTER")
    printer.acquire()
    time.sleep(2)

    print("Mahasiswa A menunggu SCANNER...")
    scanner.acquire()

    print("Mahasiswa A selesai mencetak & scan")
    scanner.release()
    printer.release()

def mahasiswa_B():
    print("Mahasiswa B mengambil SCANNER")
    scanner.acquire()
    time.sleep(2)

    print("Mahasiswa B menunggu PRINTER...")
    printer.acquire()

    print("Mahasiswa B selesai mencetak & scan")
    printer.release()
    scanner.release()

# Jalankan thread
tA = threading.Thread(target=mahasiswa_A)
tB = threading.Thread(target=mahasiswa_B)

tA.start()
tB.start()

tA.join()
tB.join()