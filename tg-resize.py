# resize all jpg files in the current dir for telegram (1280px wide)
# resized files are prefixed with 'resized-' and excluded from subsequent resize

import pyvips
import os

format="jpg"
prefix="resized-"

def resize(file):
	image = pyvips.Image.thumbnail(file, 1280)
	image.sharpen(sigma=0.5, x1=2, y2=10, y3=20, m1=1.0, m2=3)
	image.write_to_file(prefix + file, keep="none")
	os.remove(file)

files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith("." + format) and not f.startswith(prefix)]
for f in files:
	resize(f)

