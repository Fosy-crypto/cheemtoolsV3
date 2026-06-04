import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# ==================== CONFIG ====================
st.set_page_config(
    page_title="ChemLab Mini Tools",
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

# Session State Initialization
if 'analisis' not in st.session_state:
    st.session_state.analisis = False

if 'skor' not in st.session_state:
    st.session_state.skor = 0

if 'total' not in st.session_state:
    st.session_state.total = 0

# ==================== SIDEBAR ====================
with st.sidebar:
    st.markdown("# Menu Utama")
    menu = st.selectbox(
        "Pilih Fitur",
        [
            "Beranda",
            "Kalkulator Pengenceran",
            "Tebak Warna Reaksi",
            "Analisis Kesalahan Praktikum",
            "Panduan & Tips"
        ]
    )
    
    st.divider()
    st.markdown("### Tentang Aplikasi")
    st.info("ChemLab Mini Tools membantu Anda belajar kimia dengan cara interaktif!")

# ==================== HALAMAN UTAMA ====================
if menu == "Beranda":
    st.title("ChemLab Mini Tools")
    st.markdown("### Selamat datang di platform pembelajaran kimia interaktif!")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>Kalkulator</h3>
            <p>Hitung pengenceran larutan dengan mudah</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>Game Quiz</h3>
            <p>Asah pengetahuan dengan tebak warna reaksi</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>Troubleshooting</h3>
            <p>Analisis kesalahan praktikum Anda</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    st.markdown("### Mulai Sekarang!")
    st.markdown("Pilih fitur di menu sebelah kiri untuk memulai!")

# ==================== KALKULATOR PENGENCERAN ====================
elif menu == "Kalkulator Pengenceran":
    st.header("Kalkulator Pengenceran")
    st.markdown("Gunakan rumus: M1V1 = M2V2")
    
    tab1, tab2, tab3 = st.tabs(["Kalkulator", "Panduan", "Riwayat"])
    
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
                hitung_btn = st.button("Hitung V2", use_container_width=True)
                
                if hitung_btn:
                    if M2 != 0:
                        V2 = (M1 * V1) / M2
                        st.markdown(f"""
                        <div class="success-card">
                            <h4>Hasil Perhitungan</h4>
                            <h2>V2 = {V2:.2f} mL</h2>
                            <p>Air ditambahkan: {V2 - V1:.2f} mL</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
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
                        st.error("M2 tidak boleh nol!")
            
            else:
                V2 = st.number_input("Volume Akhir (V2) [mL]", min_value=0.0, value=200.0, step=10.0)
                hitung_btn = st.button("Hitung M2", use_container_width=True)
                
                if hitung_btn:
                    if V2 != 0:
                        M2 = (M1 * V1) / V2
                        st.markdown(f"""
                        <div class="success-card">
                            <h4>Hasil Perhitungan</h4>
                            <h2>M2 = {M2:.4f} mol/L</h2>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        fig = go.Figure()
                        fig.add_trace(go.Bar(
                            x=['Awal', 'Akhir'],
                            y=[M1, M2],
                            marker=dict(color=['#FF6B6B', '#4ECDC4']),
                            text=[f'{M1:.2f} M', f'{M2:.4f} M'],
                            textposition='auto',
                        ))
                        fig.update_layout(title="Perubahan Konsentrasi", height=300)
                        st.plotly_chart(fig, use_container_width=True)
                    else:
                        st.error("V2 tidak boleh nol!")
        
        with col2:
            st.subheader("Rumus & Formula")
            st.info("""
            Rumus Pengenceran:
            
            M1V1 = M2V2
            
            dimana:
            - M1 = Konsentrasi awal
            - V1 = Volume awal
            - M2 = Konsentrasi akhir
            - V2 = Volume akhir
            """)
            
            st.warning("""
            Tips Penting:
            - Pastikan satuan volume konsisten
            - Pengenceran = M berkurang, V bertambah
            - Jumlah mol zat terlarut tetap sama
            """)
    
    with tab2:
        st.markdown("""
        ### Panduan Pengenceran Larutan
        
        Pengenceran adalah proses menambahkan pelarut untuk menurunkan konsentrasi.
        
        Langkah-langkah:
        1. Hitung volume larutan pekat yang dibutuhkan
        2. Hitung volume pelarut yang ditambahkan
        3. Campurkan perlahan sambil diaduk
        4. Biarkan sebentar agar merata
        
        Contoh:
        - 100 mL HCl 2M ingin dibuat 0.5M
        - V2 = (2 x 100) / 0.5 = 400 mL
        """)
    
    with tab3:
        st.info("Riwayat perhitungan akan ditampilkan di sini")

# ==================== TEBAK WARNA REAKSI ====================
elif menu == "Tebak Warna Reaksi":
    st.header("Tebak Warna Reaksi - Game Quiz")
    
    if 'skor' not in st.session_state:
        st.session_state.skor = 0
        st.session_state.total = 0
    
    soal_list = [
        {
            "pertanyaan": "KMnO4 + Fe2+ -> warna?",
            "pilihan": ["Ungu", "Bening", "Coklat", "Hijau"],
            "jawaban": "Bening",
            "penjelasan": "KMnO4 (ungu) tereduksi menjadi Mn2+ (tidak berwarna)"
        },
        {
            "pertanyaan": "Ag+ + Cl- -> endapan?",
            "pilihan": ["Putih", "Kuning", "Biru", "Merah"],
            "jawaban": "Putih",
            "penjelasan": "AgCl membentuk endapan putih"
        },
        {
            "pertanyaan": "I2 dalam larutan -> warna?",
            "pilihan": ["Merah", "Coklat", "Ungu", "Hijau"],
            "jawaban": "Coklat",
            "penjelasan": "Iodium berwarna coklat kemerahan"
        },
        {
            "pertanyaan": "CuSO4 + NaOH -> endapan?",
            "pilihan": ["Putih", "Biru", "Merah", "Kuning"],
            "jawaban": "Biru",
            "penjelasan": "Cu(OH)2 membentuk endapan biru"
        },
        {
            "pertanyaan": "Fe3+ + SCN- -> warna?",
            "pilihan": ["Biru", "Merah", "Hijau", "Kuning"],
            "jawaban": "Merah",
            "penjelasan": "Kompleks Fe(SCN)2+ berwarna merah darah"
        }
    ]
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Skor", st.session_state.skor)
    with col2:
        st.metric("Total", st.session_state.total)
    with col3:
        if st.session_state.total > 0:
            persentase = (st.session_state.skor / st.session_state.total) * 100
            st.metric("Akurasi", f"{persentase:.0f}%")
    
    st.divider()
    
    tabs = st.tabs([f"Soal {i+1}" for i in range(len(soal_list))])
    
    for idx, (tab, soal) in enumerate(zip(tabs, soal_list)):
        with tab:
            st.subheader(soal['pertanyaan'])
            
            jawaban_user = st.radio(
                "Pilih jawaban:",
                soal['pilihan'],
                key=f"soal_{idx}"
            )
            
            col_a, col_b = st.columns(2)
            with col_a:
                if st.button(f"Cek Jawaban {idx+1}", key=f"cek_{idx}", use_container_width=True):
                    st.session_state.total += 1
                    
                    if jawaban_user == soal['jawaban']:
                        st.session_state.skor += 1
                        st.markdown(f"<div class='success-card'><h3>Benar!</h3><p>{soal['penjelasan']}</p></div>", unsafe_allow_html=True)
                    else:
                        st.markdown(f"<div class='error-card'><h3>Salah!</h3><p>Jawaban: {soal['jawaban']}</p></div>", unsafe_allow_html=True)
            
            with col_b:
                if st.button("Lihat Penjelasan", key=f"hint_{idx}", use_container_width=True):
                    st.info(soal['penjelasan'])

# ==================== ANALISIS KESALAHAN ====================
elif menu == "Analisis Kesalahan Praktikum":
    st.header("Analisis Kesalahan Praktikum")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        masalah = st.selectbox(
            "Masalah yang terjadi:",
            [
                "Pilih masalah...",
                "Larutan tidak berubah warna",
                "Hasil titrasi berbeda jauh",
                "End point terlalu cepat",
                "Kristal tidak terbentuk",
                "Gas tidak keluar"
            ]
        )
    
    with col2:
        if st.button("Analisis", use_container_width=True):
            st.session_state.analisis = True
    
    st.divider()
    
    if st.session_state.analisis:
        if masalah == "Pilih masalah...":
            st.warning("Silakan pilih masalah terlebih dahulu")
        
        elif masalah == "Larutan tidak berubah warna":
            st.markdown("""
            <div class="error-card">
                <h3>Kemungkinan Penyebab:</h3>
            </div>
            """, unsafe_allow_html=True)
            
            c1, c2, c3 = st.columns(3)
            
            with c1:
                st.markdown("""
                **Masalah Utama:**
                1. Indikator salah
                2. Reagen tidak bereaksi
                3. pH tidak sesuai
                """)
            
            with c2:
                st.markdown("""
                **Solusi:**
                1. Periksa jenis indikator
                2. Pastikan reagen segar
                3. Ukur pH larutan
                """)
            
            with c3:
                st.markdown("""
                **Pencegahan:**
                1. Catat tanggal kadaluarsa
                2. Simpan di tempat gelap
                3. Gunakan wadah tertutup
                """)
        
        elif masalah == "Hasil titrasi berbeda jauh":
            st.markdown("""
            <div class="error-card">
                <h3>Kemungkinan Penyebab:</h3>
            </div>
            """, unsafe_allow_html=True)
            
            c1, c2, c3 = st.columns(3)
            
            with c1:
                st.markdown("""
                **Masalah Utama:**
                1. Kesalahan pembacaan buret
                2. Larutan tidak homogen
                3. Teknik pipet salah
                """)
            
            with c2:
                st.markdown("""
                **Solusi:**
                1. Baca meniskus di mata sejajar
                2. Aduk larutan dengan baik
                3. Pegang pipet vertikal
                """)
            
            with c3:
                st.markdown("""
                **Pencegahan:**
                1. Kalibrasikan alat ukur
                2. Lakukan minimal 3x titrasi
                3. Ambil rata-rata yang konsisten
                """)
        
        elif masalah == "End point terlalu cepat":
            st.markdown("""
            <div class="error-card">
                <h3>Kemungkinan Penyebab:</h3>
            </div>
            """, unsafe_allow_html=True)
            
            c1, c2, c3 = st.columns(3)
            
            with c1:
                st.markdown("""
                **Masalah Utama:**
                1. Konsentrasi terlalu tinggi
                2. Salah perhitungan awal
                3. Alat tidak bersih
                """)
            
            with c2:
                st.markdown("""
                **Solusi:**
                1. Encerkan larutan
                2. Hitung ulang volume
                3. Cuci alat dengan baik
                """)
            
            with c3:
                st.markdown("""
                **Pencegahan:**
                1. Lakukan uji pendahuluan
                2. Gunakan pipet lebih kecil
                3. Tambahkan indikator hati-hati
                """)
        
        elif masalah == "Kristal tidak terbentuk":
            st.markdown(f"""
            <div class="error-card">
                <h3>Kemungkinan Penyebab:</h3>
                <ul>
                <li>Proses kristalisasi terlalu cepat</li>
                <li>Kelarutan terlalu tinggi</li>
                <li>Pengadukan berlebihan</li>
                </ul>
                <h3>Solusi:</h3>
                <ul>
                <li>Pelankan pendinginan</li>
                <li>Kentalkan larutan</li>
                <li>Biarkan diam</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        elif masalah == "Gas tidak keluar":
            st.markdown(f"""
            <div class="error-card">
                <h3>Kemungkinan Penyebab:</h3>
                <ul>
                <li>Suhu reaksi terlalu rendah</li>
                <li>Katalis tidak aktif</li>
                <li>Reagen sudah kadaluarsa</li>
                </ul>
                <h3>Solusi:</h3>
                <ul>
                <li>Panaskan reaksi</li>
                <li>Ganti katalis baru</li>
                <li>Siapkan reagen segar</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

# ==================== PANDUAN & TIPS ====================
elif menu == "Panduan & Tips":
    st.header("Panduan & Tips Belajar Kimia")
    
    tab1, tab2, tab3 = st.tabs(["Teori", "Tips Praktikum", "Reaksi"])
    
    with tab1:
        st.subheader("Teori Dasar Pengenceran & Titrasi")
        st.markdown("""
        ### 1. Pengenceran
