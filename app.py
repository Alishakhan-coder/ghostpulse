import streamlit as st
from google import genai

# Page Styling & Configuration
st.set_page_config(
    page_title="GhostPulse - Viral Content Engine", 
    page_icon="⚡", 
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #FF4B4B;
        margin-bottom: 0.2rem;
    }
    .subtitle {
        font-size: 1.1rem;
        color: #555555;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Direct API Key Configuration
API_KEY = "AQ.Ab8RN6K2yUAKc8xl0rFbbN6jc7P4MivJWQdUEtUrXvH6YE5jLQ"
client = genai.Client(api_key=API_KEY)

# Sidebar Options
st.sidebar.markdown("## 🎯 AI & Tone Engine")
writing_tone = st.sidebar.selectbox(
    "Writing Tone select karein:", 
    ["Professional & Authority", "Casual & Engaging", "Bold & Controversial", "Storytelling & Emotional", "Humorous & Witty"]
)

st.sidebar.markdown("### 📌 Platforms Select Karein")
platforms = {
    "LinkedIn Post": st.sidebar.checkbox("LinkedIn Post", value=True),
    "Twitter Thread": st.sidebar.checkbox("Twitter Thread", value=True),
    "Instagram Caption": st.sidebar.checkbox("Instagram Caption", value=True),
    "YouTube Script / Hook": st.sidebar.checkbox("YouTube Script / Hook", value=True),
    "Email Newsletter": st.sidebar.checkbox("Email Newsletter", value=True)
}

# Main Body UI
st.markdown('<p class="main-title">⚡ Viral Content Engine & Repurposing Suite</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Apna raw idea ya article dalein aur aik click mein Viral Hooks, Multi-Platform Posts, aur Human-Like Content tayar karein!</p>', unsafe_allow_html=True)

user_prompt = st.text_area(
    "Yahan apna raw content, topic ya article likhein:", 
    placeholder="Misal ke tor par: AI tools will not replace humans, but humans using AI will replace humans..."
)

if st.button("🚀 Generate Viral Content Suite", type="primary"):
    if not user_prompt.strip():
        st.warning("⚠ Pehle kuch content ya topic toh likhein!")
    else:
        selected_platforms = [p for p, active in platforms.items() if active]
        
        if not selected_platforms:
            st.warning("⚠️ Kam az kam aik platform zaroor select karein!")
        else:
            with st.spinner("🔄 Generating high-impact viral content using AI..."):
                try:
                    full_prompt = (
                        f"Act as an expert viral content creator and copywriter. "
                        f"Tone: {writing_tone}. "
                        f"Based on the following input, generate high-engagement posts for these platforms: {', '.join(selected_platforms)}. "
                        f"\n\nInput Content: {user_prompt}"
                    )
                    
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=full_prompt,
                    )
                    
                    st.success("✨ Content Successfully Generated!")
                    st.markdown("### 📋 Generated Output:")
                    st.write(response.text)
                    
                except Exception as e:
                    st.error(f"❌ Error aa gaya hai: {str(e)}")
