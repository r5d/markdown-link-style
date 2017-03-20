# -*- coding: utf-8 -*-
#
#   Copyright © 2017 markdown-link-style contributors.
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

import sys

from io import StringIO

from markdown_link_style.logging import MDLSLogger

class TestMDLSLogger(object):
    """Test class for markdown_link_style.logging.MDLSLogger.

    """

    def setup(self):
        self.stream = StringIO()
        self.logger = MDLSLogger('TestLogger', self.stream)

    def test_debug(self):
        log_msg = 'DEBUG::MSG'
        self.logger.debug(log_msg)
        assert self.stream.getvalue().strip('\n') == log_msg

    def test_info(self):
        self.logger.info('INFO::MSG')

    def test_warning(self):
        self.logger.warning('WARNING::MSG')

    def teardown(self):
        pass
