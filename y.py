import requests
import subprocess

def cek_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Website {url} online.")
            # Jalankan script lain di sini setelah mendapatkan hasil online
            subprocess.run(['bash', 'apacoba.sh'])
        else:
            print(f"Website {url} mungkin offline, atau ada masalah. Kode status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error {url}: {e}")

def tampilkan_banner(teks):
    # Menjalankan perintah toilet dari Python
    subprocess.run(['toilet', '-F',  'metal', teks])

if __name__ == "__main__":
    banner_teks = "Cek Status Web"
    tampilkan_banner(banner_teks)
   
    # Contoh penambahan cetakan setelah banner
    print("             >> Otak Kosong")

if __name__ == "__main__":
    pertanyaan = "Masukkan URL website untuk dicek (dengan http/https): "
    url = input(pertanyaan)
    cek_status(url)
