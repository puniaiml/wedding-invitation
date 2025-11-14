import streamlit as st
from datetime import datetime, time
import json

# Page configuration
st.set_page_config(
    page_title="Wedding Invitation - Megha M & Lingaraj Kammar",
    page_icon="💐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Enhanced CSS with mobile-first approach and better responsiveness
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Playfair+Display:wght@400;700&family=Cormorant+Garamond:wght@300;400;600&display=swap');
    
    /* Reset and base styles */
    * {
        box-sizing: border-box;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
    
    /* Animated background - optimized for mobile */
    .stApp {
        background: linear-gradient(-45deg, #0a0e27, #1a1f3a, #1e3c72, #2a5298);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
        padding: 0.5rem 0;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes shimmer {
        0% { background-position: -1000px 0; }
        100% { background-position: 1000px 0; }
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.03); opacity: 0.9; }
    }
    
    @keyframes glow {
        0%, 100% { box-shadow: 0 0 15px rgba(74, 144, 226, 0.3), 0 0 30px rgba(74, 144, 226, 0.15); }
        50% { box-shadow: 0 0 25px rgba(74, 144, 226, 0.5), 0 0 50px rgba(74, 144, 226, 0.3); }
    }
    
    /* Container adjustments - mobile first */
    .block-container {
        padding: 1rem 0.75rem !important;
        max-width: 100% !important;
    }
    
    /* Header styling - fully responsive */
    .wedding-header {
        text-align: center;
        padding: 1.5rem 1rem;
        background: linear-gradient(135deg, rgba(30, 60, 114, 0.95) 0%, rgba(42, 82, 152, 0.95) 50%, rgba(30, 60, 114, 0.95) 100%);
        border-radius: 15px;
        margin: 0.5rem 0 1rem;
        box-shadow: 0 10px 30px rgba(42, 82, 152, 0.4);
        border: 2px solid rgba(74, 144, 226, 0.6);
        backdrop-filter: blur(10px);
        animation: fadeInUp 1s ease-out, glow 3s ease-in-out infinite;
        position: relative;
        overflow: hidden;
    }
    
    .wedding-header::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.1), transparent);
        animation: shimmer 3s infinite;
    }
    
    .couple-names {
        font-size: 2rem;
        font-weight: bold;
        color: #ffffff;
        font-family: 'Great Vibes', cursive;
        text-shadow: 2px 2px 8px rgba(74, 144, 226, 0.8), 0 0 20px rgba(255, 255, 255, 0.3);
        margin: 0.8rem 0;
        letter-spacing: 1px;
        animation: fadeInUp 1.5s ease-out 0.3s both;
        position: relative;
        z-index: 1;
        line-height: 1.3;
        word-wrap: break-word;
    }
    
    .wedding-tagline {
        font-size: 1rem;
        color: #e8f4f8;
        font-family: 'Cormorant Garamond', serif;
        font-style: italic;
        margin: 0.5rem 0;
        animation: fadeInUp 1.5s ease-out 0.6s both;
        position: relative;
        z-index: 1;
        padding: 0 0.5rem;
        line-height: 1.5;
    }
    
    .wedding-date {
        font-size: 1.2rem;
        color: #ffffff;
        font-weight: 600;
        font-family: 'Playfair Display', serif;
        margin-top: 0.5rem;
        animation: fadeInUp 1.5s ease-out 0.9s both;
        position: relative;
        z-index: 1;
    }
    
    /* Mandala animations - responsive */
    .mandala {
        font-size: 1.5rem;
        text-align: center;
        margin: 0.8rem 0;
        filter: drop-shadow(0 0 10px rgba(74, 144, 226, 0.5));
        animation: pulse 2s ease-in-out infinite;
        letter-spacing: 0.3rem;
    }
    
    .mandala-top {
        animation: fadeInUp 1s ease-out both;
    }
    
    .mandala-bottom {
        animation: fadeInUp 1s ease-out 1.2s both;
    }
    
    /* Event cards - mobile optimized */
    .event-card {
        background: linear-gradient(135deg, rgba(26, 31, 58, 0.95) 0%, rgba(42, 53, 85, 0.95) 100%);
        padding: 1.25rem;
        border-radius: 12px;
        box-shadow: 0 8px 20px rgba(74, 144, 226, 0.25);
        margin: 0.75rem 0;
        border: 2px solid rgba(74, 144, 226, 0.3);
        transition: all 0.3s ease;
        animation: fadeInUp 0.8s ease-out both;
        backdrop-filter: blur(10px);
        position: relative;
        overflow: hidden;
    }
    
    .event-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(74, 144, 226, 0.1), transparent);
        transition: left 0.5s ease;
    }
    
    .event-card:active::before {
        left: 100%;
    }
    
    .event-title {
        color: #4a90e2;
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 0.75rem;
        font-family: 'Playfair Display', serif;
        text-shadow: 2px 2px 6px rgba(74, 144, 226, 0.4);
        line-height: 1.3;
        word-wrap: break-word;
    }
    
    .event-detail {
        font-size: 1rem;
        margin: 0.5rem 0;
        color: #e8f4f8;
        font-family: 'Cormorant Garamond', serif;
        line-height: 1.6;
        word-wrap: break-word;
    }
    
    /* Divider */
    .divider {
        text-align: center;
        margin: 1.5rem 0;
        font-size: 1.5rem;
        color: #4a90e2;
        animation: pulse 2s ease-in-out infinite;
        filter: drop-shadow(0 0 8px rgba(74, 144, 226, 0.5));
    }
    
    /* Section headers */
    .section-header {
        text-align: center;
        color: #ffffff;
        font-size: 1.8rem;
        margin: 1.5rem 0 1rem 0;
        text-shadow: 2px 2px 8px rgba(74, 144, 226, 0.6);
        font-family: 'Playfair Display', serif;
        animation: fadeInUp 0.8s ease-out both;
        padding: 0 0.5rem;
        line-height: 1.3;
        word-wrap: break-word;
    }
    
    /* Countdown box */
    .countdown-box {
        text-align: center;
        margin-top: 1rem;
        background: linear-gradient(135deg, rgba(42, 82, 152, 0.95) 0%, rgba(30, 60, 114, 0.95) 100%);
        padding: 1.25rem 1rem;
        border-radius: 12px;
        color: white;
        font-size: 1.1rem;
        font-weight: bold;
        box-shadow: 0 8px 25px rgba(74, 144, 226, 0.4);
        border: 2px solid #4a90e2;
        animation: fadeInUp 1s ease-out 1.5s both, glow 2s ease-in-out infinite;
        font-family: 'Playfair Display', serif;
        backdrop-filter: blur(10px);
    }
    
    .countdown-number {
        font-size: 2.5rem;
        color: #ffd700;
        text-shadow: 0 0 15px rgba(255, 215, 0, 0.5);
        display: block;
        margin: 0.3rem 0;
    }
    
    /* Info box */
    .info-box {
        text-align: center;
        background: linear-gradient(135deg, rgba(26, 31, 58, 0.95) 0%, rgba(42, 53, 85, 0.95) 100%);
        padding: 1.5rem 1rem;
        border-radius: 12px;
        box-shadow: 0 8px 20px rgba(74, 144, 226, 0.3);
        border: 2px solid rgba(74, 144, 226, 0.3);
        color: #e8f4f8;
        font-size: 1rem;
        line-height: 1.7;
        animation: fadeInUp 1s ease-out both;
        font-family: 'Cormorant Garamond', serif;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
        margin: 0.5rem 0;
    }
    
    .quote-text {
        font-size: 1.2rem;
        font-style: italic;
        color: #ffffff;
        font-family: 'Great Vibes', cursive;
        margin: 0.5rem 0;
        text-shadow: 2px 2px 6px rgba(74, 144, 226, 0.4);
        line-height: 1.4;
    }
    
    /* Video container - FIXED for mobile */
    .video-container {
        margin: 1rem 0;
        padding: 1rem;
        background: linear-gradient(135deg, rgba(26, 31, 58, 0.95) 0%, rgba(42, 53, 85, 0.95) 100%);
        border-radius: 12px;
        box-shadow: 0 10px 30px rgba(74, 144, 226, 0.3);
        border: 2px solid rgba(74, 144, 226, 0.4);
        animation: fadeInUp 1s ease-out both;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }
    
    .video-wrapper {
        position: relative;
        padding-bottom: 56.25%; /* 16:9 aspect ratio */
        height: 0;
        overflow: hidden;
        border-radius: 10px;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.5);
        background: #000;
    }
    
    .video-wrapper iframe {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        border: none;
    }
    
    /* Map button - mobile optimized */
    .map-button {
        background: linear-gradient(135deg, #2a5298 0%, #1e3c72 100%);
        color: white;
        padding: 14px 20px;
        border: 2px solid #4a90e2;
        border-radius: 10px;
        cursor: pointer;
        font-size: 1rem;
        width: 100%;
        margin-top: 10px;
        transition: all 0.3s ease;
        font-family: 'Cormorant Garamond', serif;
        font-weight: 600;
        box-shadow: 0 4px 12px rgba(74, 144, 226, 0.3);
        text-decoration: none;
        display: inline-block;
        min-height: 48px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    .map-button:active {
        background: linear-gradient(135deg, #3a62a8 0%, #2e4c82 100%);
        transform: translateY(-2px);
        box-shadow: 0 6px 18px rgba(74, 144, 226, 0.5);
    }
    
    /* Contact section */
    .contact-item {
        font-size: 1rem;
        line-height: 1.8;
        margin: 0.5rem 0;
    }
    
    .contact-item p {
        margin: 0.5rem 0;
        word-wrap: break-word;
    }
    
    .closing-message {
        margin-top: 1rem;
        font-size: 1.3rem;
        font-family: 'Great Vibes', cursive;
        color: #ffd700;
        text-shadow: 2px 2px 6px rgba(255, 215, 0, 0.4);
    }
    
    /* Footer copyright */
    .copyright {
        text-align: center;
        color: rgba(232, 244, 248, 0.5);
        font-size: 0.75rem;
        margin-top: 2rem;
        padding: 1rem 0.5rem;
        font-family: 'Cormorant Garamond', serif;
    }
    
    /* Streamlit specific fixes */
    .element-container {
        width: 100% !important;
    }
    
    [data-testid="stHorizontalBlock"] {
        gap: 0.5rem !important;
    }
    
    /* Map container fixes */
    [data-testid="stDeckGlJsonChart"] {
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 4px 12px rgba(74, 144, 226, 0.3);
        margin: 0.75rem 0;
        min-height: 200px !important;
    }
    
    /* ===== TABLET STYLES (768px and up) ===== */
    @media (min-width: 768px) {
        .block-container {
            padding: 1.5rem 2rem !important;
        }
        
        .wedding-header {
            padding: 2rem 1.5rem;
            border-radius: 20px;
            margin: 1rem 0 2rem;
        }
        
        .couple-names {
            font-size: 3rem;
            letter-spacing: 2px;
        }
        
        .wedding-tagline {
            font-size: 1.15rem;
        }
        
        .wedding-date {
            font-size: 1.5rem;
        }
        
        .mandala {
            font-size: 2rem;
        }
        
        .event-card {
            padding: 1.75rem;
            border-radius: 15px;
            margin: 1rem 0;
        }
        
        .event-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 35px rgba(74, 144, 226, 0.5);
        }
        
        .event-card:hover::before {
            left: 100%;
        }
        
        .event-title {
            font-size: 1.8rem;
        }
        
        .event-detail {
            font-size: 1.1rem;
        }
        
        .section-header {
            font-size: 2.5rem;
            margin: 2rem 0 1.5rem 0;
        }
        
        .countdown-box {
            padding: 1.5rem;
            font-size: 1.4rem;
        }
        
        .countdown-number {
            font-size: 3rem;
        }
        
        .info-box {
            padding: 2rem 1.5rem;
            font-size: 1.1rem;
        }
        
        .info-box:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 30px rgba(74, 144, 226, 0.5);
        }
        
        .quote-text {
            font-size: 1.4rem;
        }
        
        .video-container {
            padding: 1.5rem;
            margin: 1.5rem 0;
        }
        
        .video-container:hover {
            box-shadow: 0 15px 40px rgba(74, 144, 226, 0.6);
            transform: translateY(-3px);
        }
        
        .map-button:hover {
            background: linear-gradient(135deg, #3a62a8 0%, #2e4c82 100%);
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(74, 144, 226, 0.5);
        }
        
        .contact-item {
            font-size: 1.1rem;
        }
        
        .closing-message {
            font-size: 1.6rem;
        }
        
        [data-testid="stDeckGlJsonChart"] {
            min-height: 250px !important;
        }
    }
    
    /* ===== DESKTOP STYLES (1024px and up) ===== */
    @media (min-width: 1024px) {
        .block-container {
            padding: 2rem 3rem !important;
        }
        
        .wedding-header {
            padding: 2.5rem 2rem;
            margin: 1.5rem 0 2.5rem;
        }
        
        .couple-names {
            font-size: 4rem;
        }
        
        .wedding-tagline {
            font-size: 1.25rem;
        }
        
        .wedding-date {
            font-size: 1.7rem;
        }
        
        .mandala {
            font-size: 2.5rem;
        }
        
        .event-card {
            padding: 2rem;
            border-radius: 18px;
            margin: 1.5rem 0;
        }
        
        .event-title {
            font-size: 2rem;
        }
        
        .event-detail {
            font-size: 1.15rem;
        }
        
        .section-header {
            font-size: 3rem;
            margin: 2.5rem 0 1.5rem 0;
        }
        
        .countdown-box {
            padding: 1.75rem;
            font-size: 1.6rem;
        }
        
        .countdown-number {
            font-size: 3.5rem;
        }
        
        .info-box {
            padding: 2.5rem 2rem;
            font-size: 1.15rem;
        }
        
        .quote-text {
            font-size: 1.45rem;
        }
        
        .video-container {
            padding: 2rem;
            margin: 2rem 0;
        }
        
        .contact-item {
            font-size: 1.15rem;
        }
        
        .closing-message {
            font-size: 1.7rem;
        }
        
        [data-testid="stDeckGlJsonChart"] {
            min-height: 300px !important;
        }
    }
    
    /* ===== LARGE DESKTOP STYLES (1400px and up) ===== */
    @media (min-width: 1400px) {
        .block-container {
            max-width: 1400px !important;
            margin: 0 auto;
            padding: 2rem 5rem !important;
        }
        
        .wedding-header {
            padding: 3rem 2.5rem;
        }
        
        .couple-names {
            font-size: 4.5rem;
        }
        
        .wedding-tagline {
            font-size: 1.3rem;
        }
        
        .wedding-date {
            font-size: 1.8rem;
        }
        
        .mandala {
            font-size: 3rem;
        }
        
        .event-card {
            padding: 2.5rem;
            border-radius: 20px;
            margin: 2rem 0;
        }
        
        .event-title {
            font-size: 2.3rem;
        }
        
        .event-detail {
            font-size: 1.2rem;
        }
        
        .section-header {
            font-size: 3.5rem;
            margin: 3rem 0 2rem 0;
        }
        
        .countdown-box {
            padding: 2rem;
            font-size: 1.8rem;
        }
        
        .info-box {
            padding: 3rem 2.5rem;
            font-size: 1.2rem;
        }
        
        .quote-text {
            font-size: 1.5rem;
        }
        
        .video-container {
            padding: 2rem;
        }
        
        .contact-item {
            font-size: 1.2rem;
        }
        
        .closing-message {
            font-size: 1.8rem;
        }
    }
    
    /* Extra small device optimizations */
    @media (max-width: 380px) {
        .couple-names {
            font-size: 1.75rem;
        }
        
        .wedding-tagline {
            font-size: 0.95rem;
        }
        
        .mandala {
            font-size: 1.3rem;
            letter-spacing: 0.2rem;
        }
        
        .event-title {
            font-size: 1.3rem;
        }
        
        .event-detail {
            font-size: 0.95rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("""
<div class="wedding-header">
    <div class="mandala mandala-top">🕉️ ✨ 🪔 ✨ 🕉️</div>
    <h2 class="wedding-tagline">You are cordially invited to celebrate the union of</h2>
    <div class="couple-names">Megha M & Lingaraj Kammar</div>
    <div class="wedding-date">📅 December 8, 2025</div>
    <div class="mandala mandala-bottom">🌸 💐 🌺 💐 🌸</div>
</div>
""", unsafe_allow_html=True)

# Save the Date Section
st.markdown('<div class="divider">❀ ✦ ❀</div>', unsafe_allow_html=True)

st.markdown("""
<div class="info-box">
    <h2 style="color: #4a90e2; margin-bottom: 1rem; font-family: 'Playfair Display', serif; font-size: 1.6rem;">✨ Save The Date ✨</h2>
    <p class="quote-text">
        Two souls, one heart, united in love
    </p>
    <p style="margin-top: 1rem; font-size: 1rem;">
        Join us as we celebrate the beginning of our forever journey together
    </p>
</div>
""", unsafe_allow_html=True)

# Enhanced Countdown
wedding_date = datetime(2025, 12, 8)
days_remaining = (wedding_date - datetime.now()).days

if days_remaining > 0:
    st.markdown(f"""
    <div class="countdown-box">
        <div>🎊 Counting down to our special day 🎊</div>
        <span class="countdown-number">{days_remaining}</span>
        <div style="font-size: 1rem;">days to go!</div>
    </div>
    """, unsafe_allow_html=True)
elif days_remaining == 0:
    st.markdown("""
    <div class="countdown-box">
        <div style="font-size: 2rem;">🎉 Today is the day! 🎉</div>
    </div>
    """, unsafe_allow_html=True)

# Wedding Video Section
st.markdown('<div class="divider">❀ ✦ ❀</div>', unsafe_allow_html=True)

st.markdown("<h2 class='section-header'>🎥 Our Invitation to You</h2>", unsafe_allow_html=True)

VIDEO_ID = "15xm0hwMfXphzThOsnZK7s6uXqXyu_mbh"

st.markdown(f"""
<div class="video-container">
    <div class="video-wrapper">
        <iframe src="https://drive.google.com/file/d/{VIDEO_ID}/preview" 
                allow="autoplay"
                loading="lazy">
        </iframe>
    </div>
    <p style='text-align: center; color: #e8f4f8; margin-top: 0.75rem; font-size: 0.95rem; font-style: italic;'>
        Click play to watch our special invitation ▶️
    </p>
</div>
""", unsafe_allow_html=True)

# Events Section
st.markdown('<div class="divider">❀ ✦ ❀</div>', unsafe_allow_html=True)
st.markdown("<h1 class='section-header'>Wedding Celebration Schedule</h1>", unsafe_allow_html=True)

events = [
    {
        "name": "Wedding Ceremony",
        "icon": "💒",
        "date": "December 7 & 8, 2025",
        "time": "December 8th • 6:15 - 7:15 AM (Muhuratha)",
        "venue": "Veerashaiva Samskrutika Bhavana, Devaraj Urs Layout, Shimoga",
        "delay": "0s"
    },
    {
        "name": "Grand Reception",
        "icon": "🎉",
        "date": "December 10, 2025",
        "time": "11:00 AM onwards",
        "venue": "Shri Veerabhadreshwara Kalyana Mantapa, Rattihalli",
        "delay": "0.2s"
    }
]

for event in events:
    st.markdown(f"""
    <div class="event-card" style="animation-delay: {event['delay']};">
        <div class="event-title">{event['icon']} {event['name']}</div>
        <div class="event-detail">📅 <strong>Date:</strong> {event['date']}</div>
        <div class="event-detail">🕐 <strong>Time:</strong> {event['time']}</div>
        <div class="event-detail">📍 <strong>Venue:</strong> {event['venue']}</div>
    </div>
    """, unsafe_allow_html=True)

# Venue & Map Section
st.markdown('<div class="divider">❀ ✦ ❀</div>', unsafe_allow_html=True)
st.markdown("<h1 class='section-header'>Venue Locations</h1>", unsafe_allow_html=True)

# Responsive column layout for venues
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("""
    <div class="event-card">
        <h3 style="color: #4a90e2; font-size: 1.6rem; margin-bottom: 0.75rem;">🏛️ Wedding Ceremony</h3>
        <p style="color: #ffffff; font-size: 1.15rem; font-weight: 600; margin-bottom: 0.5rem;">Veerashaiva Samskrutika Bhavana</p>
        <p style="color: #e8f4f8; font-size: 1rem; line-height: 1.6;">
            Devaraj Urs Layout<br>
            Shimoga, Karnataka 577204
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("**📍 Location on Map:**")
    st.map(data={"lat": [13.9605261], "lon": [75.5474847]}, zoom=12, use_container_width=True)
    
    venue1_lat = 13.9605261
    venue1_lon = 75.5474847
    st.markdown(f"""
    <a href="https://www.google.com/maps/search/?api=1&query={venue1_lat},{venue1_lon}" target="_blank" style="text-decoration: none;">
        <button class="map-button">
            📍 Open in Google Maps
        </button>
    </a>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="event-card">
        <h3 style="color: #4a90e2; font-size: 1.6rem; margin-bottom: 0.75rem;">🏛️ Reception</h3>
        <p style="color: #ffffff; font-size: 1.15rem; font-weight: 600; margin-bottom: 0.5rem;">Shri Veerabhadreshwara Kalyana Mantapa</p>
        <p style="color: #e8f4f8; font-size: 1rem; line-height: 1.6;">
            Rattihalli<br>
            Haveri(D), Karnataka 581116
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("**📍 Location on Map:**")
    st.map(data={"lat": [14.4219653], "lon": [75.5099661]}, zoom=12, use_container_width=True)
    
    venue2_lat = 14.4219653
    venue2_lon = 75.5099661
    st.markdown(f"""
    <a href="https://www.google.com/maps/search/?api=1&query={venue2_lat},{venue2_lon}" target="_blank" style="text-decoration: none;">
        <button class="map-button">
            📍 Open in Google Maps
        </button>
    </a>
    """, unsafe_allow_html=True)

# Footer Contact Section
st.markdown('<div class="divider">❀ ✦ ❀</div>', unsafe_allow_html=True)
st.markdown("""
<div class="info-box" style="margin-top: 1.5rem; padding: 2rem 1rem;">
    <h3 style="color: #4a90e2; font-size: 1.8rem; margin-bottom: 1rem; font-family: 'Playfair Display', serif;">
        📞 Contact Us
    </h3>
    <div class="contact-item">
        <p><strong style="color: #ffffff;">Bride's Family:</strong> +91 96324 82371 | Mohan Kumar</p>
        <p><strong style="color: #ffffff;">Groom's Family:</strong> +91 78925 41184 | Mahesh Kammar</p>
    </div>
    <div class="closing-message">
        💝 We can't wait to celebrate with you! 💝
    </div>
    <div style="margin-top: 1rem; font-size: 1rem; color: #e8f4f8;">
        Your presence will make our day even more special
    </div>
</div>
""", unsafe_allow_html=True)

# Copyright
st.markdown("""
<div class="copyright">
    Designed with ❤️ by puneeth
</div>
""", unsafe_allow_html=True)