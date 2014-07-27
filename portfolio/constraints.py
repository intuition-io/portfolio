# -*- coding: utf-8 -*-
# vim:fenc=utf-8

'''
  Constraints functions
  ---------------------

  :copyright (c) 2014 Xavier Bruhiere.
  :license: %LICENCE%, see LICENSE for more details.
'''

import numpy as np


def box_constraint(min_bound, max_bound):
    return {'type': 'box', 'min': min_bound, 'max': max_bound}


def long_only(max_bound=None):
    ''' Limit sid allocation to positive values '''
    return box_constraint(0, max_bound)


def limited_investment(limit):
    ''' Sum of optimized weights must be 100 % '''
    return {'type': 'eq', 'fun': lambda x: np.sum(x) - limit}


def full_investment():
    ''' Sum of optimized weights must be 100 % '''
    return limited_investment(limit=1.0)
