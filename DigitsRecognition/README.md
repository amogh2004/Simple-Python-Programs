# Digit Recognition
Handwritten Digit Recognition using OpenCV, sklearn and Python | [Video](https://www.youtube.com/watch?v=ur6JY2Hl-MM)

**Check out the blog post [here](http://hanzratech.in/python/handwritten-digit-recognition-using-opencv-sklearn-and-python/) for complete notes on how the code works.**

# Dependencies
1. `cv2`
2. `sklearn`
3. `skimage`
4. `numpy`
5. `collections`

# Contents
This repository contains the following files-

1. `generateClassifier.py` - Python Script to create the classifier file `digits_cls.pkl`.
2. `performRecognition.py` - Python Script to test the classifier.
3. `digits_cls.pkl` - Classifier file for digit recognition.
4. `photo_1.jpg` - Test image number 1 to test the classifier
5. `photo_2.jpg` - Test image numbre 2 to test the classifier


**NOTE** - *I have already created the `digits_cls.pkl`, so this step is not necessary.*
```python
python generateClassifier.py
```
* To test the classifier, run the `performRecognition.py` script.
```python
python performRecognition.py -c <path to classifier file> -i <path to test image>
```
ex -
```python
python performRecognition.py -c digits_cls.pkl -i photo_1.jpg
```

