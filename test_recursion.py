__author__ = 'aouyang1'

import unittest
import RecursionClass as rc
import numpy as np
import time
import random

# run nosetests in the terminal


class TestRecursion(unittest.TestCase):

    def test_listsum(self):
        self.assertEqual(rc.listsum([1, 2, 3, 4, 5]), 15)
        self.assertEqual(rc.listsum([]), 0)

    def test_tostring(self):
        self.assertEqual(rc.tostring(9876543210), "9876543210")
        self.assertEqual(rc.tostring(0), "0")

    def test_find_paths(self):
        start_time = time.time()
        path_counts = rc.find_paths(0, 0)
        dumb_time = time.time() - start_time

        start_time = time.time()
        path_counts_eff = rc.find_paths_memo(0, 0)
        nice_time = time.time() - start_time

        print "find_paths dumb: {}, nice: {}".format(dumb_time, nice_time)

        self.assertEqual(path_counts, path_counts_eff)

    def test_find_magic(self):

        a = range(10000000)
        idx_to_save = random.choice(a)
        a = np.array(a)
        a[:idx_to_save] -= 1
        a[idx_to_save+1:] += 1
        a = list(a)

        start_time = time.time()
        magic_idx = rc.find_magic(a, 0, len(a))
        print "index: {}, value: {}, time: {}".format(magic_idx,
                                                      a[magic_idx],
                                                      time.time() - start_time)


        start_time = time.time()
        magic_idx = rc.find_magic_dumb(a)
        print "index: {}, value: {}, time: {}".format(magic_idx,
                                                      a[magic_idx],
                                                      time.time() - start_time)

    def test_subset_string(self):
        self.assertEqual(rc.subset_string("abcd"), ['a', 'b', 'c', 'd', 'ab',
                                                    'bc', 'cd', 'abc', 'bcd',
                                                    'abcd'])

    def test_permute_string(self):
        self.assertEqual(rc.permute_string("abcd", ""), ['a', 'ab', 'abc',
                                                         'abcd', 'abd', 'abdc',
                                                         'ac', 'acb', 'acbd',
                                                         'acd', 'acdb', 'ad',
                                                         'adb', 'adbc', 'adc',
                                                         'adcb', 'b', 'ba',
                                                         'bac', 'bacd', 'bad',
                                                         'badc', 'bc', 'bca',
                                                         'bcad', 'bcd', 'bcda',
                                                         'bd', 'bda', 'bdac',
                                                         'bdc', 'bdca', 'c',
                                                         'ca', 'cab', 'cabd',
                                                         'cad', 'cadb', 'cb',
                                                         'cba', 'cbad', 'cbd',
                                                         'cbda', 'cd', 'cda',
                                                         'cdab', 'cdb', 'cdba',
                                                         'd', 'da', 'dab',
                                                         'dabc', 'dac', 'dacb',
                                                         'db', 'dba', 'dbac',
                                                         'dbc', 'dbca', 'dc',
                                                         'dca', 'dcab', 'dcb',
                                                         'dcba'])



