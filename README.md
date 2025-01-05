# robosys2024_ros2
ロボットシステム学　課題2
## 目次
- [概要](#概要)

- [実行方法](#実行方法)

- [注意](#注意)

- [必要なソフトウェア](#必要なソフトウェア)

- [テスト環境](#テスト環境)

- [参考文献](#参考文献)

- [ライセンス](#ライセンス)

## 概要

このプログラムはユーザーの使用しているネットワークのダウンロード速度、アップロード速度を計測するものです.

## 実行方法
```
git clone https://github.com/MILKdaruma/robosys2024_ros2.git
```

```
colcon build
```

```
source install/setup.bash
```

```
ros2 run internet_speed_display internet_speed_node

```

2つ目のターミナルで以下のコードを実行してください。


```
ros2 topic echo /internet_speed
```

## 実行結果

```
data: 'Download Speed: 10.71 Mbps, Upload Speed: 10.38 Mbps'
---
data: 'Download Speed: 12.97 Mbps, Upload Speed: 8.93 Mbps'
---
data: 'Download Speed: 19.75 Mbps, Upload Speed: 11.44 Mbps'
---
data: 'Download Speed: 16.21 Mbps, Upload Speed: 18.45 Mbps'
---
```

## 注意

・計測中は使用しているインターネットによって時間がかかる場合があります。

・回線によってはエラーが出ることがあります。

## 必要なソフトウェア

・ros2

・使用バージョン：foxy

## テスト環境

Ubuntu 24.04

## 参考文献

ROS2でパッケージを作成してから使うまでの流れ【Python3】

https://engineeeer.com/ros2-python3-package-beginner-tutorial/

[5分でマスター]初心者はまずREADMEを書け[テンプレート付き]

https://qiita.com/Canard_engineer_c_cpp/items/81ce4e53881138dbf37f

素敵なREADMEの書き方✨

https://qiita.com/koeri3/items/f85a617dcb6efebb2cab

ハードウェア情報の取得方法

https://chantastu.hatenablog.com/entry/2023/07/15/114657

# ライセンス

・このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます。

・このパッケージのコードの一部は，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです。

https://github.com/ryuichiueda/slides_marp/tree/master/robosys2024

🄫 2025 teruma yamamoto

