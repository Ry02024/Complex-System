# Complex System: 複雑系のシミュレーション

## **概要**
本リポジトリでは、ランダムウォークやフラクタルをはじめとした **複雑系（Complex System）のシミュレーション** を扱います。

現在、以下のテーマを実装済みです：
- **ランダムウォーク**（確率的な移動をシミュレーション）
- **フラクタル（コッホ曲線）**（自己相似性・スケール不変性の可視化）

今後、以下のテーマを追加予定です：
- **ライフゲーム（セル・オートマトンを用いたシミュレーション）**

---

## **📌 現在のリリース**

### **1. ランダムウォーク**
`random_walk/` ディレクトリ内に、以下の実装を用意しています。

- `random_walk.py` … 2DランダムウォークのPythonコード
- `random_walk_notebook.ipynb` … Jupyter Notebook形式で、実行しやすい形に変換

### **2. フラクタル（コッホ曲線）**
`koch_curve/` ディレクトリ内に、以下の実装を用意しています。

- `koch_curve_notebook.ipynb` … Jupyter Notebook形式で、Google Colab で簡単に実行可能

---

## **🚀 実行方法**
### **ランダムウォーク**
Pythonがインストールされている環境で以下を実行：
```bash
python random_walk/random_walk.py
```
Google Colabで実行する場合、`random_walk_notebook.ipynb` を開く。

### **フラクタル（コッホ曲線）**
Pythonがインストールされている環境で以下を実行：
```bash
python koch_curve/koch_curve.py
```
Google Colabで実行する場合、`koch_curve_notebook.ipynb` を開く。

---

## **📂 個別プロジェクト**

| プロジェクト       | 説明                                      | GitHub                                      | Booth          |
|-------------------|--------------------------------------|--------------------------------------------|---------------|
| **ランダムウォーク** | 確率的移動をシミュレーション                 | [GitHub](https://github.com/Ry02024/Complex-System/tree/main/random_walk) | [無料ダウンロード](https://complex-dynamics.booth.pm/items/6457102) |
| **フラクタル生成** | コッホ曲線などのフラクタル描画               | [GitHub](https://github.com/Ry02024/Complex-System/tree/main/fractal)  | [無料ダウンロード](#) （準備中）|
| **ライフゲーム**   | セル・オートマトンのシミュレーション         | 準備中                                     | 準備中        |

---

## **🏛 応用例**

### **ランダムウォークの応用**
- **生物の探索行動** … アリや動物のランダムな移動
- **金融市場のモデル** … 株価変動のランダムウォーク仮説
- **分子運動のシミュレーション** … ブラウン運動のモデル

### **フラクタルの応用**
- **自然界のパターン** … 雪の結晶、シダの葉、河川の流れ
- **データ圧縮技術** … フラクタル圧縮による高効率な画像保存
- **アンテナ設計** … フラクタルアンテナ（小型・広帯域）
- **カオス理論** … フラクタル次元を用いた市場モデリング

---

## **🔗 関連記事**
✅ **Qiita記事：ランダムウォークで学ぶ複雑系の基礎**  
➡ [Qiita](https://qiita.com/ry033rdqiita/items/0f5c99c90080f88d1860)  

✅ **Note記事：フラクタル（コッホ曲線）**  
➡ [Note](https://note.com/ry0w3/n/n83ad57bb0b21)  

✅ **GitHubリリース：v1.1 - ランダムウォーク & フラクタルの実装**  
➡ [GitHub](https://github.com/Ry02024/Complex-System)
