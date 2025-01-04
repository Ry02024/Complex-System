# Complex System: 複雑系のシミュレーション

## 概要
本リポジトリでは、ランダムウォークをはじめとした **複雑系（Complex System）のシミュレーション** を扱います。  
初回リリースでは **ランダムウォーク** をテーマに、Pythonを用いたシミュレーションと可視化を行います。

今後、以下のテーマを追加予定です：
- **ランダムウォーク**
- **フラクタル（コッホ曲線、シェルピンスキーのギャスケット）**
- **ライフゲーム（セル・オートマトンを用いたシミュレーション）**

## 📌 現在のリリース：ランダムウォーク
[**random_walk/**](./random_walk) ディレクトリ内に、以下の実装を用意しています。
- `random_walk.py` … 2DランダムウォークのPythonコード
- `random_walk_notebook.ipynb` … Jupyter Notebook形式で、実行しやすい形に変換

## 🚀 実行方法
1. Pythonがインストールされている環境で以下を実行：
   ```bash
   python random_walk/random_walk.py
   ```
2. Google Colabで実行する場合、`random_walk_notebook.ipynb` を開く

## 🏛 応用例
ランダムウォークは以下の現象に応用されています：
- **生物の探索行動** … アリや動物のランダムな移動
- **金融市場のモデル** … 株価変動のランダムウォーク仮説
- **分子運動のシミュレーション** … ブラウン運動のモデル

## 🔗 関連記事
- Qiita記事：[ランダムウォークで学ぶ複雑系の基礎](https://qiita.com/ry033rdqiita/items/0f5c99c90080f88d1860)
- GitHubリリース：[v1.0 - ランダムウォークの実装](https://github.com/Ry02024/Complex-System/tree/main/random_walk)
