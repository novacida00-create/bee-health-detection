DISEASE_DATABASE = {
    "healthy": {
        "name": "Healthy",
        "name_id": "Sehat",
        "status": "healthy",
        "icon": "✅",
        "color": "#28a745",
        "description": "Lebah dalam kondisi sehat dan prima. Tidak ditemukan tanda-tanda penyakit atau parasit.",
        "gejala": [
            "Lebah aktif terbang mencari nektar",
            "Warna badan cerah dan mengkilap",
            "Sarang teratur dan bersih",
            "Ratu bertelur dengan baik",
            "Tidak ada parasit yang terlihat",
            "Populasi lebah stabil atau meningkat"
        ],
        "pengobatan": [
            {
                "metode": "Tidak Diperlukan",
                "langkah": [
                    "Lebah dalam kondisi sehat, tidak perlu pengobatan",
                    "Terus pantau kondisi sarang secara berkala",
                    "Jaga kebersihan dan kesehatan lingkungan sekitar sarang"
                ]
            }
        ],
        "pencegahan": [
            "Jaga kebersihan sarang dan area sekitarnya",
            "Pantau kondisi sarang secara berkala (minimal 2 minggu sekali)",
            "Pastikan pasokan makanan (nektar dan pollen) cukup",
            "Hindari penggunaan pestisida di sekitar area lebah",
            "Ganti ratu secara berkala (setiap 1-2 tahun)",
            "Gunakan screened bottom board untuk ventilasi"
        ],
        "madu_status": "AMAN",
        "madu_info": "Madu dari lebah sehat AMAN untuk dikonsumsi. Madu memiliki kualitas baik dengan kandungan nutrisi lengkap.",
        "estimasi_panen": "Bisa dipanen kapan saja",
        "tips_panen": [
            "Pastikan minimal 80% sarang sudah terisi madu (capped honey)",
            "Panen di pagi hari saat lebah aktif mencari nektar",
            "Sisakan minimal 20% madu untuk makanan lebah",
            "Gunakan alat panen yang bersih dan higienis",
            "Simpan madu di wadah tertutup di tempat sejuk"
        ]
    },

    "varroa_small_hive_beetles": {
        "name": "Varroa, Small Hive Beetles",
        "name_id": "Kutu Varroa & Kumbang Kecil Sarang",
        "status": "danger",
        "icon": "❌",
        "color": "#dc3545",
        "description": "Lebah terinfeksi parasit Varroa destructor dan kumbang kecil sarang (Aethina tumida). Varroa adalah parasit paling berbahaya bagi lebah madu di seluruh dunia.",
        "gejala": [
            "Kutu kecil berwarna coklat/merah menempel pada badan lebah",
            "Lebah lemah dan tidak bisa terbang dengan baik",
            "Sarang terlihat kotor dan berantakan",
            "Larva mati atau tidak berkembang dengan baik",
            "Sayap lebah terlihat tidak simetris (deformed wing virus)",
            "Populasi lebah menurun drastis dalam waktu singkat",
            "Terdapat bekas gigitan pada larva (kumbang kecil)",
            "Honeycomb rusak dan berlubang-lubang kecil"
        ],
        "pengobatan": [
            {
                "metode": "Pengobatan Kimia",
                "langkah": [
                    "Gunakan strips Amitraz (Apivar) - pasang 2 strip per kotak brood",
                    "Atau gunakan Fluvalinate (Apistan) - pasang sesuai dosis",
                    "Biarkan strip selama 6-8 minggu untuk efektifitas maksimal",
                    "Cabut strip setelah masa pengobatan selesai",
                    "Ulangi pengobatan jika tingkat infestasi masih tinggi (>3%)"
                ]
            },
            {
                "metode": "Pengobatan Organik",
                "langkah": [
                    "Gunakan oxalic acid (asam oksalat) dengan metode dribble atau sublimasi",
                    "Aplikasi Formic Acid (MAQS) pada suhu lingkungan 10-29°C",
                    "Gunakan Hop Guard 2 dari ekstrak hop alami",
                    "Thymol (Api Life Var) - efektif pada suhu 15-30°C"
                ]
            },
            {
                "metode": "Pengobatan Mekanis",
                "langkah": [
                    "Gunakan screened bottom board untuk mengurangi Varroa",
                    "Lakukan brood break (jeda telur ratu) selama 24 hari",
                    "Ganti ratu secara berkala (setiap 1-2 tahun)",
                    "Lakukan alkohol wash untuk monitoring tingkat infestasi"
                ]
            }
        ],
        "pencegahan": [
            "Inspeksi sarang minimal 2 minggu sekali",
            "Gunakan screened bottom board untuk ventilasi",
            "Monitor tingkat infestasi Varroa dengan alkohol wash (target <3%)",
            "Ganti ratu secara berkala untuk menjaga kesehatan koloni",
            "Hindari mencampur koloni dari sumber berbeda",
            "Jaga kebersihan alat peternakan"
        ],
        "madu_status": "TIDAK AMAN",
        "madu_info": "Madu dari lebah terinfeksi Varroa TIDAK AMAN untuk dikonsumsi. Varroa dapat menularkan virus berbahaya yang mengontaminasi madu.",
        "estimasi_panen": "TIDAK BOLEH dipanen sampai lebah sembuh total (minimal 2 bulan setelah pengobatan)",
        "tips_panen": [
            "Jangan panen madu selama pengobatan berlangsung",
            "Tunggu minimal 2 minggu setelah pengobatan selesai",
            "Pastikan tidak ada residu obat dalam madu",
            "Lakukan test kualitas madu sebelum dikonsumsi",
            "Konsultasikan dengan ahli peternakan lebah sebelum panen"
        ]
    },

    "few_varroa_hive_beetles": {
        "name": "Few Varroa, Hive Beetles",
        "name_id": "Sedikit Kutu Varroa & Kumbang Sarang",
        "status": "warning",
        "icon": "⚠️",
        "color": "#ffc107",
        "description": "Lebah memiliki sedikit kutu Varroa dan kumbang sarang. Kondisi masih terkendali namun perlu perhatian segera.",
        "gejala": [
            "Terdapat beberapa kutu pada badan lebah (1-5 kutu per lebah)",
            "Lebah masih aktif dan bisa terbang dengan baik",
            "Sarang masih dalam kondisi cukup baik",
            "Beberapa larva mungkin terpengaruh",
            "Populasi lebah masih stabil"
        ],
        "pengobatan": [
            {
                "metode": "Pengobatan Ringan",
                "langkah": [
                    "Aplikasikan sugar dusting (tabur gula halus) pada sarang",
                    "Gunakan minyak atsiri seperti tea tree oil atau lavender oil",
                    "Pasang beetle traps (jebakan kumbang) di dalam sarang",
                    "Gunakan oil traps dengan minyak sayur di bawah screen"
                ]
            }
        ],
        "pencegahan": [
            "Pantau lebih sering (minimal seminggu sekali)",
            "Jaga kebersihan area sekitar sarang",
            "Gunakan entrance reducer untuk membatasi akses kumbang",
            "Tingkatkan ventilasi sarang",
            "Pastikan koloni memiliki cukup tenaga kerja"
        ],
        "madu_status": "HATI-HATI",
        "madu_info": "Madu masih bisa DIKONSUMSI dengan CATATAN: pastikan tidak ada kontaminasi langsung dari parasit. Periksa madu sebelum dikonsumsi.",
        "estimasi_panen": "Bisa dipanen dengan pengawasan ketat",
        "tips_panen": [
            "Periksa madu sebelum dipanen, pastikan tidak ada parasit",
            "Gunakan filter saat ekstraksi madu",
            "Simpan madu di tempat bersih dan tertutup rapat",
            "Monitor kondisi lebah setelah panen",
            "Lakukan pengobatan lanjutan jika infestasi meningkat"
        ]
    },

    "ant_problems": {
        "name": "Ant Problems",
        "name_id": "Masalah Semut",
        "status": "warning",
        "icon": "⚠️",
        "color": "#ffc107",
        "description": "Sarang lebah terganggu oleh serangan semut dalam jumlah besar. Semut dapat mencuri madu dan mengganggu aktivitas lebah.",
        "gejala": [
            "Banyak semut di sekitar dan di dalam sarang",
            "Lebah terlihat gelisah dan agresif",
            "Beberapa madu mungkin terkontaminasi semut",
            "Sarang terlihat kotor dengan jejak semut",
            "Lebah menghabiskan waktu untuk melawan semut"
        ],
        "pengobatan": [
            {
                "metode": "Penghalang Fisik",
                "langkah": [
                    "Pasang tiang sarang dengan vaseline atau minyak mineral",
                    "Buat water moat (parit air) di sekitar tiang sarang",
                    "Gunakan ant bait (umpan semut) di sekitar sarang",
                    "Pasang sticky barrier (lem) di tiang penyangga"
                ]
            },
            {
                "metode": "Pengobatan Alami",
                "langkah": [
                    "Taburkan kayu manis atau cengkeh di sekitar sarang",
                    "Gunakan minyak peppermint sebagai pengusir semut",
                    "Bersihkan area sekitar sarang dari sisa makanan",
                    "Tanam tanaman pengusir semut seperti lavender"
                ]
            }
        ],
        "pencegahan": [
            "Jaga kebersihan area sekitar sarang",
            "Hindari menaruh makanan manis di dekat sarang",
            "Gunakan tiang sarang yang sudah di-treated",
            "Periksa sarang secara rutin minimal seminggu sekali",
            "Pastikan tidak ada sumber makanan semut di sekitar"
        ],
        "madu_status": "HATI-HATI",
        "madu_info": "Madu masih bisa DIKONSUMSI jika tidak ada kontaminasi semut langsung. Cek sebelum dikonsumsi.",
        "estimasi_panen": "Bisa dipanen setelah sarang bersih dari semut",
        "tips_panen": [
            "Pastikan sarang benar-benar bersih dari semut sebelum panen",
            "Gunakan filter saat ekstraksi madu",
            "Periksa madu sebelum dikonsumsi",
            "Simpan madu di wadah tertutup rapat",
            "Buang bagian madu yang terkontaminasi semut"
        ]
    },

    "hive_being_robbed": {
        "name": "Hive Being Robbed",
        "name_id": "Sarang Dirampas",
        "status": "danger",
        "icon": "❌",
        "color": "#dc3545",
        "description": "Sarang lebah sedang dirampas oleh lebah dari koloni lain. Kondisi sangat kritis dan memerlukan penanganan segera.",
        "gejala": [
            "Banyak lebah asing di sekitar sarang",
            "Pertempuran hebat di depan pintu masuk sarang",
            "Lebah penduduk asli terlihat lemah dan kalah",
            "Madu di sarang mulai hilang atau berkurang drastis",
            "Sarang terlihat rusak dan berantakan",
            "Banyak lebah mati di sekitar sarang",
            "Lebah asing terlihat masuk dan keluar dengan bebas"
        ],
        "pengobatan": [
            {
                "metode": "Penanganan Darurat",
                "langkah": [
                    "Tutup sebagian pintu masuk sarang (reduce entrance) hanya cukup untuk beberapa lebah",
                    "Semprotkan air dingin pada lebah perampok untuk memperlambatnya",
                    "Pasang kain basah di atas sarang untuk menenangkan lebah",
                    "Jangan buka sarang saat rampokan berlangsung",
                    "Pasang robber screen (pelindung anti-rampok)"
                ]
            },
            {
                "metode": "Pencegahan Lanjutan",
                "langkah": [
                    "Berikan pakan tambahan (sugar syrup 1:1) agar lebah tidak keluar mencari makan",
                    "Pastikan semua koloni memiliki cukup madu dan pakan",
                    "Gunakan entrance reducer untuk membatasi akses",
                    "Pantau sarang secara intensif selama beberapa hari"
                ]
            }
        ],
        "pencegahan": [
            "Jangan biarkan sarang kosong terlalu lama",
            "Berikan pakan tambahan saat sumber nektar sedikit",
            "Gunakan entrance reducer untuk membatasi akses",
            "Jangan buka sarang terlalu lama (>10 menit)",
            "Pastikan semua koloni dalam kondisi sehat dan kuat"
        ],
        "madu_status": "TIDAK AMAN",
        "madu_info": "Madu dari sarang yang dirampas TIDAK AMAN karena sudah terkontaminasi dan tercampur dengan madu dari koloni lain.",
        "estimasi_panen": "TIDAK BOLEH dipanen. Madu sudah rusak/rampok oleh koloni lain.",
        "tips_panen": [
            "Jangan panen madu dari sarang yang baru dirampas",
            "Tunggu koloni pulih dan mulai menyimpan madu baru",
            "Proses pemulihan bisa memakan waktu 2-4 minggu",
            "Pastikan ratu masih ada dan bertelur dengan baik",
            "Baru boleh panen setelah sarang terisi penuh kembali"
        ]
    },

    "missing_queen": {
        "name": "Missing Queen",
        "name_id": "Ratu Hilang/Mati",
        "status": "danger",
        "icon": "❌",
        "color": "#dc3545",
        "description": "Ratu lebah tidak ditemukan atau sudah mati. Tanpa ratu, koloni tidak bisa bertahan lama dan akan runtuh dalam 4-6 minggu.",
        "gejala": [
            "Tidak ditemukan telur atau larva muda di sarang",
            "Populasi lebah menurun drastis",
            "Lebah terlihat bingung dan tidak produktif",
            "Terdengar suara piping dari lebah pekerja",
            "Beberapa lebah mulai bertelur sendiri (laying worker)",
            "Sarang mulai kosong dari madu dan pollen",
            "Tidak ada pola brood yang teratur"
        ],
        "pengobatan": [
            {
                "metode": "Penggantian Ratu Baru",
                "langkah": [
                    "Beli ratu baru dari peternak terpercaya",
                    "Pasang ratu dalam cage (kandang ratu) di tengah sarang",
                    "Biarkan lebah pekerja menerima ratu baru selama 3-5 hari",
                    "Buka cage setelah ratu diterima oleh koloni",
                    "Pantau apakah ratu mulai bertelur dalam 1-2 minggu"
                ]
            },
            {
                "metode": "Pembuatan Ratu Baru (Queen Rearing)",
                "langkah": [
                    "Cari frame dengan telur muda (umur 1-3 hari)",
                    "Biarkan lebah membuat queen cells sendiri",
                    "Pilih queen cell terbaik untuk dipelihara",
                    "Tunggu ratu baru menetas dan kawin (2-3 minggu)",
                    "Pantau apakah ratu baru mulai bertelur"
                ]
            }
        ],
        "pencegahan": [
            "Ganti ratu secara berkala (setiap 1-2 tahun)",
            "Pantau tanda-tanda ratu mulai tua (produksi telur menurun)",
            "Pastikan ratu memiliki cukup makanan dan perawatan",
            "Hindari penggunaan pestisida yang bisa membunuh ratu",
            "Jangan terlalu sering mengganggu sarang saat ratu sedang bertelur"
        ],
        "madu_status": "TIDAK AMAN",
        "madu_info": "Tanpa ratu, koloni akan mati dalam 4-6 minggu. Madu yang tersisa tidak layak panen karena kualitas menurun.",
        "estimasi_panen": "TIDAK BOLEH dipanen. Fokus utama adalah pemulihan koloni dengan ratu baru.",
        "tips_panen": [
            "Jangan panen madu sampai ratu baru aktif bertelur",
            "Tunggu minimal 1 bulan setelah ratu baru dipasang",
            "Pastikan populasi lebah sudah pulih (minimal 5 frame bees)",
            "Baru boleh panen setelah sarang terisi penuh dengan madu",
            "Monitor perkembangan koloni setiap minggu"
        ]
    }
}

HEALTH_CLASS_MAPPING = {
    "Varroa, Small Hive Beetles": "varroa_small_hive_beetles",
    "Ant Problems": "ant_problems",
    "Few Varroa, Hive Beetles": "few_varroa_hive_beetles",
    "Healthy": "healthy",
    "Hive Being Robbed": "hive_being_robbed",
    "Missing Queen": "missing_queen",
}

def get_disease_info(health_class_name: str) -> dict:
    disease_key = HEALTH_CLASS_MAPPING.get(health_class_name, "healthy")
    return DISEASE_DATABASE.get(disease_key, DISEASE_DATABASE["healthy"])
