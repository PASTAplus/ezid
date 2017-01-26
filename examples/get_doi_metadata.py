#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: get_doi_metadata

:Synopsis:
 
:Author:
    servilla

:Created:
    1/25/17
"""

import logging

logging.basicConfig(format='%(asctime)s %(levelname)s (%(name)s): %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S%z',
                    filename='get_doi_metadata' + '.log',
                    level=logging.INFO)

logger = logging.getLogger('get_doi_metadata')

from ezid import Ezid
import properties

def main():

    ezid = Ezid(user=properties.user, passwd=properties.passwd)
    metadata = ezid.get_metadata(id=properties.doi)
    print(metadata)

    return 0


if __name__ == "__main__":
    main()