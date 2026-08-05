-- ============================================================
-- SETUP DATABASE - JALANKAN DI LARAGON/phpMyAdmin
-- ============================================================
-- Cara pakai:
-- 1. Buka Laragon
-- 2. Klik "Start All" (MySQL + Apache)
-- 3. Buka phpMyAdmin (klik menu Laragon → Database → phpMyAdmin)
-- 4. Klik tab "SQL" di phpMyAdmin
-- 5. Copy paste semua kode di bawah ini
-- 6. Klik "Go" / "Jalankan"
-- ============================================================

CREATE DATABASE IF NOT EXISTS bee_detection;
USE bee_detection;

CREATE TABLE IF NOT EXISTS detections (
    id INT AUTO_INCREMENT PRIMARY KEY,
    image_filename VARCHAR(255) NOT NULL,
    health_status VARCHAR(100) NOT NULL,
    health_name VARCHAR(200) NOT NULL,
    health_confidence FLOAT NOT NULL,
    subspecies_name VARCHAR(200) NOT NULL,
    subspecies_confidence FLOAT NOT NULL,
    message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Verifikasi tabel sudah dibuat
SELECT '✅ Database bee_detection dan tabel detections berhasil dibuat!' AS Status;
