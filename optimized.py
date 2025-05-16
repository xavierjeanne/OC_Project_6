import csv


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


def knapsack_solution(stocks, max_budget=500):
    """Find the best combination using dynamic programming (0/1 Knapsack)."""
    # Convert prices to integers (cents) to use as array indices
    # This assumes prices are in euros with 2 decimal places
    stocks_processed = []
    for stock in stocks:
        price_cents = int(stock['price'] * 100)
        profit = stock['price'] * stock['profit_percentage']
        stocks_processed.append({
            'name': stock['name'],
            'price': stock['price'],
            'price_cents': price_cents,
            'profit': profit,
            'profit_percentage': stock['profit_percentage']
        })
    
    max_budget_cents = int(max_budget * 100)
    
    # Initialize the DP table
    dp = [0] * (max_budget_cents + 1)
    selected_stocks = [[] for _ in range(max_budget_cents + 1)]
    
    # Fill the DP table
    for stock in stocks_processed:
        for budget in range(max_budget_cents, stock['price_cents'] - 1, -1):
            new_profit = dp[budget - stock['price_cents']] + stock['profit']
            if new_profit > dp[budget]:
                dp[budget] = new_profit
                selected_stocks[budget] = selected_stocks[budget - stock['price_cents']] + [stock]
    
    # Find the best solution
    best_budget = max(range(max_budget_cents + 1), key=lambda b: dp[b])
    best_combination = selected_stocks[best_budget]
    best_cost = sum(stock['price'] for stock in best_combination)
    best_profit = dp[best_budget]
    
    return best_combination, best_cost, best_profit