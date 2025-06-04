# People-Counting

# Professional People Counting with YOLOv5x

This application uses the powerful YOLOv5x model to count people in videos or YouTube live streams. The detected people count is displayed in real-time at the top right of the video.

---

## Test Video
https://github.com/user-attachments/assets/edc59627-213e-4afa-92ec-41c138c49a72

---

## 🚀 Features
- **Upload Video:** Count people frame-by-frame in any uploaded video file.
- **YouTube Live URL:** Enter a YouTube live video URL and count people in the live stream.
- **Modern UI:** Clean, professional web interface built with Streamlit.
- **Accurate Detection:** Uses YOLOv5x for best-in-class accuracy, especially in crowded scenes.

---

## 🛠️ Requirements
- Python 3.8+
- [YOLOv5](https://github.com/ultralytics/yolov5) (model is loaded automatically)
- OpenCV
- Streamlit
- yt-dlp
- torch, torchvision
- numpy

---

## ⚡ Installation

Open PowerShell and run:

```
pip install streamlit opencv-python yt-dlp torch torchvision numpy
```

---

## ▶️ Usage

1. Clone this repository and navigate to the folder.
2. Run the app:

```
python -m streamlit run people_counter_app.py
```

3. Open the web interface in your browser (usually at http://localhost:8501).
4. Choose to upload a video or enter a YouTube live URL.
5. The app will display the video with the real-time people count at the top right.

---

## ℹ️ Notes
- For YouTube live, the app processes the stream directly (no download required).
- Processing speed depends on your hardware and video resolution.
- For best results in crowded scenes, the app uses the YOLOv5x model.

---

## ⚠️ Legal Warning:
-The legality of downloading content from YouTube and similar platforms depends on the license and intended use of the content. In particular, downloading copyrighted content without permission may be illegal.

---

## ℹ️ Disadvantage
-YOLOv5x.pt is not enough for crowded(more than 50-100 people). If you need more trustable and powerful than that then you can use People-CountingV2 which is using YOLOv8x.pt.
