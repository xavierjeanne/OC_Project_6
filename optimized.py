import csv
import time
import sys


def read_stocks(file_path):
    """Reads the stocks from the file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        list: List of stocks.
    """
    stocks = []
    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                name = row[0]
                try:
                    price = float(row[1])
                    profit_percentage = float(row[2].strip('%'))/100
                    

                    if price <= 0:
                        continue
                        
                    profit = price * profit_percentage
                    stocks.append((name, price, profit))
                except (ValueError, IndexError):
                    print(f"Erreur lors de la lecture de la ligne: {row}")
    except FileNotFoundError:
        print(f"Fichier non trouvé: {file_path}")
        sys.exit(1)
        
    print(f"Nombre d'actions chargées: {len(stocks)}")
    return stocks


def knapsack_solution(stocks, max_budget=500):
    """Find the best combination using dynamic programming (0/1 Knapsack).
    
    Args:
        stocks: List of stocks, each stock can be either:
               - A tuple (name, price, profit)
               - A dictionary with 'name', 'price', and 'profit_percentage' keys
        max_budget: Maximum budget in euros
        
    Returns:
        tuple: Selected stocks, total cost, and total profit
    """
    n = len(stocks)
    capacity = int(max_budget * 100)  # Convert to cents

    # Filter out stocks that exceed the budget and ensure positive weights
    valid_stocks = []
    for i in range(n):
        # Handle both tuple and dictionary formats
        if isinstance(stocks[i], tuple):
            name, price, profit = stocks[i]
        elif isinstance(stocks[i], dict):
            name = stocks[i]['name']
            price = stocks[i]['price']
            profit = price * stocks[i]['profit_percentage']
        else:
            continue  # Skip invalid formats
            
        weight = int(price * 100)
        if 0 < weight <= capacity:  # Ensure weight is positive and within capacity
            valid_stocks.append((name, price, profit))

    if not valid_stocks:
        return [], 0, 0

    # Rest of the function remains the same
    n = len(valid_stocks)
    weights = [int(stock[1] * 100) for stock in valid_stocks]
    values = [stock[2] for stock in valid_stocks]

    # Initialize the DP table
    dp = [0] * (capacity + 1)
    keep = [[] for _ in range(capacity + 1)]

    # Fill the DP table
    for i in range(n):
        # Ensure weight is valid
        if weights[i] <= 0:
            continue
            
        for w in range(capacity, weights[i] - 1, -1):
            # Double-check to avoid negative indices
            if w >= weights[i]:
                new_value = dp[w - weights[i]] + values[i]
                if new_value > dp[w]:
                    dp[w] = new_value
                    keep[w] = keep[w - weights[i]] + [i]

    # Find the best solution
    best_w = max(range(capacity + 1), key=lambda w: dp[w])
    selected_indices = keep[best_w]
    selected_stocks = [valid_stocks[i] for i in selected_indices]

    total_cost = sum(stock[1] for stock in selected_stocks)
    total_profit = sum(stock[2] for stock in selected_stocks)

    return selected_stocks, total_cost, total_profit
    """Find the best combination using dynamic programming (0/1 Knapsack)."""
    n = len(stocks)
    capacity = int(max_budget * 100)  # Convert to cents

    # Filter out stocks that exceed the budget and ensure positive weights
    valid_stocks = []
    for i in range(n):
        weight = int(stocks[i][1] * 100)
        if 0 < weight <= capacity: 
            valid_stocks.append(stocks[i])

    if not valid_stocks:
        return [], 0, 0

    n = len(valid_stocks)
    weights = [int(stock[1] * 100) for stock in valid_stocks]
    values = [stock[2] for stock in valid_stocks]

    # Initialize the DP table
    dp = [0] * (capacity + 1)
    keep = [[] for _ in range(capacity + 1)]

    # Fill the DP table
    for i in range(n):
        # Ensure weight is valid
        if weights[i] <= 0:
            continue
            
        for w in range(capacity, weights[i] - 1, -1):
            # Double-check to avoid negative indices
            if w >= weights[i]:
                new_value = dp[w - weights[i]] + values[i]
                if new_value > dp[w]:
                    dp[w] = new_value
                    keep[w] = keep[w - weights[i]] + [i]

    # Find the best solution
    best_w = max(range(capacity + 1), key=lambda w: dp[w])
    selected_indices = keep[best_w]
    selected_stocks = [valid_stocks[i] for i in selected_indices]

    total_cost = sum(stock[1] for stock in selected_stocks)
    total_profit = sum(stock[2] for stock in selected_stocks)

    return selected_stocks, total_cost, total_profit


def main(file_path, max_budget=500):
    start = time.time()
    stocks = read_stocks(file_path)

    if not stocks:
        print(f"Error: No valid stocks found in {file_path}")
        return

    selected, cost, profit = knapsack_solution(stocks, max_budget)
    end = time.time()

    print(f"Total cost: €{cost:.2f}")
    print(f"Total profit: €{profit:.2f}")
    print(f"Rendement: {(profit/cost)*100:.2f}%")
    print("Selected stocks:")
    for name, price, profit in selected:
        print(f"- {name}: €{price:.2f} (profit: €{profit:.2f})")
    print(f"Execution time: {end - start:.4f} seconds")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = "dataset/action.csv"
    
    main(file_path)