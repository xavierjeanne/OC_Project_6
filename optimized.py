import csv
import time


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
                profit = price * profit_percentage
                stocks.append((name, price, profit))
            except (ValueError, IndexError):
                print(f"Erreur lors de la lecture de la ligne: {row}")
    return stocks


def knapsack_solution(stocks, max_budget=500):
    """Find the best combination using dynamic programming (0/1 Knapsack)."""
    # Convert prices to integers (cents) to use as array indices
    # This assumes prices are in euros with 2 decimal places
    n = len(stocks)
    capacity = int(max_budget * 100)  
    weights = [int(stock[1] * 100) for stock in stocks]
    values = [stock[2] for stock in stocks]

    dp = [0] * (capacity + 1)
    keep = [[False] * (capacity + 1) for _ in range(n)]

    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            if dp[w - weights[i]] + values[i] > dp[w]:
                dp[w] = dp[w - weights[i]] + values[i]
                keep[i][w] = True

    w = capacity
    selected_stocks = []
    for i in range(n - 1, -1, -1):
        if keep[i][w]:
            selected_stocks.append(stocks[i])
            w -= weights[i]

    total_cost = sum(stock[1] for stock in selected_stocks)
    total_profit = sum(stock[2] for stock in selected_stocks)

    return selected_stocks[::-1], total_cost, total_profit


def main(file_path, max_budget=500):
    start = time.time()
    stocks = read_stocks(file_path)
    selected, cost, profit = knapsack_solution(stocks, max_budget)
    end = time.time()

    print(f"Total cost: €{cost:.2f}")
    print(f"Total profit: €{profit:.2f}")
    print("Selected stocks:")
    for name, price, _ in selected:
        print(f"- {name}: €{price:.2f}")
    print(f"Execution time: {end - start:.4f} seconds")


if __name__ == "__main__":
    main("dataset/action.csv")