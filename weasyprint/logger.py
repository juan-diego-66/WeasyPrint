# coding: utf-8
"""
    weasyprint.logging
    ------------------

    Logging setup.

    The rest of the code gets the logger through this module rather than
    ``logging.getLogger`` to make sure that it is configured.

    :copyright: Copyright 2011-2014 Simon Sapin and contributors, see AUTHORS.
    :license: BSD, see LICENSE for details.

"""

from __future__ import division, unicode_literals

import logging

LOGGER = logging.getLogger('weasyprint')
LOGGER.addHandler(logging.NullHandler())
