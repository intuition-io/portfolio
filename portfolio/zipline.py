# -*- coding: utf-8 -*-
# vim:fenc=utf-8
'''
  :copyright (c) 2014 Quantopian, Inc.
  :license: Apache 2.0, see LICENSE for more details.
'''


class Position(object):
    def __init__(self, sid):
        self.sid = sid
        self.amount = 0
        self.cost_basis = 0.0  # per share
        self.last_sale_price = 0.0

    def __getitem__(self, key):
        return self.__dict__[key]

    def __repr__(self):
        return "Position({0})".format(self.__dict__)


class Positions(dict):
    def __missing__(self, key):
        pos = Position(key)
        self[key] = pos
        return pos


class FactoryPortfolio(object):
    def __init__(self):
        self.capital_used = 0.0
        self.starting_cash = 0.0
        self.portfolio_value = 0.0
        self.pnl = 0.0
        self.returns = 0.0
        self.cash = 0.0
        self.positions = Positions()
        self.start_date = None
        self.positions_value = 0.0

    def __getitem__(self, key):
        return self.__dict__[key]

    def __repr__(self):
        return "Portfolio({0})".format(self.__dict__)
