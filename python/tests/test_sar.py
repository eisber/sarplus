import math
import os
import pandas as pd
import unittest

from pysarplus import SARModel

# cat tests/spark-generate-cache.script | spark-shell --jars /Users/eisber/Documents/sarplus/scala/target/scala-2.11/sarplus_2.11-0.1.8.jar

def assert_compare(expected_id, expected_score, actual_prediction):
    assert expected_id == actual_prediction.id
    assert math.isclose(expected_score, actual_prediction.score, rel_tol=1e-3, abs_tol=1e-3)

class TestSar(unittest.TestCase):
    def setUp(self):
        path = os.path.dirname(os.path.realpath(__file__)) + "/sample-output.sar"
        self.model = SARModel(path)

    def test_good(self):
        y = self.model.predict([0, 1], [10, 20], 10)

        assert_compare(0, 5, y[0])
        assert_compare(1, 44, y[1])
        assert_compare(2, 64, y[2])

    def test_good_less(self):
        y = self.model.predict([0, 2], [10, 3], 5)

        assert_compare(0, 1, y[0])
        assert_compare(1, 11.6, y[1])
        assert_compare(2, 12.3, y[2])

    def test_good_require_sort(self):
        y = self.model.predict([1, 0], [20, 10], 10)

        assert_compare(0, 5, y[0])
        assert_compare(1, 44, y[1])
        assert_compare(2, 64, y[2])

    def test_pandas(self):
        item_scores = pd.DataFrame([(0, 2.3), (1, 3.1)], columns=["itemID", "score"])

        y = self.model.predict(item_scores["itemID"].values, item_scores["score"].values, 10)

        assert_compare(0, 0.85, y[0])
        assert_compare(1, 6.9699, y[1])
        assert_compare(2, 9.92, y[2])
