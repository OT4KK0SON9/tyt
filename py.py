import getpass
import os
import subprocess

# Warna teks
r = "\033[91m"
g = "\033[92m"
y = "\033[93m"
b = "\033[94m"
p = "\033[95m"
c = "\033[96m"
w = "\033[97m"

def clear_screen():
    # Bersihkan layar konsol
    os.system('cls' if os.name == 'nt' else 'clear')

def login():
    while True:
        clear_screen()  # Bersihkan layar sebelum meminta input baru
        username = input("Masukkan username: ")
        password = getpass.getpass("Masukkan password: ")

        # Cek apakah username dan password sesuai
        if username == "an" and password == "1":
            print(g + "Login berhasil!")
            # Melanjutkan ke skrip selanjutnya setelah login berhasil
            next_script()
            break  # Keluar dari loop jika login berhasil
        else:
            print("Username atau password salah. Silakan coba lagi.")

def welcome_message():
    print("Selamat datang! Anda telah berhasil login.")

def next_script():
    # Jalankan skrip selanjutnya dengan subprocess
    subprocess.run(["bash", "apacoba.sh"])

login()