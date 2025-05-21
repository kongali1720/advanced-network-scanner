
---

**Cara simpan dengan nano:**

1. Ketik `nano README.md` di terminal kamu  
2. Hapus isi file yang lama (jika ada) dengan `Ctrl + K` (untuk hapus baris) sampai kosong  
3. Copy paste seluruh teks di atas ke nano (klik kanan > paste atau shift+insert)  
4. Setelah selesai, tekan `Ctrl + O` lalu enter untuk simpan  
5. Tekan `Ctrl + X` untuk keluar nano  

**Lalu commit dan push ke GitHub:**

```bash
git add README.md
git commit -m "Update README with correct formatting and badge"
git push origin main
