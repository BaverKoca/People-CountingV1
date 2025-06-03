import streamlit as st
st.set_page_config(page_title="Professional People Counter", layout="wide")
import cv2
import torch
import yt_dlp
import tempfile
import os
import numpy as np

# Load YOLOv5 model (person detection)
@st.cache_resource
def load_model():
    return torch.hub.load('ultralytics/yolov5', 'yolov5x', pretrained=True)

model = load_model()

def count_people(frame):
    results = model(frame)
    people = [x for x in results.xyxy[0] if int(x[5]) == 0]
    return len(people), results

def process_video(video_path, stframe):
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        people_count, results = count_people(frame)
        annotated = np.squeeze(results.render())
        cv2.putText(annotated, f'People: {people_count}', (annotated.shape[1]-220, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,255,0), 3)
        stframe.image(annotated, channels="BGR", use_column_width=True)
    cap.release()

def process_youtube(url, stframe):
    # Use yt-dlp to get the direct video stream URL
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'format': 'best[ext=mp4]/best',
        'force_generic_extractor': False,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        stream_url = info.get('url', None)
        if not stream_url:
            st.error('Could not extract live stream URL.')
            return
    # OpenCV can open the direct stream URL
    cap = cv2.VideoCapture(stream_url)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        people_count, results = count_people(frame)
        annotated = np.squeeze(results.render())
        cv2.putText(annotated, f'People: {people_count}', (annotated.shape[1]-220, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,255,0), 3)
        stframe.image(annotated, channels="BGR", use_column_width=True)
    cap.release()

def main():
    st.title("👥 Professional People Counting with YOLOv5")
    st.markdown("""
    <style>
    .css-1d391kg {background-color: #f0f2f6;}
    .css-18e3th9 {padding-top: 2rem;}
    </style>
    """, unsafe_allow_html=True)
    
    choice = st.sidebar.radio("Choose input source:", ("Upload video", "YouTube live URL"))
    stframe = st.empty()
    if choice == "Upload video":
        uploaded = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov", "mkv"])
        if uploaded is not None:
            tfile = tempfile.NamedTemporaryFile(delete=False)
            tfile.write(uploaded.read())
            process_video(tfile.name, stframe)
            os.unlink(tfile.name)
    elif choice == "YouTube live URL":
        url = st.text_input("Enter YouTube live video URL")
        if url:
            st.info("Processing live video. Please wait...")
            process_youtube(url, stframe)

if __name__ == "__main__":
    main()
