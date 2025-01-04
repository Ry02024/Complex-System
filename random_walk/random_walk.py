import matplotlib.pyplot as plt
import random
import argparse

def random_walk(num_steps):
    """2Dランダムウォークをシミュレーション"""
    x, y = [0], [0]  # 初期位置

    for _ in range(num_steps):
        dx, dy = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        x.append(x[-1] + dx)
        y.append(y[-1] + dy)

    return x, y

def plot_walk(x, y, num_steps):
    """ランダムウォークをプロット"""
    plt.figure(figsize=(6, 6))
    plt.plot(x, y, marker="o", markersize=3, linestyle="-", alpha=0.6)
    plt.scatter([x[0]], [y[0]], color="red", label="Start")  # 開始点
    plt.scatter([x[-1]], [y[-1]], color="blue", label="End")  # 終点
    plt.xlim(min(x)-1, max(x)+1)
    plt.ylim(min(y)-1, max(y)+1)
    plt.title(f"2D Random Walk ({num_steps} steps)")
    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="2Dランダムウォークを実行")
    parser.add_argument("--steps", type=int, default=100, help="ランダムウォークのステップ数")
    args = parser.parse_args()

    x, y = random_walk(args.steps)
    plot_walk(x, y, args.steps)
