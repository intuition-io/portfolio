Portfolio Analytics
===================

[![Build Status](https://api.shippable.com/projects/53ce99a67c72335f045a19bb/badge/master)](https://www.shippable.com/projects/53ce99a67c72335f045a19bb)
[![Coverage Status](https://img.shields.io/coveralls/intuition-io/portfolio.svg)](https://coveralls.io/r/intuition-io/portfolio)
[![Code Health](https://landscape.io/github/intuition-io/portfolio/master/landscape.png)](https://landscape.io/github/intuition-io/portfolio/master)
[![Requirements Status](https://requires.io/github/intuition-io/portfolio/requirements.png?branch=master)](https://requires.io/github/intuition-io/portfolio/requirements/?branch=master)
[![License](https://pypip.in/license/intuition/badge.png)](https://pypi.python.org/pypi/intuition/)
[![Gitter chat](https://badges.gitter.im/intuition-io.png)](https://gitter.im/intuition-io)

> [Zipline][1] compatible extension of Portfolio, with analytics superpowers.
> Inspired by [PortfolioAnalytics][6] R package.

The project provides several portfolio optimizations that compute optimal
assets allocation regarding a various set of factors and constraints. Currently
you will get the following implementations :

* [General optimization problem with solvers][7]
* [Global Minimum Variance][8]
* [Kelly criterion][9]

To learn more about the API, check [the full documentation][3].

This project is currently part of the **intuition project**, signup for [the
private beta][2] and/or [clone your own hedge fund][4].

Finally, the whole thing is compatible with [zipline backtester][1].


Install
-------

```
$ sudo apt-get install libopenblas-dev liblapack-dev gfortran
$ pip install portfolio-analytics

... blablabla it compiles a lot of maths, grab a coffee ...
```

Or play with it right away with [docker][11]:

```
$ docker run -i -t hivetech/portfolio bash
```

A taste of it
-------------

```python
# Download some historical data
from pandas.io.data import get_data_google
ohlc_data = get_data_google(['adsk', 'ctxs', 'fb', 'nflx', 'qcom'], start='2013/01/01', end='2013/12/01')
data = ohlc_data['Close']

# Now let's optimize our portfolio weights
from portfolio.optimizations.solvers import SolverPortfolio
import portfolio.objectives as objective
import portfolio.constraints as constraint

portfolio = SolverPortfolio(objective.risk)
# Forbid short positions
portfolio.add_constraint(constraint.long_only())
# Invest every cent of our cash
portfolio.add_constraint(constraint.full_investment())

# Get optimal weights in %
pf.optimize(['ctxs', 'fb', 'nflx', 'qcom', 'adsk'], data)
Out[66]:
{'adsk': 0.49,
 'ctxs': 0.04,
 'fb': 0.17,
 'nflx': 0.0,
 'qcom': 0.29}
```

Contributing
------------

Contributors are happily welcome, [here is a place to start][10].


License
-------

Copyright 2014 Xavier Bruhiere.

*Portfolio* is available under the [Apache License, Version 2.0][5].


[1]: https://github.com/quantopian/zipline
[2]: http://intuition.io
[3]: http://doc.intuition.io
[4]: https://github.com/intuition-io/intuition
[5]: http://www.apache.org/licenses/LICENSE-2.0.html
[6]: https://r-forge.r-project.org/R/?group_id=579
[7]: http://docs.scipy.org/doc/scipy/reference/optimize.html
[8]: http://www.investopedia.com/terms/p/portfolio-variance.asp
[9]: http://www.investopedia.com/articles/trading/04/091504.asp
[10]: http://doc.intuition.io/articles/contributors.html
[11]: http://docker.io
