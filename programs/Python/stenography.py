# This script hide's text behind any media file like jpg file, mp3 file ecetera.

# This script accepts two parameter for hiding text and one parameter for finding text.

# Please install steganography python library by - pip install steganography

# This script is compatible with python 2.7


from __future__ import absolute_import,unicode_literals

import argparse

from steganography.steganography import Steganography

parser=argparse.ArgumentParser()

parser.add_argument("--carrier",help="Give path of carrier file which will contain our text.")

parser.add_argument("--stego_text",help="Enter text to hide.")

parser.add_argument("--stego_find",help="Give path of image which contains hidden text.")

args=parser.parse_args()


# Function for hide the message

def hideText(carrier_path,secret_text):

    path=carrier_path

    output_path="stego.png"

    text=secret_text

    Steganography.encode(path,output_path,text)


# Function for finding and detecting steganography

def findText(steg_img):

    secret_text=Steganography.decode(steg_img)

    print "Hidden text found :: "+secret_text


if args.carrier:

    carrier_path=args.carrier

    if args.stego_text:

        secret_text=args.stego_text

    hideText(carrier_path,secret_text)


if args.stego_find:

    steg_img=args.stego_find

    findText(steg_img)

