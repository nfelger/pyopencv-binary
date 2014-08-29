from setuptools import setup

setup(
    name='pyopencv-binary',
    version='2.4.8',

    description='Binary distribution of OpenCV wrapper',

    data_files=[('lib/python2.7/site-packages', ['cv.py', 'cv2.so'])]
)
