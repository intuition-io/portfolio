#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

'''
  Portfolio Analytics
  ------------------

  :copyright (c) 2014 Xavier Bruhiere.
  :license: Apache 2.0, see LICENSE for more details.
'''

import zipline.protocol


class PortfolioAnalytics(zipline.protocol.Portfolio):
    '''
    Zipline compatible extension of Portfolio, with analytics superpowers
    '''
    def __init__(self):
        super(zipline.protocol.Portfolio, self).__init__()
