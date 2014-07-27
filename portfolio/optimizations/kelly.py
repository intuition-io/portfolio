# -*- coding: utf-8 -*-
# vim:fenc=utf-8

'''
  :copyright (c) 2014 Xavier Bruhiere.
  :license: Apache 2.0, see LICENSE for more details.
'''

import numpy as np
import pandas as pd
import portfolio.utils
from portfolio.analytics import PortfolioAnalytics


class KellyPortfolio(PortfolioAnalytics):

    def __init__(self, **kwargs):
        # TODO Each parameters should be implemented as constraints
        # TODO And support other constaints like long_only
        self.leverage = kwargs.get('leverage', 1.0)
        self.short_pct = kwargs.get('short_pct', 0.7)
        self.port_size = kwargs.get('port_size', 25)

        super(KellyPortfolio, self).__init__()

    @portfolio.utils.preprocess
    def optimize(self, universe, prices):

        R = prices[universe].pct_change().dropna()
        # Remove bad data (non-variant)
        kelly = (R.mean() / R.var()).dropna()
        kelly.sort()
        picks = kelly.tail(self.port_size)
        # Assume a relationship between the securities and calculate the Kelly
        # leverages
        R = R[picks.index]
        C_inv = np.linalg.inv(R.cov())
        kelly = pd.Series(np.dot(C_inv, R.mean()), index=R.columns)

        # Limit short exposure if the Kelly score is negative
        # NOTE Kind of generic portfolio constraint
        kelly = kelly.apply(lambda x: max(x, self.short_pct * x))

        # Adjust result to keep the account leverage constant
        kelly *= (self.leverage / kelly.abs().sum())

        print('Done: {}'.format(kelly))
        return kelly.to_dict()
