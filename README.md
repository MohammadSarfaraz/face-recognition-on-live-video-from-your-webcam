# face-recognition-on-live-video-from-your-webcam
face recognition on live video from your webcam using python module face recognition and  OpenCV

# OpenCV
* OpenCV is the most popular library for computer vision. Originally written in C/C++, it now provides bindings for Python.

# Face recognition with OpenCV, Python, and face_recognition model

* This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the other example, but it includes some basic performance tweaks to make things run a lot faster:
*   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
*   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
* OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.
1. Get a reference to webcam #0 (the default one)
2. Load a sample picture and learn how to recognize it.
3. Create arrays of known face encodings and their names
4. Grab a single frame of video
5. Resize frame of video to 1/4 size for faster face recognition processing
6. Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
7. Only process every other frame of video to save time
8. Find all the faces and face encodings in the current frame of video
9. Display the results
Here eg. given below It recognize my face and create squre with my name print on it otherwise unknown 
![](https://github.com/MohammadSarfaraz/face-recognition-on-live-video-from-your-webcam/blob/main/test.png)


