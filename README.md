# Socket Programming: TCP vs UDP - Echo Client/Server in Python

## 📌 Deskripsi Singkat
Proyek ini mendemonstrasikan **perbedaan antara TCP dan UDP** dalam komunikasi jaringan menggunakan Python. Program terdiri dari dua jenis echo server dan client:
- **TCP Echo Server/Client**
- **UDP Echo Server/Client**

Keduanya dirancang untuk menerima pesan dari client dan mengirimkannya kembali (echo), namun dengan karakteristik protokol yang berbeda.

---

## ⚖️ Perbedaan TCP dan UDP secara Sederhana

| Aspek             | TCP (Transmission Control Protocol)                            | UDP (User Datagram Protocol)                        |
|------------------|------------------------------------------------------------------|-----------------------------------------------------|
| **Tipe Protokol** | Connection-oriented (butuh “jabat tangan” dulu)                 | Connectionless (langsung kirim saja)               |
| **Keandalan**     | Sangat andal: pesan dikirim ulang jika hilang                   | Tidak andal: pesan bisa hilang tanpa pemberitahuan |
| **Kecepatan**     | Lebih lambat karena ada proses kontrol koneksi                  | Lebih cepat karena minim proses kontrol            |
| **Penggunaan Umum** | Web, Email, File Transfer                                      | Video Streaming, Voice Call, Gaming                |
| **Contoh Nyata**  | Seperti menelpon—ada halo-halo dulu, baru ngobrol               | Seperti kirim surat langsung tanpa konfirmasi      |

---

## 🧪 Struktur Program

### 1. **TCP Echo Server dan Client**
- Server menunggu koneksi dari client.
- Setelah koneksi dibuat, client mengirim pesan.
- Server membalas pesan yang sama (echo).
- Jika client mengirim `exit`, koneksi ditutup.

### 2. **UDP Echo Server dan Client**
- Tidak perlu koneksi terlebih dahulu.
- Client langsung mengirim pesan ke server.
- Server membalas pesan yang sama (echo).
- Tidak ada koneksi permanen, hanya pengiriman paket.

---

## 🚀 Menjalankan Program

### A. Jalankan TCP Server
```bash
python3 tcp_echo_server.py
```

### B. Jalankan TCP Client
```bash
python3 tcp_echo_client.py
```

### C. Jalankan UDP Server
```bash
python3 udp_echo_server.py
```

### D. Jalankan UDP Client
```bash
python3 udp_echo_client.py
```

### Kesimpulan
TCP saat anda membutuhkan KEANDALAN, UDP saat anda membutuhkan KECEPATAN
