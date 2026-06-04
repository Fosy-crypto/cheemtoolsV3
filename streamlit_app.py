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

# ==================== THEMA MANAGEMENT ====================
if 'tema' not in st.session_state:
    st.session_state.tema = 'light'

# Dictionary Tema
TEMA_CONFIG = {
    'light': {
        'bg_color': '#ffffff',
        'text_color': '#000000',
        'primary': '#FF6B6B',
        'secondary': '#4ECDC4',
        'accent': '#FFE66D',
        'card_bg': '#f0f2f6',
        'success_bg': '#d4edda',
        'error_bg': '#f8d7da',
    },
    'dark': {
        'bg_color': '#1e1e1e',
        'text_color': '#ffffff',
        'primary': '#FF6B9D',
        'secondary': '#00D9FF',
        'accent': '#FFD700',
        'card_bg': '#2d2d2d',
        'success_bg': '#1e4620',
        'error_bg': '#4d1f1f',
    },
    'ocean': {
        'bg_color': '#e8f4f8',
        'text_color': '#003d5c',
        'primary': '#006BA6',
        'secondary': '#0496FF',
        'accent': '#00D4FF',
        'card_bg': '#cfe9f3',
        'success_bg': '#c8e6c9',
        'error_bg': '#ffcccc',
    },
    'forest': {
        'bg_color': '#f1f5f1',
        'text_color': '#1b4332',
        'primary': '#2d6a4f',
        'secondary': '#52b788',
        'accent': '#74c69d',
        'card_bg': '#d8f3dc',
        'success_bg': '#b7e4c7',
        'error_bg': '#ffcccc',
    },
    'sunset': {
        'bg_color': '#fff5f0',
        'text_color': '#5a2c1e',
        'primary': '#ff6b35',
        'secondary': '#f7931e',
        'accent': '#fdb833',
        'card_bg': '#ffe8d6',
        'success_bg': '#d4edda',
        'error_bg': '#f8d7da',
    }
}

# Ambil tema aktif
tema_aktif = TEMA_CONFIG[st.session_state.tema]

# ==================== CUSTOM CSS ====================
st.markdown(f"""
    <style>
    :root {{
        --bg-color: {tema_aktif['bg_color']};
        --text-color: {tema_aktif['text_color']};
        --primary: {tema_aktif['primary']};
        --secondary: {tema_aktif['secondary']};
        --accent: {tema_aktif['accent']};
    }}
    
    .metric-card {{
        background-color: {tema_aktif['card_bg']};
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid {tema_aktif['primary']};
        color: {tema_aktif['text_color']};
    }}
    
    .success-card {{
        background-color: {tema_aktif['success_bg']};
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid {tema_aktif['secondary']};
        color: {tema_aktif['text_color']};
    }}
    
    .error-card {{
        background-color: {tema_aktif['error_bg']};
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid {tema_aktif['primary']};
        color: {tema_aktif['text_color']};
    }}
    
    .dashboard-box {{
        background-color: {tema_aktif['card_bg']};
        padding: 25px;
        border-radius: 12px;
        border: 2px solid {tema_aktif['primary']};
        margin: 10px 0;
    }}
    </style>
""", unsafe_allow_html=True)

# ==================== SIDEBAR ====================
with st.sidebar:
    st.markdown("# ⚙️ CONTROL PANEL")
    
    # Selector Tema
    st.subheader("🎨 Pilih Tema")
    tema_pilihan = st.selectbox(
        "Pilih tema latar:",
        ["light", "dark", "ocean", "forest", "sunset"],
        index=["light", "dark", "ocean", "forest", "sunset"].index(st.session_state.tema),
        key="tema_select"
    )
    
    if tema_pilihan != st.session_state.tema:
        st.session_state.tema = tema_pilihan
        st.rerun()
    
    # Quick theme buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("💡 Light"):
            st.session_state.tema = 'light'
            st.rerun()
    with col2:
        if st.button("🌙 Dark"):
            st.session_state.tema = 'dark'
            st.rerun()
    
    col3, col4 = st.columns(2)
    with col3:
        if st.button("🌊 Ocean"):
            st.session_state.tema = 'ocean'
            st.rerun()
    with col4:
        if st.button("🌲 Forest"):
            st.session_state.tema = 'forest'
            st.rerun()
    
    st.divider()
    
    # Menu Utama
    st.markdown("# 📋 MENU UTAMA")
    menu = st.selectbox(
        "Pilih Fitur",
        [
            "📊 Dashboard",
            "🏠 Beranda",
            "📐 Kalkulator Pengenceran",
            "🎮 Tebak Warna Reaksi",
            "🧠 Analisis Kesalahan Praktikum",
            "📚 Panduan & Tips"
        ]
    )
    
    st.divider()
    st.markdown("### 📌 Info Aplikasi")
    st.info("""
    **ChemLab Mini Tools v2.0**
    
    Platform pembelajaran kimia interaktif dengan:
    - Kalkulator pengenceran
    - Game quiz warna reaksi
    - Troubleshooting praktikum
    - 5 tema warna berbeda
    """)

