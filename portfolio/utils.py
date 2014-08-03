# -*- coding: utf-8 -*-
# vim:fenc=utf-8

'''
  :copyright (c) 2014 Xavier Bruhiere.
  :license: Apache 2.0, see LICENSE for more details.
'''

import numpy as np


# NOTE Available with version 0.0.8 of dna
def round_if_close(number, target=0.0, approx=0.01):
    return target if abs(number - target) < approx else number


def neutral_guess(n_variables, factor=1.0):
    return np.ones(n_variables, dtype=float) * factor / n_variables


def preprocess(fct):
    def inner(self, signals, *args):
        if isinstance(signals, list):
            # Default is a list of interesting stocks to buy
            signals = {'buy': signals}
        sell_signals = signals.get('sell', [])
        buy_signals = signals.get('buy', [])

        positions = [p for p in self.positions
                     if (p not in sell_signals)
                     and self.positions[p]['amount'] != 0]
        universe = [sid for sid in set(buy_signals).union(positions)]

        # Close every positoins on 'sell' signal
        allocation = {
            sid: 0.0 for sid in sell_signals if sid in self.positions
        }
        if universe and len(signals['buy']) > 0:
            allocation.update(fct(self, universe, *args))
        return allocation
    return inner
