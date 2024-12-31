---
layout: page
title: Work(done)
description: This is a style guide of the Scriptor Jekyll theme
---


2024年9月~12月

## APIリファレンス改修業務

<!-- プロジェクトがわからない外部の人に説明する感じで記述する -->

やったこと
- APIのwebマニュアル表現の誤りを修正する作業

自分の立ち位置
- PM（プロジェクトの実働）
- ドキュメント記載

このPJTの意義
- 加盟店がAPIマニュアルを見ながら組み込む際、最新の表示や表現が曖昧の場合、体験価値を低下させてしまう。
- 会社の信頼を揺らがせないためにも早期修正が必要である。

自分がとった行動
- CSや問い合わせのチャンネルから検知された修正箇所をすべて直した
- また、APIリファレンスをみてて既存の修正点以外にも修正すべき箇所が何個かでてきたため、それらを主体的に検知しそれらの修正にも取り組んだ

振り返り

1. 仕事の緩急をつけること
    - 複数あるタスクの中から、どれを先に進めないけないかなどの目利きができなかったっため、先輩の視点をもらいにいく姿勢が必要だと学んだ。

2. 相談する際のフォーマットの準備
    - 人によって読みやすい文書が異なる。結論ファーストで聴きたいことをばっちりまとめて、もっていく姿勢を学んだ
3. 工数の話
    - 実際、1週間で仕上げる予定のタスクだったが、12営業日もかかってしまった。
    - 早い段階で、タスクの進捗状況を相談していくことの大事さを学んだ。
4. 現場を知ることの重要性
    - APIリファレンスで表現がおかしいところを修正する作業だったが、実際に現場の開発エンジニアがこのフォーマットを読んで認識相違なく理解できるのか？構成から変えるべきなのではないのかと思ってしまった。
    - 組み込み現場を知りたいなという気持ちになった。

## データパッチ業務

やったこと
- データパッチシステム（PRをあげたら基幹DBに書き込みできるようになるシステム）を運用Tが利用できるようにする
- すでに存在する。社内システムの改修作業。
- AWSでマルチアカウントアクセスができるようにCodepipelineやCodeBuildをiaCで記述し立ち上げたり、業務で実行できるSQLを増やす作業

自分の立ち位置
- PM（実働）
- 開発、テスト、リリース

このPJTの意義
- 運用Tが、SQLを手動で実施する運用フローだったがミスが起きやすく、属人化もしやすい。また、多忙な社内エンジニアがインフラを考える時間がとれない状況だったため、自分がインフラ面などを考えて手を動かすことで、彼らの時間削減に寄与する。
- このPJTを完遂させることで、他の部署でも展開可能になる。

自分がとった行動
- 運用Tが利用するシステムであるので、運用Tが使いやすいシステムはどういうものなのか？を定義し運用Tと検討し実装に落とし込む。
- 複数タスクが存在する中で自分がどのタスクを優先的に実行するとよいのかを検討し、達成状態や目標の修正依頼を相談
- PJTは完了したが、運用Tが利用できるようにするまでにしたい自分の意思でアウトプット（インフラを作成した）だけではなく、実働までのアウトカム（業務手順書READMEの記述）を実現した。

振り返り
- バディと一緒に相談して進めることが多かったのもあり、POにPJTに進捗共有を怠っていた。PJTの方針が変わったり、既存の路線から変更したときにはなおさら進捗共有が大事であり、定例MTGや1on1の重要性を感じた。
- 自分が何を優先して取り組むべきかのROI視点的なPJTアプローチを描けた。自分（正社員）が考えるといいタスクってなんだろうの視点を得られた。
- タスクを実施することによるメリットは人によって違ってきており、色々な視座で仕事に関する話を聞けたこと。

This is a pragraph. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo. Quisque sit amet est et sapien ullamcorper pharetra. Vestibulum erat wisi, condimentum sed, commodo vitae, ornare sit amet, wisi. Aenean fermentum, elit eget tincidunt condimentum, eros ipsum rutrum orci, sagittis tempus lacus enim ac dui. Donec non enim in turpis pulvinar facilisis. Ut felis.

# Heading 1

**Quisque facilisis erat a dui**. Nam malesuada ornare dolor. Cras gravida, diam sit amet rhoncus ornare, erat elit consectetuer erat, id egestas pede nibh eget odio. Proin tincidunt, velit vel porta elementum, magna diam molestie sapien, non aliquet massa pede eu diam. Aliquam iaculis. Fusce et ipsum et nulla tristique facilisis.

## Heading 2

Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Morbi commodo, ipsum sed pharetra gravida, orci magna rhoncus neque, id pulvinar odio lorem non turpis. Nullam sit amet enim. Suspendisse id velit vitae ligula volutpat condimentum. Aliquam erat volutpat. Sed quis velit. Nulla facilisi. Nulla libero.

### Heading 3

Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Morbi commodo, ipsum sed pharetra gravida, orci magna rhoncus neque, id pulvinar odio lorem non turpis. Nullam sit amet enim. Suspendisse id velit vitae ligula volutpat condimentum. Aliquam erat volutpat. Sed quis velit. Nulla facilisi. Nulla libero.

#### Heading 4

Quisque facilisis erat a dui. Nam malesuada ornare dolor. Cras gravida, diam sit amet rhoncus ornare, erat elit consectetuer erat, id egestas pede nibh eget odio. Proin tincidunt, velit vel porta elementum, magna diam molestie sapien, non aliquet massa pede eu diam. Aliquam iaculis.

##### Heading 5

Curabitur pellentesque facilisis orci, ut rhoncus nulla scelerisque ac. Integer in magna vel justo venenatis ornare vitae vel sem.

###### Heading 6

Nulla tempus tortor nec nunc volutpat commodo. Vivamus efficitur imperdiet velit sagittis pellentesque. In fringilla dui nec dolor sollicitudin, et scelerisque elit pellentesque. Integer vestibulum viverra sem, vel ornare nibh. Proin lobortis elit nunc, ut consequat elit vulputate sit amet.

## Emphasis

**This is bold text**

*This is italic text*

~~Strikethrough~~

## Links

[I'm an inline-style link](https://www.google.com)

[I'm an inline-style link with title](https://www.google.com "Google's Homepage")

## Quoting

>“Creativity is allowing yourself to make mistakes. Design is knowing which ones to keep.”

Lorem ipsum dolor sit amet, `consectetuer adipiscing` elit. Morbi commodo, ipsum sed pharetra gravida, orci magna rhoncus neque, id pulvinar odio lorem non turpis. Nullam sit amet enim. Suspendisse id velit vitae ligula volutpat condimentum. Aliquam erat volutpat. Sed quis velit. Nulla facilisi. Nulla libero.


## Lists
Here is an unordered list of items, typically rendered as a bulleted list:

+ Donec non tortor in arcu mollis feugiat
+ Lorem ipsum dolor sit amet, consectetuer adipiscing elit
+ Donec id eros eget quam aliquam gravida
+ Vivamus convallis urna id felis
+ Nulla porta tempus sapien

Here is an ordered list of items, typically rendered as a numbered list:

1. Donec non tortor in arcu mollis feugiat
2. Lorem ipsum dolor sit amet, consectetuer adipiscing elit
3. Donec id eros eget quam aliquam gravida
4. Vivamus convallis urna id felis
5. Nulla porta tempus sapien

### Tables

| Title | Title |
| ------| ----- |
| Text  | Text  |
| Text  | Text  |
| Text  | Text  |