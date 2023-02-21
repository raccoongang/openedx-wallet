openedx-wallet
#############################

.. note::

  TODO: describe the purpose and provide a general concept for this tool.

Purpose
*******

A simple storage backend for Open edX Credentials `verifiable credentials` onboarding.

TODO: describe

Getting Started
***************

Developing
==========

One Time Setup
--------------
.. code-block::

  # Clone the repository
  git clone git@github.com:openedx/openedx-wallet.git
  cd openedx-wallet

  # Set up a virtualenv using virtualenvwrapper with the same name as the repo and activate it
  mkvirtualenv -p python3.8 openedx-wallet


Every time you develop something in this repo
---------------------------------------------
.. code-block::

  # Activate the virtualenv
  workon openedx-wallet

  # Grab the latest code
  git checkout main
  git pull

  # Install/update the dev requirements
  (optional) make upgrade
  make requirements

  # Run the tests and quality checks (to verify the status before you make any changes)
  make validate

  # Make a new branch for your changes
  git checkout -b <your_github_username>/<short_description>

  # Using your favorite editor, edit the code to make your change.
  vim ...

  # Run your new tests
  pytest ./path/to/new/tests

  # Run all the tests and quality checks
  make validate

  # Commit all your changes
  git commit ...
  git push

  # Open a PR and ask for review.

Deploying
=========

This app is aimed to be installed into the Open edX Credentials IDA python environment.

Getting Help
************

Documentation
=============

TODO: where to find more details?

License
*******

The code in this repository is licensed under the Apache Software License 2.0 unless
otherwise noted.

Please see `LICENSE.txt <LICENSE.txt>`_ for details.

Reporting Security Issues
*************************

Please do not report security issues in public. Please email security@tcril.org.
