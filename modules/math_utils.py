"""
数値計算のユーティリティ関数を提供するモジュール
"""

import math
from typing import List, Union

def calculate_statistics(numbers: List[Union[int, float]]) -> dict:
    """
    数値リストの基本統計量を計算する関数
    
    Args:
        numbers (List[Union[int, float]]): 数値のリスト
    
    Returns:
        dict: 平均値、中央値、最小値、最大値を含む辞書
    """
    if not numbers:
        return {
            "mean": None,
            "median": None,
            "min": None,
            "max": None
        }
    
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    
    # 中央値の計算
    if n % 2 == 0:
        median = (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    else:
        median = sorted_numbers[n//2]
    
    return {
        "mean": sum(numbers) / len(numbers),
        "median": median,
        "min": min(numbers),
        "max": max(numbers)
    }

def is_prime(n: int) -> bool:
    """
    数値が素数かどうかをチェックする関数
    
    Args:
        n (int): チェックする数値
    
    Returns:
        bool: 素数の場合True、そうでない場合False
    """
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    # テスト用のサンプルコード
    test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    stats = calculate_statistics(test_numbers)
    print("Statistics for", test_numbers)
    print(f"Mean: {stats['mean']}")
    print(f"Median: {stats['median']}")
    print(f"Min: {stats['min']}")
    print(f"Max: {stats['max']}")
    
    # 素数のテスト
    test_number = 17
    print(f"Is {test_number} prime? {is_prime(test_number)}")
