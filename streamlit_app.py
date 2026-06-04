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

# ==================== THEMA MANAGEMENT ====================
if 'tema' not in st.session_state:
    st.session_state.tema = 'light'

TEMA_CONFIG = {
    'light': {'bg_color': '#ffffff', 'text_color': '#000000', 'primary': '#FF6B6B', 'secondary': '#4ECDC4', 'accent': '#FFE66D', 'card_bg': '#f0f2f6', 'success_bg': '#d4edda', 'error_bg': '#f8d7da'},
    'dark': {'bg_color': '#1e1e1e', 'text_color': '#ffffff', 'primary': '#FF6B9D', 'secondary': '#00D9FF', 'accent': '#FFD700', 'card_bg': '#2d2d2d', 'success_bg': '#1e4620', 'error_bg': '#4d1f1f'},
    'ocean': {'bg_color': '#e8f4f8', 'text_color': '#003d5c', 'primary': '#006BA6', 'secondary': '#0496FF', 'accent': '#00D4FF', 'card_bg': '#cfe9f3', 'success_bg': '#c8e6c9', 'error_bg': '#ffcccc'},
    'forest': {'bg_color': '#f1f5f1', 'text_color': '#1b4332', 'primary': '#2d6a4f', 'secondary': '#52b788', 'accent': '#74c69d', 'card_bg': '#d8f3dc', 'success_bg': '#b7e4c7', 'error_bg': '#ffcccc'},
    'sunset': {'bg_color': '#fff5f0', 'text_color': '#5a2c1e', 'primary': '#ff6b35', 'secondary': '#f7931e', 'accent': '#fdb833', 'card_bg': '#ffe8d6', 'success_bg': '#d4edda', 'error_bg': '#f8d7da'}
}

tema_aktif = TEMA_CONFIG[st.session_state.tema]

# ==================== CUSTOM CSS ====================
st.markdown(f"""
<style>
:root {{ --bg-color: {tema_aktif['bg_color']}; --text-color: {tema_aktif['text_color']}; --primary: {tema_aktif['primary']}; --secondary: {tema_aktif['secondary']}; }}
.metric-card {{ background-color: {tema_aktif['card_bg']}; padding: 20px; border-radius: 10px; border-left: 5px solid {tema_aktif['primary']}; color: {tema_aktif['text_color']}; }}
.success-card {{ background-color: {tema_aktif['success_bg']}; padding: 15px; border-radius: 8px; border-left: 5px solid {tema_aktif['secondary']}; color: {tema_aktif['text_color']}; }}
.error-card {{ background-color: {tema_aktif['error_bg']}; padding: 15px; border-radius: 8px; border-left: 5px solid {tema_aktif['primary']}; color: {tema_aktif['text_color']}; }}
.dashboard-box {{ background-color: {tema_aktif['card_bg']}; padding: 25px; border-radius: 12px; border: 2px solid {tema_aktif['primary']}; margin: 10px 0; }}
</style>
""", unsafe_allow_html=True)

# ==================== SIDEBAR ====================
with st.sidebar:
    st.markdown("# ⚙️ CONTROL PANEL")
    
    st.subheader("🎨 Pilih Tema")
    tema_pilihan = st.selectbox("Pilih tema:", ["light", "dark", "ocean", "forest", "sunset"], index=0, key="tema_select")
    
    if tema_pilihan != st.session_state.tema:
        st.session_state.tema = tema_pilihan
        st.rerun()
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("💡 Light"):
            st.session_state.tema = 'light'
            st.rerun()
    with col2:
        if st.button("🌙 Dark"):
            st.session_state.tema = 'dark'
            st.rerun()
    
    st.divider()
    
    st.markdown("# 📋 MENU UTAMA")
    menu = st.selectbox("Pilih Fitur", ["📊 Dashboard", "🏠 Beranda", "📐 Kalkulator Pengenceran", "🎮 Tebak Warna Reaksi", "🧠 Analisis Kesalahan", "📚 Panduan & Tips"])
    
    st.divider()
    st.markdown("### 📌 Info Aplikasi")
    st.info("ChemLab Mini Tools v2.0 - Platform pembelajaran kimia interaktif")

