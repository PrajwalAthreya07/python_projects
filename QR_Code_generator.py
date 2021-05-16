#QR Code generator using pyqrcode package in python
#importing the package called as pyqrcode

import pyqrcode as df

#adding the URL link for which a QR Code needs to be generated
abc = df.create("https://www.youtube.com/")

#creating a folder using svg command
abc.svg("url.svg")

