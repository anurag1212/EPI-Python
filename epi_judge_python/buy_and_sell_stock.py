from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    min_price, max_profit = float('inf'), 0
    for i in range(len(prices)):
        curr = prices[i]
        min_price = curr if curr < min_price else min_price
        curr_profit = curr - min_price
        max_profit = max(curr_profit, max_profit)
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
