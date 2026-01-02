.. sphinx-test-project documentation master file, created by
   sphinx-quickstart on Fri Jan  2 15:15:24 2026.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

sphinx-test-project documentation
=================================

YK's project to learn the ``Sphinx`` documentation package. See the
`github repo @ <https://github.com/yuppiekisaragi/sphinx-test-project#>`_
documentation for details.

Note, assuming that one starts in the top-level sphinx-test-project dir,
(as seen on GitHub), all of the actual code is under ./src. The project
is configured as follows:

.. code-block:: console

./docs/ - everything related to Sphinx
./src/test.py - Simple test file with basic functions that Sphinx should
   produce documentation for.
./docs/source/conf.py - Basic Sphinx configuration, which also includes
   the necessary directive to add the sphinx-test-project/ dir to the
   very beginning of sys.path, to ensure that modules can be referenced
   using the appropriate name when generating updated API documentation.

.. code-block:: console

   ### clone the repo locally & install dependencies
   git clone https://github.com/yuppiekisaragi/sphinx-test-project && cd sphinx-test-project
   python3 -m venv .
   source bin/activate
   pip install -r requirements.txt

   ### generate the docs!
   sphinx-apidoc -f -o docs/source src
   cd docs && make html

.. note::
   This project is under active development!

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules
