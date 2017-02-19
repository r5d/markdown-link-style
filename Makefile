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

test:
	@nosetests
.PHONY: test

build-dist:
	@python setup.py sdist bdist_wheel
.PHONY: build-dist

egg:
	@python setup.py egg_info
.PHONY: egg

upload:
	@twine upload -r pypi -s -i \
		'1534 126D 8C8E AD29 EDD9  1396 6BE9 3D8B F866 4377' \
		dist/*.tar.gz
	@twine upload -r pypi -s -i \
		'1534 126D 8C8E AD29 EDD9  1396 6BE9 3D8B F866 4377' \
		dist/*.whl
.PHONY: upload

clean-build:
	@rm -rf build/
	@rm -rf dist/
	@rm -rf *.egg-info

clean-pyc:
	@find . -name '*.pyc' -exec rm -f {} +

clean-venv:
	@rm -rf bin/
	@rm -rf include/
	@rm -rf lib/
	@rm -rf local/
	@rm -rf man/
.PHONY: clean-venv
