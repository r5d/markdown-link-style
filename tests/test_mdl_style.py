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

import os
import os.path
import sys


from io import StringIO
from random import randint
from unittest import mock


from mistune import Renderer, Markdown
from nose.tools import *
from pkg_resources import resource_string, resource_filename


from markdown_link_style._version import __version__
from mdl_style import *
from mdl_style import _get_args, _mdl_stylize


def _get_data(f):
    rs = resource_string(__name__, "/".join(["data", f]))
    return rs.decode()


def _get_data_path(f):
    return resource_filename(__name__, "/".join(["data", f]))


class TestLSRendererIL(object):
    """Test class for mdl_style.LSRenderer inline link style.

    """

    def setup(self):
        self.md = LSMarkdown(link_style="inline")

    def test_autolink_00(self):
        d = _get_data("autolink_00.md")
        d_expected = _get_data("autolink_00-expected.md")
        assert_equals(self.md(d), d_expected)

    def test_link_footnote_to_inline_style_conversion_00(self):
        d = _get_data("inline_link_style_00.md")
        expected_result = _get_data("inline_link_style_00-expected.md")
        assert_equal(self.md(d), expected_result)

    def test_link_footnote_to_inline_style_conversion_01(self):
        d = _get_data("inline_link_style_01.md")
        expected_result = _get_data("inline_link_style_01-expected.md")
        assert_equal(self.md(d), expected_result)

    def test_renderer_parses_images_00(self):
        d = _get_data("inline_parses_images_00.md")
        expected_result = _get_data("inline_parses_images_00-expected.md")
        assert_equal(self.md(d), expected_result)

    def test_renderer_does_not_parse_link_breaks_00(self):
        d = _get_data("does_not_parse_link_breaks_00.md")
        assert_equal(self.md(d), d)

    def test_renderer_does_not_parse_headers_00(self):
        d = _get_data("does_not_parse_headers_00.md")
        assert_equal(self.md(d), d)

    def test_renderer_does_not_parse_blockquotes_00(self):
        d = _get_data("does_not_parse_blockquotes_00.md")
        assert_equal(self.md(d), d)

    def test_renderer_does_not_parse_lists_00(self):
        d = _get_data("does_not_parse_lists_00.md")
        assert_equal(self.md(d), d)

    def test_renderer_does_not_parse_codeblocks_00(self):
        d = _get_data("does_not_parse_codeblocks_00.md")
        assert_equal(self.md(d), d)

    def test_renderer_does_not_parse_hrules_00(self):
        d = _get_data("does_not_parse_hrules_00.md")
        assert_equal(self.md(d), d)

    def test_renderer_does_not_parse_emphasis_00(self):
        d = _get_data("does_not_parse_emphasis_00.md")
        assert_equal(self.md(d), d)

    def test_renderer_does_not_parse_code_00(self):
        d = _get_data("does_not_parse_code_00.md")
        assert_equal(self.md(d), d)

    def teardown(self):
        pass


class TestLSRendererFN(object):
    """Test class for mdl_style.LSRenderer footnote link style.

    """

    def setup(self):
        self.md = LSMarkdown(link_style="footnote")

    def test_autolink_00(self):
        d = _get_data("autolink_00.md")
        d_expected = _get_data("autolink_00-expected.md")
        assert_equals(self.md(d), d_expected)

    def test_link_inline_to_footnote_style_conversion_00(self):
        d = _get_data("footnote_link_style_00.md")
        expected_result = _get_data("footnote_link_style_00-expected.md")
        assert_equal(self.md(d), expected_result)

    def test_link_inline_to_footnote_style_conversion_01(self):
        d = _get_data("footnote_link_style_01.md")
        expected_result = _get_data("footnote_link_style_01-expected.md")
        assert_equal(self.md(d), expected_result)

    def test_renderer_parses_images_00(self):
        d = _get_data("footnote_parses_images_00.md")
        expected_result = _get_data("footnote_parses_images_00-expected.md")
        assert_equal(self.md(d), expected_result)

    def test_renderer_does_not_parse_link_breaks_00(self):
        d = _get_data("does_not_parse_link_breaks_00.md")
        assert_equal(self.md(d), d)

    def test_renderer_does_not_parse_headers_00(self):
        d = _get_data("does_not_parse_headers_00.md")
        assert_equal(self.md(d), d)

    def test_renderer_does_not_parse_blockquotes_00(self):
        d = _get_data("does_not_parse_blockquotes_00.md")
        assert_equal(self.md(d), d)

    def test_renderer_does_not_parse_lists_00(self):
        d = _get_data("does_not_parse_lists_00.md")
        assert_equal(self.md(d), d)

    def test_renderer_does_not_parse_codeblocks_00(self):
        d = _get_data("does_not_parse_codeblocks_00.md")
        assert_equal(self.md(d), d)

    def test_renderer_does_not_parse_hrules_00(self):
        d = _get_data("does_not_parse_hrules_00.md")
        assert_equal(self.md(d), d)

    def test_renderer_does_not_parse_emphasis_00(self):
        d = _get_data("does_not_parse_emphasis_00.md")
        assert_equal(self.md(d), d)

    def test_renderer_does_not_parse_code_00(self):
        d = _get_data("does_not_parse_code_00.md")
        assert_equal(self.md(d), d)

    def teardown(self):
        pass