# ==================== DASHBOARD ====================
if menu == "📊 Dashboard":
    st.title("📊 Dashboard ChemLab")
    
    if 'total' not in st.session_state:
        st.session_state.total = 0
    if 'skor' not in st.session_state:
        st.session_state.skor = 0
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"<div class='dashboard-box'><h3>Quiz Dimainkan</h3><h1>{st.session_state.total}</h1></div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='dashboard-box'><h3>Jawaban Benar</h3><h1>{st.session_state.skor}</h1></div>", unsafe_allow_html=True)
    with col3:
        akurasi = (st.session_state.skor / st.session_state.total * 100) if st.session_state.total > 0 else 0
        st.markdown(f"<div class='dashboard-box'><h3>Akurasi</h3><h1>{akurasi:.0f}%</h1></div>", unsafe_allow_html=True)
    with col4:
        st.markdown(f"<div class='dashboard-box'><h3>Tema</h3><h1>{st.session_state.tema.upper()}</h1></div>", unsafe_allow_html=True)
    
    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Distribusi Jawaban")
        if st.session_state.total > 0:
            fig = go.Figure(go.Pie(labels=['Benar', 'Salah'], values=[st.session_state.skor, st.session_state.total - st.session_state.skor], marker=dict(colors=[tema_aktif['secondary'], tema_aktif['primary']])))
            fig.update_layout(height=350, paper_bgcolor=tema_aktif['bg_color'])
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Belum ada data quiz!")
    with col2:
        st.subheader("Progress")
        fig2 = go.Figure(go.Bar(x=['Kalkulator', 'Quiz', 'Troubleshooting'], y=[5, st.session_state.total, 3], marker=dict(color=tema_aktif['secondary'])))
        fig2.update_layout(height=350, paper_bgcolor=tema_aktif['bg_color'])
        st.plotly_chart(fig2, use_container_width=True)

# ==================== BERANDA ====================
elif menu == "🏠 Beranda":
    st.title("🧪 ChemLab Mini Tools v2.0")
    st.markdown("### Selamat datang di platform pembelajaran kimia interaktif!")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div class='metric-card'><h3>📊 Kalkulator</h3><p>Hitung pengenceran larutan dengan rumus M₁V₁ = M₂V₂</p></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='metric-card'><h3>🎮 Game Quiz</h3><p>Asah pengetahuan warna reaksi</p></div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='metric-card'><h3>🧠 Troubleshooting</h3><p>Analisis kesalahan praktikum</p></div>", unsafe_allow_html=True)
    
    st.divider()
    st.subheader("Tema: Light, Dark, Ocean, Forest, Sunset")

# ==================== KALKULATOR ====================
elif menu == "📐 Kalkulator Pengenceran":
    st.header("📐 Kalkulator Pengenceran")
    st.markdown("Rumus: **M₁V₁ = M₂V₂**")
    
    tab1, tab2, tab3 = st.tabs(["Kalkulator", "Panduan", "Riwayat"])
    
    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Input Data")
            M1 = st.number_input("Konsentrasi Awal (M1)", min_value=0.0, value=1.0, step=0.1)
            V1 = st.number_input("Volume Awal (V1)", min_value=0.0, value=100.0, step=10.0)
            
            pilihan = st.radio("Hitung:", ["Volume Akhir (V2)", "Konsentrasi Akhir (M2)"])
            
            if pilihan == "Volume Akhir (V2)":
                M2 = st.number_input("Konsentrasi Akhir (M2)", min_value=0.0, value=0.5, step=0.1)
                if st.button("Hitung V2"):
                    if M2 > 0:
                        V2 = (M1 * V1) / M2
                        st.markdown(f"<div class='success-card'><h4>✅ Hasil</h4><h2>V2 = {V2:.2f} mL</h2><p>Air ditambahkan: {V2-V1:.2f} mL</p></div>", unsafe_allow_html=True)
                    else:
                        st.error("M2 tidak boleh nol!")
            else:
                V2 = st.number_input("Volume Akhir (V2)", min_value=0.0, value=200.0, step=10.0)
                if st.button("Hitung M2"):
                    if V2 > 0:
                        M2 = (M1 * V1) / V2
                        st.markdown(f"<div class='success-card'><h4>✅ Hasil</h4><h2>M2 = {M2:.4f} mol/L</h2></div>", unsafe_allow_html=True)
                    else:
                        st.error("V2 tidak boleh nol!")
        with col2:
            st.subheader("Rumus")
            st.info("M₁V₁ = M₂V₂")

