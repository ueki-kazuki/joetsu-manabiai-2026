import pygame  # pygame（ゲームエンジン）をインポート
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, MOUSEMOTION, MOUSEBUTTONDOWN, Rect
from pygame._sdl2.video import Window
import random


def main():
    (がめんはば, がめんたかさ) = (500, 1024)  # 画面サイズ
    (よこ, たて) = (150, 150)  # 初期位置
    (よこ, たて) = (150, がめんたかさ - たて)  # 初期位置
    (はば, たかさ) = (30, 30)  # プレイヤーの幅と高さ
    fps = 30  # 描画速度（フレームレート）
    たま = []  # 弾を管理用のリスト
    (いどうそくど, たまのそくど, てきのそくど) = (10, 10, 10)  # 移動速度（弾）と敵
    カウンタ = 0  # カウンタ（敵の出現管理）
    てきのでにくさ = 50  # 敵の出現間隔


    # しょりかいし
    # がめんをしょきかする
    pygame.init()  # ライブラリの初期化
    pygame.display.set_caption("超絶怒涛シューティング")  # ウインドウのタイトル設定
    がめん = pygame.display.set_mode((がめんはば, がめんたかさ))  # 画面サイズをw，hで設定
    まど = Window.from_display_module()  # 今のウインドウを取得
    まど.focus()  # ウインドウを他より前に出す

    じぶん = Rect(よこ, たて, はば, たかさ)  # 四角形（プレイヤー）
    じぶんのいろ = (255, 0, 0)  # 色の設定（赤）
    とけい = pygame.time.Clock()  # 時間管理用オブジェクトの作成
    てきたち = [Rect(random.randrange(0, がめんはば), 0, はば, たかさ)]  # 敵を管理用のリスト
    てきのいろ = (0, 0, 255)  # 色の設定（青）
    たまのおおきさ = 10  # 弾の大きさ

    # ゲームのメインループ
    while True:  # イベント処理用ループ
        がめん.fill((0, 0, 0))  # 黒で塗りつぶす
        pygame.draw.rect(がめん, じぶんのいろ, じぶん)  # 四角形（プレイヤー）

        for i, item in enumerate(たま):  # 弾の数だけ繰り返し
            item.move_ip(0, -たまのそくど)  # 弾の移動処理
            pygame.draw.circle(
                がめん, (0, 255, 0), (item.x, item.y), item.w / 2
            )  # 弾の描画処理
            if item.y < 0:  # 弾が画面外に出た場合
                たま.pop(i)  # 弾の削除
            for j, てき in enumerate(てきたち):  # 敵の数だけ繰り返し
                if てき.x <= item.x <= てき.x + はば and てき.y <= item.y <= てき.y + たかさ:
                    てきたち.pop(j)  # 敵の削除

        for i, てき in enumerate(てきたち):  # 敵の数だけ繰り返し
            てき.move_ip(0, てきのそくど)  # 敵の移動処理
            pygame.draw.rect(がめん, てきのいろ, てき)  # 敵の描画処理
            if てき.y > がめんたかさ:  # 敵が画面外に出た場合
                てきたち.pop(i)  # 敵の削除

        カウンタ += 1  # カウンタ増加
        if カウンタ > てきのでにくさ:  # 出現間隔チェック
            てきたち.append(Rect(random.randrange(0, がめんはば), 0, はば, たかさ))  # 敵生成
            カウンタ = 0  # カウンタ初期化

        pygame.display.update()  # 描画の更新

        とけい.tick(fps)  # FPSの設定
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:  # 左矢印キーが押された場合
            じぶん.move_ip(-いどうそくど, 0)
        elif pressed_keys[pygame.K_RIGHT]:  # 右矢印キーが押された場合
            じぶん.move_ip(いどうそくど, 0)
        elif pressed_keys[pygame.K_SPACE]:  # スペースキーが押された場合
            たま.append(Rect(じぶん.x + はば / 2, じぶん.y, たまのおおきさ, たまのおおきさ))  # 円（弾））

        for イベント in pygame.event.get():  # イベント処理用の繰り返し
            if イベント.type == QUIT:  # ウインドウが閉じられた場合
                return
            elif (
                イベント.type == KEYDOWN and イベント.key == K_ESCAPE
            ):  # エスケープキーが押された場合
                return
            elif (
                イベント.type == MOUSEBUTTONDOWN and イベント.button == 1
            ):  # マウスをクリックした場合
                cx, cy = イベント.pos  # クリック時のマウス座標を取得
                cx += はば / 2
                たま.append(Rect(cx, cy, たまのおおきさ, たまのおおきさ))  # 円（弾））


if __name__ == "__main__":
    main()
