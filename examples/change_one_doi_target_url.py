#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: change_one_doi_target_url

:Synopsis:
 
:Author:
    servilla

:Created:
    1/25/17
"""

import logging

logging.basicConfig(format='%(asctime)s %(levelname)s (%(name)s): %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S%z',
                    filename='change_one_doi_target_url' + '.log',
                    level=logging.INFO)

logger = logging.getLogger('change_one_doi_target_url')

from ezid import Ezid
import properties


def main():

    ezid = Ezid(user=properties.user, passwd=properties.passwd)
    target = '_target: https://new.target_url.org/object.html'
    ezid.set_metadata(id=properties.doi, attribute=target)

    return 0


if __name__ == "__main__":
    main()