#!/usr/bin/env python
###############################################################################
#
#    Arithmetic Solver
#
#    Copyright (c) Clément HUBER
#
#    MIT License
#
###############################################################################

__author__ = "Clément HUBER"
__copyright__ = "Clément HUBER"
__license__ = "MIT"

# IMPORTS =====================================================================

import sys
import logging

# BODY ========================================================================


_logger = logging.getLogger(__name__)


def setup_logging(loglevel):
    """
    Setup basic logging

    Arguments:
    ----------
      loglevel (int): minimum loglevel for emitting messages
    """

    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"

    logging.basicConfig(level=loglevel,
                        stream=sys.stdout,
                        format=logformat,
                        datefmt="%Y-%m-%d %H:%M:%S")
