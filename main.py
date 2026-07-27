import pygame  # pygame（ゲームエンジン）をインポート
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, MOUSEMOTION, MOUSEBUTTONDOWN, Rect
import random


def main():
    (がめんはば, がめんたかさ) = (500, 500)  # 画面サイズ
    (よこ, たて) = (150, 150)  # 初期位置
    (はば, たかさ) = (30, 30)  # プレイヤーの幅と高さ
    fps = 30  # 描画速度（フレームレート）
    いどうそくど = 10  # 移動速度（弾）
    たま = []  # 弾を管理用のリスト
    (いどうそくど, てきのそくど) = (10, 10)  # 移動速度（弾）と敵
    カウンタ = 0  # カウンタ（敵の出現管理）
    てきのでにくさ = 50  # 敵の出現間隔
    pygame.init()  # ライブラリの初期化
    pygame.display.set_caption("超絶怒涛シューティング")  # ウインドウのタイトル設定
    がめん = pygame.display.set_mode((がめんはば, がめんたかさ))  # 画面サイズをw，hで設定

    じぶん = Rect(よこ, たて, はば, たかさ)  # 四角形（プレイヤー）
    じぶんのいろ = (255, 0, 0)  # 色の設定（赤）
    とけい = pygame.time.Clock()  # 時間管理用オブジェクトの作成
    てき = Rect(random.randrange(0, がめんはば), 0, はば, たかさ)
    てきのいろ = (0, 0, 255)  # 色の設定（青）
    たまのおおきさ = 10  # 弾の大きさ

    while True:  # イベント処理用ループ
        がめん.fill((0, 0, 0))  # 黒で塗りつぶす
        pygame.draw.rect(がめん, じぶんのいろ, じぶん)  # 四角形（プレイヤー）

        for i, item in enumerate(たま):  # 弾の数だけ繰り返し
            item.move_ip(0, -いどうそくど)  # 弾の移動処理
            pygame.draw.circle(
                がめん, (0, 255, 0), (item.x, item.y), item.w / 2
            )  # 弾の描画処理
            if item.y < 0:  # 弾が画面外に出た場合
                たま.pop(i)  # 弾の削除

        てき.move_ip(0, てきのそくど)  # 敵の移動処理
        pygame.draw.rect(がめん, てきのいろ, てき)  # 敵の描画処理

        カウンタ += 1  # カウンタ増加
        if カウンタ > てきのでにくさ:  # 出現間隔チェック
            てき = Rect(random.randrange(0, がめんはば), 0, はば, たかさ)  # 敵生成
            カウンタ = 0  # カウンタ初期化

        pygame.display.update()  # 描画の更新

        とけい.tick(fps)  # FPSの設定
        for イベント in pygame.event.get():  # イベント処理用の繰り返し
            if イベント.type == QUIT:  # ウインドウが閉じられた場合
                return
            elif (
                イベント.type == KEYDOWN and イベント.key == K_ESCAPE
            ):  # エスケープキーが押された場合
                return
            elif イベント.type == MOUSEMOTION:  # マウスが移動した場合
                よこ, たて = イベント.pos
                じぶん.move_ip((よこ - じぶん.x), (たて - じぶん.y))
            elif イベント.type == pygame.K_LEFT:  # 左矢印キーが押された場合
                じぶん.move_ip(-10, 0)
            elif イベント.type == pygame.K_RIGHT:  # 右矢印キーが押された場合
                じぶん.move_ip(10, 0)
            elif イベント.type == pygame.K_SPACE:  # スペースキーが押された場合
                たま.append(Rect(じぶん.x + はば / 2, じぶん.y, たまのおおきさ, たまのおおきさ))  # 円（弾））
            elif (
                イベント.type == MOUSEBUTTONDOWN and イベント.button == 1
            ):  # マウスをクリックした場合
                cx, cy = イベント.pos  # クリック時のマウス座標を取得
                cx += はば / 2
                たま.append(Rect(cx, cy, たまのおおきさ, たまのおおきさ))  # 円（弾））


if __name__ == "__main__":
    main()
