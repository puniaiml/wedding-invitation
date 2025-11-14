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
    
    /* FIXED: Animated background - Rich wedding theme */
    .stApp {
        background: linear-gradient(-45deg, 
            #1a0a2e, #2d1b4e, #4a1942, #6b2c5c, #3d2463, #1f4068
        ) !important;
        background-size: 400% 400% !important;
        animation: gradientShift 20s ease infinite !important;
        padding: 0.5rem 0 !important;
        position: relative !important;
        overflow-x: hidden !important;
        min-height: 100vh !important;
    }
    
    /* Ensure content is visible */
    .main .block-container {
        background: transparent !important;
        position: relative !important;
        z-index: 10 !important;
    }
    
    /* Floating particles effect */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(2px 2px at 20% 30%, rgba(255, 215, 0, 0.3), transparent),
            radial-gradient(2px 2px at 60% 70%, rgba(255, 182, 193, 0.3), transparent),
            radial-gradient(1px 1px at 50% 50%, rgba(255, 255, 255, 0.4), transparent),
            radial-gradient(1px 1px at 80% 10%, rgba(255, 215, 0, 0.4), transparent),
            radial-gradient(2px 2px at 90% 60%, rgba(255, 192, 203, 0.3), transparent),
            radial-gradient(1px 1px at 33% 80%, rgba(255, 255, 255, 0.3), transparent);
        background-size: 200% 200%;
        animation: sparkle 15s ease-in-out infinite;
        pointer-events: none;
        z-index: 1;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        25% { background-position: 50% 75%; }
        50% { background-position: 100% 50%; }
        75% { background-position: 50% 25%; }
        100% { background-position: 0% 50%; }
    }
    
    @keyframes sparkle {
        0%, 100% { 
            opacity: 0.6;
            background-position: 0% 0%;
        }
        50% { 
            opacity: 1;
            background-position: 100% 100%;
        }
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(40px) scale(0.95);
        }
        to {
            opacity: 1;
            transform: translateY(0) scale(1);
        }
    }
    
    @keyframes shimmer {
        0% { 
            background-position: -1000px 0;
            opacity: 0;
        }
        50% {
            opacity: 0.8;
        }
        100% { 
            background-position: 1000px 0;
            opacity: 0;
        }
    }
    
    @keyframes pulse {
        0%, 100% { 
            transform: scale(1) rotate(0deg); 
            opacity: 1; 
        }
        25% {
            transform: scale(1.05) rotate(2deg);
        }
        50% { 
            transform: scale(1.08) rotate(0deg); 
            opacity: 0.9; 
        }
        75% {
            transform: scale(1.05) rotate(-2deg);
        }
    }
    
    @keyframes glow {
        0%, 100% { 
            box-shadow: 
                0 0 20px rgba(255, 215, 0, 0.3), 
                0 0 40px rgba(255, 182, 193, 0.2),
                0 0 60px rgba(186, 85, 211, 0.15),
                inset 0 0 20px rgba(255, 255, 255, 0.05);
        }
        50% { 
            box-shadow: 
                0 0 35px rgba(255, 215, 0, 0.5), 
                0 0 70px rgba(255, 182, 193, 0.35),
                0 0 100px rgba(186, 85, 211, 0.25),
                inset 0 0 30px rgba(255, 255, 255, 0.1);
        }
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        25% { transform: translateY(-10px) rotate(2deg); }
        50% { transform: translateY(-15px) rotate(0deg); }
        75% { transform: translateY(-10px) rotate(-2deg); }
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateX(-50px) rotate(-5deg);
        }
        to {
            opacity: 1;
            transform: translateX(0) rotate(0deg);
        }
    }
    
    @keyframes heartbeat {
        0%, 100% { transform: scale(1); }
        10% { transform: scale(1.1); }
        20% { transform: scale(1); }
        30% { transform: scale(1.15); }
        40% { transform: scale(1); }
    }
    
    /* Container adjustments - mobile first */
    .block-container {
        padding: 1rem 0.75rem !important;
        max-width: 100% !important;
        position: relative;
        z-index: 2;
    }
    
    /* Header styling - fully responsive */
    .wedding-header {
        text-align: center;
        padding: 1.5rem 1rem;
        background: linear-gradient(135deg, 
            rgba(106, 17, 203, 0.9) 0%, 
            rgba(186, 85, 211, 0.85) 25%,
            rgba(219, 112, 147, 0.9) 50%,
            rgba(186, 85, 211, 0.85) 75%,
            rgba(106, 17, 203, 0.9) 100%
        );
        border-radius: 15px;
        margin: 0.5rem 0 1rem;
        box-shadow: 
            0 15px 40px rgba(186, 85, 211, 0.4),
            0 5px 15px rgba(255, 215, 0, 0.2),
            inset 0 1px 3px rgba(255, 255, 255, 0.2);
        border: 3px solid rgba(255, 215, 0, 0.4);
        position: relative;
        overflow: hidden;
        animation: fadeInUp 1.2s ease-out, glow 4s ease-in-out infinite;
    }
    
    .wedding-header::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(
            45deg, 
            transparent, 
            rgba(255, 215, 0, 0.3), 
            rgba(255, 182, 193, 0.2),
            transparent
        );
        animation: shimmer 4s infinite;
    }
    
    .couple-names {
        font-size: 2rem;
        font-weight: bold;
        color: #ffd700;
        font-family: 'Great Vibes', cursive;
        text-shadow: 
            3px 3px 10px rgba(255, 215, 0, 0.6),
            0 0 30px rgba(255, 182, 193, 0.4),
            0 0 50px rgba(186, 85, 211, 0.3),
            2px 2px 4px rgba(0, 0, 0, 0.5);
        margin: 0.8rem 0;
        letter-spacing: 1px;
        animation: fadeInUp 1.5s ease-out 0.3s both, float 6s ease-in-out infinite;
        position: relative;
        z-index: 1;
        line-height: 1.3;
        word-wrap: break-word;
    }
    
    .wedding-tagline {
        font-size: 1rem;
        color: #ffb6c1;
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
        filter: drop-shadow(0 0 15px rgba(255, 215, 0, 0.6)) drop-shadow(0 0 25px rgba(255, 182, 193, 0.4));
        animation: pulse 3s ease-in-out infinite;
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
        background: linear-gradient(135deg, 
            rgba(75, 0, 130, 0.85) 0%, 
            rgba(106, 13, 173, 0.9) 50%,
            rgba(75, 0, 130, 0.85) 100%
        );
        padding: 1.25rem;
        border-radius: 12px;
        box-shadow: 
            0 10px 30px rgba(186, 85, 211, 0.3),
            0 5px 15px rgba(255, 105, 180, 0.2),
            inset 0 1px 2px rgba(255, 255, 255, 0.1);
        margin: 0.75rem 0;
        border: 2px solid rgba(255, 182, 193, 0.4);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        animation: fadeInUp 0.8s ease-out both, slideIn 0.6s ease-out both;
        backdrop-filter: blur(15px);
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
        background: linear-gradient(
            90deg, 
            transparent, 
            rgba(255, 215, 0, 0.15), 
            rgba(255, 182, 193, 0.15),
            transparent
        );
        transition: left 0.6s ease;
    }
    
    .event-card::after {
        content: '✨';
        position: absolute;
        top: 10px;
        right: 10px;
        font-size: 1.5rem;
        opacity: 0;
        transform: scale(0) rotate(0deg);
        transition: all 0.4s ease;
    }
    
    .event-card:active::before {
        left: 100%;
    }
    
    .event-card:active::after {
        opacity: 1;
        transform: scale(1) rotate(180deg);
    }
    
    .event-title {
        color: #ffd700;
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 0.75rem;
        font-family: 'Playfair Display', serif;
        text-shadow: 
            2px 2px 8px rgba(255, 215, 0, 0.5),
            0 0 20px rgba(255, 182, 193, 0.3);
        line-height: 1.3;
        word-wrap: break-word;
        animation: fadeInUp 1s ease-out both;
    }
    
    .event-detail {
        font-size: 1rem;
        margin: 0.5rem 0;
        color: #ffb6c1;
        font-family: 'Cormorant Garamond', serif;
        line-height: 1.6;
        word-wrap: break-word;
    }
    
    /* Divider */
    .divider {
        text-align: center;
        margin: 1.5rem 0;
        font-size: 1.5rem;
        color: #ffd700;
        animation: pulse 3s ease-in-out infinite;
        filter: drop-shadow(0 0 10px rgba(255, 215, 0, 0.5));
    }
    
    /* Section headers */
    .section-header {
        text-align: center;
        color: #ffd700;
        font-size: 1.8rem;
        margin: 1.5rem 0 1rem 0;
        text-shadow: 
            3px 3px 10px rgba(255, 215, 0, 0.6),
            0 0 30px rgba(255, 182, 193, 0.4),
            0 0 50px rgba(186, 85, 211, 0.3);
        font-family: 'Playfair Display', serif;
        animation: fadeInUp 0.8s ease-out both, float 5s ease-in-out infinite;
        padding: 0 0.5rem;
        line-height: 1.3;
        word-wrap: break-word;
        position: relative;
    }
    
    /* Countdown box */
    .countdown-box {
        text-align: center;
        margin-top: 1rem;
        background: linear-gradient(135deg, 
            rgba(139, 0, 139, 0.9) 0%, 
            rgba(186, 85, 211, 0.85) 50%,
            rgba(139, 0, 139, 0.9) 100%
        );
        padding: 1.25rem 1rem;
        border-radius: 12px;
        color: white;
        font-size: 1.1rem;
        font-weight: bold;
        box-shadow: 
            0 10px 35px rgba(186, 85, 211, 0.5),
            0 5px 15px rgba(255, 215, 0, 0.3),
            inset 0 1px 3px rgba(255, 255, 255, 0.2);
        border: 3px solid rgba(255, 215, 0, 0.4);
        position: relative;
        animation: fadeInUp 1s ease-out 1.5s both, glow 3s ease-in-out infinite, heartbeat 2s ease-in-out infinite;
        font-family: 'Playfair Display', serif;
        backdrop-filter: blur(10px);
        overflow: hidden;
    }
    
    .countdown-number {
        font-size: 2.5rem;
        color: #ffd700;
        text-shadow: 
            0 0 20px rgba(255, 215, 0, 0.8),
            0 0 40px rgba(255, 182, 193, 0.5),
            3px 3px 10px rgba(0, 0, 0, 0.5);
        display: block;
        margin: 0.3rem 0;
        animation: pulse 2s ease-in-out infinite;
        font-weight: 900;
    }
    
    /* Info box */
    .info-box {
        text-align: center;
        background: linear-gradient(135deg, 
            rgba(75, 0, 130, 0.85) 0%, 
            rgba(106, 13, 173, 0.9) 50%,
            rgba(75, 0, 130, 0.85) 100%
        );
        padding: 1.5rem 1rem;
        border-radius: 12px;
        box-shadow: 
            0 10px 30px rgba(186, 85, 211, 0.4),
            0 5px 15px rgba(255, 105, 180, 0.2),
            inset 0 1px 2px rgba(255, 255, 255, 0.1);
        border: 2px solid rgba(255, 182, 193, 0.4);
        color: #ffb6c1;
        font-size: 1rem;
        line-height: 1.7;
        animation: fadeInUp 1s ease-out both;
        font-family: 'Cormorant Garamond', serif;
        backdrop-filter: blur(15px);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        margin: 0.5rem 0;
        position: relative;
        overflow: hidden;
    }
    
    .info-box::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(
            45deg,
            transparent,
            rgba(255, 215, 0, 0.1),
            rgba(255, 182, 193, 0.1),
            transparent
        );
        animation: shimmer 5s infinite;
    }
    
    .quote-text {
        font-size: 1.2rem;
        font-style: italic;
        color: #ffd700;
        font-family: 'Great Vibes', cursive;
        margin: 0.5rem 0;
        text-shadow: 
            2px 2px 8px rgba(255, 215, 0, 0.6),
            0 0 20px rgba(255, 182, 193, 0.4);
        line-height: 1.4;
        animation: float 4s ease-in-out infinite;
    }
    
    /* Video container */
    .video-container {
        margin: 1rem 0;
        padding: 1rem;
        background: linear-gradient(135deg, 
            rgba(75, 0, 130, 0.85) 0%, 
            rgba(106, 13, 173, 0.9) 50%,
            rgba(75, 0, 130, 0.85) 100%
        );
        border-radius: 12px;
        box-shadow: 
            0 15px 40px rgba(186, 85, 211, 0.4),
            0 5px 15px rgba(255, 105, 180, 0.2),
            inset 0 1px 2px rgba(255, 255, 255, 0.1);
        border: 2px solid rgba(255, 182, 193, 0.4);
        animation: fadeInUp 1s ease-out both;
        backdrop-filter: blur(15px);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
        overflow: hidden;
    }
    
    .video-container::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(
            45deg,
            transparent,
            rgba(255, 215, 0, 0.1),
            transparent
        );
        animation: shimmer 6s infinite;
    }
    
    .video-wrapper {
        position: relative;
        padding-bottom: 56.25%;
        height: 0;
        overflow: hidden;
        border-radius: 10px;
        box-shadow: 
            0 10px 30px rgba(0, 0, 0, 0.6),
            0 0 20px rgba(255, 215, 0, 0.2);
        background: #000;
        border: 2px solid rgba(255, 215, 0, 0.3);
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
        background: linear-gradient(135deg, 
            #8b008b 0%, 
            #ba55d3 50%, 
            #8b008b 100%
        );
        color: white;
        padding: 14px 20px;
        border: 2px solid #ffd700;
        border-radius: 10px;
        cursor: pointer;
        font-size: 1rem;
        width: 100%;
        margin-top: 10px;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        font-family: 'Cormorant Garamond', serif;
        font-weight: 600;
        box-shadow: 
            0 6px 18px rgba(186, 85, 211, 0.4),
            0 2px 8px rgba(255, 215, 0, 0.2);
        text-decoration: none;
        display: flex;
        align-items: center;
        justify-content: center;
        min-height: 48px;
        position: relative;
        overflow: hidden;
    }
    
    .map-button::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        border-radius: 50%;
        background: rgba(255, 215, 0, 0.3);
        transform: translate(-50%, -50%);
        transition: width 0.6s, height 0.6s;
    }
    
    .map-button:active::before {
        width: 300px;
        height: 300px;
    }
    
    .map-button:active {
        background: linear-gradient(135deg, 
            #9b109b 0%, 
            #ca65e3 50%, 
            #9b109b 100%
        );
        transform: translateY(-2px) scale(0.98);
        box-shadow: 
            0 10px 25px rgba(186, 85, 211, 0.6),
            0 4px 12px rgba(255, 215, 0, 0.4);
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
        text-shadow: 
            2px 2px 8px rgba(255, 215, 0, 0.6),
            0 0 20px rgba(255, 182, 193, 0.4);
        animation: heartbeat 3s ease-in-out infinite;
    }
    
    /* Footer copyright */
    .copyright {
        text-align: center;
        color: rgba(255, 182, 193, 0.5);
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
    
    /* TABLET STYLES (768px and up) */
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
        
        .event-card:hover {
            transform: translateY(-5px) scale(1.02);
            box-shadow: 
                0 20px 45px rgba(186, 85, 211, 0.6),
                0 10px 25px rgba(255, 105, 180, 0.4);
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
    <h2 style="color: #ffd700; margin-bottom: 1rem; font-family: 'Playfair Display', serif; font-size: 1.6rem;">✨ Save The Date ✨</h2>
    <p class="quote-text">
        Two souls, one heart, united in love
    </p>
    <p style="margin-top: 1rem; font-size: 1rem; color: #ffb6c1;">
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
    <p style='text-align: center; color: #ffb6c1; margin-top: 0.75rem; font-size: 0.95rem; font-style: italic;'>
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
        <h3 style="color: #ffd700; font-size: 1.6rem; margin-bottom: 0.75rem;">🏛️ Wedding Ceremony</h3>
        <p style="color: #ffffff; font-size: 1.15rem; font-weight: 600; margin-bottom: 0.5rem;">Veerashaiva Samskrutika Bhavana</p>
        <p style="color: #ffb6c1; font-size: 1rem; line-height: 1.6;">
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
        <h3 style="color: #ffd700; font-size: 1.6rem; margin-bottom: 0.75rem;">🏛️ Reception</h3>
        <p style="color: #ffffff; font-size: 1.15rem; font-weight: 600; margin-bottom: 0.5rem;">Shri Veerabhadreshwara Kalyana Mantapa</p>
        <p style="color: #ffb6c1; font-size: 1rem; line-height: 1.6;">
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
    <h3 style="color: #ffd700; font-size: 1.8rem; margin-bottom: 1rem; font-family: 'Playfair Display', serif;">
        📞 Contact Us
    </h3>
    <div class="contact-item">
        <p><strong style="color: #ffffff;">Bride's Family:</strong> +91 96324 82371 | Mohan Kumar</p>
        <p><strong style="color: #ffffff;">Groom's Family:</strong> +91 78925 41184 | Mahesh Kammar</p>
    </div>
    <div class="closing-message">
        💝 We can't wait to celebrate with you! 💝
    </div>
    <div style="margin-top: 1rem; font-size: 1rem; color: #ffb6c1;">
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