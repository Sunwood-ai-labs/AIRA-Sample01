"""
文字列処理のユーティリティ関数を提供するモジュール
"""

def reverse_string(text: str) -> str:
    """
    文字列を反転させる関数
    
    Args:
        text (str): 入力文字列
    
    Returns:
        str: 反転した文字列
    """
    return text[::-1]

def count_words(text: str) -> int:
    """
    文字列内の単語数をカウントする関数
    
    Args:
        text (str): 入力文字列
    
    Returns:
        int: 単語数
    """
    words = text.split()
    return len(words)

def is_palindrome(text: str) -> bool:
    """
    文字列が回文かどうかをチェックする関数
    
    Args:
        text (str): チェックする文字列
    
    Returns:
        bool: 回文の場合True、そうでない場合False
    """
    # 空白と大文字小文字を無視して比較
    cleaned_text = ''.join(text.lower().split())
    return cleaned_text == cleaned_text[::-1]

if __name__ == "__main__":
    # テスト用のサンプルコード
    sample_text = "Hello World"
    print(f"Original text: {sample_text}")
    print(f"Reversed: {reverse_string(sample_text)}")
    print(f"Word count: {count_words(sample_text)}")
    
    palindrome_test = "A man a plan a canal Panama"
    print(f"Is '{palindrome_test}' a palindrome? {is_palindrome(palindrome_test)}")
