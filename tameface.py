#!/bin/python
import os
import sys
from PIL import Image
from PIL.ExifTags import TAGS

image = sys.argv[1]

for (tag,value) in Image.open(image)._getexif().iteritems():
        print '%s = %s' % (TAGS.get(tag), value)
