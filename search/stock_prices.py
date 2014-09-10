"""
Given a time-ordered list of stock prices, give the best buy-sell strategy

e.g [300, 200, 500, 1000, 100, 800]
ans: 200, 1000

"""
import unittest


class TestAlg(unittest.TestCase):
    """ Test cases for the algorithm"""

    def test_1(self):
        stock_prices = [300, 200, 500, 1000, 100, 800]
        self.assertEqual(best_value(stock_prices), (200, 1000))

    def test_2(self):
        N = 10**5
        stock_prices = list(range(N))
        self.assertEqual(best_value(stock_prices), (0, N-1))

    def test_3(self):
        stock_prices = []
        self.assertRaises(IndexError, best_value, stock_prices)


def best_value(stock):
    """Find best (buy, sell) tuple

    Args:
        stock: list of time-ordered stock values
    Returns:
        tuple of (buy, sell) values
    Raises:
        IndexError if len(stock) < 2
    """
    best_sell = sell = stock.pop()
    buy = stock.pop()

    while stock:
        num = stock.pop()
        if num < buy:
            buy = num
            sell = best_sell
        elif best_sell - num > sell - buy:
            sell, buy = best_sell, num
        elif num > best_sell:
            best_sell = num

    return (buy, sell)


if __name__ == "__main__":
    unittest.main()
