# hivetech/intuition image
# A raring box with Intuition (https://github.com/hackliff/intuition installed
# and ready to use
#   docker run -i -t hivetech/portfolio bash
# VERSION 0.0.0

FROM hivetech/batcave:base
MAINTAINER Xavier Bruhiere <xavier.bruhiere@gmail.com>

ADD . /portfolio
RUN cd /portfolio && make
RUN apt-get clean && rm -rf \
  /portofolio/build \
  /tmp/* /var/tmp/* \
  /var/lib/apt/lists/* \
  /etc/dpkg/dpkg.cfg.d/02apt-speedup \
  /etc/ssh/ssh_host_*
