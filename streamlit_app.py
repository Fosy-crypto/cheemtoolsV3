import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
# ==================== CONFIG ====================
st.set_page_config(
    page_title="🧪 ChemLab Mini Tools",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #FF6B6B;
    }
    .success-card {
        background-color: #d4edda;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #28a745;
    }
    .error-card {
        background-color: #f8d7da;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #dc3545;
    }
    </style>
""", unsafe_allow_html=True)
if 'analisis' not in st.session_state:
    st.session_state.analisis = False

if 'skor' not in st.session_state:
    st.session_state.skor = 0

if 'total' not in st.session_state:
    st.session_state.total = 0
# ==================== SIDEBAR ====================
with st.sidebar:
    st.markdown("# ⚙️ Menu Utama")
    menu = st.selectbox(
        "Pilih Fitur",
        [
            "🏠 Beranda",
            "📊 Kalkulator Pengenceran",
            "🎮 Tebak Warna Reaksi",
            "🧠 Analisis Kesalahan Praktikum",
            "📚 Panduan & Tips"
        ]
    )
    
    st.divider()
    st.markdown("### 📌 Tentang Aplikasi")
    st.info("ChemLab Mini Tools membantu Anda belajar kimia dengan cara yang interaktif dan menyenangkan!")

# ==================== HALAMAN UTAMA ====================
if menu == "🏠 Beranda":
    st.title("🧪 ChemLab Mini Tools")
    st.markdown("### Selamat datang di platform pembelajaran kimia interaktif!")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>📊 Kalkulator</h3>
            <p>Hitung pengenceran larutan dengan mudah</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>🎮 Game Quiz</h3>
            <p>Asah pengetahuan dengan tebak warna reaksi</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>🧠 Troubleshooting</h3>
            <p>Analisis kesalahan praktikum Anda</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    st.markdown("### 🚀 Mulai Sekarang!")
    st.markdown("Pilih fitur di menu sebelah kiri untuk memulai pembelajaran!")

# ==================== KALKULATOR PENGENCERAN ====================
elif menu == "📊 Kalkulator Pengenceran":
    st.header("📊 Kalkulator Pengenceran")
    st.markdown("Gunakan rumus: **M₁V₁ = M₂V₂**")
    
    tab1, tab2, tab3 = st.tabs(["📐 Kalkulator", "📖 Panduan", "💾 Riwayat"])
    
    with tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Input Data")
            M1 = st.number_input("Konsentrasi Awal (M1) [mol/L]", min_value=0.0, value=1.0, step=0.1)
            V1 = st.number_input("Volume Awal (V1) [mL]", min_value=0.0, value=100.0, step=10.0)
            
            pilihan_hitung = st.radio(
                "Apa yang ingin dihitung?",
                ["Volume Akhir (V2)", "Konsentrasi Akhir (M2)"]
            )
            
            if pilihan_hitung == "Volume Akhir (V2)":
                M2 = st.number_input("Konsentrasi Akhir (M2) [mol/L]", min_value=0.0, value=0.5, step=0.1)
                hitung_btn = st.button("🔢 Hitung V2", use_container_width=True)
                
                if hitung_btn:
                    if M2 != 0:
                        V2 = (M1 * V1) / M2
                        st.markdown(f"""
                        <div class="success-card">
                            <h4>✅ Hasil Perhitungan</h4>
                            <h2>V2 = {V2:.2f} mL</h2>
                            <p><strong>Arti:</strong> Encerkan {V1:.0f} mL larutan {M1} M dengan air hingga volumenya menjadi {V2:.2f} mL</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Visualisasi
                        fig = go.Figure()
                        fig.add_trace(go.Bar(
                            x=['Awal', 'Akhir'],
                            y=[V1, V2],
                            marker=dict(color=['#FF6B6B', '#4ECDC4']),
                            text=[f'{V1:.0f} mL', f'{V2:.2f} mL'],
                            textposition='auto',
                        ))
                        fig.update_layout(title="Perubahan Volume", height=300)
                        st.plotly_chart(fig, use_container_width=True)
                    else:
                        st.error("❌ M2 tidak boleh nol!")
            
            else:  # Hitung M2
                V2 = st.number_input("Volume Akhir (V2) [mL]", min_value=0.0, value=200.0, step=10.0)
                hitung_btn = st.button("🔢 Hitung M2", use_container_width=True)
                
                if hitung_btn:
                    if V2 != 0:
                        M2 = (M1 * V1) / V2
                        st.markdown(f"""
                        <div class="success-card">
                            <h4>✅ Hasil Perhitungan</h4>
                            <h2>M2 = {M2:.4f} mol/L</h2>
                            <p><strong>Arti:</strong> Konsentrasi larutan setelah pengenceran menjadi {M2:.4f} mol/L</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Visualisasi
                        fig = go.Figure()
                        fig.add_trace(go.Bar(
                            x=['Awal', 'Akhir'],
                            y=[M1, M2],
                            marker=dict(color=['#FF6B6B', '#4ECDC4']),
                            text=[f'{M1:.2f} mol/L', f'{M2:.4f} mol/L'],
                            textposition='auto',
                        ))
                        fig.update_layout(title="Perubahan Konsentrasi", height=300)
                        st.plotly_chart(fig, use_container_width=True)
                    else:
                        st.error("❌ V2 tidak boleh nol!")
        
        with col2:
            st.subheader("📐 Rumus & Formula")
            st.info("""
            **Rumus Pengenceran:**
            
            M₁V₁ = M₂V₂
            
            Dimana:
            - M₁ = Konsentrasi awal (mol/L)
            - V₁ = Volume awal (mL)
            - M₂ = Konsentrasi akhir (mol/L)
            - V₂ = Volume akhir (mL)
            """)
            
            st.warning("""
            **💡 Tips Penting:**
            - Pastikan satuan volume konsisten
            - Pengenceran = M berkurang, V bertambah
            - Jumlah mol zat terlarut tetap sama
            """)
    
    with tab2:
        st.markdown("""
        ### 📖 Panduan Pengenceran Larutan
        
        **Apa itu pengenceran?**
        Pengenceran adalah proses menambahkan pelarut (biasanya air) ke dalam larutan untuk menurunkan konsentrasinya.
        
        **Langkah-langkah praktis:**
        1. Hitung berapa banyak larutan pekat yang dibutuhkan
        2. Hitung berapa banyak pelarut (air) yang ditambahkan
        3. Campurkan perlahan sambil diaduk
        4. Biarkan sebentar agar merata
        
        **Contoh soal:**
        - Anda punya 100 mL larutan HCl 2 M
        - Ingin membuat larutan HCl 0.5 M
        - Berapa volume akhir yang dihasilkan?
        - **Jawab:** V₂ = (2 × 100) / 0.5 = 400 mL
        """)
    
    with tab3:
        st.info("💾 Riwayat perhitungan akan ditampilkan di sini")

# ==================== TEBAK WARNA REAKSI ====================
elif menu == "🎮 Tebak Warna Reaksi":
    st.header("🎮 Tebak Warna Reaksi - Game Quiz")
    
    if 'skor' not in st.session_state:
        st.session_state.skor = 0
        st.session_state.total = 0
    
    # Soal-soal
    soal_list = [
        {
            "pertanyaan": "KMnO4 + Fe²⁺ → warna apa?",
            "pilihan": ["Ungu", "Bening", "Coklat", "Hijau"],
            "jawaban": "Bening",
            "penjelasan": "KMnO4 (ungu) tereduksi menjadi Mn²⁺ (tidak berwarna). Ungu hilang → Bening"
        },
        {
            "pertanyaan": "Ag⁺ + Cl⁻ → endapan warna?",
            "pilihan": ["Putih", "Kuning", "Biru", "Merah"],
            "jawaban": "Putih",
            "penjelasan": "AgCl membentuk endapan putih yang tidak larut dalam air"
        },
        {
            "pertanyaan": "I₂ dalam larutan → warna?",
            "pilihan": ["Merah", "Coklat", "Ungu", "Hijau"],
            "jawaban": "Coklat",
            "penjelasan": "I₂ (iodium) dalam larutan berubah menjadi warna coklat kemerahan"
        },
        {
            "pertanyaan": "CuSO4 + NaOH → endapan?",
            "pilihan": ["Putih", "Biru", "Merah", "Kuning"],
            "jawaban": "Biru",
            "penjelasan": "Cu(OH)₂ membentuk endapan biru muda"
        },
        {
            "pertanyaan": "Fe³⁺ + SCN⁻ → warna?",
            "pilihan": ["Biru", "Merah", "Hijau", "Kuning"],
            "jawaban": "Merah",
            "penjelasan": "Kompleks [Fe(SCN)]²⁺ memberikan warna merah/merah darah"
        }
    ]
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Skor", st.session_state.skor)
    with col2:
        st.metric("Total Soal", st.session_state.total)
    with col3:
        if st.session_state.total > 0:
            persentase = (st.session_state.skor / st.session_state.total) * 100
            st.metric("Akurasi", f"{persentase:.0f}%")
    
    st.divider()
    
    tabs = st.tabs([f"Soal {i+1}" for i in range(len(soal_list))])
    
    for idx, (tab, soal) in enumerate(zip(tabs, soal_list)):
        with tab:
            st.subheader(f"❓ {soal['pertanyaan']}")
            
            jawaban_user = st.radio(
                "Pilih jawaban:",
                soal['pilihan'],
                key=f"soal_{idx}"
            )
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"✅ Cek Jawaban {idx+1}", use_container_width=True):
                    st.session_state.total += 1
                    
                    if jawaban_user == soal['jawaban']:
                        st.session_state.skor += 1
                        st.markdown(f"""
                        <div class="success-card">
                            <h3>🎉 Benar!</h3>
                            <p>{soal['penjelasan']}</p>
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div class="error-card">
                            <h3>❌ Salah!</h3>
                            <p><strong>Jawaban benar:</strong> {soal['jawaban']}</p>
                            <p><strong>Penjelasan:</strong> {soal['penjelasan']}</p>
                        </div>
                        """, unsafe_allow_html=True)
            
           with col2:
    if st.button(
        "💡 Lihat Penjelasan",
        key=f"penjelasan_{idx}",
        use_container_width=True
    ):
        st.info(soal['penjelasan'])
# ==================== ANALISIS KESALAHAN ====================
elif menu == "🧠 Analisis Kesalahan Praktikum":
    st.header("🧠 Analisis Kesalahan Praktikum")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        masalah = st.selectbox(
            "Masalah yang terjadi:",
            [
                "Pilih masalah...",
                "❌ Larutan tidak berubah warna",
                "❌ Hasil titrasi berbeda jauh",
                "⏱️ End point terlalu cepat",
                "🧂 Kristal tidak terbentuk",
                "🫧 Gas tidak keluar"
            ]
        )
    
    with col2:
        if st.button("🔍 Analisis", use_container_width=True):
            st.session_state.analisis = True
    
    st.divider()
    
    if 'analisis' in st.session_state and st.session_state.analisis:
        if masalah == "Pilih masalah...":
            st.warning("Silakan pilih masalah terlebih dahulu")
        
        elif masalah == "❌ Larutan tidak berubah warna":
            st.markdown("""
            <div class="error-card">
                <h3>📋 Kemungkinan Penyebab:</h3>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("""
                **🔴 Masalah Utama:**
                1. Indikator salah
                2. Reagen tidak bereaksi
                3. pH tidak sesuai
                """)
            
            with col2:
                st.markdown("""
                **🟡 Solusi:**
                1. Periksa jenis indikator
                2. Pastikan reagen segar
                3. Ukur pH larutan
                """)
            
            with col3:
                st.markdown("""
                **🟢 Pencegahan:**
                1. Catat tanggal kadaluarsa
                2. Simpan di tempat gelap
                3. Gunakan wadah tertutup
                """)
        
        elif masalah == "❌ Hasil titrasi berbeda jauh":
            st.markdown("""
            <div class="error-card">
                <h3>📋 Kemungkinan Penyebab:</h3>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("""
                **🔴 Masalah Utama:**
                1. Kesalahan pembacaan buret
                2. Larutan tidak homogen
                3. Teknik pipet salah
                """)
            
            with col2:
                st.markdown("""
                **🟡 Solusi:**
                1. Baca meniskus di mata sejajar
                2. Aduk larutan dengan baik
                3. Pegang pipet vertikal
                """)
            
            with col3:
                st.markdown("""
                **🟢 Pencegahan:**
                1. Kalibrasikan alat ukur
                2. Lakukan minimal 3x titrasi
                3. Ambil rata-rata yang konsisten
                """)
        
        elif masalah == "⏱️ End point terlalu cepat":
            st.markdown("""
            <div class="error-card">
                <h3>📋 Kemungkinan Penyebab:</h3>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("""
                **🔴 Masalah Utama:**
                1. Konsentrasi terlalu tinggi
                2. Salah perhitungan awal
                3. Alat tidak bersih
                """)
            
            with col2:
                st.markdown("""
                **🟡 Solusi:**
                1. Encerkan larutan
                2. Hitung ulang volume
                3. Cuci alat dengan baik
                """)
            
            with col3:
                st.markdown("""
                **🟢 Pencegahan:**
                1. Lakukan uji pendahuluan
                2. Gunakan pipet lebih kecil
                3. Tambahkan indikator hati-hati
                """)

# ==================== PANDUAN & TIPS ====================
elif menu == "📚 Panduan & Tips":
    st.header("📚 Panduan & Tips Belajar Kimia")
    
    tab1, tab2, tab3 = st.tabs(["📖 Teori", "🎯 Tips Praktikum", "⚗️ Reaksi Umum"])
    
    with tab1:
        st.subheader("Teori Dasar Pengenceran & Titrasi")
        st.markdown("""
        ### 1. Pengenceran Larutan
        **Pengenceran** adalah proses menambahkan pelarut untuk mengurangi konsentrasi larutan.
        
        - Mol zat terlarut tetap sama
        - Volume bertambah
        - Konsentrasi berkurang
        
        ### 2. Titrasi
        **Titrasi** adalah teknik untuk menentukan konsentrasi larutan dengan cara mereaksikannya dengan larutan standar.
        
        - Digunakan untuk analisis kuantitatif
        - Memerlukan indikator untuk menentukan end point
        - Harus dilakukan minimal 3 kali untuk hasil akurat
        """)
    
    with tab2:
        st.subheader("🎯 Tips Sukses Praktikum")
        st.markdown("""
        #### Persiapan Sebelum Praktikum
        - ✅ Baca SOP dengan teliti
        - ✅ Siapkan semua alat dan bahan
        - ✅ Periksa kondisi alat (bersih, tidak bocor)
        - ✅ Gunakan APD lengkap (jas lab, sarung tangan, kacamata)
        
        #### Selama Praktikum
        - 🔍 Amati perubahan dengan cermat
        - 📝 Catat data secara real-time
        - 🧼 Cuci alat setelah digunakan
        - 🚨 Minta bantuan jika ada yang tidak jelas
        
        #### Setelah Praktikum
        - 📊 Analisis data dengan statistik
        - 🤔 Bandingkan dengan literatur
        - 📋 Tulis laporan yang jelas dan terstruktur
        """)
    
    with tab3:
        st.subheader("⚗️ Reaksi Kimia Umum & Warnanya")
        
        data_reaksi = {
            "Reaksi": [
                "KMnO₄ (ungu) + Fe²⁺",
                "Ag⁺ + Cl⁻",
                "I₂ dalam larutan",
                "CuSO₄ + NaOH",
                "Fe³⁺ + SCN⁻",
                "K₄[Fe(CN)₆] + Fe³⁺",
                "Cu²⁺ + NH₃"
            ],
            "Warna Hasil": [
                "Bening (ungu hilang)",
                "Endapan putih",
                "Coklat kemerahan",
                "Endapan biru",
                "Merah darah",
                "Biru Prusia",
                "Biru terang"
            ],
            "Catatan": [
                "Permanganat tereduksi",
                "AgCl tidak larut",
                "Halogens berwarna",
                "Cu(OH)₂ membentuk endapan",
                "Kompleks Fe-SCN",
                "Kompleks besi sianida",
                "Kompleks ammin"
            ]
        }
        
        df_reaksi = pd.DataFrame(data_reaksi)
        st.dataframe(df_reaksi, use_container_width=True)

st.divider()
st.markdown("""
<div style="text-align: center; color: #888;">
    <p>🧪 <strong>ChemLab Mini Tools</strong> | Dibuat untuk membantu pembelajaran kimia yang lebih interaktif</p>
    <p>© 2026 | Versio 2.0</p>
</div>
""", unsafe_allow_html=True)
