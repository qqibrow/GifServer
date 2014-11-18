GifServer
=========
A simple http file upload server which will convert the video passed in into gif and send it back.

Install
0. Platforms
Have tried it on RHEL6 and Max OSX 10.9.4. Should work on most of the Linux system. For Windows, feel happy to try!
1. Python
Make sure your python version is 2.7+. One of the dependencies "moviepy" will not work under 2.7. 
For detail, Please check the [issue link](https://github.com/Zulko/moviepy/issues/87).
2. pip
Please follow the [pip install instruction](http://pip.readthedocs.org/en/latest/installing.html).
3. [flask](http://flask.pocoo.org/)
Simple run pip install flask. (May need root permission).
4. moviepy
Please follow the install instruction [here](http://zulko.github.io/moviepy/install.html). 
**Please don't forget to install ffmpeg and ImageMagick according to the install moviepy instruction page!**
5. Pillow
Additional requirement from moviepy is Pillow, which will be used for the resize functionality. Simple run:
pip install pillow should be fine.




