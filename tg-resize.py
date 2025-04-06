# resize & sharpen all jpg files in the target dir for Telegram (2560px wide)
# resized files are prefixed with 'resized-' and excluded from subsequent resize
# original files are deleted

import pyvips
import os
import sys

format="jpg"
prefix="resized-"
max_size=2560

dir = sys.argv[1] if len(sys.argv) > 1 else '.'

def resize(path, filename):
	file = os.path.join(path, filename)
	print("resizing " + file)
	image = pyvips.Image.thumbnail(file, max_size)
	image = image.sharpen(sigma=0.5, x1=2, y2=5, y3=20, m1=0.5, m2=1)
	image.write_to_file(os.path.join(path, prefix + filename), keep="none")
	os.remove(file)

for dirpath, dirnames, filenames in os.walk(dir):
   for filename in filenames:
      if filename.endswith("." + format) and not filename.startswith(prefix):
         resize(dirpath, filename)
