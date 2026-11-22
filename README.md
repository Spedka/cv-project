# cv-project
 
A small group project for learning computer vision in Python with OpenCV. We build things one step at a time, starting with the basics of how an image is stored and working up from there. Everything here is a work in progress.
 
## Goals
 
- Understand how images are represented in memory (arrays, channels, color order) instead of just calling functions.
- Learn the core OpenCV operations by building small command-line tools.
- Keep each step small enough to explain, test and commit on its own.

## Setup
 
Python 3
 
Windows (PowerShell):
 
```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
 
Mac or Linux:
 
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
 
If PowerShell blocks the activate script, run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once and try again.

## Progress so far
 
- [x] Load an image from a command-line argument, with error handling for a missing or unreadable file
- [x] Convert color to grayscale and check the result by hand against OpenCV's weighted formula
- [x] Gaussian blur, and how kernel size and sigma each affect it
- [x] Canny edge detection and how the two thresholds change the result
- [ ] Adjustable thresholds with live sliders
