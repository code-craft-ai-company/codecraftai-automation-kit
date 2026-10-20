===============================
Code Craft AI Automation Kit
===============================

The ``codecraftai-automation-kit`` repository serves as a template repository that companies and organizations can utilize to get test automation projects off the ground and headed in a great direction very rapidly. It ties together the ``codecraftai-*`` suite into a ready-to-brand starting point, with curated conventions, configuration layouts, and an end-to-end user guide.

.. note::

   This is a template repository, not a package, and it is not published to PyPI. Do not install it; start a new
   project from it instead, with GitHub's **Use this template** button or:

   .. code-block:: bash

      gh repo create <your-project> --template code-craft-ai-company/codecraftai-automation-kit

   The ``codecraftai-*`` packages it builds on are published to PyPI and install from there.

Status
======

This repository is currently a stub awaiting implementation. See the intended
scope above and ``userguide/`` for the automation-kit guidance that will drive
future development.

Repository Structure
====================

- ``development/`` - Runtime environment scripts.
- ``repository-setup/`` - Repository homing and setup scripts.
- ``source/packages/`` - Package source code (scaffolding).
- ``source/testroots/testplus/`` - TestPlus test roots (scaffolding).
- ``source/sphinx/`` - Sphinx documentation sources.
- ``userguide/`` - Full automation-kit user guide covering branding, configuration, coupling, and CLI usage.

Environment Setup
=================

When working in a Codex container:

.. code-block:: bash

   ./development/setup-agent-container

For local development:

.. code-block:: bash

   ./repository-setup/rehome-repository
   ./development/setup-envrionment

Standards and Conventions
=========================

- Naming conventions: ``userguide/10-02-naming-conventions.rst``
- Code organization: ``userguide/10-01-code-organization.rst``
- Coding standards: ``userguide/10-00-coding-standards.rst``

Additional Resources
====================

- Repository branding: ``userguide/00-00-repository-branding.rst``
- Getting started: ``userguide/02-00-getting-started.rst``
- Automation configuration: ``userguide/03-00-automation-configuration.rst``
- Testrun sequencing: ``userguide/04-00-testrun-sequencing.rst``
- Command line: ``userguide/08-00-command-line.rst``
- Documentation build: ``userguide/11-00-documentation-build.rst``
