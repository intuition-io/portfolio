# -*- coding: utf-8 -*-
# vim:fenc=utf-8

'''
  :copyright (c) 2014 Xavier Bruhiere.
  :license: Apache 2.0, see LICENSE for more details.
'''

import abc
import portfolio.zipline

NO_BOUND = None


class PortfolioAnalytics(portfolio.zipline.FactoryPortfolio):
    '''
    Zipline compatible extension of Portfolio, with analytics superpowers
    '''

    __metaclass__ = abc.ABCMeta

    def __init__(self):
        super(PortfolioAnalytics, self).__init__()
        self._constraints = []
        self._min_bound, self._max_bound = NO_BOUND, NO_BOUND

    def add_constraint(self, constraint):
        # TODO Check constraint structure (with schema ?)
        if constraint['type'] == 'box':
            self._min_bound = constraint['min']
            self._max_bound = constraint['max']
        else:
            self._constraints.append(constraint)

    def _box_constraint(self, i):
        ''' Lower and upper bound current state '''
        return [[self._min_bound, self._max_bound] for _ in range(i)]

    @abc.abstractmethod
    def optimize(self, signals, *args):
        pass
