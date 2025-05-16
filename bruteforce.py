import csv
from itertools import combinations


def read_stocks(file_path):
    """Reads the stocks from the file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        list: List of stocks.
    """
    stocks = []
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            name = row[0]
            try:
                price = float(row[1])
                profit_percentage = float(row[2].strip('%'))/100
                stocks.append({
                    "name": name,
                    "price": price,
                    "profit_percentage": profit_percentage
                })
            except (ValueError, IndexError):
                print(f"Erreur lors de la lecture de la ligne: {row}")
    return stocks


def calculate_profit(combination):
    """ Calculate the total profit for a combination of stocks.

        Args:
            combination (list): List of stocks in the combination.

        Returns:
            tuple: Total cost and total profit.
    """

    total_cost = sum(stock['price'] for stock in combination)
    total_profit = sum(stock['price'] * stock['profit_percentage']
                       for stock in combination)

    return total_cost, total_profit


def find_best_combination(stocks, max_budget=500):
    """ Find the best combination of stocks using brute force.

        Args:
            stocks (list): List of stocks.
            max_budget (float): Maximum budget for the combination.

        Returns:
            tuple: Best combination of stocks, total cost, and total profit.
    """
    best_combination = []
    best_profit = 0
    best_cost = 0

    # Try all possible combinations of stocks
    for i in range(1, len(stocks) + 1):
        for combo in combinations(stocks, i):
            cost, profit = calculate_profit(combo)
            if cost <= max_budget and profit > best_profit:
                best_combination = combo
                best_profit = profit
                best_cost = cost
    return best_combination, best_cost, best_profit


