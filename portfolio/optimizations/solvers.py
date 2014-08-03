# -*- coding: utf-8 -*-
# vim:fenc=utf-8

'''
  :copyright (c) 2014 Xavier Bruhiere.
  :license: Apache 2.0, see LICENSE for more details.
'''

from scipy import optimize
import portfolio.utils
from portfolio.analytics import PortfolioAnalytics


class SolverPortfolio(PortfolioAnalytics):

    def __init__(self, objective_func, solver='SLSQP'):
        self._objective = objective_func
        self._solver = solver
        self._optimizer = optimize.minimize

        super(SolverPortfolio, self).__init__()

    # TODO Make the solver pluggable
    # TODO If no universe provided, try to use *args quotes ?
    @portfolio.utils.preprocess
    def optimize(self, universe, *args):
        L = len(universe)
        kwargs = {
            'fun': self._objective,
            # NOTE What is the influence of this vector ?
            'x0': portfolio.utils.neutral_guess(L),
            'args': tuple([universe] + list(args)),
            'method': self._solver,
            'constraints': self._constraints,
            'bounds': self._box_constraint(L),
            'options': {'disp': False, 'maxiter': 30}
        }
        result = self._optimizer(**kwargs)
        print('Done: {} ({} iterations)'.format(
            result.message, result.nit))

        if result.success:
            allocation = {
                sid: portfolio.utils.round_if_close(result.x[i])
                for i, sid in enumerate(universe)
            }

        return allocation if result.success else {}
