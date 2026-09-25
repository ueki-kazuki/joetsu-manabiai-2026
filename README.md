# 超絶怒涛シューティング

Python と pygame-ce で作った、シンプルなシューティングゲームです。自機を左右に動かし、弾で敵を倒して得点を競います。ゲームのコードを読みながら、順次実行、条件分岐、繰り返し、当たり判定を学べる教材として利用できます。

## 必要なもの

- macOS
- Anaconda または Miniconda
- Python 3.12

依存ライブラリは `requirements.txt` で管理しています。

## 環境の作成

ターミナルで、リポジトリのルートから次を実行します。

```sh
conda create -n mokumoku_20260926 python=3.12
conda activate mokumoku_20260926
python -m pip install -r requirements.txt
```

`cond activate` ではなく、正しくは `conda activate` です。

## 起動方法

仮想環境を有効にしてから、リポジトリのルートで実行します。

```sh
conda activate mokumoku_20260926
python main.py
```

VS Codeでは、Pythonインタープリターに `mokumoku_20260926` 環境を選択してください。

`images/` フォルダの `player.png`、`enemy.png`、`bullet.png` を読み込むため、`main.py` と画像フォルダの位置は変更しないでください。

## 操作方法

| 操作 | 動き |
| --- | --- |
| ← / → | 自機を左右に動かす |
| Space | 自機から弾を発射する |
| マウス左クリック | クリックした位置から弾を発射する |
| I | 四角形表示と画像表示を切り替える |
| Enter | ゲームオーバー後に再開する |
| Esc | ゲームを終了する |

敵にぶつかるとゲームオーバーです。敵を弾で倒すと10点増えます。

## 開発時の確認

```sh
python -m py_compile main.py
```

ゲームの変更後は、通常表示と画像表示の両方で、自機の移動、弾の発射、敵との当たり判定、ゲームオーバー後の再開を確認してください。
