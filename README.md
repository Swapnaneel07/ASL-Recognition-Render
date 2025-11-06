# ASL-Recognition-Render

A small project that detects American Sign Language (ASL) hand signs from images/video frames and renders the detected keypoints for visualization.

This repository contains a lightweight web interface and a backend script that work together to detect ASL hand signs and show the detected keypoints. If you just want to try a hosted inference API, see the Live API below.

## Live demo / Hosted API

You can use the hosted keypoint API here:

https://asl-keypoint-api.onrender.com

This endpoint accepts image frames (live video feed) and returns detected hand keypoints and a predicted ASL sign (where available).

## What this repo contains

- `app.py` — Backend script (Flask or similar) used to run the detection service locally.
- `index.html` — Simple web page UI to capture/upload images and display detected keypoints.
- `requirements.txt` — Python dependencies needed to run the project locally.
- `start.sh` — Optional startup script for Unix-like systems.

Note: The repository is intentionally small — it focuses on keypoint detection and rendering rather than a full production deployment.

## Features

- Detects hand keypoints for ASL hand signs
- Renders keypoints on top of images/video frames for easy visualization
- Simple web UI for local testing
- Optional local backend for running inference (see `app.py`)

## Quick start (local)

Prerequisites: Python 3.8+ and a virtual environment are recommended.

1. Create and activate a virtual environment:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the backend (if provided):

```powershell
python app.py
```

4. Open `index.html` in a browser to use the simple UI, or call the hosted API above.

## Using the hosted API

The hosted API at `https://asl-keypoint-api.onrender.com` accepts image frames and returns JSON containing detected hand keypoints and a predicted label where applicable. Refer to the API docs (if available) or inspect responses to learn the exact request/response formats.

## Developer notes and assumptions

- This README assumes the inference endpoint and local `app.py` expose similar behavior. If the project contains a different server framework, adjust run instructions accordingly.
- If you modify the model or dependencies, update `requirements.txt` to keep reproducible installs.

## Credits

Created by the repository owner. Uses standard computer-vision and keypoint detection approaches. If you used external models or libraries, please update this section with proper attribution.

## License

Specify a license here (e.g., MIT) or add a `LICENSE` file to the repository.

---

