import unittest
import pandas as pd
from pysarplus import SARModel


class TestSar(unittest.TestCase):
    def test1(self):
        x = SARModel("/Users/eisber/Documents/Recommenders/cpp-cache/output5")

        y = x.predict([0, 1], [10, 20], 10)

        for p in y:
            print("%d -> %f" % (p.id, p.score))

    def test2(self):
        x = SARModel("/Users/eisber/Documents/Recommenders/cpp-cache/output5")

        y = x.predict([0, 2], [10, 3], 5)

        for p in y:
            print("%d -> %f" % (p.id, p.score))

    def test3(self):
        x = SARModel("/Users/eisber/Documents/Recommenders/cpp-cache/output5")

        y = x.predict([1, 0], [20, 10], 10)

        for p in y:
            print("%d -> %f" % (p.id, p.score))

    def test4(self):
        x = SARModel("/Users/eisber/Documents/Recommenders/cpp-cache/output5")

        item_scores = pd.DataFrame([(0, 2.3), (1, 3.1)], columns=["itemID", "score"])

        y = x.predict(item_scores["itemID"].values, item_scores["score"].values, 10)

        for p in y:
            print("%d -> %f" % (p.id, p.score))
