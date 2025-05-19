# 🧠 Socket Programming: TCP vs UDP - Echo Client/Server in Python

##  Deskripsi Singkat
Proyek ini mendemonstrasikan **perbedaan fundamental antara TCP dan UDP** dalam komunikasi jaringan menggunakan Python.

Program terdiri dari dua jenis echo server dan client:
- ✅ **TCP Echo Server/Client**
- ✅ **UDP Echo Server/Client**

Keduanya dirancang untuk menerima pesan dari client dan mengirimkannya kembali (**echo**), namun dengan karakteristik protokol yang sangat berbeda.

---

##  Perbandingan TCP vs UDP

| Aspek              | TCP (Transmission Control Protocol)                            | UDP (User Datagram Protocol)                        |
|-------------------|------------------------------------------------------------------|-----------------------------------------------------|
| **Tipe Protokol**  | Connection-oriented (harus "kenalan" dulu)                      | Connectionless (langsung kirim saja)               |
| **Keandalan**      | Andal: menjamin pesan sampai (dengan urutan benar)              | Tidak andal: pesan bisa hilang/tidak berurutan     |
| **Kecepatan**      | Relatif lambat karena verifikasi koneksi                        | Cepat karena tanpa overhead koneksi                |
| **Overhead**       | Tinggi (handshake, ACK, re-send)                                | Rendah (langsung kirim paket)                      |
| **Penggunaan Umum**| Web, Email, FTP, SSH                                             | Streaming video, VoIP, DNS, gaming real-time       |
| **Analogi Nyata**  | Seperti telepon: ada salam, lalu bicara                         | Seperti walkie-talkie: langsung bicara             |

---

## Cara Kerja TCP vs UDP secara Visual

### Skema Koneksi TCP (Connection-Oriented)
```text
          TCP Client                             TCP Server
         ------------                          ---------------
        | socket()     |                      | socket()       |
        | connect()    | <--- Handshake ----> | accept()       |
        | write()      | -------------------> | read()         |
        | read()       | <------------------- | write()        |
         ------------                          ---------------

➡ Client melakukan 3-way handshake ke server sebelum bisa bertukar data.
➡ Koneksi bersifat permanen sampai salah satu memutuskan.
➡ Server mendengarkan koneksi dan menerima satu-per-satu.
```

### Skema Koneksi UDP (Connectionless)
```text
          UDP Client                             UDP Server
         ------------                          ---------------
        | socket()     |                      | socket()       |
        | sendto()     | -------------------> | recvfrom()     |
        | recvfrom()   | <------------------- | sendto()       |
         ------------                          ---------------

➡ Tidak ada handshake: client langsung mengirim pesan ke alamat tujuan.
➡ Server tidak tahu siapa yang akan mengirim, hanya menunggu paket.
➡ Hubungan tidak permanen: seperti "sekali kirim, selesai."
```

### Struktur Program
#### 1. TCP Echo Server dan Client
- Server membuat socket, bind ke alamat & port, lalu listen().
- Server memanggil accept() untuk menerima koneksi.
- Client melakukan connect() dan mengirim pesan.
- Server menerima (recv) lalu membalas (send) kembali ke client.
- Koneksi ditutup saat client mengetik exit.

#### 2. UDP Echo Server dan Client
- Server membuat socket dan bind ke alamat & port.
- Client langsung mengirim data ke server menggunakan sendto().
- Server menerima data (recvfrom()), mencetak, lalu membalas (sendto()).
- Tidak ada sesi atau koneksi permanen — setiap paket berdiri sendiri.

### Penutup: Kapan menggunakan TCP dan UDP?
- Gunakan TCP jika perlu keandalan: website, login, pengiriman data penting.
- Gunakan UDP jika perlu kecepatan dan bisa menoleransi kehilangan: video call, game online, live Sosmed.
