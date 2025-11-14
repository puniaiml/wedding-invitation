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

# Enhanced CSS with beautiful animations
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Playfair+Display:wght@400;700&family=Cormorant+Garamond:wght@300;400;600&display=swap');
    
    /* Animated background */
    .stApp {
        background: linear-gradient(-45deg, #0a0e27, #1a1f3a, #1e3c72, #2a5298);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Floating particles */
    @keyframes float {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-20px) rotate(180deg); }
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
        50% { transform: scale(1.05); opacity: 0.8; }
    }
    
    @keyframes glow {
        0%, 100% { box-shadow: 0 0 20px rgba(74, 144, 226, 0.4), 0 0 40px rgba(74, 144, 226, 0.2); }
        50% { box-shadow: 0 0 30px rgba(74, 144, 226, 0.6), 0 0 60px rgba(74, 144, 226, 0.4); }
    }
    
    /* Header styling with animation */
    .wedding-header {
        text-align: center;
        padding: 4rem 2rem;
        background: linear-gradient(135deg, rgba(30, 60, 114, 0.95) 0%, rgba(42, 82, 152, 0.95) 50%, rgba(30, 60, 114, 0.95) 100%);
        border-radius: 25px;
        margin-bottom: 3rem;
        box-shadow: 0 15px 50px rgba(42, 82, 152, 0.5);
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
        font-size: 4.5rem;
        font-weight: bold;
        color: #ffffff;
        font-family: 'Great Vibes', cursive;
        text-shadow: 3px 3px 12px rgba(74, 144, 226, 0.8), 0 0 30px rgba(255, 255, 255, 0.3);
        margin: 1.5rem 0;
        letter-spacing: 3px;
        animation: fadeInUp 1.5s ease-out 0.3s both;
        position: relative;
        z-index: 1;
    }
    
    .wedding-tagline {
        font-size: 1.3rem;
        color: #e8f4f8;
        font-family: 'Cormorant Garamond', serif;
        font-style: italic;
        margin: 1rem 0;
        animation: fadeInUp 1.5s ease-out 0.6s both;
        position: relative;
        z-index: 1;
    }
    
    .wedding-date {
        font-size: 1.8rem;
        color: #ffffff;
        font-weight: 600;
        font-family: 'Playfair Display', serif;
        margin-top: 1rem;
        animation: fadeInUp 1.5s ease-out 0.9s both;
        position: relative;
        z-index: 1;
    }
    
    /* Mandala animations */
    .mandala {
        font-size: 3rem;
        text-align: center;
        margin: 1.5rem 0;
        filter: drop-shadow(0 0 15px rgba(74, 144, 226, 0.6));
        animation: pulse 2s ease-in-out infinite;
    }
    
    .mandala-top {
        animation: fadeInUp 1s ease-out both;
    }
    
    .mandala-bottom {
        animation: fadeInUp 1s ease-out 1.2s both;
    }
    
    /* Event cards with hover effects */
    .event-card {
        background: linear-gradient(135deg, rgba(26, 31, 58, 0.95) 0%, rgba(42, 53, 85, 0.95) 100%);
        padding: 2.5rem;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(74, 144, 226, 0.3);
        margin: 2rem 0;
        border-left: 5px solid #4a90e2;
        border: 2px solid rgba(74, 144, 226, 0.3);
        transition: all 0.4s ease;
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
    
    .event-card:hover::before {
        left: 100%;
    }
    
    .event-card:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 20px 50px rgba(74, 144, 226, 0.5);
        border-color: #4a90e2;
    }
    
    .event-title {
        color: #4a90e2;
        font-size: 2.3rem;
        font-weight: bold;
        margin-bottom: 1rem;
        font-family: 'Playfair Display', serif;
        text-shadow: 2px 2px 8px rgba(74, 144, 226, 0.4);
    }
    
    .event-detail {
        font-size: 1.2rem;
        margin: 0.8rem 0;
        color: #e8f4f8;
        font-family: 'Cormorant Garamond', serif;
        line-height: 1.6;
    }
    
    /* Divider with animation */
    .divider {
        text-align: center;
        margin: 3rem 0;
        font-size: 2.5rem;
        color: #4a90e2;
        animation: pulse 2s ease-in-out infinite;
        filter: drop-shadow(0 0 10px rgba(74, 144, 226, 0.5));
    }
    
    /* Section headers */
    .section-header {
        text-align: center;
        color: #ffffff;
        font-size: 3.5rem;
        margin: 3rem 0 2rem 0;
        text-shadow: 3px 3px 10px rgba(74, 144, 226, 0.6);
        font-family: 'Playfair Display', serif;
        animation: fadeInUp 0.8s ease-out both;
    }
    
    /* Countdown box with animation */
    .countdown-box {
        text-align: center;
        margin-top: 2rem;
        background: linear-gradient(135deg, rgba(42, 82, 152, 0.95) 0%, rgba(30, 60, 114, 0.95) 100%);
        padding: 2rem;
        border-radius: 20px;
        color: white;
        font-size: 1.8rem;
        font-weight: bold;
        box-shadow: 0 10px 35px rgba(74, 144, 226, 0.5);
        border: 2px solid #4a90e2;
        animation: fadeInUp 1s ease-out 1.5s both, glow 2s ease-in-out infinite;
        font-family: 'Playfair Display', serif;
        backdrop-filter: blur(10px);
    }
    
    .countdown-number {
        font-size: 3.5rem;
        color: #ffd700;
        text-shadow: 0 0 20px rgba(255, 215, 0, 0.5);
        display: block;
        margin: 0.5rem 0;
    }
    
    /* Info box */
    .info-box {
        text-align: center;
        background: linear-gradient(135deg, rgba(26, 31, 58, 0.95) 0%, rgba(42, 53, 85, 0.95) 100%);
        padding: 2.5rem;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(74, 144, 226, 0.4);
        border: 2px solid rgba(74, 144, 226, 0.3);
        color: #e8f4f8;
        font-size: 1.2rem;
        line-height: 1.8;
        animation: fadeInUp 1s ease-out both;
        font-family: 'Cormorant Garamond', serif;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }
    
    .info-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(74, 144, 226, 0.5);
    }
    
    .quote-text {
        font-size: 1.5rem;
        font-style: italic;
        color: #ffffff;
        font-family: 'Great Vibes', cursive;
        margin: 1rem 0;
        text-shadow: 2px 2px 8px rgba(74, 144, 226, 0.4);
    }
    
    /* Video container */
    .video-container {
        margin: 2rem 0;
        padding: 2rem;
        background: linear-gradient(135deg, rgba(26, 31, 58, 0.95) 0%, rgba(42, 53, 85, 0.95) 100%);
        border-radius: 20px;
        box-shadow: 0 15px 40px rgba(74, 144, 226, 0.4);
        border: 2px solid rgba(74, 144, 226, 0.4);
        animation: fadeInUp 1s ease-out both;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }
    
    .video-container:hover {
        box-shadow: 0 20px 50px rgba(74, 144, 226, 0.6);
        transform: translateY(-5px);
    }
    
    /* Map button styling */
    .map-button {
        background: linear-gradient(135deg, #2a5298 0%, #1e3c72 100%);
        color: white;
        padding: 15px 30px;
        border: 2px solid #4a90e2;
        border-radius: 12px;
        cursor: pointer;
        font-size: 1.1rem;
        width: 100%;
        margin-top: 15px;
        transition: all 0.3s ease;
        font-family: 'Cormorant Garamond', serif;
        font-weight: 600;
        box-shadow: 0 5px 15px rgba(74, 144, 226, 0.3);
    }
    
    .map-button:hover {
        background: linear-gradient(135deg, #3a62a8 0%, #2e4c82 100%);
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(74, 144, 226, 0.5);
    }
    
    /* Footer copyright */
    .copyright {
        text-align: center;
        color: rgba(232, 244, 248, 0.5);
        font-size: 0.75rem;
        margin-top: 3rem;
        padding: 1rem;
        font-family: 'Cormorant Garamond', serif;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .couple-names {
            font-size: 2.5rem;
        }
        .section-header {
            font-size: 2rem;
        }
        .event-title {
            font-size: 1.8rem;
        }
        .countdown-number {
            font-size: 2.5rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Header Section with enhanced design
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

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("""
    <div class="info-box">
        <h2 style="color: #4a90e2; margin-bottom: 1.5rem; font-family: 'Playfair Display', serif; font-size: 1.8rem;">✨ Save The Date ✨</h2>
        <p class="quote-text" font-size: 3.2rem>
            Two souls, one heart, united in love
        </p>
        <p style="margin-top: 1.5rem; font-size: 1.2rem;">
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
            <div style="font-size: 1.3rem;">days to go!</div>
        </div>
        """, unsafe_allow_html=True)
    elif days_remaining == 0:
        st.markdown("""
        <div class="countdown-box">
            <div style="font-size: 2.5rem;">🎉 Today is the day! 🎉</div>
        </div>
        """, unsafe_allow_html=True)

# Wedding Video Section
st.markdown('<div class="divider">❀ ✦ ❀</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([0.2, 4, 0.2])  # Maximum width
with col2:
    st.markdown("<h2 class='section-header' style='font-size: 2.5rem; margin: 1.5rem 0;'>🎥 Our Invitation to You</h2>", unsafe_allow_html=True)
    
    VIDEO_ID = "15xm0hwMfXphzThOsnZK7s6uXqXyu_mbh"
    
    st.markdown(f"""
    <div class="video-container">
        <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; border-radius: 15px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);">
            <iframe src="https://drive.google.com/file/d/{VIDEO_ID}/preview" 
                    width="100%" 
                    height="100%" 
                    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;"
                    allow="autoplay">
            </iframe>
        </div>
        <p style='text-align: center; color: #e8f4f8; margin-top: 1rem; font-size: 1rem; font-style: italic;'>
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

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="event-card">
        <h3 style="color: #4a90e2; font-size: 2rem; margin-bottom: 1rem;">🏛️ Wedding Ceremony</h3>
        <p style="color: #ffffff; font-size: 1.3rem; font-weight: 600; margin-bottom: 0.5rem;">Veerashaiva Samskrutika Bhavana</p>
        <p style="color: #e8f4f8; font-size: 1.1rem; line-height: 1.6;">
            Devaraj Urs Layout<br>
            Shimoga, Karnataka 577204
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("**📍 Location on Map:**")
    st.map(data={"lat": [13.9605261], "lon": [75.5474847]}, zoom=12)
    
    venue1_lat = 13.9605261
    venue1_lon = 75.5474847
    st.markdown(f"""
    <a href="https://www.google.com/maps/search/?api=1&query={venue1_lat},{venue1_lon}" target="_blank">
        <button class="map-button">
            📍 Open in Google Maps
        </button>
    </a>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="event-card">
        <h3 style="color: #4a90e2; font-size: 2rem; margin-bottom: 1rem;">🏛️ Reception</h3>
        <p style="color: #ffffff; font-size: 1.3rem; font-weight: 600; margin-bottom: 0.5rem;">Shri Veerabhadreshwara Kalyana Mantapa</p>
        <p style="color: #e8f4f8; font-size: 1.1rem; line-height: 1.6;">
            Rattihalli<br>
            Haveri(D), Karnataka 581116
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("**📍 Location on Map:**")
    st.map(data={"lat": [14.4219653], "lon": [75.5099661]}, zoom=12)
    
    venue2_lat = 14.4219653
    venue2_lon = 75.5099661
    st.markdown(f"""
    <a href="https://www.google.com/maps/search/?api=1&query={venue2_lat},{venue2_lon}" target="_blank">
        <button class="map-button">
            📍 Open in Google Maps
        </button>
    </a>
    """, unsafe_allow_html=True)

# Footer Contact Section
st.markdown('<div class="divider">❀ ✦ ❀</div>', unsafe_allow_html=True)
st.markdown("""
<div class="info-box" style="margin-top: 2rem; padding: 3rem;">
    <h3 style="color: #4a90e2; font-size: 2.2rem; margin-bottom: 1.5rem; font-family: 'Playfair Display', serif;">
        📞 Contact Us
    </h3>
    <div style="font-size: 1.2rem; line-height: 2;">
        <p><strong style="color: #ffffff;">Bride's Family:</strong> +91 96324 82371 | Mohan Kumar</p>
        <p><strong style="color: #ffffff;">Groom's Family:</strong> +91 78925 41184 | Mahesh Kammar</p>
    </div>
    <div style="margin-top: 2rem; font-size: 1.8rem; font-family: 'Great Vibes', cursive; color: #ffd700; text-shadow: 2px 2px 8px rgba(255, 215, 0, 0.4);">
        💝 We can't wait to celebrate with you! 💝
    </div>
    <div style="margin-top: 1.5rem; font-size: 1.1rem; color: #e8f4f8;">
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