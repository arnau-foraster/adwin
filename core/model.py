# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

import numpy


class Adwin(object):
    """Adaptative sliding window implementation."""

    def __init__(self, d, size_w, w):
        self.confidence = d  # confidence parameter
        self.size_w = size_w
        self.window = w

        logging.debug(
            'Init Adwin with data: %s | %s | %s',
            self.confidence,
            self.size_w,
            self.window,
        )

    def avg(self, w):
        mean = numpy.mean(w)
        logging.debug('Avg value: %s', mean)

        return mean

    def e_cut(self, size_w0, size_w1):
        # m = 1/(1/n 0 + 1/n 1 ) i δ 0 = δ/n
        m = 1 / ((1 / float(size_w0)) + (1 / float(size_w1)))
        # delta
        delta = float(self.confidence / float(self.size_w))
        e = numpy.sqrt(float((1 / (2 * m))) * numpy.log10(float(4 / delta)))
        logging.debug('e: %s', e)
        return e

    def apply_algorithm(self, w_list, x_t, m):
        self.window.append(x_t)
        lenght_w_list = len(w_list)

        if lenght_w_list > self.size_w:
            self.window.pop(0)

        if lenght_w_list == self.size_w:
            logging.debug('Current window: %s', self.window)

            for i in range(1, self.size_w):
                w0_slice = self.window[:i]
                w1_slice = self.window[i:]

                mean_slice0 = self.avg(w0_slice)
                mean_slice1 = self.avg(w1_slice)
                means_diff = numpy.absolute(mean_slice0 - mean_slice1)

                if means_diff > self.e_cut(len(w0_slice), len(w1_slice)):
                    # update window
                    logging.debug('Update window with slice: %s', w1_slice)
                    self.window = w1_slice

            return self.avg(self.window)
