# -*- coding: utf-8 -*-
#
#    Copyright © 2017 markdown-link-style contributors. See CONTRIBUTORS.
#
#    This file is part of markdown-link-style.
#
#   markdown-link-style is free software: you can redistribute it
#   and/or modify it under the terms of the GNU General Public License
#   as published by the Free Software Foundation, either version 3 of
#   the License, or (at your option) any later version.
#
#   markdown-link-style is distributed in the hope that it will be
#   useful, but WITHOUT ANY WARRANTY; without even the implied
#   warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#   See the GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with markdown-link-style (see COPYING).  If not, see
#   <http://www.gnu.org/licenses/>.

import logging

class MDLSLogger(object):
    """Logging utility for modules in markdown-link-style.

    """

    def __init__(self, name):
        self.logger = logging.getLogger(name)

    def debug(msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)

    def info(msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def warning(msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)

    def error(msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)

    def critical(msg, *args, **kwargs):
        self.logger.critical(msg, *args, **kwargs)

    def log(msg, *args, **kwargs):
        self.logger.log(msg, *args, **kwargs)

    def exception(msg, *args, **kwargs):
        self.logger.exception(msg, *args, **kwargs)
