# -*- coding: utf-8 -*-
# vim:fenc=utf-8

'''
  :copyright (c) 2014 Xavier Bruhiere.
  :license: Apache 2.0, see LICENSE for more details.
'''

import numpy as np
import portfolio.utils
from portfolio.analytics import PortfolioAnalytics


# https://www.quantopian.com/posts/global-minimum-variance-portfolio?c=1
class GlobalMinimumVariance(PortfolioAnalytics):

    @portfolio.utils.preprocess
    def optimize(self, universe, prices):
        allocation = {}
        try:
            returns = (prices.shift() / prices - 1).fillna(method='bfill')
            returns = returns[universe].transpose()
            L = len(returns)
            # create a covariance matrix
            covariance_matrix = np.cov(returns, y=None, rowvar=1,
                                       bias=0, ddof=None)
            covariance_matrix = np.matrix(covariance_matrix)

            # calculate global minimum portfolio weights
            # NOTE This must be x
            one_vector = np.matrix(np.ones(L)).transpose()
            # NOTE Or this one ?
            one_row = np.matrix(np.ones(L))
            covariance_matrix_inv = np.linalg.inv(covariance_matrix)
            numerator = np.dot(covariance_matrix_inv, one_vector)
            denominator = np.dot(np.dot(one_row, covariance_matrix_inv),
                                 one_vector)

            weights = numerator / denominator
        except Exception, error:
            print(error)
            weights = [np.nan] * L

        if np.isnan(weights).any() or not weights.any():
            print('Could not compute weigths')
        else:
            for i, sid in enumerate(prices[universe]):
                allocation[sid] = float(weights[i])

        return allocation
