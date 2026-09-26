import streamlit as st
from youtube_analyzer import build_youtube_agent


st.set_page_config(
    page_title="YouTube Video Analyzer",
    page_icon="🎥",
    layout="centered"
)


st.title("🎥 AI YouTube Video Analyzer")

st.write(
    "Enter a YouTube video link and get an AI-powered analysis."
)


@st.cache_resource
def get_agent():
    return build_youtube_agent()


agent = get_agent()


video_url = st.text_input(
    "Enter YouTube Video Link",
    placeholder="https://www.youtube.com/watch?v=..."
)


if st.button("Analyze Video"):

    if video_url:

        with st.spinner("Analyzing video..."):

            response = agent.run(
                f"Analyze this video: {video_url}"
            )

        st.markdown("### 📊 Video Analysis")
        st.markdown(response.content)

    else:
        st.warning("Please enter a YouTube video link.")