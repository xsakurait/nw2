畳み込み層　小さいフィルターで画像全体を走査してかけ合わせて合算する
　初期段階　Conv2D(N(何枚のフィルター),(a,b(フィルターの大きさ)),3(カラー画像なら３、モノクロなら１))
もう１層畳み込み層
Conv2D(M,(c,d))(上同様)
フィルター毎にRGBそれぞれ合計するので
畳み込みの結果はN枚となる 

プーリング層　小さな区画を１画素に縮約する処理。多少の画素のずれへの耐性高める
MaxPooling2D(pool_size=(2,2))
プーリングサイズ４だから、画素４この正方形のが措置が１番大きい奴だけとり、出力するので
元が4×4の画像の場合、2×2の大きさとなる

活性化　生体ニューロン（脳の反応回路）が反応するとき電気信号が出る
活性化関数　犬の画像を見たときニューロンが犬だと反応するが、
ほかのニューロンに電気信号を渡すときの大きさをあらわした関数
Activation ReLU 0より小さいと0多いとそのままの値

CNN全体像
畳み込み層（Conv2D）
活性化関数
プーリング層
活性化関数
平滑化
ドロップアウト　一度学習化ネットワークの一部忘れさせ誤差最小（こうばいほうによって極小値に落ち着いてしまう）にする
model.add(Dropout(0.5))#50％の重みを忘れさせる(0~1.0)
全結合ネットワーク
ソフトマックス

極小値とは定義域内でかたむきがせいからふにかわるところ
最小値　とはていぎいきで一番値が小さなところ
ここまでで６時間学習してる

全結合層　すべてのニューロン(Dense1ノード)が次の層のニューロンに接続している
model.add(Dense(128) )128このノードを持つ全結合レイヤー追加

Softmax関数　複数のカテゴリが起こる確率出力
model.add(Activation('softmax'))

ラベルとクラスの違い
全体集合をいくつかの部分集合に分けるのはクラス分類問題
そして、部分集合間に重複なく、いずれかの部分集合に必ず属する
その逆がラベリング問題
その部分集合をクラス
部分集合２つ　２クラス問題
３つ以上　多クラス問題
人間だと「会社員」、「アルバイト」どっちもの人いるのでそれぞれラベル
全体集合犬だと　それぞれクラス


