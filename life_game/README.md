# Life Game: セル・オートマトンによるシミュレーション

## **📌 概要**
ライフゲーム（Life Game）は、イギリスの数学者 **ジョン・コンウェイ（John Conway）** によって考案された**セル・オートマトン**の一種です。非常にシンプルなルールでありながら、**複雑なパターンの創発** を観察できます。

本プロジェクトでは、Pythonを用いて **ライフゲームをシミュレーションし、アニメーションとして可視化** します。

---

## **📌 ルール**
ライフゲームは、以下の4つのルールに従ってセルの状態が変化します。

1. **誕生**: 死んでいるセル（0）が、周囲にちょうど3つの生存セル（1）を持つ場合、生きる（1）
2. **生存**: 生きているセル（1）が、周囲に2つまたは3つの生存セルを持つ場合、生き続ける（1）
3. **過疎**: 生きているセル（1）が、周囲に1つ以下の生存セルしかない場合、死ぬ（0）
4. **過密**: 生きているセル（1）が、周囲に4つ以上の生存セルがある場合、死ぬ（0）

このルールを **すべてのセルに適用しながら、世代を更新** していきます。

---

## **📌 実装内容**
✅ Python による **ライフゲームのシミュレーション**
✅ `matplotlib.animation` を使った **アニメーション化**
✅ `NumPy` を利用した **効率的な更新処理**
✅ **Google Colab での実行** をサポート

---

## **🚀 実行方法**

### **📌 1. Google Colabで実行する**
ライフゲームの動作を **Google Colab で簡単に実行** できます。

[![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1PKX1IFVdZrAWJiNdROHXL5sCxpP_VInR?usp=sharing)

### **📌 2. ローカル環境で実行する**（未実装）
1. 必要なライブラリをインストール
   ```bash
   pip install numpy matplotlib
   ```
2. `life_game.py` を実行
   ```bash
   python life_game.py
   ```

---

## **📂 ファイル構成**
```
life_game/
│── life_game.py                 # Pythonスクリプト版（未実装）
│── life_game_notebook.ipynb      # Google Colab用ノートブック
│── README.md                     # 本ファイル
```

---

## **📌 関連リンク**
✅ **GitHub（ソースコード）**  
➡ [Complex-System/LifeGame](https://github.com/Ry02024/Complex-System/tree/main/life_game)  

✅ **Qiita（技術記事）**  
➡ 準備中

✅ **Note（プロジェクトの背景・解説）**  
➡ 準備中

✅ **Booth（無料ダウンロード）**  
➡ 準備中

---

## **📌 まとめ**
- **ライフゲームは、シンプルなルールで複雑なパターンを生み出すセル・オートマトンの代表例** です。
- **Pythonを使ってシミュレーションし、Google Colabで簡単に試せる環境を用意しました。**
- 今後は **創発現象やスマートシティのモデリング** への応用も検討しています。

🚀 **スターを押して応援してください！** ⭐
