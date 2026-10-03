import os
import time
import streamlit as st
from google import genai

# === MULTI-KEY FREE POOL (2 Accounts) ===
API_KEYS = [
    "AQ.Ab8RN6JOVPcKkC5XdVQgp-HDIwXRLsB1Rb2qcxvLIrNtwBPK4A",  # Pehli key
    "AQ.Ab8RN6LRJMQ760bG-4mj24YV16DgDoAPY4mmtc5bUFV2Mcgs8w"                 # Doosri key yahan dalein
]

# Page Styling
st.set_page_config(page_title="Content Engine - Viral Creator Suite", page_icon="⚡", layout="wide")

st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ Viral Content Engine & Repurposing Suite")
st.markdown("Apna raw idea ya article dalein aur aik click mein **Viral Hooks, Multi-Platform Posts, aur Human-Like Content** tayar karein!")

# Sidebar Settings
st.sidebar.header("🎯 AI & Tone Engine")
tone = st.sidebar.selectbox(
    "Writing Tone select karein:",
    ["Professional & Authority", "Casual & Conversational", "Witty & Storyteller", "Bold & Controversial / Hook-heavy"]
)

st.sidebar.subheader("📌 Platforms Select Karein")
platforms = {
    "LinkedIn": st.sidebar.checkbox("LinkedIn Post", value=True),
    "Twitter": st.sidebar.checkbox("Twitter Thread", value=True),
    "Instagram": st.sidebar.checkbox("Instagram Caption", value=True),
    "YouTube": st.sidebar.checkbox("YouTube Script / Hook", value=True),
    "Newsletter": st.sidebar.checkbox("Email Newsletter", value=True)
}

# Main Input Section
user_topic = st.text_area("Yahan apna raw content, topic ya article likhein:", height=170, placeholder="Misal ke tor par: AI tools will not replace humans...")

if st.button("🚀 Generate Viral Content Suite", type="primary"):
    selected_platforms = [p for p, active in platforms.items() if active]
    
    if not user_topic.strip():
        st.warning("Barah-e-karam pehle kuch text ya topic enter karein!")
    elif not selected_platforms:
        st.warning("Kam az kam aik platform zaroor select karein!")
    else:
        with st.spinner("AI aap ka 100% human-like viral content tayar kar raha hai... Thoda intezar karein ✨"):
            selected_str = ", ".join(selected_platforms)
            
            prompt = f"""
            Aap aik top-tier human content creator aur master storyteller hain. Aap kabhi bhi robotic, formal, ya typical AI jaisi language use nahi karte. 
            Aap ki likhi hui zuban bilkul natural, conversational, engaging aur dil ko choo lene wali hoti hai, jese aik real human social media par likhta hai (short paragraphs, powerful hooks, relatable storytelling, aur zero corporate jargon).
            
            Neeche diye gaye topic/content ko in platforms ke liye adapt karein: {selected_str}.
            Writing Tone: {tone}
            
            Raw Content / Topic: {user_topic}
            
            Aap ko response is exact format mein dena hai:
            ---HOOKS---
            [Yahan 3 bohot hi zabardast, high-converting, aur human-sounding scroll-stopping hooks dein]
            
            ---CONTENT---
            Har selected platform ke liye alag heading ke sath mukammal content generate karein jo parhne mein bilkul asli human-written lage aur log usay foran like/share karein.
            """
            
            success = False
            response = None
            last_error = None
            
            # Fallback models list in case of 503 high demand
            models_to_try = ['gemini-3.8-flash', 'gemini-2.5-flash', 'gemini-2.0-flash']
            
            for key in API_KEYS:
                if success:
                    break
                for model_name in models_to_try:
                    try:
                        client = genai.Client(api_key=key)
                        response = client.models.generate_content(
                            model=model_name,
                            contents=prompt
                        )
                        success = True
                        break
                    except Exception as e:
                        last_error = e
                        time.sleep(1)
                        continue

            if success and response:
                st.success("🎉 Aap ka viral aur human-like content suite kamyaabi se tayar ho gaya hai!")
                st.markdown("---")
                
                full_text = response.text
                
                # Interactive Tabs for each section
                tab_list = ["🔥 Viral Hooks"] + [f"📌 {p}" for p in selected_platforms]
                tabs = st.tabs(tab_list)
                
                with tabs[0]:
                    st.subheader("🔥 Scroll-Stopping Viral Hooks")
                    st.markdown("Yeh rahi aapki post ke liye sab se behtareen human-touch wali opening lines:")
                    st.markdown(full_text)
                
                for idx, platform in enumerate(selected_platforms, start=1):
                    if idx < len(tabs):
                        with tabs[idx]:
                            st.subheader(f"✨ {platform} Content")
                            st.markdown(full_text)
                            
                st.markdown("---")
                st.subheader("📥 Pora Content View aur Copy Karein")
                st.text_area("Yahan se apnay poore content ko asani se copy kar sakte hain:", full_text, height=300)
                
            else:
                st.error(f"Server busy hone ki wajah se error aa gaya hai: {last_error}")
                st.info("💡 Tip: Yeh Google server par high traffic ki wajah se hai (503 error). Thodi der baad dobara button par click karein.")