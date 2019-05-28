# -*- coding: utf-8 -*-
import unittest

from core import algorithm


class GroundTests(unittest.TestCase):
    def setUp(self):
        self.window = [1, 2, 3, 4]
        self.adwin = algorithm.Adwin(1, len(self.window), self.window)

    def test_init(self):
        self.assertIsNotNone(self.adwin)

    def test__e_cut(self):
        self.assertIsNotNone(self.adwin.e_cut(len(self.window[:1]),
                                              len(self.window[1:])))

    def test_core_algorithm(self):
        self.window.pop(0)
        self.adwin.apply(self.window, 1, 0)
