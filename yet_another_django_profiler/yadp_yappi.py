# encoding: utf-8
#
# This software may be modified and distributed under the terms
# of the 3-clause BSD license.  See the LICENSE file for details.

from __future__ import unicode_literals

import yappi


class YappiProfile(object):
    """ Wrapper class that represents Yappi profiling backend with API matching
        the cProfile.
    """
    def __init__(self):
        self.stats = None

    def runcall(self, func, *args, **kw):
        self.enable()
        try:
            return func(*args, **kw)
        finally:
            self.disable()

    def enable(self):
        yappi.start()

    def disable(self):
        yappi.stop()

    def create_stats(self):
        self.stats = yappi.convert2pstats(yappi.get_func_stats()).stats
