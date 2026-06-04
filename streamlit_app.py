 🔧 Kode yang sudah diperbaiki

```python
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
    • 🧮 Kalkulator pengenceran
    • 🎯 Game quiz warna reaksi
    • 🔧 Troubleshooting praktikum
    • 🎨 5 tema warna berbeda
    """)

# ==================== DASHBOARD ====================
if menu == "📊 Dashboard":
    st.title("📊 Dashboard ChemLab")
    
    # Inisialisasi session state jika belum ada
    if 'total' not in st.session_state:
        st.session_state.total = 0
    if 'skor' not in st.session_state:
        st.session_state.skor = 0
    
    # Statistik cards
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
    
    # Charts
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
            st.info("📭 Belum ada data quiz!")
    
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
        st.markdown(f"""
        <div class="metric-card">
            <h3>📊 Kalkulator</h3>
            <p>Hitung pengenceran larutan dengan mudah menggunakan rumus M₁V₁ = M₂V₂</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <h3>🎮 Game Quiz</h3>
            <p>Asah pengetahuan dengan tebak warna reaksi dan dapatkan skor</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <h3>🧠 Troubleshooting</h3>
            <p>Analisis kesalahan praktikum dan temukan solusinya</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    st.subheader("🎨 Tema yang Tersedia:")
    st.markdown(f"""
    - 💡 **Light** - Terang dan minimalis
    - 🌙 **Dark** - Gelap untuk mata yang nyaman
    - 🌊 **Ocean** - Biru seperti laut
    - 🌲 **Forest** - Hijau alam yang menenangkan
    - 🌅 **Sunset** - Warna hangat matahari terbenam
    
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
                        air_ditambahkan = V2 - V1
                        st.markdown(f"""
                        <div class="success-card">
                            <h4>✅ Hasil Perhitungan</h4>
                            <h2>V2 = {V2:.2f} mL</h2>
                            <p><strong>Arti:</strong> Encerkan {V1:.0f} mL larutan {M1} M dengan air hingga volume menjadi {V2:.2f} mL</p>
                            <p><strong>Air yang ditambahkan:</strong> {air_ditambahkan:.2f} mL</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Visualisasi
                        fig = go.Figure()
                        fig.add_trace(go.Bar(
                            x=['Awal', 'Akhir'],
                            y=[V1, V2],
                            marker=dict(color=[tema_aktif['primary'], tema_aktif['secondary']]),
                            text=[f'{V1:.0f} mL', f'{V2:.2f} mL'],
                            textposition='auto',
                        ))
                        fig.update_layout(
                            title="Perubahan Volume",
                            height=300,
                            paper_bgcolor=tema_aktif['bg_color'],
                            plot_bgcolor=tema_aktif['card_bg'],
                            font=dict(color=tema_aktif['text_color'])
                        )
                        st.plotly_chart(fig, use_container_width=True)
                    else:
                        st.error("❌ M2 tidak boleh nol atau negatif!")
            
            else:  # Hitung M2
                V2 = st.number_input("Volume Akhir (V2) [mL]", min_value=0.0, value=200.0, step=10.0)
                hitung_btn = st.button("🔢 Hitung M2", use_container_width=True)
                
                if hitung_btn:
                    if V2 > 0:
                        M2 = (M1 * V1) / V2
                        pengenceran = M1 / M2 if M2 > 0 else 0
                        st.markdown(f"""
                        <div class="success-card">
                            <h4>✅ Hasil Perhitungan</h4>
                            <h2>M2 = {M2:.4f} mol/L</h2>
                            <p><strong>Arti:</strong> Konsentrasi larutan setelah pengenceran menjadi {M2:.4f} mol/L</p>
                            <p><strong>Tingkat pengenceran:</strong> {pengenceran:.2f} kali</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Visualisasi
                        fig = go.Figure()
                        fig.add_trace(go.Bar(
                            x=['Awal', 'Akhir'],
                            y=[M1, M2],
                            marker=dict(color=[tema_aktif['primary'], tema_aktif['secondary']]),
                            text=[f'{M1:.2f} M', f'{M2:.4f} M'],
                            textposition='auto',
                        ))
                        fig.update_layout(
                            title="Perubahan Konsentrasi",
                            height=300,
                            paper_bgcolor=tema_aktif['bg_color'],
                            plot_bgcolor=tema_aktif['card_bg'],
                            font=dict(color=tema_aktif['text_color'])
                        )
                        st.plotly_chart(fig, use_container_width=True)
                    else:
                        st.error("❌ V2 tidak boleh nol atau negatif!")
        
        with col2:
            st.subheader("📐 Rumus & Formula")
            st.info("""
            **Rumus Pengenceran:**
            
            M₁V₁ = M₂V₂
            
            Keterangan:
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
        - **Jawab:** V₂ =
