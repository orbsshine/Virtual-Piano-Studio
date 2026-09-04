# Virtual Piano Studio

**Virtual Piano Studio** adalah aplikasi instrumen piano virtual sederhana berbasis Python dan Pygame. Aplikasi ini memungkinkan pengguna memainkan nada piano menggunakan keyboard komputer atau klik mouse, sekaligus mencatat aktivitas sesi bermain ke dalam file riwayat.

---

## 🎹 Fitur Utama

- **Interaksi Fleksibel**: Mainkan tuts piano menggunakan tombol keyboard (`Z`, `X`, `C`, `V`, `B`, `N`, `M`, `E`) atau klik langsung pada tuts visual dengan mouse.
- **Tampilan Visual Informatif**: Menampilkan tuts piano interaktif, panduan tombol, dan nada yang sedang dimainkan (*Current Note*).
- **Pencatatan Riwayat (Session History)**: Mencatat waktu pembukaan sesi serta riwayat penekanan nada ke file `riwayat_bermain.txt` dan struktur data memori.

---

## 🎵 Pemetaan Nada & Tombol (Key Mapping)

| Tombol Keyboard | Nada (Note) | File Audio |
| :---: | :---: | :--- |
| `Z` | C4 | `assets/notes/C4.wav` |
| `X` | D4 | `assets/notes/D4.wav` |
| `C` | E4 | `assets/notes/E4.wav` |
| `V` | F4 | `assets/notes/F4.wav` |
| `B` | G4 | `assets/notes/G4.wav` |
| `N` | A4 | `assets/notes/A4.wav` |
| `M` | B4 | `assets/notes/B4.wav` |
| `E` | C5 | `assets/notes/C5.wav` |

---

## 📁 Struktur Direktori

```text
.
├── assets/
│   └── notes/
│       ├── C4.wav
│       ├── D4.wav
│       ├── E4.wav
│       ├── F4.wav
│       ├── G4.wav
│       ├── A4.wav
│       ├── B4.wav
│       └── C5.wav
├── Virtual Piano Studio.py
├── riwayat_bermain.txt   (dibuat otomatis)
└── README.md
```

---

## 🚀 Cara Menjalankan

1. **Prasyarat**: Pastikan Python dan library `pygame` telah terpasang:
   ```bash
   pip install pygame
   ```

2. **Jalankan Aplikasi**:
   ```bash
   python "Virtual Piano Studio.py"
   ```
