# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest

from core import model


class GroundTests(unittest.TestCase):
    def setUp(self):
        self.window = [1, 2, 3, 4]
        self.adwin = model.Adwin(1, len(self.window), self.window)

    def test_init(self):
        self.assertIsNotNone(self.adwin)

    def test__e_cut(self):
        self.assertIsNotNone(self.adwin.e_cut(len(self.window[:1]),
                                              len(self.window[1:])))

    def test_core_algorithm(self):
        self.window.pop(0)
        self.adwin.apply_algorithm(self.window, 1, 0)
