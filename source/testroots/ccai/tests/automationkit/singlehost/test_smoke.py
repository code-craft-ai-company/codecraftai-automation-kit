"""
    .. module:: test_smoke
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Proves the kit's package and both test frameworks import in
               the built environment.  Replace with tests of your product
               code; keep the test tree mirroring the source tree
               (source/packages/<ns>/x/y.py -> tests/<pkg>/singlehost/x/test_y.py).

    .. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2026, Code Craft AI LLC"
__credits__ = []


import importlib

from ccai import testbase


def test_kit_package_imports() -> None:
    """
        The product package this repository ships is importable.
    """
    module = importlib.import_module("ccai.automationkit")
    testbase.assert_true(hasattr(module, "__file__"))
    return


def test_frameworks_are_wired() -> None:
    """
        Both frameworks the kit is built on resolve from the environment:
        testbase for single-host suites, testplus for distributed jobs.
    """
    for name in ("ccai.testbase", "ccai.testplus"):
        importlib.import_module(name)
    return
