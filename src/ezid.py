#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: ezid

:Synopsis:
    Operate on Datacite/EZID metadata for a DOI

:Author:
    servilla

:Created:
    1/25/17
"""


import logging

logging.basicConfig(format='%(asctime)s %(levelname)s (%(name)s): %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S%z', filename='ezid.log',
                    level=logging.INFO)

logger = logging.getLogger('ezid')

import requests
from requests.auth import HTTPBasicAuth

class Ezid(object):

    headers = {'Content-type': 'text/plain; charset=UTF-8'}
    base_url = 'https://ezid.cdlib.org/id/'

    def __init__(self, user=None, passwd=None):
        self.user = user
        self.passwd = passwd
        self.auth = (self.user, self.passwd)

    def set_headers(self, headers=None):
        Ezid.headers = headers

    def add_header(self, key=None, value=None):
        Ezid.headers[key] = value

    def get_headers(self):
        return Ezid.headers

    def set_base_url(self, base_url=None):
        Ezid.base_url = base_url

    def get_base_url(self):
        return Ezid.base_url

    def get_metadata(self, id=None):
        url = Ezid.base_url + id
        metadata = None
        try:
            r = requests.get(url=url, auth=self.auth, headers=Ezid.headers)
            metadata = r.text
            logger.info(r.status_code)
        except Exception as e:
            logger.error(e)

        return metadata

    def set_metadata(self, id=None, attribute=None):
        url = Ezid.base_url + id
        try:
            r = requests.post(url=url, auth=self.auth, headers=Ezid.headers,
                              data=attribute)
            logger.info(r.status_code)
            logger.info(r.text)
        except Exception as e:
            logger.error(e)


def main():


    return 0


if __name__ == "__main__":
    main()