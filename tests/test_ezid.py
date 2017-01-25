#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: test_ezid

:Synopsis:

:Author:
    servilla
  
:Created:
    1/25/17
"""

import unittest
import logging

logging.basicConfig(format='%(asctime)s %(levelname)s (%(name)s): %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S%z', level=logging.WARN)

logger = logging.getLogger('test_ezid')


import properties
from ezid import Ezid

class TestEzid(unittest.TestCase):

    def setUp(self):
        self.ezid = Ezid(user=properties.user, passwd=properties.passwd)

    def tearDown(self):
        pass

    def test_get_metadata(self):
        metadata = self.ezid.get_metadata(id=properties.doi)
        print(metadata)
        self.assertIsNotNone(metadata)

if __name__ == '__main__':
    unittest.main()