# ==================== QUIZ ====================
elif menu == "🎮 Tebak Warna Reaksi":
    st.header("🎮 Tebak Warna Reaksi")
    
    if 'skor' not in st.session_state:
        st.session_state.skor = 0
        st.session_state.total = 0
    
    soal_list = [
        {"q": "KMnO4 + Fe²⁺ → warna?", "p": ["Ungu", "Bening", "Coklat", "Hijau"], "j": "Bening", "x": "KMnO4 tereduksi menjadi Mn²⁺ (tidak berwarna)"},
        {"q": "Ag⁺ + Cl⁻ → endapan?", "p": ["Putih", "Kuning", "Biru", "Merah"], "j": "Putih", "x": "AgCl membentuk endapan putih"},
        {"q": "I₂ dalam larutan → warna?", "p": ["Merah", "Coklat", "Ungu", "Hijau"], "j": "Coklat", "x": "Iodium berwarna coklat kemerahan"},
        {"q": "CuSO4 + NaOH → endapan?", "p": ["Putih", "Biru", "Merah", "Kuning"], "j": "Biru", "x": "Cu(OH)₂ membentuk endapan biru"},
        {"q": "Fe³⁺ + SCN⁻ → warna?", "p": ["Biru", "Merah", "Hijau", "Kuning"], "j": "Merah", "x": "Kompleks Fe(SCN)²⁺ merah darah"}
    ]
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Skor", st.session_state.skor)
    with col2:
        st.metric("Total", st.session_state.total)
    with col3:
        if st.session_state.total > 0:
            st.metric("Akurasi", f"{(st.session_state.skor/st.session_state.total)*100:.0f}%")
    
    st.divider()
    
    for idx, soal in enumerate(soal_list):
        with st.expander(f"Soal {idx+1}: {soal['q']}"):
            jawab = st.radio("Pilih:", soal['p'], key=f"q{idx}")
            if st.button(f"Cek Jawaban {idx+1}", key=f"btn{idx}"):
                st.session_state.total += 1
                if jawab == soal['j']:
                    st.session_state.skor += 1
                    st.markdown(f"<div class='success-card'>✅ Benar! {soal['x']}</div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<div class='error-card'>❌ Salah! Jawaban: {soal['j']}</div>", unsafe_allow_html=True)

# ==================== TROUBLESHOOTING ====================
elif menu == "🧠 Analisis Kesalahan":
    st.header("🧠 Analisis Kesalahan Praktikum")
    
    masalah = st.selectbox("Pilih masalah:", ["", "Larutan tidak berubah warna", "Hasil titrasi berbeda jauh", "End point terlalu cepat", "Kristal tidak terbentuk", "Gas tidak keluar"])
    
    if st.button("Analisis"):
        if masalah == "Larutan tidak berubah warna":
            st.markdown("""
            <div class="error-card">
            <h3>📋 Kemungkinan Penyebab:</h3>
            <ul><li>Indikator salah</li><li>Reagen tidak bereaksi</li><li>pH tidak sesuai</li></ul>
            <h3>Solusi:</h3>
            <ul><li>Periksa jenis indikator</li><li>Pastikan reagen segar</li><li>Ukur pH larutan</li></ul>
            </div>
            """, unsafe_allow_html=True)
        elif masalah == "Hasil titrasi berbeda jauh":
            st.markdown("""
            <div class="error-card">
            <h3>📋 Kemungkinan Penyebab:</h3>
            <ul><li>Kesalahan pembacaan buret</li><li>Larutan tidak homogen</li><li>Teknik pipet salah</li></ul>
            <h3>Solusi:</h3>
            <ul><li>Baca meniskus di mata sejajar</li><li>Aduk larutan dengan baik</li><li>Pegang pipet vertikal</li></ul>
            </div>
            """, unsafe_allow_html=True)
        elif masalah == "End point terlalu cepat":
            st.markdown("""
            <div class="error-card">
            <h3>📋 Kemungkinan Penyebab:</h3>
            <ul><li>Konsentrasi terlalu tinggi</li><li>Salah perhitungan awal</li></ul>
            <h3>Solusi:</h3>
            <ul><li>Encerkan larutan</li><li>Hitung ulang volume</li></ul>
            </div>
            """, unsafe_allow_html=True)
        elif masalah == "Kristal tidak terbentuk":
            st.markdown("<div class='error-card'><h3>Solusi:</h3><ul><li>Periksa kecepatan pendinginan</li><li>Periksa kemurnian bahan</li><li>Tunggu lebih lama</li></ul></div>", unsafe_allow_html=True)
        elif masalah == "Gas tidak keluar":
            st.markdown("<div class='error-card'><h3>Solusi:</h3><ul><li>Periksa suhu reaksi</li><li>Periksa katalis</li><li>Ganti reagen</li></ul></div>", unsafe_allow_html=True)

# ==================== PANDUAN ====================
elif menu == "📚 Panduan & Tips":
    st.header("📚 Panduan & Tips")
    
    tab1, tab2, tab3 = st.tabs(["Teori", "Tips Praktikum", "Reaksi"])
    
    with tab1:
        st.markdown("""
        ### Pengenceran Larutan
        Menambahkan pelarut untuk menurunkan konsentrasi.
        
        ### Titrasi
        Teknik menentukan konsentrasi dengan larutan standar.
        """)
    
    with tab2:
        st.markdown("""
        ### Persiapan
        - Baca SOP dengan teliti
        - Siapkan semua alat dan bahan
        - Gunakan APD lengkap
        
        ### Selama Praktikum
        - Amati perubahan dengan cermat
        - Catat data secara real-time
        - Cuci alat setelah digunakan
        """)
    
    with tab3:
        df = pd.DataFrame({
            "Reaksi": ["KMnO4 + Fe²⁺", "Ag⁺ + Cl⁻", "CuSO4 + NaOH", "Fe³⁺ + SCN⁻"],
