#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: make_one_doi_unavailable

:Synopsis:
 
:Author:
    servilla

:Created:
    1/25/17
"""

import logging

logging.basicConfig(format='%(asctime)s %(levelname)s (%(name)s): %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S%z',
                    filename='make_one_doi_unavailable' + '.log',
                    level=logging.INFO)

logger = logging.getLogger('make_one_doi_unavailable')

from ezid import Ezid
import properties


def main():

    ezid = Ezid(user=properties.user, passwd=properties.passwd)
    ezid.set_metadata(id=properties.doi, attribute='_status: unavailable | '
                                                   'invalid content')

    return 0


if __name__ == "__main__":
    main()