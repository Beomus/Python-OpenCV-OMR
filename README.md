# Optical Mark Reading with Python and OpenCV
Simple script to do some basic OMR
**Original**
![Original](https://imgur.com/7vfAng8.jpg)
**Graded**
![Graded](https://imgur.com/OaV2UtV.png)
## Installation 
`$ pip install opencv-python imutils`

## Known Issues
- This picture was taken from Google and the answer key was randomly generated, so in case you're wondering, this person _**DID NOT BUTCHER HIS/HER TEST ENTIRELY**_!
- Depending on the picture/image you use, you need to tweak `cv2.thesh()` thresh and max values in order to recognize the contours better.
- The script do not support **Bird's eye view transformation** but the `imutils` library has a tool for that please check that out. 

## TODO
- Add a system to automatically deny any question that has multiple answers
- Birds'eye view transformation (check _KNOWN ISSUE_)
