Test Roots
==========

This folder holds the test root(s).  A test root is the directory that carries
the ``__testroot__.py`` marker; the test runner is pointed at it with
``--root`` and test packages are named relative to it.  The root is named for
your organization's namespace (this template uses ``ccai``):

    source/testroots/ccai/                 <- test root (__testroot__.py)
        tests/
            automationkit/                 <- one package per product package
                singlehost/                <- runs on one machine, no external resources
                distributed/               <- multi-node scenarios (see below)

Mirror the source hierarchy under ``tests/<package>/singlehost``: the tests for
``source/packages/ccai/automationkit/x/y.py`` go in
``tests/automationkit/singlehost/x/test_y.py``.

Which runner
------------

This repository's jobs are ``DistributedTestJob``s, so run the tree through
testplus' own command line::

    source .venv/bin/activate
    testplus testing run --root=./source/testroots/ccai --includes=ccai.tests --output=./.output/local

Do not use ``testbase testing run`` here.  It builds a plain single-host job
with no landscape.  That works right up until a test package originates
landscape couplings at import time -- the moment you add real devices, e.g.
a package whose ``__init__`` does ``from ccai.landscaping.factories import
create_landscape, create_linux_client_coordinator_coupling`` -- and then the
run aborts during framework attachment, before any test executes, with

    KeyError: 'landscape'

``testplus testing run`` wires the landscape lifecycle, so single-host,
helper-process and device-backed packages all run under one command; an
undeclared landscape simply means "no devices".

Distributed scenarios
---------------------

``tests/automationkit/distributed`` ships in two tiers:

* ``test_localhost_cluster`` -- runs everywhere.  Helper PROCESSES on
  127.0.0.1 stand in for remote nodes, so fan-out, isolation and concurrency
  are exercised without a second machine.
* ``test_multihost_scenarios`` -- the same scenarios over real SSH hosts from
  the active landscape.  Gated: every test skips unless
  ``CCAI_DISTRIBUTED_TESTS=1`` is set AND the landscape declares at least two
  ssh hosts.  Point ``--landscape`` at your declaration when you have machines.
