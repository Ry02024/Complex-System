# ランダムウォーク - Pythonによるシミュレーション

## 概要
ランダムウォークは、ランダムな動きのシミュレーションであり、確率過程の基本モデルとして重要です。  
このディレクトリには、Pythonを用いた2Dランダムウォークの実装が含まれています。

## 🔧 ファイル構成
- `random_walk.py` … 2Dランダムウォークの基本実装
- `random_walk_notebook.ipynb` … Google Colab用のJupyter Notebook
- `images/` … 可視化結果のスクリーンショットやGIF

## 🏃‍♂️ **実装例**
以下は、`random_walk.py` を活用した Notebook で可視化したランダムウォークのアニメーションです。

```python
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
from IPython.display import HTML

# --- `random_walk.py` の関数を定義 ---
def random_walk(num_steps):
    """2Dランダムウォークをシミュレーション"""
    x, y = [0], [0]  # 初期位置

    for _ in range(num_steps):
        dx, dy = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        x.append(x[-1] + dx)
        y.append(y[-1] + dy)

    return x, y

# ランダムウォークのアニメーション
def animate_random_walk(num_steps=100):
    x, y = [0], [0]
    fig, ax = plt.subplots(figsize=(6, 6))
    line, = ax.plot([], [], lw=2)

    def update(frame):
        dx, dy = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        x.append(x[-1] + dx)
        y.append(y[-1] + dy)
        line.set_data(x, y)
        return line,

    ani = animation.FuncAnimation(fig, update, frames=num_steps, interval=100, blit=True)
    return ani

HTML(animate_random_walk().to_jshtml())


## 📌 参考リンク
- [GitHubリポジトリトップ](../README.md)
- [Qiita記事](https://qiita.com/ry033rdqiita/items/0f5c99c90080f88d1860)
