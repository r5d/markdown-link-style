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

from mistune import Renderer, Markdown
from nose.tools import *
from pkg_resources import resource_string

from mdl_style import *


def _get_data(f):
    rs = resource_string(__name__, '/'.join(['data', f]))
    return rs.decode()

class TestLSRendererIL(object):
    """Test class for mdl_style.LSRenderer inline link style.

    """

    def setup(self):
        self.md = LSMarkdown(link_style='inline')

    def test_autolink_00(self):
        d = _get_data('autolink_00.md')
        d_expected = _get_data('autolink_00-expected.md')
        assert_equals(self.md(d), d_expected)

    def test_link_footnote_to_inline_style_conversion_00(self):
        d = _get_data('inline_link_style_00.md')
        expected_result = _get_data('inline_link_style_00-expected.md')
        assert_equal(self.md(d), expected_result)

    def test_link_footnote_to_inline_style_conversion_01(self):
        d = _get_data('inline_link_style_01.md')
        expected_result = _get_data('inline_link_style_01-expected.md')
        assert_equal(self.md(d), expected_result)

    def test_renderer_parses_images_00(self):
        d = _get_data('inline_parses_images_00.md')
        expected_result = _get_data(
            'inline_parses_images_00-expected.md')
        assert_equal(self.md(d), expected_result)

    def test_renderer_does_not_parse_link_breaks_00(self):
        d = _get_data('does_not_parse_link_breaks_00.md')
        assert_equal(self.md(d), d)

    def test_renderer_does_not_parse_headers_00(self):
        d = _get_data('does_not_parse_headers_00.md')
        assert_equal(self.md(d), d)

    def test_renderer_does_not_parse_blockquotes_00(self):
        d = _get_data('does_not_parse_blockquotes_00.md')
        assert_equal(self.md(d), d)

    def test_renderer_does_not_parse_lists_00(self):
        d = _get_data('does_not_parse_lists_00.md')
        assert_equal(self.md(d), d)

    def test_renderer_does_not_parse_codeblocks_00(self):
        d = _get_data('does_not_parse_codeblocks_00.md')
        assert_equal(self.md(d), d)

    def test_renderer_does_not_parse_hrules_00(self):
        d = _get_data('does_not_parse_hrules_00.md')
        assert_equal(self.md(d), d)

    def test_renderer_does_not_parse_emphasis_00(self):
        d = _get_data('does_not_parse_emphasis_00.md')
        assert_equal(self.md(d), d)

    def test_renderer_does_not_parse_code_00(self):
        d = _get_data('does_not_parse_code_00.md')
        assert_equal(self.md(d), d)

    def teardown(self):
        pass


class TestLSRendererFN(object):
    """Test class for mdl_style.LSRenderer footnote link style.

    """

    def setup(self):
        self.md = LSMarkdown(link_style='footnote')

    def test_autolink_00(self):
        d = _get_data('autolink_00.md')
        d_expected = _get_data('autolink_00-expected.md')
        assert_equals(self.md(d), d_expected)

    def test_link_inline_to_footnote_style_conversion_00(self):
        d = _get_data('footnote_link_style_00.md')
        expected_result = _get_data(
            'footnote_link_style_00-expected.md')
        assert_equal(self.md(d), expected_result)

    def test_link_inline_to_footnote_style_conversion_01(self):
        d = _get_data('footnote_link_style_01.md')
        expected_result = _get_data(
            'footnote_link_style_01-expected.md')
        assert_equal(self.md(d), expected_result)

    def test_renderer_parses_images_00(self):
        d = _get_data('footnote_parses_images_00.md')
        expected_result = _get_data(
            'footnote_parses_images_00-expected.md')
        assert_equal(self.md(d), expected_result)

    def test_renderer_does_not_parse_link_breaks_00(self):
        d = _get_data('does_not_parse_link_breaks_00.md')
        assert_equal(self.md(d), d)

    def test_renderer_does_not_parse_headers_00(self):
        d = _get_data('does_not_parse_headers_00.md')
        assert_equal(self.md(d), d)

    def test_renderer_does_not_parse_blockquotes_00(self):
        d = _get_data('does_not_parse_blockquotes_00.md')
        assert_equal(self.md(d), d)

    def test_renderer_does_not_parse_lists_00(self):
        d = _get_data('does_not_parse_lists_00.md')
        assert_equal(self.md(d), d)

    def test_renderer_does_not_parse_codeblocks_00(self):
        d = _get_data('does_not_parse_codeblocks_00.md')
        assert_equal(self.md(d), d)

    def test_renderer_does_not_parse_hrules_00(self):
        d = _get_data('does_not_parse_hrules_00.md')
        assert_equal(self.md(d), d)

    def test_renderer_does_not_parse_emphasis_00(self):
        d = _get_data('does_not_parse_emphasis_00.md')
        assert_equal(self.md(d), d)

    def test_renderer_does_not_parse_code_00(self):
        d = _get_data('does_not_parse_code_00.md')
        assert_equal(self.md(d), d)

    def teardown(self):
        pass
