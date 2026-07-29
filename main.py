import pygame  # pygame（ゲームエンジン）をインポート
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, MOUSEMOTION, MOUSEBUTTONDOWN, Rect
from pygame._sdl2.video import Window
import random
import os


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
    とくてん = 0  # とくてん
    ゲームオーバー = False  # ゲームオーバーかどうか
    がぞうモード = False  # 画像で表示するかどうか
    がぞうフォルダ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")  # 画像の場所


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
    じぶんのがぞう = pygame.image.load(os.path.join(がぞうフォルダ, "player.png")).convert_alpha()  # 自機の画像
    てきのがぞう = pygame.image.load(os.path.join(がぞうフォルダ, "enemy.png")).convert_alpha()  # 敵の画像
    たまのがぞう = pygame.image.load(os.path.join(がぞうフォルダ, "bullet.png")).convert_alpha()  # 弾の画像
    フォント = pygame.font.Font(None, 40)  # もじの表示用

    # ゲームのメインループ
    while True:  # イベント処理用ループ
        がめん.fill((0, 0, 0))  # 黒で塗りつぶす
        if がぞうモード:  # 画像で表示する場合
            がめん.blit(じぶんのがぞう, じぶん)  # 画像（プレイヤー）
        else:
            pygame.draw.rect(がめん, じぶんのいろ, じぶん)  # 四角形（プレイヤー）

        if not ゲームオーバー:  # ゲームオーバーでない場合だけ動かす
            for i, item in enumerate(たま):  # 弾の数だけ繰り返し
                item.move_ip(0, -たまのそくど)  # 弾の移動処理
                if がぞうモード:  # 画像で表示する場合
                    がめん.blit(たまのがぞう, item)  # 画像（弾）
                else:
                    pygame.draw.circle(
                        がめん, (0, 255, 0), (item.x, item.y), item.w / 2
                    )  # 弾の描画処理
                if item.y < 0:  # 弾が画面外に出た場合
                    たま.pop(i)  # 弾の削除
                for j, てき in enumerate(てきたち):  # 敵の数だけ繰り返し
                    if てき.x <= item.x <= てき.x + はば and てき.y <= item.y <= てき.y + たかさ:
                        てきたち.pop(j)  # 敵の削除
                        とくてん += 10  # とくてん加算

            for i, てき in enumerate(てきたち):  # 敵の数だけ繰り返し
                てき.move_ip(0, てきのそくど)  # 敵の移動処理
                if がぞうモード:  # 画像で表示する場合
                    がめん.blit(てきのがぞう, てき)  # 画像（敵）
                else:
                    pygame.draw.rect(がめん, てきのいろ, てき)  # 敵の描画処理
                if じぶん.colliderect(てき):  # 自機に敵があたった場合
                    ゲームオーバー = True
                elif てき.y > がめんたかさ:  # 敵が画面外に出た場合
                    てきたち.pop(i)  # 敵の削除

            カウンタ += 1  # カウンタ増加
            if カウンタ > てきのでにくさ:  # 出現間隔チェック
                てきたち.append(Rect(random.randrange(0, がめんはば), 0, はば, たかさ))  # 敵生成
                カウンタ = 0  # カウンタ初期化

        とくてんもじ = フォント.render(f"SCORE {とくてん}", True, (255, 255, 255))  # とくてんの表示
        がめん.blit(とくてんもじ, (10, 10))
        if ゲームオーバー:  # ゲームオーバーの場合
            ゲームオーバーもじ = フォント.render("GAME OVER", True, (255, 255, 255))
            がめん.blit(ゲームオーバーもじ, ゲームオーバーもじ.get_rect(center=(がめんはば // 2, がめんたかさ // 2)))

        pygame.display.update()  # 描画の更新

        とけい.tick(fps)  # FPSの設定
        if not ゲームオーバー:  # ゲームオーバーでない場合だけ動かす
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_LEFT]:  # 左矢印キーが押された場合
                じぶん.move_ip(-いどうそくど, 0)
            elif pressed_keys[pygame.K_RIGHT]:  # 右矢印キーが押された場合
                じぶん.move_ip(いどうそくど, 0)
            elif pressed_keys[pygame.K_SPACE]:  # スペースキーが押された場合
                たま.append(Rect(じぶん.x + はば / 2, じぶん.y, たまのおおきさ, たまのおおきさ))  # 円（弾））
            if じぶん.x < 0:  # 左はしより外に出た場合
                じぶん.x = 0
            elif じぶん.x > がめんはば - はば:  # 右はしより外に出た場合
                じぶん.x = がめんはば - はば

        for イベント in pygame.event.get():  # イベント処理用の繰り返し
            if イベント.type == QUIT:  # ウインドウが閉じられた場合
                return
            elif (
                イベント.type == KEYDOWN and イベント.key == K_ESCAPE
            ):  # エスケープキーが押された場合
                return
            elif イベント.type == KEYDOWN and イベント.key == pygame.K_i:  # 「い」キーが押された場合
                がぞうモード = not がぞうモード  # 画像で表示するかどうかを切りかえる
            elif (
                イベント.type == KEYDOWN and イベント.key == pygame.K_SPACE and ゲームオーバー
            ):  # ゲームオーバー中にスペースキーが押された場合
                じぶん = Rect(よこ, たて, はば, たかさ)  # 自機をもとの位置にもどす
                たま = []  # 弾を消す
                てきたち = [Rect(random.randrange(0, がめんはば), 0, はば, たかさ)]  # 敵をもとにもどす
                カウンタ = 0  # カウンタをもとにもどす
                とくてん = 0  # とくてんをもとにもどす
                ゲームオーバー = False  # ゲームオーバーをかいじょ
            elif (
                イベント.type == MOUSEBUTTONDOWN and イベント.button == 1 and not ゲームオーバー
            ):  # マウスをクリックした場合
                cx, cy = イベント.pos  # クリック時のマウス座標を取得
                cx += はば / 2
                たま.append(Rect(cx, cy, たまのおおきさ, たまのおおきさ))  # 円（弾））


if __name__ == "__main__":
    main()
