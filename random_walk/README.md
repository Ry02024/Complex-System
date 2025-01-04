# ランダムウォーク - Pythonによるシミュレーション

## 概要
ランダムウォークは、ランダムな動きのシミュレーションであり、確率過程の基本モデルとして重要です。  
このディレクトリには、Pythonを用いた2Dランダムウォークの実装が含まれています。

## 🔧 ファイル構成
- `random_walk.py` … 2Dランダムウォークの基本実装
- `random_walk_notebook.ipynb` … Google Colab用のJupyter Notebook
- `images/` … 可視化結果のスクリーンショットやGIF

## 🏃‍♂️ コードの説明
```python
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

# ステップ数と初期位置を設定
num_steps = 100  # ステップ数
x, y = [0], [0]  # 初期位置

# ランダムウォークのステップを計算する関数
def random_walk(i):
    dx, dy = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])  # ランダムに方向を選択
    x.append(x[-1] + dx)
    y.append(y[-1] + dy)
    line.set_data(x, y)
    return line,

# プロットの初期設定
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-num_steps // 2, num_steps // 2)
ax.set_ylim(-num_steps // 2, num_steps // 2)
ax.set_title("ランダムウォークのアニメーション")
line, = ax.plot([], [], lw=2)

# アニメーションを設定
ani = FuncAnimation(fig, random_walk, frames=num_steps, interval=100, blit=True)

# アニメーションを表示
plt.show()
```

## 📌 参考リンク
- [GitHubリポジトリトップ](../README.md)
- [Qiita記事](https://qiita.com/ry033rdqiita/items/0f5c99c90080f88d1860)
