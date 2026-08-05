# ============================================================
# SCRIPT EXPORT MODEL - JALANKAN DI GOOGLE COLAB
# ============================================================
# Cara pakai:
# 1. Buka Colab notebook Anda (Deteksi_lebah_madu.ipynb)
# 2. Copy semua code di bawah ini
# 3. Paste di cell baru di bawah cell terakhir
# 4. Jalankan cell tersebut
# 5. Download file .h5 yang muncul
# ============================================================

import os
import shutil
from google.colab import files

# Pastikan model sudah di-train
try:
    print("📦 Menyimpan model...")
    
    # Simpan model subspecies
    model1.save('best_model1.weights.h5')
    print("✅ Model 1 (Subspecies) tersimpan")
    
    # Simpan model health
    model2.save('best_model2.weights.h5')
    print("✅ Model 2 (Health) tersimpan")
    
    # Tampilkan info file
    print("\n📊 Info File:")
    print(f"   Model 1: {os.path.getsize('best_model1.weights.h5') / 1024 / 1024:.2f} MB")
    print(f"   Model 2: {os.path.getsize('best_model2.weights.h5') / 1024 / 1024:.2f} MB")
    
    # Download ke komputer Anda
    print("\n⬇️  Downloading model ke komputer Anda...")
    files.download('best_model1.weights.h5')
    files.download('best_model2.weights.h5')
    
    print("\n✅ Selesai! File .h5 sudah didownload ke komputer Anda.")
    print("📁 Sekarang copy file ke folder: D:\\deteksi lebah madu\\models\\")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("Pastikan Anda sudah menjalankan cell training model sebelumnya!")
