# Optical Mark Reading with Python and OpenCV
Simple script to do some basic OMR
**Original**
![Original](https://imgur.com/7vfAng8.jpg)
**Graded**
<<<<<<< HEAD
![Graded](https://imgur.com/1PYSVWk.png)
=======
![Graded](https://imgur.com/OaV2UtV.png)
>>>>>>> c3d918de412526d1e14ea6ceb411e951d3292512
## Installation 
`$ pip install opencv-python imutils`

## Known Issues
- This picture was taken from Google and the answer key was randomly generated, so in case you're wondering, this person _**DID NOT BUTCHER HIS/HER TEST ENTIRELY**_!
<<<<<<< HEAD
- Depending on the picture/image you use, you need to tweak `cv2.theshold()` thresh and max values in order to recognize the contours better.
- Resizing the image might cause some problems when detecting for contours, but not super major problems, they can be fixed with `cv2.threshold()`
- The script do not support **Bird's eye view transformation** but the `imutils` library has a tool for that: `from imutils.perspective import four_point_transform` 
- Depending on the picture you use _(with/without Bird's eye view)_, there might be some problem sorting the contours, the package `imutils` has a method for that `from imutils import contours` but it was inaccurate since some are 1 pixel values apart which change the order of contours

=======
- Depending on the picture/image you use, you need to tweak `cv2.thesh()` thresh and max values in order to recognize the contours better.
- The script do not support **Bird's eye view transformation** but the `imutils` library has a tool for that please check that out. 
- Accuracy is not the best at the moment, there are some tweakings to be done.

## TODO
- Add a system to automatically deny any question that has multiple answers
- Birds'eye view transformation (check _KNOWN ISSUE_)
>>>>>>> c3d918de412526d1e14ea6ceb411e951d3292512
