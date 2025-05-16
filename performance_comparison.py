import time
from bruteforce import find_best_combination, read_stocks
from optimized import knapsack_solution


def compare_performance(file_path):
    
    stocks = read_stocks(file_path)
    # Measure brute force performance
    start_time = time.time()
    bf_result = find_best_combination(stocks)
    bf_time = time.time() - start_time

    # Measure optimized solution performance
    start_time = time.time()
    opt_result = knapsack_solution(stocks)
    opt_time = time.time() - start_time

    print(f"Brute Force: {bf_time:.4f} seconds")
    print(f"Optimized: {opt_time:.4f} seconds")
    print(f"Speedup: {bf_time/opt_time:.2f}x")

    # Compare results
    bf_profit = bf_result[2]
    opt_profit = opt_result[2]
    print(f"Brute Force profit: {bf_profit}")
    print(f"Optimized profit: {opt_profit}")
    print(f"Profit difference: {abs(bf_profit - opt_profit)}")


if __name__ == "__main__":
    compare_performance("dataset/action.csv")

    stocks = read_stocks("dataset/action.csv")
    best_combination, best_cost, best_profit = find_best_combination(stocks)

    print("Meilleure combinaison d'actions:")
    for stock in best_combination:
        print(f"{stock['name']}: {stock['price']} €,"
              f"{stock['profit_percentage'] * 100:.2f}%")

    print(f"Coût total: {best_cost} €")
    print(f"Bénéfice total: {best_profit} €")
    
    best_combination, best_cost, best_profit = knapsack_solution(stocks)

    print("Meilleure combinaison d'actions:")
    for stock in best_combination:
        print(f"{stock['name']}: {stock['price']} €,"
              f"{stock['profit_percentage'] * 100:.2f}%")

    print(f"Coût total: {best_cost} €")
    print(f"Bénéfice total: {best_profit} €")