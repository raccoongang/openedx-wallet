openedx-wallet
##############

A simple internal storage backend for Verifiable Credentials application within the Open edX Credentials service.

Note: implemented as a Credentials plugin.

Purpose
=======

Recently Open edX Credentials gained initial verifiable credentials support.
It's `verifiable_credentials` application allows creation (issuance) of verifiable credentials based on
the internally produced in Open edX ecosystem credentials (currently, achieved Program Certificates).

Learners are able to:

- **request an issuance** of a verifiable credential that "mirrors" internal Open edX credential;
- **upload** issued verifiable credential to an **external storage**;

Currently, the only implemented (built-in) storage is the Learner Record Wallet (mobile application).
The Learner Record Wallet usage configuration includes some semi-formal steps to start working on a particular
Open edX installation.

This plugin adds another optional storage backend that is aimed to serve as a playground for
the Verifiable Credentials feature.

Functionality outline
---------------------

The `openedx-wallet` plugin utilizes storages extension point of the `verifiable_credentials` app.
The plugin extends a list of available for usage verifiable credentials storages.

Prerequisites:

- Credentials service is configured with Verifiable Credentials feature enabled
- a new UI іs available within the Learner Record micro-frontend
- there must be at list 1 storage enabled for usage
- `openedx-wallet` backend is included to the default storages configuration

With active `openedx-wallet` backend another action button ("Download") becomes available within the Verifiable Credentials UI.
Action button label (e.g. "Download") is configurable.

Once learners click action button, instead of to be redirected to a mobile app (LC Wallet usage case), they are
navigated to the internal plugin's `wallet-setup` page that allows a manual interactive ("Verifiable Credential requirements"
web form) setup for further verifiable credential issuance.

When the "Verifiable Credential requirements" form is valid (see below), a learner is able to submit the issuance request.

A standard verifiable credential issuance process happens and a newly created artifact is returned in response.

On response learners are redirected to the another internal `wallet-result` page:

- issued verifiable credential is rendered (prettified JSON) within the result page;
- issued verifiable credential is available for download ("Save locally" button);

Verifiable Credential requirements form
---------------------------------------

An options could be:

- required - to set a subject DID;
- (optionally) to set a holder DID;
- (optionally) to force a data model to use (by default: VC Data Model | Open Badges v3.0);
- (optionally) to set expiration period;
- ...
- future: to compose verifiable presentations;
- future: to share with browser extension(s) - investigate on the "CHAPI" use cases;

Use cases
---------

onboarding
  - interested parties are able to investigate on a verifiable credentials nature;
  - interested parties are able to have a quick trial of the Open edX Verifiable Credentials feature (w/o LC Wallet prerequisites);

production use
  - learners - (in theory) want to download verifiable credentials for not yet integrated wallets (with the further import from a disk);

further development
  - QA/developers - future functionality extensions (new data models, new proof methods, etc.)

------

Getting Started
===============

Developing
----------

**One Time Setup**

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
============

Documentation
=============

TODO: where to find more details?

License
=======

The code in this repository is licensed under the Apache Software License 2.0 unless
otherwise noted.

Please see `LICENSE.txt <LICENSE.txt>`_ for details.

Reporting Security Issues
=========================

Please do not report security issues in public. Please email security@tcril.org.