# ==================== DASHBOARD ====================
if menu == "📊 Dashboard":
    st.title("📊 Dashboard ChemLab")
    
    if 'total' not in st.session_state:
        st.session_state.total = 0
    if 'skor' not in st.session_state:
        st.session_state.skor = 0
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="dashboard-box">
            <h3>🎮 Quiz Dimainkan</h3>
            <h1>{st.session_state.total}</h1>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="dashboard-box">
            <h3>✅ Jawaban Benar</h3>
            <h1>{st.session_state.skor}</h1>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        akurasi = (st.session_state.skor / st.session_state.total * 100) if st.session_state.total > 0 else 0
        st.markdown(f"""
        <div class="dashboard-box">
            <h3>📈 Akurasi</h3>
            <h1>{akurasi:.0f}%</h1>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="dashboard-box">
            <h3>🎨 Tema Aktif</h3>
            <h1>{st.session_state.tema.upper()}</h1>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Distribusi Jawaban")
        if st.session_state.total > 0:
            fig = go.Figure(data=[
                go.Pie(
                    labels=['Benar', 'Salah'],
                    values=[st.session_state.skor, st.session_state.total - st.session_state.skor],
                    marker=dict(colors=[tema_aktif['secondary'], tema_aktif['primary']])
                )
            ])
            fig.update_layout(height=350, paper_bgcolor=tema_aktif['bg_color'], font=dict(color=tema_aktif['text_color']))
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Belum ada data quiz!")
    
    with col2:
        st.subheader("🎯 Progress Pembelajaran")
        aktivitas = {
            "Kalkulator": 5,
            "Quiz": st.session_state.total,
            "Troubleshooting": 3,
            "Panduan": 10
        }
        
        fig2 = go.Figure(data=[
            go.Bar(
                x=list(aktivitas.keys()),
                y=list(aktivitas.values()),
                marker=dict(color=tema_aktif['secondary'])
            )
        ])
        fig2.update_layout(height=350, paper_bgcolor=tema_aktif['bg_color'], plot_bgcolor=tema_aktif['card_bg'], font=dict(color=tema_aktif['text_color']))
        st.plotly_chart(fig2, use_container_width=True)

# ==================== HALAMAN BERANDA ====================
elif menu == "🏠 Beranda":
    st.title("🧪 ChemLab Mini Tools v2.0")
    st.markdown("### Selamat datang di platform pembelajaran kimia interaktif!")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>📊 Kalkulator</h3>
            <p>Hitung pengenceran larutan dengan mudah menggunakan rumus M₁V₁ = M₂V₂</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>🎮 Game Quiz</h3>
            <p>Asah pengetahuan dengan tebak warna reaksi dan dapatkan skor</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>🧠 Troubleshooting</h3>
            <p>Analisis kesalahan praktikum dan temukan solusinya</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    st.subheader("🎨 Tema yang Tersedia:")
    st.markdown("""
    - **Light** - Terang dan minimalis
    - **Dark** - Gelap untuk mata yang nyaman
    - **Ocean** - Biru seperti laut
    - **Forest** - Hijau alam yang menenangkan
    - **Sunset** - Warna hangat matahari terbenam
    
    **Pilih tema favorit Anda di sidebar!**
    """)

# ==================== KALKULATOR PENGENCERAN ====================
elif menu == "📐 Kalkulator Pengenceran":
    st.header("📐 Kalkulator Pengenceran")
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
                    if M2 > 0:
                        V2 = (M1 * V1) / M2
                        st.markdown(f"""
                        <div class="success-card">
                            <h4>✅ Hasil Perhitungan</h4>
                            <h2>V2 = {V2:.2f} mL</h2>
                            <p>Air yang ditambahkan: {V2 - V1:.2f} mL</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        fig = go.Figure()
                        fig.add_trace(go.Bar(
                            x=['Awal', 'Akhir'],
                            y=[V1, V2],
                            marker=dict(color=[tema_aktif['primary'], tema_aktif['secondary']])
                        ))
                        fig.update_layout(height=300, paper_bgcolor=tema_aktif['bg_color'])
                        st.plotly_chart(fig, use_container_width=True)
                    else:
                        st.error("M2 tidak boleh nol!")
            
            else:
                V2 = st.number_input("Volume Akhir (V2) [mL]", min_value=0.0, value=200.0, step=10.0)
                hitung_btn = st.button("🔢 Hitung M2", use_container_width=True)
                
                if hitung_btn:
                    if V2 > 0:
                        M2 = (M1 * V1) / V2
                        st.markdown(f"""
                        <div class="success-card">
                            <h4>✅ Hasil Perhitungan</h4>
                            <h2>M2 = {M2:.4f} mol/L</h2>
                            <p>Tingkat pengenceran: {M1/M2:.2f}x</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        fig = go.Figure()
                        fig.add_trace(go.Bar(
                            x=['Awal', 'Akhir'],
                            y=[M1, M2],
                            marker=dict(color=[tema_aktif['primary'], tema_aktif['secondary']])
                        ))
                        fig.update_layout(height=300, paper_bgcolor=tema_aktif['bg_color'])
                        st.plotly_chart(fig, use_container_width=True)
                    else:
                        st.error("V2 tidak boleh nol!")
        
        with col2:
            st.subheader("📐 Rumus")
            st.info("""
            **M₁V₁ = M₂V₂**
            
            M1 = Konsentrasi awal
            V1 = Volume awal
            M2 = Konsentrasi akhir
            V2 = Volume akhir
            """)
    
    with tab2:
        st.markdown("""
        ### 📖 Panduan Pengenceran
        
        Pengenceran = menambahkan pelarut untuk menurunkan konsentrasi.
        
        **Contoh:**
        - 100 mL HCl 2M → HCl 0.5M
        - V2 = (2 × 100) / 0.5 = 400 mL
        """)
    
    with tab3:
        st.info("Riwayat akan ditampilkan di sini")

# ==================== QUIZ WARNA REAKSI ====================
elif menu == "🎮 Tebak Warna Reaksi":
    st.header("🎮 Tebak Warna Reaksi - Game Quiz")
    
    if 'skor' not in st.session_state:
        st.session_state.skor = 0
        st.session_state.total = 0
    
    soal_list = [
        {
            "pertanyaan": "KMnO4 + Fe²⁺ → warna apa?",
            "pilihan": ["Ungu", "Bening", "Coklat", "Hijau"],
            "jawaban": "Bening",
            "penjelasan": "KMnO4 (ungu) tereduksi menjadi Mn²⁺ (tidak berwarna)"
        },
        {
            "pertanyaan": "Ag⁺ + Cl⁻ → endapan warna?",
            "pilihan": ["Putih", "Kuning", "Biru", "Merah"],
            "jawaban": "Putih",
            "penjelasan": "AgCl membentuk endapan putih"
        },
        {
            "pertanyaan": "I₂ dalam larutan → warna?",
            "pilihan": ["Merah", "Coklat", "Ungu", "Hijau"],
            "jawaban": "Coklat",
            "penjelasan": "Iodium berwarna coklat kemerahan"
        },
        {
            "pertanyaan": "CuSO4 + NaOH → endapan?",
            "pilihan": ["Putih", "Biru", "Merah", "Kuning"],
            "jawaban": "Biru",
            "penjelasan": "Cu(OH)₂ membentuk endapan biru"
        },
        {
            "pertanyaan": "Fe³⁺ + SCN⁻ → warna?",
            "pilihan": ["Biru", "Merah", "Hijau", "Kuning"],
            "jawaban": "Merah",
            "penjelasan": "Kompleks Fe(SCN)²⁺ berwarna merah darah"
        }
    ]
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Skor", st.session_state.skor)
    with col2:
        st.metric("Total", st.session_state.total)
    with col3:
        if st.session_state.total > 0:
            st
