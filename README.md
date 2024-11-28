# AIRA-Sample01

AIRA (AI Ready Architecture) のサンプルコードリポジトリです。
AIアプリケーション開発のためのベースとなる設計や実装例を提供します。

## 🎯 概要

このプロジェクトは、AIRAのアーキテクチャに基づいた実装サンプルを提供します。
モジュール化された設計により、拡張性と保守性の高いAIアプリケーションの開発が可能です。

## 📂 ディレクトリ構造

```
AIRA-Sample01/
├── modules/          # 機能別モジュール
│   ├── string_utils.py  # 文字列処理ユーティリティ
│   └── math_utils.py    # 数値計算ユーティリティ
└── README.md         # このファイル
```

## 🎁 提供する機能

### 📝 文字列処理モジュール (string_utils.py)

文字列操作のための基本的な機能を提供します：

- `reverse_string()`: 文字列を反転
- `count_words()`: 単語数をカウント
- `is_palindrome()`: 回文判定

```python
from modules.string_utils import reverse_string, is_palindrome

# 文字列の反転
text = "Hello, World!"
print(reverse_string(text))  # "!dlroW ,olleH"

# 回文チェック
palindrome = "A man a plan a canal Panama"
print(is_palindrome(palindrome))  # True
```

### 🔢 数値計算モジュール (math_utils.py)

数値データの分析と計算機能を提供します：

- `calculate_statistics()`: 基本統計量の計算
- `is_prime()`: 素数判定

```python
from modules.math_utils import calculate_statistics, is_prime

# 統計計算
numbers = [1, 2, 3, 4, 5]
stats = calculate_statistics(numbers)
print(stats)  # {"mean": 3.0, "median": 3, "min": 1, "max": 5}

# 素数判定
print(is_prime(17))  # True
```

## 💻 動作環境

- Python 3.8以上
- 追加のライブラリは必要ありません（標準ライブラリのみ使用）

## 🚀 使い方

1. リポジトリのクローン
```bash
git clone [リポジトリURL]
cd AIRA-Sample01
```

2. モジュールの使用
```python
from modules.string_utils import reverse_string
from modules.math_utils import calculate_statistics

# サンプルコード
text = "AIRA Sample"
print(reverse_string(text))

data = [10, 20, 30, 40, 50]
print(calculate_statistics(data))
```

## ⭐ 今後の予定

- 新しい文字列処理機能の追加
- データ検証機能の実装
- パフォーマンス最適化

## 👥 コントリビューション

プロジェクトへの貢献を歓迎します：

1. このリポジトリをフォーク
2. 機能ブランチの作成 (`git checkout -b feature/amazing-feature`)
3. 変更をコミット (`git commit -m 'Add amazing feature'`)
4. ブランチをプッシュ (`git push origin feature/amazing-feature`)
5. Pull Requestを作成

## 📝 ライセンス

本プロジェクトはMITライセンスで提供されています。詳細は[LICENSE](LICENSE)ファイルを参照してください。

## 📫 連絡先・コミュニティ

- 質問・バグ報告: GitHubのIssueをご利用ください
- ディスカッション: GitHubのDiscussionsをご利用ください
