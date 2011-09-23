import os
import unittest

from PIL import Image
import numpy as np

from pycoast import ContourWriter

class Test(unittest.TestCase):

    def test_europe(self):
        euro_img = Image.open(os.path.join(os.path.dirname(__file__), 
                              'contours_europe.png'))
        euro_data = np.array(euro_img)

        img = Image.new('RGB', (640, 480))
        proj4_string = '+proj=stere +lon_0=8.00 +lat_0=50.00 +lat_ts=50.00 +ellps=WGS84'
        area_extent = (-3363403.31,-2291879.85,2630596.69,2203620.1)
        cw = ContourWriter('/home/esn/data/gshhs')
        cw.add_coastlines(img, proj4_string, area_extent, resolution='l', level=4)
        cw.add_rivers(img, proj4_string, area_extent, level=5, outline='blue')
        cw.add_borders(img, proj4_string, area_extent, outline=(255, 0, 0))
        res = np.array(img)
        self.failUnless(np.array_equal(euro_data, res), 'Writing of conturs failed')

