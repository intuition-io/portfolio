# -*- coding: utf-8 -*-
# vim:fenc=utf-8

'''
  :copyright (c) 2014 Xavier Bruhiere.
  :license: Apache 2.0, see LICENSE for more details.
'''

import numpy as np


def risk(x, sids, data, penalty=0):
    ''' Use the covariance matrix from returns '''
    returns = np.diff(data[sids], axis=0)
    p = np.asarray(returns)
    Acov = np.cov(p.T)
    return np.dot(x, np.dot(Acov, x)) + penalty


def expected_return(x, sids, data, target=None):
    ''' Maximize expected returns '''
    returns = (data[sids].shift() / data[sids] - 1).mean().values
    if target:
        fitness = np.dot((target - returns), x)
    else:
        fitness = 1 / np.dot(returns, x)
    return fitness


def sharpe_ratio(x, sids, data, factor=252, rf=0.15):
    ''' Maximize Sharpe ration indicator '''
    returns = data[sids].shift() / data[sids] - 1
    data_ret = returns.mean().values
    data_std = returns.std().values
    sharpe = (data_ret * factor - rf) / (data_std * np.sqrt(factor))
    return 1 / np.dot(sharpe, x)


def fair(x, *args):
    ''' Reduce gap between weights '''
    return np.std(x)
