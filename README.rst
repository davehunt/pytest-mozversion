pytest-mozversion
=================

pytest-mozversion is a plugin for `pytest <http://pytest.org>`_ that extracts
Mozilla application version information metadata and makes it available via
pytest-metadata.

.. image:: https://img.shields.io/badge/license-MPL%202.0-blue.svg
   :target: https://github.com/davehunt/pytest-mozversion/blob/master/LICENSE
   :alt: License
.. image:: https://img.shields.io/pypi/v/pytest-mozversion.svg
   :target: https://pypi.python.org/pypi/pytest-mozversion/
   :alt: PyPI
.. image:: https://img.shields.io/travis/davehunt/pytest-mozversion.svg
   :target: https://travis-ci.org/davehunt/pytest-mozversion/
   :alt: Travis
.. image:: https://img.shields.io/github/issues-raw/davehunt/pytest-mozversion.svg
   :target: https://github.com/davehunt/pytest-mozversion/issues
   :alt: Issues
.. image:: https://img.shields.io/requires/github/davehunt/pytest-mozversion.svg
   :target: https://requires.io/github/davehunt/pytest-mozversion/requirements/?branch=master
   :alt: Requirements

Requirements
------------

You will need the following prerequisites in order to use pytest-mozversion:

- Python 2.7, 3.6, PyPy, or PyPy3
- pytest 2.9.0 or newer

Installation
------------

To install pytest-mozversion:

.. code-block:: bash

  $ pip install pytest-mozversion

Usage
-----

If you provide a base URL via the pytest-base-url plugin, then
pytest-mozversion will automatically look for a `__version__` endpoint, and add
the results to a `version` key within the metadata provided by pytest-metadata.

Resources
---------

- `Release Notes <http://github.com/davehunt/pytest-mozversion/blob/master/CHANGES.rst>`_
- `Issue Tracker <http://github.com/davehunt/pytest-mozversion/issues>`_
- `Code <http://github.com/davehunt/pytest-mozversion/>`_