class TestMdlStyleMdlStylize(object):
    """Testing mdl_style._mdl_stylize.

    """

    @classmethod
    def setup_class(self):
        self.test_data = {}

        self.test_data["inline"] = {}
        self.test_data["inline"]["in"] = _get_data("inline_link_style_00.md")
        self.test_data["inline"]["out"] = _get_data("inline_link_style_00-expected.md")

        self.test_data["footnote"] = {}
        self.test_data["footnote"]["in"] = _get_data("footnote_link_style_00.md")
        self.test_data["footnote"]["out"] = _get_data(
            "footnote_link_style_00-expected.md"
        )

        self.in_file = "in_file.md"
        self.out_file = "out_file.md"

    def setup(self):
        self.link_style = ["inline", "footnote"][randint(0, 1)]

        with open(self.in_file, "w") as f:
            f.write(self.test_data[self.link_style]["in"])

    def test_mdl_stylize_infile(self):
        args = _get_args([self.link_style, self.in_file])
        _mdl_stylize(args)  # the test.

        with open(self.in_file, "r") as f:
            assert_equal(f.read(), self.test_data[self.link_style]["out"])

    def test_mdl_stylize_infile_outfile(self):
        args = _get_args([self.link_style, self.in_file, self.out_file])
        _mdl_stylize(args)

        with open(self.out_file, "r") as f:
            assert_equal(f.read(), self.test_data[self.link_style]["out"])

    def teardown(self):
        if os.path.isfile(self.in_file):
            os.remove(self.in_file)

        if os.path.isfile(self.out_file):
            os.remove(self.out_file)


class TestMdlStyleGetArgs(object):
    """Testing mdl_style._get_args.

    """

    def setup(self):
        self.out = None

    @raises(SystemExit)
    def test_get_args_version(self):
        real_exit = sys.exit

        def mock_exit(args):
            assert_equal(sys.stdout.getvalue(), __version__ + "\n")
            real_exit(args)

        with mock.patch("sys.stdout", new_callable=StringIO) as out, mock.patch(
            "sys.exit", new=mock_exit
        ):
            raw_args = ["--version"]
            _get_args(raw_args)

    def test_get_args_inline_infile(self):
        lstyle = "inline"
        md_file = "autolink_00.md"
        raw_args = [lstyle, _get_data_path(md_file)]
        args = _get_args(raw_args)
        assert_equal(args.link_style, lstyle)
        assert_equal(args.in_file.read(), _get_data(md_file))

    def test_get_args_inline_infile_outfile(self):
        lstyle = "inline"
        md_file = "autolink_00.md"
        raw_args = [lstyle, _get_data_path(md_file), "outfile.md"]
        args = _get_args(raw_args)
        assert_equal(args.link_style, lstyle)
        assert_equal(args.in_file.read(), _get_data(md_file))
        assert_equal(type(args.out_file), str)

    def test_get_args_footnote_infile(self):
        lstyle = "footnote"
        md_file = "autolink_00.md"
        raw_args = [lstyle, _get_data_path(md_file)]
        args = _get_args(raw_args)
        assert_equal(args.link_style, lstyle)
        assert_equal(args.in_file.read(), _get_data(md_file))

    def test_get_args_footnote_infile_outfile(self):
        lstyle = "footnote"
        md_file = "autolink_00.md"
        raw_args = [lstyle, _get_data_path(md_file), "outfile.md"]
        args = _get_args(raw_args)
        assert_equal(args.link_style, lstyle)
        assert_equal(args.in_file.read(), _get_data(md_file))
        assert_equal(type(args.out_file), str)

    def teardown(self):
        pass
