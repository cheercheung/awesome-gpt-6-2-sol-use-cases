<div align="center">

<h1>GPT-6.2 Sol · デモとユースケース</h1>

<a href="https://evolink.ai/?utm_source=github&utm_medium=banner&utm_campaign=gpt-6-2-sol-usecases&utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/covers/cover-1c4c7490be0406351b48.svg" width="760" alt="GPT-6.2 Sol community demos and use cases"></a>

[![License](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey)](LICENSE) [![Browse EvoLink models](https://img.shields.io/badge/Browse_models-EvoLink-111111)](https://evolink.ai/models?utm_source=github&utm_medium=badge&utm_campaign=gpt-6-2-sol-usecases&utm_content=model_catalog)

[![English](https://img.shields.io/badge/English-2563eb)](README.md) [![Español](https://img.shields.io/badge/Espa%C3%B1ol-2563eb)](README_es.md) [![Português](https://img.shields.io/badge/Portugu%C3%AAs-2563eb)](README_pt.md) [![日本語](https://img.shields.io/badge/%E6%97%A5%E6%9C%AC%E8%AA%9E-2563eb)](README_ja.md) [![한국어](https://img.shields.io/badge/%ED%95%9C%EA%B5%AD%EC%96%B4-2563eb)](README_ko.md) [![Deutsch](https://img.shields.io/badge/Deutsch-2563eb)](README_de.md) [![Français](https://img.shields.io/badge/Fran%C3%A7ais-2563eb)](README_fr.md) [![Türkçe](https://img.shields.io/badge/T%C3%BCrk%C3%A7e-2563eb)](README_tr.md) [![繁體中文](https://img.shields.io/badge/%E7%B9%81%E9%AB%94%E4%B8%AD%E6%96%87-2563eb)](README_zh-TW.md) [![简体中文](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-2563eb)](README_zh-CN.md) [![Русский](https://img.shields.io/badge/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-2563eb)](README_ru.md)

</div>

<a id="introduction"></a>
## 🍌 はじめに

**投稿者が GPT-6.2 Sol によるものと説明しているコミュニティのデモを集めました。元の投稿では、各タスクの内容や結果を確認できます。**

<a id="overview"></a>
## 📊 概要

- **123 件のユースケース · GPT-6.2 Sol**. 元の投稿を123件収録しています。121件は成果を示し、2件は未完了の試行を記録しています。15件では原文のプロンプトを確認できます。
- 3D シーンとモデリング · クリエイティブなグラフィックとアニメーション · ウェブサイトとインターフェース · ゲーム開発 · パソコンの使用と絵を描くこと · コンピュータの使用とコミュニケーション
- 各事例には、元の投稿、投稿者、日付、証拠の種類、確認できる結果を掲載しています。
- 利用可能な場合はパブリック プロンプトを使用します。結果を比較するときは、元の入力を保持します。

> [!NOTE]
> **クリップと静止画には出力が表示されます。モデル ラベルは作成者に帰属され、基礎となるモデルのバージョンは未検証のままです。映像を共有するエントリは、メディア ファミリごとにデータ内にまとめて保存されます。**

<a id="quick-start"></a>
## ⚡ クイックスタート

1. メニューからタスクを選択します。
2. プレビューを開いてソース メディアを確認し、元の投稿を読んでコンテキストを確認します。
3. 利用可能な場合はパブリック プロンプトを使用します。結果を比較するときは、元の入力を保持します。

[OpenAI のモデル一覧を見る](https://developers.openai.com/api/docs/models)

<a id="menu"></a>
## 📑 メニュー

| ケース | カテゴリ | 見どころ | 種類 |
| --- | --- | --- | --- |
| [概要](#overview) | ナビゲーション | 概要 | — |
| [クイックスタート](#quick-start) | ナビゲーション | クイックスタート | — |
| [関連リポジトリ](#related-repositories) | ナビゲーション | 関連リポジトリ | — |
| [謝辞](#acknowledge) | ナビゲーション | 謝辞 | — |
| [ケース 2. 郊外の家とペリカンのスケッチ](#case-2) | [3D シーンとモデリング](#category-three) | レンダリングされたシーンとコンパクトな描画テストを組み合わせます。 | Demo |
| [ケース 5. 同じプロンプトの Three.js 帆船の比較](#case-5) | [3D シーンとモデリング](#category-three) | 2 つの出力が同じ船舶概要の詳細とインタラクションをどのように処理するかを比較します。 | Evaluation |
| [ケース 6. 山の谷を渡る赤い電車](#case-6) | [3D シーンとモデリング](#category-three) | 移動する車両と風景を共有シーンで比較します。 | Evaluation |
| [ケース 9. 廃墟となったコロッセオを 2 つのシーンで表現](#case-9) | [3D シーンとモデリング](#category-three) | 2 つの再構成でカメラのカバー範囲と建築の詳細を比較します。 | Evaluation |
| [ケース 15. AETHERIA 浮島は EnvolDev によって共有されます](#case-15) | [3D シーンとモデリング](#category-three) | 浮かぶ風景の中をカメラを追ってみましょう。 | Demo |
| [ケース 16. 以前の比較による紫色の毛皮で覆われたキャラクター](#case-16) | [3D シーンとモデリング](#category-three) | 同じポスト内のリファレンス出力から新しいキャラクター クリップを分離します。 | Demo |
| [ケース 18. 庭を運ぶ翼のある象](#case-18) | [3D シーンとモデリング](#category-three) | 単一の空想の前提を使用して、構成をさまざまな角度から検証します。 | Demo |
| [ケース 20. rubenssoto_ai が共有する Three.js ブラック ホールの比較](#case-20) | [3D シーンとモデリング](#category-three) | 同じブラック ホール シーンへの目に見えるアプローチを比較します。 | Evaluation |
| [ケース 21. スティルウォーターガーデンの比較](#case-21) | [3D シーンとモデリング](#category-three) | 共有の庭仕事における造園と水処理を比較してください。 | Evaluation |
| [ケース 24. 輝く降着円盤を持つブラックホール](#case-24) | [3D シーンとモデリング](#category-three) | シミュレーションのカメラ ビュー、パーティクル、ライティングを検査します。 | Demo |
| [ケース 26. 星が爆発して超新星になる](#case-26) | [3D シーンとモデリング](#category-three) | 最初の星から衝撃波までの視覚効果を追跡します。 | Demo |
| [ケース 27. 海の波と夕暮れの灯台](#case-27) | [3D シーンとモデリング](#category-three) | 海のシーン全体で光と色がどのように変化するかを比較してください。 | Demo |
| [ケース 28. ブラウザ竜巻シミュレーション](#case-28) | [3D シーンとモデリング](#category-three) | シーンが回転、雲、地面の破片をどのように組み合わせているかを調べます。 | Demo |
| [ケース 33. 赤い橋が架かる竹林の聖域](#case-33) | [3D シーンとモデリング](#category-three) | 複数のカメラ アングルを使用して、レイヤー化された 3D シーンを調べます。 | Demo |
| [ケース 34. 歩きやすいThree.jsの波の絵](#case-34) | [3D シーンとモデリング](#category-three) | 絵画がナビゲート可能なシーンになると何が変わるかを調べてください。 | Demo |
| [ケース 37. Blenderでモデル化されたモンスターハウス](#case-37) | [3D シーンとモデリング](#category-three) | 3 つのラベル付き Blender ビューのジオメトリとシルエットを比較します。 | Evaluation |
| [ケース 38. karanC_12 が共有する Three.js 帆船](#case-38) | [3D シーンとモデリング](#category-three) | 再投稿に従って、ブラウザ シーン用に建造された船を確認してください。 | Demo |
| [ケース 39. AETHERIA 浮遊島 by Mr_Salio](#case-39) | [3D シーンとモデリング](#category-three) | カメラのフライスルーを使用して、シーンのスケールと深さを調べます。 | Demo |
| [ケース 40. 1 つの HTML ファイル内のインタラクティブな帆船](#case-40) | [3D シーンとモデリング](#category-three) | リギング、セイル、移動視点を使用してブラウザ モデルを検査します。 | Demo |
| [ケース 42. 五軒の庭ボクセル中庭](#case-42) | [3D シーンとモデリング](#category-three) | コンパクトなボクセル環境で構成とレイヤリングを検査します。 | Demo |
| [ケース 44. VraserX が共有する Three.js ブラック ホールの比較](#case-44) | [3D シーンとモデリング](#category-three) | 共有クリップ内のペアのブラック ホール シーンを検査します。 | Evaluation |
| [ケース 45. jessexai_ が共有するさくら村の昼と夜のデモ](#case-45) | [3D シーンとモデリング](#category-three) | 昼と夜でシーンを切り替えた場合の効果を検証します。 | Demo |
| [ケース 47. 廃墟となったコロッセオの外観と内部](#case-47) | [3D シーンとモデリング](#category-three) | 建物内をカメラで追跡して、どの詳細が表示されるかを確認します。 | Demo |
| [ケース 48. TokenGremlin による Three.js ブラック ホールの比較](#case-48) | [3D シーンとモデリング](#category-three) | 2 つのブラック ホール出力でのカメラの動きと照明を比較します。 | Evaluation |
| [ケース 49. 桜の中庭とWonder Atlasプレビュー](#case-49) | [3D シーンとモデリング](#category-three) | 2 つの Web シーンがアーキテクチャと深さをどのように処理するかを調べます。 | Demo |
| [ケース 50. 再構築されたTesla Roadster](#case-50) | [3D シーンとモデリング](#category-three) | 馴染みのある車を形状やディテールの参考にしてください。 | Demo |
| [ケース 53. Haleeeemahh が共有するさくら村の昼と夜のデモ](#case-53) | [3D シーンとモデリング](#category-three) | 同じ村が昼間と暗闇でどのように読み取られるかを比較してください。 | Demo |
| [ケース 54. VraserX が共有するさくら村の昼と夜のデモ](#case-54) | [3D シーンとモデリング](#category-three) | ペアになった照明状態を使用して、単一の環境を検査します。 | Demo |
| [ケース 56. TokenGremlin によるさくら村の昼と夜のデモ](#case-56) | [3D シーンとモデリング](#category-three) | 照明の切り替えを使用して、2 つの州の 1 つの村を比較します。 | Demo |
| [ケース 57. 室内と空の景色を楽しめる家](#case-57) | [3D シーンとモデリング](#category-three) | 3D 建物が内部ビューと外部ビューにわたって一貫性を保っているかどうかを検査します。 | Demo |
| [ケース 58. 単一の HTML Three.js ブラック ホール](#case-58) | [3D シーンとモデリング](#category-three) | クリップと静止画を使用して、1 つのシーンが複数の視点をどのように処理するかを確認します。 | Demo |
| [ケース 59. 浮かぶThree.js宮殿](#case-59) | [3D シーンとモデリング](#category-three) | 吊り下げられた宮殿の規模と表現をさまざまな角度から観察します。 | Demo |
| [ケース 63. 機械式腕時計の分解表示](#case-63) | [3D シーンとモデリング](#category-three) | 文字盤を観察し、モデルが各層をどう分解して見せるか確認します。 | Demo |
| [ケース 64. 2つの仏塔シーンを比較](#case-64) | [3D シーンとモデリング](#category-three) | 仏塔、木々、水面の配置を2つの出力で比べます。 | Evaluation |
| [ケース 65. Three.jsで作った錦鯉の中庭](#case-65) | [3D シーンとモデリング](#category-three) | 錦鯉の動きを追い、水面の揺れや反射を観察します。 | Demo |
| [ケース 66. 駐車場を通過する竜巻](#case-66) | [3D シーンとモデリング](#category-three) | 嵐のシミュレーションで駐車場の破片がどう動くか確認します。 | Demo |
| [ケース 68. 操作できるボーイング787-9の模型](#case-68) | [3D シーンとモデリング](#category-three) | 表示を切り替えながら機体外部とエンジンを確認します。 | Demo |
| [ケース 70. VoxelBench 2での生成エラー](#case-70) | [3D シーンとモデリング](#category-three) | 描画結果を採点する前に、生成されたボクセル用コードが動作するか確かめる。 | Benchmark |
| [ケース 71. ゴッホ風の世界を描くガウシアンスプラッティング](#case-71) | [3D シーンとモデリング](#category-three) | 同じ構図を、移動できる2つのシーンがどう表現するか比べる。 | Evaluation |
| [ケース 72. 生成した背景を使った風船の家](#case-72) | [3D シーンとモデリング](#category-three) | Three.jsで背景を作る指定がある場合は、シーンの素材まで確認する。 | Limit |
| [ケース 73. HTMLで再現したルーブ・ゴールドバーグ装置](#case-73) | [3D シーンとモデリング](#category-three) | 連鎖反応で次の仕掛けにどう動きが伝わるかを見る。 | Demo |
| [ケース 76. 機械仕掛けのハチを並べて比較](#case-76) | [3D シーンとモデリング](#category-three) | 可動部の仕上がりと操作画面の構成を別々に評価する。 | Evaluation |
| [ケース 81. 地図をもとにした歩行メカをThree.jsで描く](#case-81) | [3D シーンとモデリング](#category-three) | 同じ地図データと制作指示を使い、アニメーションを見比べる。 | Evaluation |
| [ケース 83. 参照画像からポートレートを再構成](#case-83) | [3D シーンとモデリング](#category-three) | ポーズ、衣装、シーンの形状を参照画像と見比べる。 | Evaluation |
| [ケース 84. 4つのモデルで作ったシカ](#case-84) | [3D シーンとモデリング](#category-three) | 角の形、関節、体の比率を並べて比較する。 | Evaluation |
| [ケース 85. 4モデルで作る「Alpine Gold」の航空機シーン](#case-85) | [3D シーンとモデリング](#category-three) | 同じ航空機の制作指示で、形状、舞台設定、制作時間を比較する。 | Evaluation |
| [ケース 86. Solのバージョン別ボクセル出力一覧](#case-86) | [3D シーンとモデリング](#category-three) | 評価セット全体を判断する前に、各プロンプトで品質が落ちた例を探す。 | Evaluation |
| [ケース 87. 2つのコーディングツールで作った浮遊ボクセル王国](#case-87) | [3D シーンとモデリング](#category-three) | ボクセルのシーンを比較する際は、使ったツールと実際の経過時間を記録する。 | Evaluation |
| [ケース 89. 2通りの表現で描いた灯台](#case-89) | [3D シーンとモデリング](#category-three) | 同じ制作指示で、構図と描画スタイルがどう変わるかを比較する。 | Evaluation |
| [ケース 90. 最大の推論強度で描いたコントローラー](#case-90) | [3D シーンとモデリング](#category-three) | 同じ制作指示で、ボタンの配置と筐体の形状を比較する。 | Evaluation |
| [ケース 91. 動きが異なる4つの風船付きの家](#case-91) | [3D シーンとモデリング](#category-three) | 風船に対して家がどのように動くかを見る。 | Evaluation |
| [ケース 92. 映画『タイタニック』の一場面を3Dで再現](#case-92) | [3D シーンとモデリング](#category-three) | 各作例の顔の細部、人物や物の配置、カメラの構図を比較する。 | Evaluation |
| [ケース 96. 島々を中心に構成した海のシーン](#case-96) | [3D シーンとモデリング](#category-three) | 島の描き方を細かく指定せず、出力ごとの構図の選択を比較する。 | Demo |
| [ケース 102. 組み立てと分解の両方を見られるヘリコプター](#case-102) | [3D シーンとモデリング](#category-three) | 同じ3Dモデルを飛行時と部品を展開した状態で確認する。 | Demo |
| [ケース 104. 細部まで作り込んだ2つのBMWモデル](#case-104) | [3D シーンとモデリング](#category-three) | 同じ制作指示で、シルエット、素材の表現、カメラアングルを比較する。 | Evaluation |
| [ケース 105. 船と海面の表現を比較](#case-105) | [3D シーンとモデリング](#category-three) | 同じ制作指示で、船の航跡、水面の反射、シーンの反応を比べる。 | Evaluation |
| [ケース 106. 推論強度xhighで描いたエッフェル塔](#case-106) | [3D シーンとモデリング](#category-three) | 推論強度をそろえ、構造物本体と周囲のシーンを比較する。 | Evaluation |
| [ケース 107. 水面と照明を調整できる島](#case-107) | [3D シーンとモデリング](#category-three) | カメラを周囲に回しながら、水面の波紋や照明の操作を試す。 | Demo |
| [ケース 109. 同じトラック運転シーンを4回作り比べる](#case-109) | [3D シーンとモデリング](#category-three) | 使用したコーディングツールを記録しながら、同じ運転シーンを比較する。 | Evaluation |
| [ケース 111. Blenderで作った細部まで見える室内と街並み](#case-111) | [3D シーンとモデリング](#category-three) | 室内の小物と、窓の向こうに見える景色を確認する。 | Demo |
| [ケース 113. 2つのコーディングモデルで作ったPS5コントローラー](#case-113) | [3D シーンとモデリング](#category-three) | 正面に加え、背面の外装と側面のボタンも確認する。 | Evaluation |
| [ケース 115. 操作できる3種類の地球儀](#case-115) | [3D シーンとモデリング](#category-three) | 地球儀を回しながら、照明とインターフェースの動きを比較する。 | Evaluation |
| [ケース 116. ブラックホールのそばで自転車に乗るペリカン](#case-116) | [3D シーンとモデリング](#category-three) | 複数回のプロンプト入力を経て、シーンがどう変化したかを確認する。 | Demo |
| [ケース 117. 貨物コンテナを中心に据えた2つの3Dシーン](#case-117) | [3D シーンとモデリング](#category-three) | 照明、小物、表面の質感の表現を比較する。 | Evaluation |
| [ケース 121. Three.jsで描く湖畔](#case-121) | [3D シーンとモデリング](#category-three) | カメラがボートや滝のそばを通る様子を追い、シーンの細部を確認する。 | Demo |
| [ケース 122. 人間が採点したインタラクティブな3Dシーン](#case-122) | [3D シーンとモデリング](#category-three) | インタラクティブなモデリングを比較する際は、評価セットと採点方法をそろえる。 | Benchmark |
| [ケース 3. 3D で見る人類の歴史と AI の未来](#case-3) | [クリエイティブなグラフィックとアニメーション](#category-graphics) | 物語の概要を一連のアニメーション シーンに変換します。 | Demo |
| [ケース 8. ブラウザペイントスタジオのTiboポートレート](#case-8) | [クリエイティブなグラフィックとアニメーション](#category-graphics) | ページがポートレートを構築する際に、ポートレートの段階を検査します。 | Demo |
| [ケース 10. 0x0SojalSec が共有する Sam Altman の肖像画](#case-10) | [クリエイティブなグラフィックとアニメーション](#category-graphics) | 大まかな形状から完成したポートレートへの移行を追跡します。 | Demo |
| [ケース 11. Avenoxai が共有する Sam Altman の肖像画](#case-11) | [クリエイティブなグラフィックとアニメーション](#category-graphics) | ブラウザーのデモンストレーションでポートレートがどのように作成されるかをご覧ください。 | Demo |
| [ケース 12. pengsonal が共有する Sam Altman の肖像画](#case-12) | [クリエイティブなグラフィックとアニメーション](#category-graphics) | ブラウザ シーンがポートレートのディテールを追加する順序を調べてください。 | Demo |
| [ケース 13. GeekCatX が共有する Sam Altman の肖像画](#case-13) | [クリエイティブなグラフィックとアニメーション](#category-graphics) | クリップを使用して、最初の構成と完成した画像を比較します。 | Demo |
| [ケース 14. ブラウザペイントキャンバス内のSam Altmanポートレート](#case-14) | [クリエイティブなグラフィックとアニメーション](#category-graphics) | ポートレートがブロックインされた色からより細かい特徴へと変化していく様子を観察してください。 | Demo |
| [ケース 19. ブラウザペイントキャンバス内のDario Amodeiポートレート](#case-19) | [クリエイティブなグラフィックとアニメーション](#category-graphics) | 舞台化されたポートレートのガイドとなる参考画像をご覧ください。 | Demo |
| [ケース 22. 4 つの SVG アニメーションと Opus 5.5 の比較](#case-22) | [クリエイティブなグラフィックとアニメーション](#category-graphics) | いくつかの SVG 被写体のモーションとディテールを比較します。 | Evaluation |
| [ケース 23. Ananth7e による別の Sam Altman 肖像画の投稿](#case-23) | [クリエイティブなグラフィックとアニメーション](#category-graphics) | 共有記録を使用して、ブラウザーのポートレートがどのように形作られるかを検査します。 | Demo |
| [ケース 25. コードのみの SVG として記述された 2 つのポートレート イラスト](#case-25) | [クリエイティブなグラフィックとアニメーション](#category-graphics) | どのように作成されたかを判断する前に、レンダリングされたポートレートを比較してください。 | Demo |
| [ケース 29. 月明かりに照らされたドット絵の日本の街](#case-29) | [クリエイティブなグラフィックとアニメーション](#category-graphics) | コンパクトなアニメーション シーンを使用して、照明と詳細を検査します。 | Demo |
| [ケース 30. BMXに乗りながらジャグリングするライオン](#case-30) | [クリエイティブなグラフィックとアニメーション](#category-graphics) | 変化する季節の背景に対して調整された動きをテストします。 | Demo |
| [ケース 31. 横から見た疾走する馬](#case-31) | [クリエイティブなグラフィックとアニメーション](#category-graphics) | 単純な動作サイクルを通じて脚と尾を検査します。 | Demo |
| [ケース 32. 竹の中をBMXに乗るクジャク](#case-32) | [クリエイティブなグラフィックとアニメーション](#category-graphics) | ホイールの動きと詳細なキャラクターの動きを比較してください。 | Demo |
| [ケース 35. フォトリアルなポートレートプレビュー](#case-35) | [クリエイティブなグラフィックとアニメーション](#category-graphics) | 目に見える結果を検査し、作成者がそれをどのように説明したかを記録します。 | Demo |
| [ケース 36. Sydney Sweeney ポートレートのベクトル化](#case-36) | [クリエイティブなグラフィックとアニメーション](#category-graphics) | ベクター ワークフローを評価するときに中間イメージを追跡します。 | Demo |
| [ケース 46. 横から見た走っているチーター](#case-46) | [クリエイティブなグラフィックとアニメーション](#category-graphics) | 固定プロファイル ビューを使用して、歩行と体の動きを比較します。 | Demo |
| [ケース 51. 自転車に乗るペリカンと2匹のカニ](#case-51) | [クリエイティブなグラフィックとアニメーション](#category-graphics) | 複数のアニメーション キャラクターのタイミングを 1 回のショットで検査します。 | Demo |
| [ケース 52. Sol 設定間の PS5 コントローラーの比較](#case-52) | [クリエイティブなグラフィックとアニメーション](#category-graphics) | 使い慣れた製品を使用して、輪郭と陰影を比較します。 | Evaluation |
| [ケース 55. 緑色のBMW M4 CSのプロフィールイラスト](#case-55) | [クリエイティブなグラフィックとアニメーション](#category-graphics) | 見慣れた車両でプロポーションやプロフィールのディテールを確認してください。 | Demo |
| [ケース 60. 孫悟空「大鬧天宮」のSVG比較](#case-60) | [クリエイティブなグラフィックとアニメーション](#category-graphics) | 同じ孫悟空の場面を3つのシステムがどう構成したか比べます。 | Evaluation |
| [ケース 74. コードで作った炎と音](#case-74) | [クリエイティブなグラフィックとアニメーション](#category-graphics) | モーション作品を比較するときは費用と生成時間に加えて映像の尺も記録する。 | Evaluation |
| [ケース 79. 15秒のモーションデザイン課題](#case-79) | [クリエイティブなグラフィックとアニメーション](#category-graphics) | 同じ課題を与え、文字組み、場面転換、動きの表現を比較する。 | Evaluation |
| [ケース 88. 2つのモデルが描いた疾走する馬](#case-88) | [クリエイティブなグラフィックとアニメーション](#category-graphics) | ループを一周させ、脚の運びと歩幅を見比べる。 | Evaluation |
| [ケース 94. コードで作った900フレームのアニメーション](#case-94) | [クリエイティブなグラフィックとアニメーション](#category-graphics) | キャラクター、動き、音が最終出力にどう反映されるかを確認する。 | Demo |
| [ケース 98. アニメーションになったバナナのイラスト](#case-98) | [クリエイティブなグラフィックとアニメーション](#category-graphics) | 身近な題材で、モデルが動きと登場人物をどう加えるかを確認する。 | Demo |
| [ケース 101. 単一HTMLファイルで描く自転車に乗ったペリカン](#case-101) | [クリエイティブなグラフィックとアニメーション](#category-graphics) | 同じSVGの制作指示で、鳥と自転車の動きを並べて確認する。 | Evaluation |
| [ケース 103. Ultraで生成した2本の棒人間アニメーション](#case-103) | [クリエイティブなグラフィックとアニメーション](#category-graphics) | 同じアニメーションの指示を繰り返し、実行ごとの差を確認する。 | Evaluation |
| [ケース 110. Sol、Opus、Qwenが描く雨の自転車配達](#case-110) | [クリエイティブなグラフィックとアニメーション](#category-graphics) | 3つの出力で、夜景と自転車の動きを比較する。 | Evaluation |
| [ケース 112. 雨の中を自転車で料理を配達するペリカン](#case-112) | [クリエイティブなグラフィックとアニメーション](#category-graphics) | 反射、水たまり、道路設備、動きのある背景を個別に確認する。 | Evaluation |
| [ケース 114. 日中に自転車に乗るペリカンの2つの作例](#case-114) | [クリエイティブなグラフィックとアニメーション](#category-graphics) | 動きの質と実行時間を併せて比較する。 | Evaluation |
| [ケース 118. SVGで動かす剣の決闘](#case-118) | [クリエイティブなグラフィックとアニメーション](#category-graphics) | 動きのタイミングとシルエットが、ベクターアニメーションの動きにどう説得力を与えるかを見る。 | Demo |
| [ケース 120. SVGで写真のような風景を描く](#case-120) | [クリエイティブなグラフィックとアニメーション](#category-graphics) | 自然の風景をベクターで描いたとき、どの細部が残るかを確認する。 | Demo |
| [ケース 123. 推論強度別のペリカンSVG](#case-123) | [クリエイティブなグラフィックとアニメーション](#category-graphics) | 推論強度ごとに、ペダル、足、車体フレームの位置関係を確認する。 | Evaluation |
| [ケース 4. 時間の終わりのインタラクティブ ブラック ホール](#case-4) | [ウェブサイトとインターフェース](#category-web) | インタラクティブな Three.js ページの焦点としてブラック ホールを使用します。 | Demo |
| [ケース 7. Island Atlas 昼夜切り替え付き](#case-7) | [ウェブサイトとインターフェース](#category-web) | コンパクトな 3D アイランドを使用して、Web インターフェイスで照明状態をテストします。 | Demo |
| [ケース 41. Codex および API での参照イメージのテスト](#case-41) | [ウェブサイトとインターフェース](#category-web) | 違いを特定する前に、同じリファレンスを使用して 2 つの出力が何を行うかを比較してください。 | Evaluation |
| [ケース 61. 回転する七角形の中の重力ボール](#case-61) | [ウェブサイトとインターフェース](#category-web) | 容器が回転するとボールがどう動くか確認します。 | Demo |
| [ケース 69. ブガッティ・シロンの360度コンフィギュレーター](#case-69) | [ウェブサイトとインターフェース](#category-web) | カメラが車の周りを移動する様子を見ながら、塗装の仕上がりを比べます。 | Demo |
| [ケース 75. ブラウザー操作でGeoGuessrの場所を特定](#case-75) | [ウェブサイトとインターフェース](#category-web) | モデル間で開始地点、制限時間、距離の基準をそろえる。 | Benchmark |
| [ケース 77. Blenderのモデルを使ったチョウの展示サイト](#case-77) | [ウェブサイトとインターフェース](#category-web) | 回転できる標本に拡大表示と観察情報を組み合わせる。 | Demo |
| [ケース 80. Browser Useのタスク達成率と操作ステップ数](#case-80) | [ウェブサイトとインターフェース](#category-web) | 同じブラウザー評価セットで、達成率、所要時間、操作ステップ数を比較する。 | Benchmark |
| [ケース 82. Perplexityのエージェント評価「WANDR」](#case-82) | [ウェブサイトとインターフェース](#category-web) | タスクのスコアと1件あたりの費用を併せて比較する。 | Benchmark |
| [ケース 108. Wikipediaの50ページから指定記事にたどり着く](#case-108) | [ウェブサイトとインターフェース](#category-web) | 移動時間を計測する際は、到達先と開始ページを固定する。 | Benchmark |
| [ケース 119. エージェントのセッションを管理するかんばんプラグイン](#case-119) | [ウェブサイトとインターフェース](#category-web) | タスク、セッション、レビュー待ちの項目が画面上でどう結び付くかを確認する。 | Integration |
| [ケース 17. PELICAN PANIC ボクセルチェイスゲーム](#case-17) | [ゲーム開発](#category-game) | 短い追跡ゲームを使用して、コントロール、フィードバック、および終了状態を検査します。 | Demo |
| [ケース 62. ブラウザーで動くルービックキューブ](#case-62) | [ゲーム開発](#category-game) | プレビューでキューブの回転とステッカーの配置を確認します。 | Demo |
| [ケース 67. 海岸沿いのレースゲームの試作](#case-67) | [ゲーム開発](#category-game) | レース中にカウントダウン、速度表示、コースマップが読み取りやすいか確認します。 | Demo |
| [ケース 78. 倉庫番の問題セットを全問クリア](#case-78) | [ゲーム開発](#category-game) | クリアした部屋数を記録し、手順を再生して行き詰まる場面を確認する。 | Benchmark |
| [ケース 93. RuneScapeで2つのクエストを攻略](#case-93) | [ゲーム開発](#category-game) | エージェントが選んだクエストと受け取った報酬を確認する。 | Benchmark |
| [ケース 95. タッチ操作に対応したマルチプレイヤーのブラウザーゲーム](#case-95) | [ゲーム開発](#category-game) | 各ビルドをプレイし、操作の改善点を具体的に伝える。 | Demo |
| [ケース 97. 村づくりのブラウザーゲーム「Lanternkeep」](#case-97) | [ゲーム開発](#category-game) | マップと目標パネルが村づくりの流れをどう支えるかを見る。 | Demo |
| [ケース 99. スクリーンショットだけで『ポケットモンスター ファイアレッド』を進める](#case-99) | [ゲーム開発](#category-game) | ゲームを操作するエージェントの到達点とクリア時間を記録する。 | Benchmark |
| [ケース 1. Freddie Mercury の MS Paint](#case-1) | [パソコンの使用と絵を描くこと](#category-painting) | ポートレートを使用して、デスクトップ描画の試行によって何が生成されるかを検査します。 | Demo |
| [ケース 100. ブラウザー上のお絵描きキャンバスに描いた肖像](#case-100) | [パソコンの使用と絵を描くこと](#category-painting) | 描画途中のフレームを、キャンバス横に表示された参照画像と見比べる。 | Demo |
| [ケース 43. メッセージを中継する未完了の試み](#case-43) | [コンピュータの使用とコミュニケーション](#category-communication) | この試みを使用して、デスクトップ ワークフローがどこで停止したかを確認します。 | Limit |

<a id="category-three"></a>
## 🧊 3D シーンとモデリング

<a id="case-2"></a>
### ケース 2: [郊外の家とペリカンのスケッチ](https://x.com/kimmonismus/status/2119543483048268179) (投稿者 [@kimmonismus](https://x.com/kimmonismus))

**レンダリングされたシーンとコンパクトな描画テストを組み合わせます。**

この投稿には、Three.js の家のジオラマとペリカンの絵が表示されています。著者はモデルの帰属を質問として表現しています。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-02/2119532455732391936-fa2a8f20e72b385fb876.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-02/2119532455732391936-fa2a8f20e72b385fb876.png" width="640" alt="ソースプレビュー 1 · 郊外の家とペリカンのスケッチ"></a>
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119532301629444096-59cbe92bb0ac66550f15.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-02/2119532301629444096-poster-3bee934f98dcb35913e6.jpg" width="640" alt="ソースプレビュー 2 · 郊外の家とペリカンのスケッチ"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119532301629444096-59cbe92bb0ac66550f15.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-02/2119532554088742912-0aa402b50c531d333c76.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-02/2119532554088742912-0aa402b50c531d333c76.jpg" width="640" alt="ソースプレビュー 3 · 郊外の家とペリカンのスケッチ"></a>

Type: Demo | Date: 2026-11-08

---

<a id="case-5"></a>
### ケース 5: [同じプロンプトの Three.js 帆船の比較](https://x.com/marcthecreatorr/status/2119503438405136765) (投稿者 [@marcthecreatorr](https://x.com/marcthecreatorr))

**2 つの出力が同じ船舶概要の詳細とインタラクションをどのように処理するかを比較します。**

このクリップでは 2 隻の帆船を比較しています。著者は、1 回の実行では 27 分と 3 ドル、もう 1 回の実行では 95 分と 16 ドルを報告しています。これらの数字は投稿から得られます。

**プロンプト:**

```
create an interactive sailing ship in three.js, make it detailed as possible:
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119502925797953536-f1e1d1b1900d66b4eb77.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-05/2119502925797953536-poster-116cd4a4d6e1cb5d973f.jpg" width="640" alt="ソースプレビュー 1 · 同じプロンプトの Three.js 帆船の比較"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119502925797953536-f1e1d1b1900d66b4eb77.mp4)


Type: Evaluation | Date: 2026-11-08

---

<a id="case-6"></a>
### ケース 6: [山の谷を渡る赤い電車](https://x.com/Bhavani_00007/status/2119503354405720140) (投稿者 [@Bhavani_00007](https://x.com/Bhavani_00007))

**移動する車両と風景を共有シーンで比較します。**

ラベル付きの 2 つの出力は、緑の谷を通る高架線を走行する赤い列車を示しています。ソースでは、結果に Sol 6.2 および Opus 5.5 というラベルが付けられます。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119503068949856256-bca1ef454e3e673e2bce.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-06/2119503068949856256-poster-aa72e097b1fd4a84966f.jpg" width="640" alt="ソースプレビュー 1 · 山の谷を渡る赤い電車"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119503068949856256-bca1ef454e3e673e2bce.mp4)


Type: Evaluation | Date: 2026-11-08

---

<a id="case-9"></a>
### ケース 9: [廃墟となったコロッセオを 2 つのシーンで表現](https://x.com/aGim_asf/status/2119498787282436207) (投稿者 [@aGim_asf](https://x.com/aGim_asf))

**2 つの再構成でカメラのカバー範囲と建築の詳細を比較します。**

このクリップは、Sol routed というラベルの付いた結果と、Opus 5.5 というラベルの付いた結果を組み合わせています。サンプルビューには外観、俯瞰、夜景などが含まれます。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119498709633220608-26722fac9106b56240f3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-09/2119498709633220608-poster-8243d0e74884908136c0.jpg" width="640" alt="ソースプレビュー 1 · 廃墟となったコロッセオを 2 つのシーンで表現"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119498709633220608-26722fac9106b56240f3.mp4)


Type: Evaluation | Date: 2026-11-08

---

<a id="case-15"></a>
### ケース 15: [AETHERIA 浮島は EnvolDev によって共有されます](https://x.com/EnvolDev/status/2119482078341591479) (投稿者 [@EnvolDev](https://x.com/EnvolDev))

**浮かぶ風景の中をカメラを追ってみましょう。**

クリップは島、滝、寺院の間を移動してから、エンド タイトルが表示されます。これは、コレクションの他のエントリに示されている AETHERIA 映像と一致します。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119437684120707072-bd2ec92a5b611ac8fbd3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-15/2119437684120707072-poster-633f997463e30650c978.jpg" width="640" alt="ソースプレビュー 1 · AETHERIA 浮島は EnvolDev によって共有されます"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119437684120707072-bd2ec92a5b611ac8fbd3.mp4)


Type: Demo | Date: 2026-11-08

---

<a id="case-16"></a>
### ケース 16: [以前の比較による紫色の毛皮で覆われたキャラクター](https://x.com/xbquan/status/2119479402052657395) (投稿者 [@xbquan](https://x.com/xbquan))

**同じポスト内のリファレンス出力から新しいキャラクター クリップを分離します。**

ビデオでは紫色のキャラクターが回転する様子が見られます。 2 つの静止画像には Opus 5.5 および GPT-6.1 Sol というラベルが付けられており、以前の比較に属しています。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119478886493040640-b74d054d9845c14539a7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-16/2119478886493040640-poster-311533a33c0d7347ebba.jpg" width="640" alt="ソースプレビュー 1 · 以前の比較による紫色の毛皮で覆われたキャラクター"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119478886493040640-b74d054d9845c14539a7.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-16/2119479019515396096-43ac0320808f9c27b0e1.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-16/2119479019515396096-43ac0320808f9c27b0e1.png" width="640" alt="ソースプレビュー 2 · 以前の比較による紫色の毛皮で覆われたキャラクター"></a>
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-16/2119479313682837504-7663aa353ea789acf78d.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-16/2119479313682837504-7663aa353ea789acf78d.png" width="640" alt="ソースプレビュー 3 · 以前の比較による紫色の毛皮で覆われたキャラクター"></a>

Type: Demo | Date: 2026-11-08

---

<a id="case-18"></a>
### ケース 18: [庭を運ぶ翼のある象](https://x.com/SahilPanhotra/status/2119478318949126549) (投稿者 [@SahilPanhotra](https://x.com/SahilPanhotra))

**単一の空想の前提を使用して、構成をさまざまな角度から検証します。**

このシーンには、滝と夕日のある雲の上の日本庭園を運ぶ金色の翼の象が描かれています。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119478210362830848-d6ea2866b74f766af2f6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-18/2119478210362830848-poster-b78507b1cfbff6fee052.jpg" width="640" alt="ソースプレビュー 1 · 庭を運ぶ翼のある象"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119478210362830848-d6ea2866b74f766af2f6.mp4)


Type: Demo | Date: 2026-11-08

---

<a id="case-20"></a>
### ケース 20: [rubenssoto_ai が共有する Three.js ブラック ホールの比較](https://x.com/rubenssoto_ai/status/2119473734109237340) (投稿者 [@rubenssoto_ai](https://x.com/rubenssoto_ai))

**同じブラック ホール シーンへの目に見えるアプローチを比較します。**

再投稿では、Three.js ブラック ホールの比較と Opus の結果を共有しています。同じ内容が他のエントリーにも登場します。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119423566944854016-8c4caf17341d8a78d874.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-20/2119423566944854016-poster-f1b3ec251b11ad98c812.jpg" width="640" alt="ソースプレビュー 1 · rubenssoto_ai が共有する Three.js ブラック ホールの比較"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119423566944854016-8c4caf17341d8a78d874.mp4)


Type: Evaluation | Date: 2026-11-08

---

<a id="case-21"></a>
### ケース 21: [スティルウォーターガーデンの比較](https://x.com/vikktorrrre/status/2119473712751649201) (投稿者 [@vikktorrrre](https://x.com/vikktorrrre))

**共有の庭仕事における造園と水処理を比較してください。**

著者は、池の庭での 2 つのテイクを示し、それぞれの実行で 20 分で 9 ドルだったのに対し、1 時間で 20 ドルだったと報告しています。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119473584762396672-106a151b52cb169e2c2c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-21/2119473584762396672-poster-7a0d4ba33d4950366036.jpg" width="640" alt="ソースプレビュー 1 · スティルウォーターガーデンの比較"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119473584762396672-106a151b52cb169e2c2c.mp4)


Type: Evaluation | Date: 2026-11-08

---

<a id="case-24"></a>
### ケース 24: [輝く降着円盤を持つブラックホール](https://x.com/pankajkumar_dev/status/2119469657291997366) (投稿者 [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**シミュレーションのカメラ ビュー、パーティクル、ライティングを検査します。**

このクリップには、ブラック ホールとその発光円盤がいくつかの角度から示されています。著者はコードを説明し、外部アセットを使用していないと言っています。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119468024617160704-bfc0fbb47f7d3c7694cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-24/2119468024617160704-poster-9ac25331c401e957fc81.jpg" width="640" alt="ソースプレビュー 1 · 輝く降着円盤を持つブラックホール"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119468024617160704-bfc0fbb47f7d3c7694cf.mp4)


Type: Demo | Date: 2026-11-08

---

<a id="case-26"></a>
### ケース 26: [星が爆発して超新星になる](https://x.com/pankajkumar_dev/status/2119465155109196254) (投稿者 [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**最初の星から衝撃波までの視覚効果を追跡します。**

このクリップには、輝く星、赤と青のプラズマ、拡大する衝撃波が示されています。シミュレーションの様子をキャプチャします。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119464782411780096-387c3d42a21af2cb937f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-26/2119464782411780096-poster-83e58d5fd87089919ef5.jpg" width="640" alt="ソースプレビュー 1 · 星が爆発して超新星になる"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119464782411780096-387c3d42a21af2cb937f.mp4)


Type: Demo | Date: 2026-11-08

---

<a id="case-27"></a>
### ケース 27: [海の波と夕暮れの灯台](https://x.com/Mr_Salio/status/2119464940964593751) (投稿者 [@Mr_Salio](https://x.com/Mr_Salio))

**海のシーン全体で光と色がどのように変化するかを比較してください。**

このクリップには、波、月明かりの下の灯台、夕日のパレットが表示されます。原文では音についても説明されています。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119464564764913664-797c1ea0854763829f67.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-27/2119464564764913664-poster-79cdd1e25017c48eb939.jpg" width="640" alt="ソースプレビュー 1 · 海の波と夕暮れの灯台"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119464564764913664-797c1ea0854763829f67.mp4)


Type: Demo | Date: 2026-11-08

---

<a id="case-28"></a>
### ケース 28: [ブラウザ竜巻シミュレーション](https://x.com/Cayden970207/status/2119464819229344113) (投稿者 [@Cayden970207](https://x.com/Cayden970207))

**シーンが回転、雲、地面の破片をどのように組み合わせているかを調べます。**

このクリップでは、竜巻をいくつかの角度から示しています。著者は 22 分間の実行を報告し、短いプロンプトを提供します。

**プロンプト:**

```
生成一个画面非常逼真的龙卷风 ，要在threejs 场景里面可以互动
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119464225299152896-e1c4fd72c33b93d86e9f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-28/2119464225299152896-poster-ce3fad26759899389fec.jpg" width="640" alt="ソースプレビュー 1 · ブラウザ竜巻シミュレーション"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119464225299152896-e1c4fd72c33b93d86e9f.mp4)


Type: Demo | Date: 2026-11-08

---

<a id="case-33"></a>
### ケース 33: [赤い橋が架かる竹林の聖域](https://x.com/HarshithLucky3/status/2119453449423323141) (投稿者 [@HarshithLucky3](https://x.com/HarshithLucky3))

**複数のカメラ アングルを使用して、レイヤー化された 3D シーンを調べます。**

このクリップには、パビリオン、赤い橋、岩、花、滝が表示されています。ソースにはそのプロンプトが含​​まれています。

**プロンプト:**

```
Bamboo sanctuary in the middle of beautiful forest using three js
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119453077665423360-a208c63131dd89043dd8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-33/2119453077665423360-poster-1711535c6895a7010577.jpg" width="640" alt="ソースプレビュー 1 · 赤い橋が架かる竹林の聖域"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119453077665423360-a208c63131dd89043dd8.mp4)


Type: Demo | Date: 2026-11-08

---

<a id="case-34"></a>
### ケース 34: [歩きやすいThree.jsの波の絵](https://x.com/TokenGremlin/status/2119443826674749609) (投稿者 [@TokenGremlin](https://x.com/TokenGremlin))

**絵画がナビゲート可能なシーンになると何が変わるかを調べてください。**

この投稿では、カメラが移動できるシーンと参照画像を組み合わせています。著者は、これを外部アセットのない単一の HTML ファイルとして説明しています。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119443779702628352-c8ae18612dedfbd4291a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-34/2119443779702628352-poster-7c67dab031b1f7e6770a.jpg" width="640" alt="ソースプレビュー 1 · 歩きやすいThree.jsの波の絵"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119443779702628352-c8ae18612dedfbd4291a.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-34/2119443814934851584-c1bc6009a5d9a1dd22c7.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-34/2119443814934851584-c1bc6009a5d9a1dd22c7.jpg" width="640" alt="ソースプレビュー 2 · 歩きやすいThree.jsの波の絵"></a>

Type: Demo | Date: 2026-11-08

---

<a id="case-37"></a>
### ケース 37: [Blenderでモデル化されたモンスターハウス](https://x.com/maxt3chno/status/2119440388876321209) (投稿者 [@maxt3chno](https://x.com/maxt3chno))

**3 つのラベル付き Blender ビューのジオメトリとシルエットを比較します。**

パネルには、Astra、「routed GPT Sol 6.2」、および Opus 5.5 というラベルが付いています。モンスターハウスをさまざまな角度から紹介します。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119439156862472192-769177330371f94ec66f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-37/2119439156862472192-poster-60c3b1403ff3d2354053.jpg" width="640" alt="ソースプレビュー 1 · Blenderでモデル化されたモンスターハウス"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119439156862472192-769177330371f94ec66f.mp4)


Type: Evaluation | Date: 2026-11-08

---

<a id="case-38"></a>
### ケース 38: [karanC_12 が共有する Three.js 帆船](https://x.com/karanC_12/status/2119438098438504502) (投稿者 [@karanC_12](https://x.com/karanC_12))

**再投稿に従って、ブラウザ シーン用に建造された船を確認してください。**

この投稿では、著者のオリジナルのデモンストレーションと同じ帆船の素材からの映像が共有されています。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119436763835854848-c880c3e4797b29bb5bc2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-38/2119436763835854848-poster-426019e1b44be6bbbaf8.jpg" width="640" alt="ソースプレビュー 1 · karanC_12 が共有する Three.js 帆船"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119436763835854848-c880c3e4797b29bb5bc2.mp4)


Type: Demo | Date: 2026-11-08

---

<a id="case-39"></a>
### ケース 39: [AETHERIA 浮遊島 by Mr_Salio](https://x.com/Mr_Salio/status/2119437812604838342) (投稿者 [@Mr_Salio](https://x.com/Mr_Salio))

**カメラのフライスルーを使用して、シーンのスケールと深さを調べます。**

このクリップには、雲、浮島、寺院、滝が示されています。 EnvolDev の投稿では、一致する映像が共有されています。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119437684120707072-bd2ec92a5b611ac8fbd3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-39/2119437684120707072-poster-633f997463e30650c978.jpg" width="640" alt="ソースプレビュー 1 · AETHERIA 浮遊島 by Mr_Salio"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119437684120707072-bd2ec92a5b611ac8fbd3.mp4)


Type: Demo | Date: 2026-11-08

---

<a id="case-40"></a>
### ケース 40: [1 つの HTML ファイル内のインタラクティブな帆船](https://x.com/marcthecreatorr/status/2119437126194335764) (投稿者 [@marcthecreatorr](https://x.com/marcthecreatorr))

**リギング、セイル、移動視点を使用してブラウザ モデルを検査します。**

著者は詳細な Three.js 船を提示し、それを 1 つの HTML ファイルとして説明します。コレクション内の別の投稿でも同じ映像が共有されています。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119436763835854848-c880c3e4797b29bb5bc2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-40/2119436763835854848-poster-426019e1b44be6bbbaf8.jpg" width="640" alt="ソースプレビュー 1 · 1 つの HTML ファイル内のインタラクティブな帆船"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119436763835854848-c880c3e4797b29bb5bc2.mp4)


Type: Demo | Date: 2026-11-08

---

<a id="case-42"></a>
### ケース 42: [五軒の庭ボクセル中庭](https://x.com/kdnbmb/status/2119431894412476609) (投稿者 [@kdnbmb](https://x.com/kdnbmb))

**コンパクトなボクセル環境で構成とレイヤリングを検査します。**

スチールには、重塔、桜、太鼓橋、池が描かれています。泳ぐ魚について著者が解説しています。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-42/2119431646592069633-57818fd711183654054f.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-42/2119431646592069633-57818fd711183654054f.jpg" width="640" alt="ソースプレビュー 1 · 五軒の庭ボクセル中庭"></a>

Type: Demo | Date: 2026-11-08

---

<a id="case-44"></a>
### ケース 44: [VraserX が共有する Three.js ブラック ホールの比較](https://x.com/VraserX/status/2119424978747842791) (投稿者 [@VraserX](https://x.com/VraserX))

**共有クリップ内のペアのブラック ホール シーンを検査します。**

再投稿では、他のエントリーと同じ比較資料を共有しています。メディアは投稿で提示された 2 つの結果を示しています。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119423566944854016-8c4caf17341d8a78d874.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-44/2119423566944854016-poster-f1b3ec251b11ad98c812.jpg" width="640" alt="ソースプレビュー 1 · VraserX が共有する Three.js ブラック ホールの比較"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119423566944854016-8c4caf17341d8a78d874.mp4)


Type: Evaluation | Date: 2026-11-08

---

<a id="case-45"></a>
### ケース 45: [jessexai_ が共有するさくら村の昼と夜のデモ](https://x.com/jessexai_/status/2119424781367881920) (投稿者 [@jessexai_](https://x.com/jessexai_))

**昼と夜でシーンを切り替えた場合の効果を検証します。**

この投稿では、他のエントリに登場する Three.js 村の記録を共有しています。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119409755286384640-c9f151ea8d8c1145a64f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-45/2119409755286384640-poster-f4e8ce732e65c67f2e4c.jpg" width="640" alt="ソースプレビュー 1 · jessexai_ が共有するさくら村の昼と夜のデモ"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119409755286384640-c9f151ea8d8c1145a64f.mp4)


Type: Demo | Date: 2026-11-08

---

<a id="case-47"></a>
### ケース 47: [廃墟となったコロッセオの外観と内部](https://x.com/theaidesk_/status/2119424068298625344) (投稿者 [@theaidesk_](https://x.com/theaidesk_))

**建物内をカメラで追跡して、どの詳細が表示されるかを確認します。**

クリップは、外側、内側、およびオーバーヘッドアングルをカバーします。その構造は、比較動画の上段にある結果と一致します。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119424041870065664-5940ed4a62430aeee154.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-47/2119424041870065664-poster-fc51687c2ad9f59e9e63.jpg" width="640" alt="ソースプレビュー 1 · 廃墟となったコロッセオの外観と内部"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119424041870065664-5940ed4a62430aeee154.mp4)


Type: Demo | Date: 2026-11-08

---

<a id="case-48"></a>
### ケース 48: [TokenGremlin による Three.js ブラック ホールの比較](https://x.com/TokenGremlin/status/2119423600692166703) (投稿者 [@TokenGremlin](https://x.com/TokenGremlin))

**2 つのブラック ホール出力でのカメラの動きと照明を比較します。**

このクリップは、Three.js シーンと Opus の比較を組み合わせています。他のクリエイターがこの素材を別の投稿で共有しています。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119423566944854016-8c4caf17341d8a78d874.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-48/2119423566944854016-poster-f1b3ec251b11ad98c812.jpg" width="640" alt="ソースプレビュー 1 · TokenGremlin による Three.js ブラック ホールの比較"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119423566944854016-8c4caf17341d8a78d874.mp4)


Type: Evaluation | Date: 2026-11-08

---

<a id="case-49"></a>
### ケース 49: [桜の中庭とWonder Atlasプレビュー](https://x.com/kdnbmb/status/2119421877160456664) (投稿者 [@kdnbmb](https://x.com/kdnbmb))

**2 つの Web シーンがアーキテクチャと深さをどのように処理するかを調べます。**

一方の静止画は桜のボクセルの中庭を示しています。もう 1 つは、Wonder Atlas のペトラを示しています。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-49/2119421806884872192-b4a23bb6a9e591b16af5.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-49/2119421806884872192-b4a23bb6a9e591b16af5.jpg" width="640" alt="ソースプレビュー 1 · 桜の中庭とWonder Atlasプレビュー"></a>
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-49/2119421844998549504-3b77677048389bb1f0db.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-49/2119421844998549504-3b77677048389bb1f0db.jpg" width="640" alt="ソースプレビュー 2 · 桜の中庭とWonder Atlasプレビュー"></a>

Type: Demo | Date: 2026-11-08

---

<a id="case-50"></a>
### ケース 50: [再構築されたTesla Roadster](https://x.com/gadi_neelesh/status/2119421520040894709) (投稿者 [@gadi_neelesh](https://x.com/gadi_neelesh))

**馴染みのある車を形状やディテールの参考にしてください。**

クリップは再構成された Tesla Roadster を示しています。著者は、出力が GPT-6.1 Sol からのものであるかどうかを明らかにしません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119420776025862144-34cfb4f66073bab24c47.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-50/2119420776025862144-poster-740ec7cd066be6b76cd5.jpg" width="640" alt="ソースプレビュー 1 · 再構築されたTesla Roadster"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119420776025862144-34cfb4f66073bab24c47.mp4)


Type: Demo | Date: 2026-11-08

---

<a id="case-53"></a>
### ケース 53: [Haleeeemahh が共有するさくら村の昼と夜のデモ](https://x.com/Haleeeemahh/status/2119413889649746386) (投稿者 [@Haleeeemahh](https://x.com/Haleeeemahh))

**同じ村が昼間と暗闇でどのように読み取られるかを比較してください。**

この投稿では、Sakura マテリアル ファミリの Three.js 村の映像を共有しています。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119409755286384640-c9f151ea8d8c1145a64f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-53/2119409755286384640-poster-f4e8ce732e65c67f2e4c.jpg" width="640" alt="ソースプレビュー 1 · Haleeeemahh が共有するさくら村の昼と夜のデモ"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119409755286384640-c9f151ea8d8c1145a64f.mp4)


Type: Demo | Date: 2026-11-08

---

<a id="case-54"></a>
### ケース 54: [VraserX が共有するさくら村の昼と夜のデモ](https://x.com/VraserX/status/2119413032157843780) (投稿者 [@VraserX](https://x.com/VraserX))

**ペアになった照明状態を使用して、単一の環境を検査します。**

このクリップは、さくら村の映像を共有する別の投稿です。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119409755286384640-c9f151ea8d8c1145a64f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-54/2119409755286384640-poster-f4e8ce732e65c67f2e4c.jpg" width="640" alt="ソースプレビュー 1 · VraserX が共有するさくら村の昼と夜のデモ"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119409755286384640-c9f151ea8d8c1145a64f.mp4)


Type: Demo | Date: 2026-11-08

---

<a id="case-56"></a>
### ケース 56: [TokenGremlin によるさくら村の昼と夜のデモ](https://x.com/TokenGremlin/status/2119409785900552548) (投稿者 [@TokenGremlin](https://x.com/TokenGremlin))

**照明の切り替えを使用して、2 つの州の 1 つの村を比較します。**

録画には、昼と夜のThree.js村が表示されます。他のいくつかの投稿でも同じ映像が共有されています。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119409755286384640-c9f151ea8d8c1145a64f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-56/2119409755286384640-poster-f4e8ce732e65c67f2e4c.jpg" width="640" alt="ソースプレビュー 1 · TokenGremlin によるさくら村の昼と夜のデモ"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119409755286384640-c9f151ea8d8c1145a64f.mp4)


Type: Demo | Date: 2026-11-08

---

<a id="case-57"></a>
### ケース 57: [室内と空の景色を楽しめる家](https://x.com/SPAC89/status/2119404108675215871) (投稿者 [@SPAC89](https://x.com/SPAC89))

**3D 建物が内部ビューと外部ビューにわたって一貫性を保っているかどうかを検査します。**

添付ファイルには、家、リビング ルーム、ベッドルーム、テラス、および航空写真が表示されます。著者は、xhigh テストについてさまざまな評価を行っています。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119403044274114560-550bb6f548146e501c0d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-57/2119403044274114560-poster-d67aab45193acc82e42a.jpg" width="640" alt="ソースプレビュー 1 · 室内と空の景色を楽しめる家"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119403044274114560-550bb6f548146e501c0d.mp4)


Type: Demo | Date: 2026-11-08

---

<a id="case-58"></a>
### ケース 58: [単一の HTML Three.js ブラック ホール](https://x.com/TokenGremlin/status/2119395930805879165) (投稿者 [@TokenGremlin](https://x.com/TokenGremlin))

**クリップと静止画を使用して、1 つのシーンが複数の視点をどのように処理するかを確認します。**

著者は、結果を単一の HTML ファイルとして説明しています。この投稿では、レンダリングされたシーンとは異なる種類の証拠に関する知識調査も報告されています。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119394874591944704-eb5a8d946e5f40a8212d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-58/2119394874591944704-poster-604b07cc348c3f438afe.jpg" width="640" alt="ソースプレビュー 1 · 単一の HTML Three.js ブラック ホール"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119394874591944704-eb5a8d946e5f40a8212d.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-58/2119395920999497728-91692619ab6baecef6db.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-58/2119395920999497728-91692619ab6baecef6db.jpg" width="640" alt="ソースプレビュー 2 · 単一の HTML Three.js ブラック ホール"></a>
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-58/2119395925982355456-9154ce589ec778c4ee10.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-58/2119395925982355456-9154ce589ec778c4ee10.jpg" width="640" alt="ソースプレビュー 3 · 単一の HTML Three.js ブラック ホール"></a>

Type: Demo | Date: 2026-11-08

---

<a id="case-59"></a>
### ケース 59: [浮かぶThree.js宮殿](https://x.com/TokenGremlin/status/2119371334878744648) (投稿者 [@TokenGremlin](https://x.com/TokenGremlin))

**吊り下げられた宮殿の規模と表現をさまざまな角度から観察します。**

ソースには、Three.js シーンに浮かぶ宮殿が示されており、使用されたモデルについて推測されています。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119371292654653440-a83394c3789cf19b3193.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-59/2119371292654653440-poster-a972ea05e9def1fc1fe3.jpg" width="640" alt="ソースプレビュー 1 · 浮かぶThree.js宮殿"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119371292654653440-a83394c3789cf19b3193.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-59/2119371325634433025-5b751df2d6a45b82b403.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-59/2119371325634433025-5b751df2d6a45b82b403.jpg" width="640" alt="ソースプレビュー 2 · 浮かぶThree.js宮殿"></a>
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-59/2119371330516566016-b39d93dfe248ca1a9f0f.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-59/2119371330516566016-b39d93dfe248ca1a9f0f.jpg" width="640" alt="ソースプレビュー 3 · 浮かぶThree.js宮殿"></a>

Type: Demo | Date: 2026-11-08

---

<a id="case-63"></a>
### ケース 63: [機械式腕時計の分解表示](https://x.com/VeknQAQ/status/2119644781710303276) (投稿者 [@VeknQAQ](https://x.com/VeknQAQ))

**文字盤を観察し、モデルが各層をどう分解して見せるか確認します。**

動画は組み上がった腕時計から、文字盤と内部部品を離して並べた分解表示へ切り替わります。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119644705072046080-2e9ea2a58509a7177571.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-63/2119644705072046080-poster-ed92564c349b8e9d5637.jpg" width="640" alt="ソースプレビュー 1 · 機械式腕時計の分解表示"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119644705072046080-2e9ea2a58509a7177571.mp4)

Type: Demo | Date: 2026-11-09

---

<a id="case-64"></a>
### ケース 64: [2つの仏塔シーンを比較](https://x.com/Aurora0x3f/status/2119664137685045606) (投稿者 [@Aurora0x3f](https://x.com/Aurora0x3f))

**仏塔、木々、水面の配置を2つの出力で比べます。**

動画では上段が GPT-6.2 Sol、下段が Opus 5.5 と表示されています。投稿者は Opus 5.5 の結果を好みました。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119663168578637824-e1a40ebc49f22aacda95.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-64/2119663168578637824-poster-b2b794870967829859d6.jpg" width="640" alt="ソースプレビュー 1 · 2つの仏塔シーンを比較"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119663168578637824-e1a40ebc49f22aacda95.mp4)

Type: Evaluation | Date: 2026-11-09

---

<a id="case-65"></a>
### ケース 65: [Three.jsで作った錦鯉の中庭](https://x.com/SahilPanhotra/status/2119666543864782937) (投稿者 [@SahilPanhotra](https://x.com/SahilPanhotra))

**錦鯉の動きを追い、水面の揺れや反射を観察します。**

投稿者によると、中庭は Three.js を使い、1つの HTML ファイルで作られています。動画では、反射が変化する水面の下を錦鯉が石や葉のそばを泳いでいきます。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119648453227884544-bee45570bdf53daf5f45.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-65/2119648453227884544-poster-4425357fdd67709bd4fb.jpg" width="640" alt="ソースプレビュー 1 · Three.jsで作った錦鯉の中庭"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119648453227884544-bee45570bdf53daf5f45.mp4)

Type: Demo | Date: 2026-11-09

---

<a id="case-66"></a>
### ケース 66: [駐車場を通過する竜巻](https://x.com/bei351009016/status/2119668859796124087) (投稿者 [@bei351009016](https://x.com/bei351009016))

**嵐のシミュレーションで駐車場の破片がどう動くか確認します。**

動画では、ミニチュアの駐車場の上に竜巻が発生し、車や建物の上で破片が渦を巻きます。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119668021623201792-fe62c5ab6f21ecf5e155.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-66/2119668021623201792-poster-17a3e6466176103ddd18.jpg" width="640" alt="ソースプレビュー 1 · 駐車場を通過する竜巻"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119668021623201792-fe62c5ab6f21ecf5e155.mp4)

Type: Demo | Date: 2026-11-09

---

<a id="case-68"></a>
### ケース 68: [操作できるボーイング787-9の模型](https://x.com/iamtheQwen/status/2119687952213397549) (投稿者 [@iamtheQwen](https://x.com/iamtheQwen))

**表示を切り替えながら機体外部とエンジンを確認します。**

録画では、回転できる787-9、複数の表示角度、エンジン断面が確認できます。投稿者は降着装置の切り替えと気流のデモも挙げています。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119687852141551616-093a9713679a3d5eb80b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-68/2119687852141551616-poster-6fc1887412c7a1937b45.jpg" width="640" alt="ソースプレビュー 1 · 操作できるボーイング787-9の模型"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119687852141551616-093a9713679a3d5eb80b.mp4)

Type: Demo | Date: 2026-11-09

---

<a id="case-70"></a>
### ケース 70: [VoxelBench 2での生成エラー](https://x.com/voxelbench/status/2122778737959969177) (投稿者 [@voxelbench](https://x.com/voxelbench))

**描画結果を採点する前に、生成されたボクセル用コードが動作するか確かめる。**

VoxelBenchによると、このテストではGPT-6.2 Solで62件、GPT-6.2 Astraで19件のエラーが発生した。運営者は構文エラーや定義漏れなどを原因に挙げている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-70/2122777747541868545-95f3c71b7db391dfffcd.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-70/2122777747541868545-95f3c71b7db391dfffcd.jpg" width="640" alt="ソースプレビュー 1 · VoxelBench 2での生成エラー"></a>

Type: Benchmark | Date: 2026-11-17

---

<a id="case-71"></a>
### ケース 71: [ゴッホ風の世界を描くガウシアンスプラッティング](https://x.com/sshayahmet/status/2122778769597554693) (投稿者 [@sshayahmet](https://x.com/sshayahmet))

**同じ構図を、移動できる2つのシーンがどう表現するか比べる。**

作者はSolとOpus 5.5のシーンを並べて公開した。報告ではSolは約1時間で5.45ドル、Opusは53分で12.14ドルだった。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122778178783752192-8bc5b1a659aaf321bca3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-71/2122778178783752192-poster-0bc27584cc18b44c255a.jpg" width="640" alt="ソースプレビュー 1 · ゴッホ風の世界を描くガウシアンスプラッティング"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122778178783752192-8bc5b1a659aaf321bca3.mp4)

Type: Evaluation | Date: 2026-11-17

---

<a id="case-72"></a>
### ケース 72: [生成した背景を使った風船の家](https://x.com/TimJayas/status/2122780669973787008) (投稿者 [@TimJayas](https://x.com/TimJayas))

**Three.jsで背景を作る指定がある場合は、シーンの素材まで確認する。**

映像では風船で浮く家を複数の角度から確認できる。作者によると、Solは背景をコードで組まず、画像生成モデルで遠景を作った。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122779173106364417-ce071a2bea10e55854ce.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-72/2122779173106364417-poster-c3a6e52c7e7cc9a4c981.jpg" width="640" alt="ソースプレビュー 1 · 生成した背景を使った風船の家"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122779173106364417-ce071a2bea10e55854ce.mp4)

Type: Limit | Date: 2026-11-17

---

<a id="case-73"></a>
### ケース 73: [HTMLで再現したルーブ・ゴールドバーグ装置](https://x.com/lucian__03/status/2122782073102663874) (投稿者 [@lucian__03](https://x.com/lucian__03))

**連鎖反応で次の仕掛けにどう動きが伝わるかを見る。**

作者はGPT-6.2 SolをMaxで使い、指示は1回だったと報告した。映像には鋼球が通るレールや歯車、連続して倒れるドミノが映る。作者によると制作は約25分、費用は3.03ドルだった。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122772945982660608-a1e7d3419ebbeb4c61bb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-73/2122772945982660608-poster-c2517a3063d7ae324d03.jpg" width="640" alt="ソースプレビュー 1 · HTMLで再現したルーブ・ゴールドバーグ装置"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122772945982660608-a1e7d3419ebbeb4c61bb.mp4)

Type: Demo | Date: 2026-11-17

---

<a id="case-76"></a>
### ケース 76: [機械仕掛けのハチを並べて比較](https://x.com/thtbee_/status/2122810531669311645) (投稿者 [@thtbee_](https://x.com/thtbee_))

**可動部の仕上がりと操作画面の構成を別々に評価する。**

映像では2つの機械仕掛けのハチと操作画面を並べて確認できる。作者はAstraの部品配置を評価し、両方の画面にレイアウト上の課題があったと述べた。Solは43分で3.84ドルだったという。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122803167826219008-c7328affdb02e5aa7e77.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-76/2122803167826219008-poster-11682fb3b82ccdb1450c.jpg" width="640" alt="ソースプレビュー 1 · 機械仕掛けのハチを並べて比較"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122803167826219008-c7328affdb02e5aa7e77.mp4)

Type: Evaluation | Date: 2026-11-17

---

<a id="case-81"></a>
### ケース 81: [地図をもとにした歩行メカをThree.jsで描く](https://x.com/simonw/status/2122822310428279136) (投稿者 [@simonw](https://x.com/simonw))

**同じ地図データと制作指示を使い、アニメーションを見比べる。**

Simon Willisonは、CodexでUltraに設定して実行したAstraとSolの結果を公開した。どちらも地図からメカへの変形が弱いと評した。

**プロンプト:**

```
Make a three js animation where yonkers stands up as a big mech (cool stand up motion) and stomps around manhattan and queens and Brooklyn, use openstreetmap mapping data
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122822265545125888-d31b1b651b7e509c87fc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-81/2122822265545125888-poster-5c704da713fe7f81b82f.jpg" width="640" alt="ソースプレビュー 1 · 地図をもとにした歩行メカをThree.jsで描く"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122822265545125888-d31b1b651b7e509c87fc.mp4)

Type: Evaluation | Date: 2026-11-17

---

<a id="case-83"></a>
### ケース 83: [参照画像からポートレートを再構成](https://x.com/_3912657840/status/2122812216877678897) (投稿者 [@_3912657840](https://x.com/_3912657840))

**ポーズ、衣装、シーンの形状を参照画像と見比べる。**

作者は現行と以前のGPTモデルに、約5分で参照画像を再現するよう指示した。スクリーンショットには各出力に対応するモデル名が付いている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-83/2122811098290397184-49690f8f4b78dc6c7886.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-83/2122811098290397184-49690f8f4b78dc6c7886.jpg" width="640" alt="ソースプレビュー 1 · 参照画像からポートレートを再構成"></a>

Type: Evaluation | Date: 2026-11-17

---

<a id="case-84"></a>
### ケース 84: [4つのモデルで作ったシカ](https://x.com/fawnunwrap/status/2122809542660825292) (投稿者 [@fawnunwrap](https://x.com/fawnunwrap))

**角の形、関節、体の比率を並べて比較する。**

FawnBenchの比較画像には、Sol、Astra、Opus 5.5、Fable 5.2が生成したシカが並んでいる。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122809522817290242-e5a7a38336a7144f4dbd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-84/2122809522817290242-poster-06fd5d64cd46e327916c.jpg" width="640" alt="ソースプレビュー 1 · 4つのモデルで作ったシカ"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122809522817290242-e5a7a38336a7144f4dbd.mp4)

Type: Evaluation | Date: 2026-11-17

---

<a id="case-85"></a>
### ケース 85: [4モデルで作る「Alpine Gold」の航空機シーン](https://x.com/EnvolDev/status/2122803967272866254) (投稿者 [@EnvolDev](https://x.com/EnvolDev))

**同じ航空機の制作指示で、形状、舞台設定、制作時間を比較する。**

作者によると、Solの実行は30分47秒で、費用は2.07ドルだった。動画ではAstra、Fable 5.2、Opus 5.5の結果と比較している。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122801610845982720-2c969b11731feb423c11.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-85/2122801610845982720-poster-d154bd6f581c0cdf0622.jpg" width="640" alt="ソースプレビュー 1 · 4モデルで作る「Alpine Gold」の航空機シーン"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122801610845982720-2c969b11731feb423c11.mp4)

Type: Evaluation | Date: 2026-11-17

---

<a id="case-86"></a>
### ケース 86: [Solのバージョン別ボクセル出力一覧](https://x.com/Angaisb_/status/2122799122331640187) (投稿者 [@Angaisb_](https://x.com/Angaisb_))

**評価セット全体を判断する前に、各プロンプトで品質が落ちた例を探す。**

作者はボクセルで作ったオブジェクトを一覧で公開し、比較では改善した例よりも品質が落ちた例のほうが多かったと報告した。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-86/2122798589545959424-f20f1a56ed0ed66f03d5.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-86/2122798589545959424-f20f1a56ed0ed66f03d5.jpg" width="640" alt="ソースプレビュー 1 · Solのバージョン別ボクセル出力一覧"></a>

Type: Evaluation | Date: 2026-11-17

---

<a id="case-87"></a>
### ケース 87: [2つのコーディングツールで作った浮遊ボクセル王国](https://x.com/marcthecreatorr/status/2122797460087083359) (投稿者 [@marcthecreatorr](https://x.com/marcthecreatorr))

**ボクセルのシーンを比較する際は、使ったツールと実際の経過時間を記録する。**

作者は各実行で作った浮遊王国を公開した。Codex CLIのSolでは28分、Claude CodeのSonnet 5.5では35分かかったと報告した。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122797078279512065-dd7e34ef4e2498971541.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-87/2122797078279512065-poster-15dac2e27a87a1f97249.jpg" width="640" alt="ソースプレビュー 1 · 2つのコーディングツールで作った浮遊ボクセル王国"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122797078279512065-dd7e34ef4e2498971541.mp4)

Type: Evaluation | Date: 2026-11-17

---

<a id="case-89"></a>
### ケース 89: [2通りの表現で描いた灯台](https://x.com/Mr_Salio/status/2122790293095448948) (投稿者 [@Mr_Salio](https://x.com/Mr_Salio))

**同じ制作指示で、構図と描画スタイルがどう変わるかを比較する。**

作者によると、両モデルに同じプロンプトを渡した。モデル名付きの動画では、Solの映画風の海岸とAstraのローポリの島を見比べられる。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122790247327010816-1259306616718e0fb170.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-89/2122790247327010816-poster-ce5bbe0f800a308d5b1c.jpg" width="640" alt="ソースプレビュー 1 · 2通りの表現で描いた灯台"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122790247327010816-1259306616718e0fb170.mp4)

Type: Evaluation | Date: 2026-11-17

---

<a id="case-90"></a>
### ケース 90: [最大の推論強度で描いたコントローラー](https://x.com/notjazii/status/2122788824187371714) (投稿者 [@notjazii](https://x.com/notjazii))

**同じ制作指示で、ボタンの配置と筐体の形状を比較する。**

元の投稿にはSol、Astra、Opus 5.5で作ったコントローラー画像が、モデル名付きで掲載されている。作者によると、Solには9分かかり、費用は0.53ドルだった。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-90/2122788803912007680-dacabe773c79e522bd2c.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-90/2122788803912007680-dacabe773c79e522bd2c.jpg" width="640" alt="ソースプレビュー 1 · 最大の推論強度で描いたコントローラー"></a>

Type: Evaluation | Date: 2026-11-17

---

<a id="case-91"></a>
### ケース 91: [動きが異なる4つの風船付きの家](https://x.com/noclipepe/status/2122787081252753482) (投稿者 [@noclipepe](https://x.com/noclipepe))

**風船に対して家がどのように動くかを見る。**

作者は同じ課題から得た4つの出力を比較し、Sol版で家が揺れる点に注目した。Solの実行にかかった時間は10分52秒と報告している。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122784867914002432-8d00ba7c14ff79aae8d8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-91/2122784867914002432-poster-513d81113d03a86cb940.jpg" width="640" alt="ソースプレビュー 1 · 動きが異なる4つの風船付きの家"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122784867914002432-8d00ba7c14ff79aae8d8.mp4)

Type: Evaluation | Date: 2026-11-17

---

<a id="case-92"></a>
### ケース 92: [映画『タイタニック』の一場面を3Dで再現](https://x.com/Super_Nius/status/2122783736895013239) (投稿者 [@Super_Nius](https://x.com/Super_Nius))

**各作例の顔の細部、人物や物の配置、カメラの構図を比較する。**

作者は『タイタニック』の一場面を現行と以前のGPTモデルで作り比べ、Astra版で描かれた顔に注目した。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122782517963231232-01580fcc6b1aba4b397c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-92/2122782517963231232-poster-da2d1171d78bce30c474.jpg" width="640" alt="ソースプレビュー 1 · 映画『タイタニック』の一場面を3Dで再現"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122782517963231232-01580fcc6b1aba4b397c.mp4)

Type: Evaluation | Date: 2026-11-17

---

<a id="case-96"></a>
### ケース 96: [島々を中心に構成した海のシーン](https://x.com/kdnbmb/status/2122770348974150021) (投稿者 [@kdnbmb](https://x.com/kdnbmb))

**島の描き方を細かく指定せず、出力ごとの構図の選択を比較する。**

作者は添付のレンダリングがSolの結果だと説明した。並行して実行していたAstraは、その時点ではまだ処理中だったという。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-96/2122770338882678784-3685e75d3c25d27356e3.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-96/2122770338882678784-3685e75d3c25d27356e3.jpg" width="640" alt="ソースプレビュー 1 · 島々を中心に構成した海のシーン"></a>

Type: Demo | Date: 2026-11-17

---

<a id="case-102"></a>
### ケース 102: [組み立てと分解の両方を見られるヘリコプター](https://x.com/CodeByNZ/status/2122760051454562368) (投稿者 [@CodeByNZ](https://x.com/CodeByNZ))

**同じ3Dモデルを飛行時と部品を展開した状態で確認する。**

作者によると、Solでの制作時間は7分だった。動画にはヘリコプターの飛行と、部品の配置を示す分解図が収められている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122759643076149248-ab3c69be40939668496f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-102/2122759643076149248-poster-a400c88eda4d8bad52e1.jpg" width="640" alt="ソースプレビュー 1 · 組み立てと分解の両方を見られるヘリコプター"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122759643076149248-ab3c69be40939668496f.mp4)

Type: Demo | Date: 2026-11-17

---

<a id="case-104"></a>
### ケース 104: [細部まで作り込んだ2つのBMWモデル](https://x.com/RezAIT00/status/2122759334782226869) (投稿者 [@RezAIT00](https://x.com/RezAIT00))

**同じ制作指示で、シルエット、素材の表現、カメラアングルを比較する。**

作者はSolとAstraが生成した精細なBMWを見せ、Astraの結果をわずかに好んだ。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122759152346726401-3f101f403955d33ccfa0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-104/2122759152346726401-poster-ffd8fecbdde8686dcd4e.jpg" width="640" alt="ソースプレビュー 1 · 細部まで作り込んだ2つのBMWモデル"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122759152346726401-3f101f403955d33ccfa0.mp4)

Type: Evaluation | Date: 2026-11-17

---

<a id="case-105"></a>
### ケース 105: [船と海面の表現を比較](https://x.com/LuminaBench/status/2122758425520029886) (投稿者 [@LuminaBench](https://x.com/LuminaBench))

**同じ制作指示で、船の航跡、水面の反射、シーンの反応を比べる。**

モデル名付きの比較映像にはSol 6.2とSol 6.1がAstraおよびOpusと並ぶ。テスト担当者は、この課題ではSol 6.1より改善したと報告した。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122758142068969472-316188886f8375c689ce.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-105/2122758142068969472-poster-5b7355ad9d812079fe16.jpg" width="640" alt="ソースプレビュー 1 · 船と海面の表現を比較"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122758142068969472-316188886f8375c689ce.mp4)

Type: Evaluation | Date: 2026-11-17

---

<a id="case-106"></a>
### ケース 106: [推論強度xhighで描いたエッフェル塔](https://x.com/RezAIT00/status/2122758069784621228) (投稿者 [@RezAIT00](https://x.com/RezAIT00))

**推論強度をそろえ、構造物本体と周囲のシーンを比較する。**

作者はSolとAstraで作ったとして、エッフェル塔の出力を公開した。どちらも設定はxhighだった。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122758010401386496-51b887d17e5c63d5499e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-106/2122758010401386496-poster-c0a4fd7777d7fdd60fc9.jpg" width="640" alt="ソースプレビュー 1 · 推論強度xhighで描いたエッフェル塔"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122758010401386496-51b887d17e5c63d5499e.mp4)

Type: Evaluation | Date: 2026-11-17

---

<a id="case-107"></a>
### ケース 107: [水面と照明を調整できる島](https://x.com/Super_Nius/status/2122755138414920061) (投稿者 [@Super_Nius](https://x.com/Super_Nius))

**カメラを周囲に回しながら、水面の波紋や照明の操作を試す。**

作者は、Solでの制作時間は14分だったと報告した。デモでは、デフォルメされた島と、ポインターの動きに反応する水面が見られる。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122754375148085249-33fc598b8af98e28b469.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-107/2122754375148085249-poster-4252a9591fe52677efe3.jpg" width="640" alt="ソースプレビュー 1 · 水面と照明を調整できる島"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122754375148085249-33fc598b8af98e28b469.mp4)

Type: Demo | Date: 2026-11-17

---

<a id="case-109"></a>
### ケース 109: [同じトラック運転シーンを4回作り比べる](https://x.com/Aurora0x3f/status/2122213713650593923) (投稿者 [@Aurora0x3f](https://x.com/Aurora0x3f))

**使用したコーディングツールを記録しながら、同じ運転シーンを比較する。**

作者はモデル名付きで4つのトラックのシーンを公開した。Solの所要時間は15分56秒で、GPTにはCodex、QwenにはQoderを使ったという。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122210853999312896-ff27a563edb434e73b99.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-109/2122210853999312896-poster-c6d956ffa1c75f6b6112.jpg" width="640" alt="ソースプレビュー 1 · 同じトラック運転シーンを4回作り比べる"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122210853999312896-ff27a563edb434e73b99.mp4)

Type: Evaluation | Date: 2026-11-16

---

<a id="case-111"></a>
### ケース 111: [Blenderで作った細部まで見える室内と街並み](https://x.com/kdnbmb/status/2122035562798567611) (投稿者 [@kdnbmb](https://x.com/kdnbmb))

**室内の小物と、窓の向こうに見える景色を確認する。**

作者はMaxで約30分実行したと報告した。公開した作例では、家具のある室内と窓の外の建物が見える。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-111/2122035087764058112-21b99f2331bdc5cbd5f6.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-111/2122035087764058112-21b99f2331bdc5cbd5f6.jpg" width="640" alt="ソースプレビュー 1 · Blenderで作った細部まで見える室内と街並み"></a>

Type: Demo | Date: 2026-11-15

---

<a id="case-113"></a>
### ケース 113: [2つのコーディングモデルで作ったPS5コントローラー](https://x.com/Stargridcompass/status/2121528563254043015) (投稿者 [@Stargridcompass](https://x.com/Stargridcompass))

**正面に加え、背面の外装と側面のボタンも確認する。**

テスト担当者によると、Solは11分、Gemini 4 Hydrogenは3分だった。Solモデルは背面と側面の細部がより充実していたと報告している。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2121451983882059776-f3bfbfcac4a44b9ccf3f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-113/2121451983882059776-poster-af0dc5a722b4dba5734b.jpg" width="640" alt="ソースプレビュー 1 · 2つのコーディングモデルで作ったPS5コントローラー"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2121451983882059776-f3bfbfcac4a44b9ccf3f.mp4)

Type: Evaluation | Date: 2026-11-14

---

<a id="case-115"></a>
### ケース 115: [操作できる3種類の地球儀](https://x.com/Stargridcompass/status/2121208957276713181) (投稿者 [@Stargridcompass](https://x.com/Stargridcompass))

**地球儀を回しながら、照明とインターフェースの動きを比較する。**

作者は同じプロンプトで作った3つの出力をモデル名付きで並べ、Fable 5.2を1位、Solを2位、Gemini 4 Hydrogenを3位とした。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2121198943153405952-cf0ef283fad351f72f02.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-115/2121198943153405952-poster-26d869e61ab575160a19.jpg" width="640" alt="ソースプレビュー 1 · 操作できる3種類の地球儀"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2121198943153405952-cf0ef283fad351f72f02.mp4)

Type: Evaluation | Date: 2026-11-13

---

<a id="case-116"></a>
### ケース 116: [ブラックホールのそばで自転車に乗るペリカン](https://x.com/Jason85885174/status/2120886487860527125) (投稿者 [@Jason85885174](https://x.com/Jason85885174))

**複数回のプロンプト入力を経て、シーンがどう変化したかを確認する。**

作者は先行提供のSolへのルーティングで作ったインタラクティブなシーンだと説明している。プロンプトを3回送り、約90分で完成したと報告した。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2120886190480183296-db1ef2a4fc62055a4696.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-116/2120886190480183296-poster-4a7d5e8156c155b585a6.jpg" width="640" alt="ソースプレビュー 1 · ブラックホールのそばで自転車に乗るペリカン"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2120886190480183296-db1ef2a4fc62055a4696.mp4)

Type: Demo | Date: 2026-11-12

---

<a id="case-117"></a>
### ケース 117: [貨物コンテナを中心に据えた2つの3Dシーン](https://x.com/TokenGremlin/status/2120851437437530584) (投稿者 [@TokenGremlin](https://x.com/TokenGremlin))

**照明、小物、表面の質感の表現を比較する。**

作者はSolとFable 5.2の名前が付いた静止画を公開した。どちらも暗い工業施設を背景に、貨物コンテナと小物を描いている。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-117/2120851426377154560-5e73730ee10437b2a7be.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-117/2120851426377154560-5e73730ee10437b2a7be.jpg" width="640" alt="ソースプレビュー 1 · 貨物コンテナを中心に据えた2つの3Dシーン"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-117/2120851432718962688-6004a93f85caaab2a67e.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-117/2120851432718962688-6004a93f85caaab2a67e.jpg" width="640" alt="ソースプレビュー 2 · 貨物コンテナを中心に据えた2つの3Dシーン"></a>

Type: Evaluation | Date: 2026-11-12

---

<a id="case-121"></a>
### ケース 121: [Three.jsで描く湖畔](https://x.com/TokenGremlin/status/2119852532616790037) (投稿者 [@TokenGremlin](https://x.com/TokenGremlin))

**カメラがボートや滝のそばを通る様子を追い、シーンの細部を確認する。**

作者はテクスチャと照明を使い、Three.jsでシーンを作ったと報告した。静止画と録画の両方を公開している。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119849730087833600-0b28005a595952cec608.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-121/2119849730087833600-poster-d187b20c8f8cc0131a9e.jpg" width="640" alt="ソースプレビュー 1 · Three.jsで描く湖畔"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119849730087833600-0b28005a595952cec608.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-121/2119850475327496192-c54cc99aee779e8ff0a1.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-121/2119850475327496192-c54cc99aee779e8ff0a1.jpg" width="640" alt="ソースプレビュー 2 · Three.jsで描く湖畔"></a>

Type: Demo | Date: 2026-11-09

---

<a id="case-122"></a>
### ケース 122: [人間が採点したインタラクティブな3Dシーン](https://x.com/ArtificialAnlys/status/2122750641647010227) (投稿者 [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**インタラクティブなモデリングを比較する際は、評価セットと採点方法をそろえる。**

Artificial Analysisが公開当日に報告したAA-3Dスコアは、GPT-6.2 Solが1259、Astraが1318、Claude Fable 5.2が1271だった。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-122/2122747871909089280-5008660ef583b6004dbd.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-122/2122747871909089280-5008660ef583b6004dbd.jpg" width="640" alt="ソースプレビュー 1 · 人間が採点したインタラクティブな3Dシーン"></a>

Type: Benchmark | Date: 2026-11-17

---

<a id="category-graphics"></a>
## 🎨 クリエイティブなグラフィックとアニメーション

<a id="case-3"></a>
### ケース 3: [3D で見る人類の歴史と AI の未来](https://x.com/imjustnewatai/status/2119518062034792958) (投稿者 [@imjustnewatai](https://x.com/imjustnewatai))

**物語の概要を一連のアニメーション シーンに変換します。**

録画ではマルチシーンの 3D アニメーションが表示されます。著者の公的プロンプトは、ネアンデルタール人から AI の台頭を経て、想像上の未来へと移ります。

**プロンプト:**

```
Create a cinematic 3D animation telling humanity’s story, from the age of Neanderthals through our greatest advances and the rise of AI. Then imagine a future where AI achieves recursive self-improvement in 2027, and progress doubles or triples every year, transforming Earth in increasingly astonishing ways. Come up with your own scenes and transitions, connecting everything into one compelling story.
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119517968493113344-17865404f54bd3f80fbd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-03/2119517968493113344-poster-62d6ae1e6365eb443bd6.jpg" width="640" alt="ソースプレビュー 1 · 3D で見る人類の歴史と AI の未来"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119517968493113344-17865404f54bd3f80fbd.mp4)


Type: Demo | Date: 2026-11-08

---

<a id="case-8"></a>
### ケース 8: [ブラウザペイントスタジオのTiboポートレート](https://x.com/Mr_Salio/status/2119499550373425297) (投稿者 [@Mr_Salio](https://x.com/Mr_Salio))

**ページがポートレートを構築する際に、ポートレートの段階を検査します。**

Portrait Studio ページでは、参考写真の横に幅広いカラー ブロックから Tibo のポートレートを作成します。クリップにはページのアニメーションが表示されます。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119499524137697280-bf003228060e83ba80ee.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-08/2119499524137697280-poster-669f62240a226482c71b.jpg" width="640" alt="ソースプレビュー 1 · ブラウザペイントスタジオのTiboポートレート"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119499524137697280-bf003228060e83ba80ee.mp4)


Type: Demo | Date: 2026-11-08

---

<a id="case-10"></a>
### ケース 10: [0x0SojalSec が共有する Sam Altman の肖像画](https://x.com/0x0SojalSec/status/2119489612876026325) (投稿者 [@0x0SojalSec](https://x.com/0x0SojalSec))

**大まかな形状から完成したポートレートへの移行を追跡します。**

この投稿では、Sam Altman ペイント クリップを共有します。コレクション内の他の投稿も同じ内容を共有しています。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119471570100113408-6537886f519fcb2581ca.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-10/2119471570100113408-poster-4fa1b097dbe57a86b319.jpg" width="640" alt="ソースプレビュー 1 · 0x0SojalSec が共有する Sam Altman の肖像画"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119471570100113408-6537886f519fcb2581ca.mp4)


Type: Demo | Date: 2026-11-08

---

<a id="case-11"></a>
### ケース 11: [Avenoxai が共有する Sam Altman の肖像画](https://x.com/Avenoxai/status/2119489025484419304) (投稿者 [@Avenoxai](https://x.com/Avenoxai))

**ブラウザーのデモンストレーションでポートレートがどのように作成されるかをご覧ください。**

この投稿は、コレクションの他の場所で示されているのと同じ進歩的な Sam Altman のポートレートを共有しています。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119481355943948288-d9ec44b4a8efb666f3fe.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-11/2119481355943948288-poster-b169fc202c4358aef6ab.jpg" width="640" alt="ソースプレビュー 1 · Avenoxai が共有する Sam Altman の肖像画"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119481355943948288-d9ec44b4a8efb666f3fe.mp4)


Type: Demo | Date: 2026-11-08

---

<a id="case-12"></a>
### ケース 12: [pengsonal が共有する Sam Altman の肖像画](https://x.com/pengsonal/status/2119487069500456985) (投稿者 [@pengsonal](https://x.com/pengsonal))

**ブラウザ シーンがポートレートのディテールを追加する順序を調べてください。**

このクリップは、この素材を共有する他の投稿と同じ Sam Altman 絵画ファミリーに属しています。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119471570100113408-6537886f519fcb2581ca.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-12/2119471570100113408-poster-4fa1b097dbe57a86b319.jpg" width="640" alt="ソースプレビュー 1 · pengsonal が共有する Sam Altman の肖像画"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119471570100113408-6537886f519fcb2581ca.mp4)


Type: Demo | Date: 2026-11-08

---

<a id="case-13"></a>
### ケース 13: [GeekCatX が共有する Sam Altman の肖像画](https://x.com/GeekCatX/status/2119482381375815956) (投稿者 [@GeekCatX](https://x.com/GeekCatX))

**クリップを使用して、最初の構成と完成した画像を比較します。**

この投稿では、他のエントリーと同じメディアファミリーの進歩的な Sam Altman のポートレートが共有されています。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119471570100113408-6537886f519fcb2581ca.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-13/2119471570100113408-poster-4fa1b097dbe57a86b319.jpg" width="640" alt="ソースプレビュー 1 · GeekCatX が共有する Sam Altman の肖像画"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119471570100113408-6537886f519fcb2581ca.mp4)


Type: Demo | Date: 2026-11-08

---

<a id="case-14"></a>
### ケース 14: [ブラウザペイントキャンバス内のSam Altmanポートレート](https://x.com/Ananth7e/status/2119482362614677566) (投稿者 [@Ananth7e](https://x.com/Ananth7e))

**ポートレートがブロックインされた色からより細かい特徴へと変化していく様子を観察してください。**

著者は Sam Altman のブラウザ ペイント デモを紹介します。同じ記録が他のいくつかの投稿にも掲載されています。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119481355943948288-d9ec44b4a8efb666f3fe.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-14/2119481355943948288-poster-b169fc202c4358aef6ab.jpg" width="640" alt="ソースプレビュー 1 · ブラウザペイントキャンバス内のSam Altmanポートレート"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119481355943948288-d9ec44b4a8efb666f3fe.mp4)


Type: Demo | Date: 2026-11-08

---

<a id="case-19"></a>
### ケース 19: [ブラウザペイントキャンバス内のDario Amodeiポートレート](https://x.com/Ananth7e/status/2119475282528932231) (投稿者 [@Ananth7e](https://x.com/Ananth7e))

**舞台化されたポートレートのガイドとなる参考画像をご覧ください。**

ブラウザのデモでは、写真の横に Dario Amodei のポートレートが展開されます。録画にはペイントのシーケンスが表示されます。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119474852453306369-dc2f6dd1c623765520a2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-19/2119474852453306369-poster-16fd35c8363e7611ce48.jpg" width="640" alt="ソースプレビュー 1 · ブラウザペイントキャンバス内のDario Amodeiポートレート"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119474852453306369-dc2f6dd1c623765520a2.mp4)


Type: Demo | Date: 2026-11-08

---

<a id="case-22"></a>
### ケース 22: [4 つの SVG アニメーションと Opus 5.5 の比較](https://x.com/Ananth7e/status/2119473497504428334) (投稿者 [@Ananth7e](https://x.com/Ananth7e))

**いくつかの SVG 被写体のモーションとディテールを比較します。**

ラベル付きの比較には、宇宙での配達、コーヒーマシン、レコードプレーヤー、温室が含まれます。観察されたシーンは、より長いクリップのサンプルからのものです。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119472766353313794-9e720b31f2e3325a6830.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-22/2119472766353313794-poster-81c1db39bbb46647fee0.jpg" width="640" alt="ソースプレビュー 1 · 4 つの SVG アニメーションと Opus 5.5 の比較"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119472766353313794-9e720b31f2e3325a6830.mp4)


Type: Evaluation | Date: 2026-11-08

---

<a id="case-23"></a>
### ケース 23: [Ananth7e による別の Sam Altman 肖像画の投稿](https://x.com/Ananth7e/status/2119471963790065987) (投稿者 [@Ananth7e](https://x.com/Ananth7e))

**共有記録を使用して、ブラウザーのポートレートがどのように形作られるかを検査します。**

この投稿は、他の Sam Altman エントリと同じプログレッシブ ペイント マテリアルを指します。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119471570100113408-6537886f519fcb2581ca.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-23/2119471570100113408-poster-4fa1b097dbe57a86b319.jpg" width="640" alt="ソースプレビュー 1 · Ananth7e による別の Sam Altman 肖像画の投稿"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119471570100113408-6537886f519fcb2581ca.mp4)


Type: Demo | Date: 2026-11-08

---

<a id="case-25"></a>
### ケース 25: [コードのみの SVG として記述された 2 つのポートレート イラスト](https://x.com/marcthecreatorr/status/2119466616693850352) (投稿者 [@marcthecreatorr](https://x.com/marcthecreatorr))

**どのように作成されたかを判断する前に、レンダリングされたポートレートを比較してください。**

投稿には2枚のポートレート画像が含まれています。著者はこれらをコードのみの SVG 出力と説明しています。

**プロンプト:**

```
generate an SVG of Ana de Armas and Sam Altman
(do not cheat)
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-25/2119466601804132352-31318df37f6caba7293c.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-25/2119466601804132352-31318df37f6caba7293c.jpg" width="640" alt="ソースプレビュー 1 · コードのみの SVG として記述された 2 つのポートレート イラスト"></a>
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-25/2119466601816666112-8e9d5270da1add44ca55.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-25/2119466601816666112-8e9d5270da1add44ca55.jpg" width="640" alt="ソースプレビュー 2 · コードのみの SVG として記述された 2 つのポートレート イラスト"></a>

Type: Demo | Date: 2026-11-08

---

<a id="case-29"></a>
### ケース 29: [月明かりに照らされたドット絵の日本の街](https://x.com/SahilPanhotra/status/2119461852426219747) (投稿者 [@SahilPanhotra](https://x.com/SahilPanhotra))

**コンパクトなアニメーション シーンを使用して、照明と詳細を検査します。**

GIF には、桜、塔、橋、反射、小さなボートが表示されます。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119461819278602240-92e36b249f95f46fbbc1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-29/2119461819278602240-poster-0df42c94083b4c7a1d00.jpg" width="640" alt="ソースプレビュー 1 · 月明かりに照らされたドット絵の日本の街"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119461819278602240-92e36b249f95f46fbbc1.mp4)


Type: Demo | Date: 2026-11-08

---

<a id="case-30"></a>
### ケース 30: [BMXに乗りながらジャグリングするライオン](https://x.com/SahilPanhotra/status/2119458278115835912) (投稿者 [@SahilPanhotra](https://x.com/SahilPanhotra))

**変化する季節の背景に対して調整された動きをテストします。**

このアニメーションでは、ライオンがBMXに乗ってボールを投げている様子が描かれています。サンプリングされたフレームには、ポーズと背景の変化が表示されます。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119458208041574400-65d9c5f9e0c9dae6a35f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-30/2119458208041574400-poster-43c1f3849344f031dd3f.jpg" width="640" alt="ソースプレビュー 1 · BMXに乗りながらジャグリングするライオン"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119458208041574400-65d9c5f9e0c9dae6a35f.mp4)


Type: Demo | Date: 2026-11-08

---

<a id="case-31"></a>
### ケース 31: [横から見た疾走する馬](https://x.com/HarshithLucky3/status/2119458168338301327) (投稿者 [@HarshithLucky3](https://x.com/HarshithLucky3))

**単純な動作サイクルを通じて脚と尾を検査します。**

サンプルされたフレームには、四肢の位置を変えながら疾走する馬が横から示されています。

**プロンプト:**

```
Horse running in side view
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119457903589646336-6fe234afbdb557492d14.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-31/2119457903589646336-poster-2e4c31974841a99a4465.jpg" width="640" alt="ソースプレビュー 1 · 横から見た疾走する馬"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119457903589646336-6fe234afbdb557492d14.mp4)


Type: Demo | Date: 2026-11-08

---

<a id="case-32"></a>
### ケース 32: [竹の中をBMXに乗るクジャク](https://x.com/SahilPanhotra/status/2119453829632868388) (投稿者 [@SahilPanhotra](https://x.com/SahilPanhotra))

**ホイールの動きと詳細なキャラクターの動きを比較してください。**

動画では、尾羽を広げたクジャクが竹林の中を BMX で走っています。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119453646454964224-3614c844c591897f7cb8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-32/2119453646454964224-poster-0dd6b3fd00fa99aa9b94.jpg" width="640" alt="ソースプレビュー 1 · 竹の中をBMXに乗るクジャク"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119453646454964224-3614c844c591897f7cb8.mp4)


Type: Demo | Date: 2026-11-08

---

<a id="case-35"></a>
### ケース 35: [フォトリアルなポートレートプレビュー](https://x.com/SadAlbert10/status/2119443244509802679) (投稿者 [@SadAlbert10](https://x.com/SadAlbert10))

**目に見える結果を検査し、作成者がそれをどのように説明したかを記録します。**

画像は詳細なポートレートを示しています。プレビューは出力の視覚的な証拠を提供します。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-35/2119443020227727360-71913855e02651437cb9.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-35/2119443020227727360-71913855e02651437cb9.jpg" width="640" alt="ソースプレビュー 1 · フォトリアルなポートレートプレビュー"></a>

Type: Demo | Date: 2026-11-08

---

<a id="case-36"></a>
### ケース 36: [Sydney Sweeney ポートレートのベクトル化](https://x.com/SadAlbert10/status/2119440420682011095) (投稿者 [@SadAlbert10](https://x.com/SadAlbert10))

**ベクター ワークフローを評価するときに中間イメージを追跡します。**

スクリーンショットは、PNG 入力とベクトル化呼び出しを示しています。 2 番目の添付ファイルは、そのワークフローによって作成されたポートレートを示しています。

**プロンプト:**

```
make an ultra realistic SVG of Sydney Sweeny
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-36/2119439861157707776-69b2db4eca9eb1493e6b.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-36/2119439861157707776-69b2db4eca9eb1493e6b.png" width="640" alt="ソースプレビュー 1 · Sydney Sweeney ポートレートのベクトル化"></a>
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-36/2119440248157683712-d00b68e7e2aa37f8ec7b.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-36/2119440248157683712-d00b68e7e2aa37f8ec7b.jpg" width="640" alt="ソースプレビュー 2 · Sydney Sweeney ポートレートのベクトル化"></a>

Type: Demo | Date: 2026-11-08

---

<a id="case-46"></a>
### ケース 46: [横から見た走っているチーター](https://x.com/HarshithLucky3/status/2119424342773866559) (投稿者 [@HarshithLucky3](https://x.com/HarshithLucky3))

**固定プロファイル ビューを使用して、歩行と体の動きを比較します。**

このクリップには、チーターが走行中にさまざまな姿勢をとる様子が映されています。著者は、Opus の結果を好むと報告しています。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119424200662556672-37c18d0191bd9b6c27aa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-46/2119424200662556672-poster-f977110905db5bd671d8.jpg" width="640" alt="ソースプレビュー 1 · 横から見た走っているチーター"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119424200662556672-37c18d0191bd9b6c27aa.mp4)


Type: Demo | Date: 2026-11-08

---

<a id="case-51"></a>
### ケース 51: [自転車に乗るペリカンと2匹のカニ](https://x.com/HarshithLucky3/status/2119418918616150080) (投稿者 [@HarshithLucky3](https://x.com/HarshithLucky3))

**複数のアニメーション キャラクターのタイミングを 1 回のショットで検査します。**

サンプリングされたサイドビュー フレームには、移動する車輪、手足、カメラの位置が表示されます。

**プロンプト:**

```
SVG animation of pelican and 2 crabs riding bicycles side view
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119418838148366336-495e5e6b9a3a4f396f52.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-51/2119418838148366336-poster-753362afc6ea3f66a03f.jpg" width="640" alt="ソースプレビュー 1 · 自転車に乗るペリカンと2匹のカニ"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119418838148366336-495e5e6b9a3a4f396f52.mp4)


Type: Demo | Date: 2026-11-08

---

<a id="case-52"></a>
### ケース 52: [Sol 設定間の PS5 コントローラーの比較](https://x.com/marcthecreatorr/status/2119417283328000436) (投稿者 [@marcthecreatorr](https://x.com/marcthecreatorr))

**使い慣れた製品を使用して、輪郭と陰影を比較します。**

2 つのコントローラー イメージには、GPT-6.1 Sol MAX ルーティングおよびベーシックというラベルが付けられています。投稿にはレンダリングされたイメージが表示されます。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-52/2119417273249095680-f0fea371a0a411ae9aef.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-52/2119417273249095680-f0fea371a0a411ae9aef.jpg" width="640" alt="ソースプレビュー 1 · Sol 設定間の PS5 コントローラーの比較"></a>

Type: Evaluation | Date: 2026-11-08

---

<a id="case-55"></a>
### ケース 55: [緑色のBMW M4 CSのプロフィールイラスト](https://x.com/HarshithLucky3/status/2119412698119373104) (投稿者 [@HarshithLucky3](https://x.com/HarshithLucky3))

**見慣れた車両でプロポーションやプロフィールのディテールを確認してください。**

添付ファイルは緑色のBMW M4 CSを横から見たものです。

**プロンプト:**

```
SVG of BMW M4 CS side view
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-55/2119412669946204160-2b4789da7aa53b1095b0.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-55/2119412669946204160-2b4789da7aa53b1095b0.jpg" width="640" alt="ソースプレビュー 1 · 緑色のBMW M4 CSのプロフィールイラスト"></a>

Type: Demo | Date: 2026-11-08

---

<a id="case-60"></a>
### ケース 60: [孫悟空「大鬧天宮」のSVG比較](https://x.com/xbquan/status/2119581984989364514) (投稿者 [@xbquan](https://x.com/xbquan))

**同じ孫悟空の場面を3つのシステムがどう構成したか比べます。**

投稿者は3枚の画像を順に、最高設定の GPT-6.2 Sol、Qoder の QoDuck、WorkBuddy の HY4 と記しています。返信で公開したプロンプトは、SVGを1案だけ作り、スクリーンショットで確認しないよう求めています。

[元のプロンプトを掲載した作者の返信](https://x.com/xbquan/status/2119582058922316169)

**プロンプト:**

```
用尽你的一切能力，用代码画一张孙悟空的大闹天宫名场面的svg图片，我想要尽可能的还原，只能画一版，不准截图检查。
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-60/2119580835200516096-1e4e7a136e429b696a7a.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-60/2119580835200516096-1e4e7a136e429b696a7a.jpg" width="640" alt="ソースプレビュー 1 · 孫悟空「大鬧天宮」のSVG比較"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-60/2119581876805640192-01552031d537dc13d897.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-60/2119581876805640192-01552031d537dc13d897.jpg" width="640" alt="ソースプレビュー 2 · 孫悟空「大鬧天宮」のSVG比較"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-60/2119581974092546048-c61fe179e1741227a187.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-60/2119581974092546048-c61fe179e1741227a187.png" width="640" alt="ソースプレビュー 3 · 孫悟空「大鬧天宮」のSVG比較"></a>

Type: Evaluation | Date: 2026-11-09

---

<a id="case-74"></a>
### ケース 74: [コードで作った炎と音](https://x.com/camperaigg/status/2122794828266377538) (投稿者 [@camperaigg](https://x.com/camperaigg))

**モーション作品を比較するときは費用と生成時間に加えて映像の尺も記録する。**

作者は映像と音をコードで作るxhighの実行を2件比較した。報告ではSolは12分・0.73ドルで12秒、Opus 5.5は85分・18.40ドルで24秒の映像を出力した。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122794767960752128-e2e19e403efea0d778cc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-74/2122794767960752128-poster-5dc5e43235499f8378cf.jpg" width="640" alt="ソースプレビュー 1 · コードで作った炎と音"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122794767960752128-e2e19e403efea0d778cc.mp4)

Type: Evaluation | Date: 2026-11-17

---

<a id="case-79"></a>
### ケース 79: [15秒のモーションデザイン課題](https://x.com/Leviwoyun/status/2122846422676701267) (投稿者 [@Leviwoyun](https://x.com/Leviwoyun))

**同じ課題を与え、文字組み、場面転換、動きの表現を比較する。**

作者は2本の映像と元のプロンプトを公開した。一方は折り紙のような形の回転が中心で、もう一方は信号の表示から紫の幾何学的な形へ展開する。

**プロンプト:**

```
制作一段 15 秒的动态图形视频，展示你是一位多么出色的动态设计师，就像是你简历上的作品集一样，使用任何你认为能产出最佳效果的工具或技术。你拥有完全的创作自由，优先追求卓越的视觉设计、大胆的艺术指导、引人注目的构图和富有力量的动态表现，让每一秒都有价值。全力以赴。
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122845749499310081-01cb8b6073d8916e9b09.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-79/2122845749499310081-poster-1159d01955e99da02391.jpg" width="640" alt="ソースプレビュー 1 · 15秒のモーションデザイン課題"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122845749499310081-01cb8b6073d8916e9b09.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122846110117183488-30f1277d34e59656f484.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-79/2122846110117183488-poster-7b07819920bd6a3fe88d.jpg" width="640" alt="ソースプレビュー 2 · 15秒のモーションデザイン課題"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122846110117183488-30f1277d34e59656f484.mp4)

Type: Evaluation | Date: 2026-11-18

---

<a id="case-88"></a>
### ケース 88: [2つのモデルが描いた疾走する馬](https://x.com/jony_palino/status/2122796926961647919) (投稿者 [@jony_palino](https://x.com/jony_palino))

**ループを一周させ、脚の運びと歩幅を見比べる。**

動画にはAstraとSolのモデル名が表示され、それぞれの馬が走る様子を並べて見られる。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122781224338939905-9fac5a374f5ddc54f8a8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-88/2122781224338939905-poster-b06065421603cc7f6f6c.jpg" width="640" alt="ソースプレビュー 1 · 2つのモデルが描いた疾走する馬"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122781224338939905-9fac5a374f5ddc54f8a8.mp4)

Type: Evaluation | Date: 2026-11-17

---

<a id="case-94"></a>
### ケース 94: [コードで作った900フレームのアニメーション](https://x.com/morsenxxx/status/2122771021828948464) (投稿者 [@morsenxxx](https://x.com/morsenxxx))

**キャラクター、動き、音が最終出力にどう反映されるかを確認する。**

作者によると、キャラクター、アニメーション、サウンドトラックはコードで生成した。公開された作品の長さは30秒。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122768959980118016-519fd034e8c095b6bc01.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-94/2122768959980118016-poster-ef4789678264a50b8b9f.jpg" width="640" alt="ソースプレビュー 1 · コードで作った900フレームのアニメーション"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122768959980118016-519fd034e8c095b6bc01.mp4)

Type: Demo | Date: 2026-11-17

---

<a id="case-98"></a>
### ケース 98: [アニメーションになったバナナのイラスト](https://x.com/AdamHoltererer/status/2122765119835029581) (投稿者 [@AdamHoltererer](https://x.com/AdamHoltererer))

**身近な題材で、モデルが動きと登場人物をどう加えるかを確認する。**

作者が公開したSolのバナナのテストでは、描かれたバナナがキャラクターの動く場面の一部になる。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122765018739441664-63474f1acf4d1d5e18b1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-98/2122765018739441664-poster-a235f39f622e3848c495.jpg" width="640" alt="ソースプレビュー 1 · アニメーションになったバナナのイラスト"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122765018739441664-63474f1acf4d1d5e18b1.mp4)

Type: Demo | Date: 2026-11-17

---

<a id="case-101"></a>
### ケース 101: [単一HTMLファイルで描く自転車に乗ったペリカン](https://x.com/Super_Nius/status/2122760765174391124) (投稿者 [@Super_Nius](https://x.com/Super_Nius))

**同じSVGの制作指示で、鳥と自転車の動きを並べて確認する。**

作者はプロンプトを公開し、6.2と6.1の出力を比較した。Solの描き方の変化は小幅だったと報告している。

**プロンプト:**

```
创建一个HTML文件，使用SVG绘制一只鹈鹕3D骑自行车的动画。输出单文件HTML。
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122760254945673216-c6b375b036ac15cc3a2b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-101/2122760254945673216-poster-d0903f87dd4ac9dee18a.jpg" width="640" alt="ソースプレビュー 1 · 単一HTMLファイルで描く自転車に乗ったペリカン"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122760254945673216-c6b375b036ac15cc3a2b.mp4)

Type: Evaluation | Date: 2026-11-17

---

<a id="case-103"></a>
### ケース 103: [Ultraで生成した2本の棒人間アニメーション](https://x.com/DanielZambrini/status/2122759375337214121) (投稿者 [@DanielZambrini](https://x.com/DanielZambrini))

**同じアニメーションの指示を繰り返し、実行ごとの差を確認する。**

作者はSolをUltraに設定した2回の結果を公開し、制作時間はそれぞれ13分と12分だったと報告した。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122758829104328704-4fe90331a8b43e8cc76c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-103/2122758829104328704-poster-2e025ca80aa35e6c9676.jpg" width="640" alt="ソースプレビュー 1 · Ultraで生成した2本の棒人間アニメーション"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122758829104328704-4fe90331a8b43e8cc76c.mp4)

Type: Evaluation | Date: 2026-11-17

---

<a id="case-110"></a>
### ケース 110: [Sol、Opus、Qwenが描く雨の自転車配達](https://x.com/Stargridcompass/status/2122184571269853307) (投稿者 [@Stargridcompass](https://x.com/Stargridcompass))

**3つの出力で、夜景と自転車の動きを比較する。**

作者は配達員のペリカンを描いた3つの作例をモデル名付きで公開し、この比較ではOpus 5.5を好んだ。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122183328228909056-562a9b17b2bc7222fb58.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-110/2122183328228909056-poster-9550a8f62aa13cde8a3a.jpg" width="640" alt="ソースプレビュー 1 · Sol、Opus、Qwenが描く雨の自転車配達"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122183328228909056-562a9b17b2bc7222fb58.mp4)

Type: Evaluation | Date: 2026-11-16

---

<a id="case-112"></a>
### ケース 112: [雨の中を自転車で料理を配達するペリカン](https://x.com/Stargridcompass/status/2121543669882745007) (投稿者 [@Stargridcompass](https://x.com/Stargridcompass))

**反射、水たまり、道路設備、動きのある背景を個別に確認する。**

作者は雨の配達シーンでSolとFable 5.2を比較し、水たまりと反射はSol版を好んだ。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2121535105013334016-7271e00bcbdb0a0caf42.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-112/2121535105013334016-poster-4a1d19351363ee575584.jpg" width="640" alt="ソースプレビュー 1 · 雨の中を自転車で料理を配達するペリカン"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2121535105013334016-7271e00bcbdb0a0caf42.mp4)

Type: Evaluation | Date: 2026-11-14

---

<a id="case-114"></a>
### ケース 114: [日中に自転車に乗るペリカンの2つの作例](https://x.com/Stargridcompass/status/2121505035976597773) (投稿者 [@Stargridcompass](https://x.com/Stargridcompass))

**動きの質と実行時間を併せて比較する。**

作者は同じ制作指示に対するSolとGemini 4 Hydrogenの結果を公開した。実行時間はSolが13分、Hydrogenが3分と報告している。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2121503397702459392-e951142e407012e2ef01.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-114/2121503397702459392-poster-2f40d730171de43b3581.jpg" width="640" alt="ソースプレビュー 1 · 日中に自転車に乗るペリカンの2つの作例"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2121503397702459392-e951142e407012e2ef01.mp4)

Type: Evaluation | Date: 2026-11-14

---

<a id="case-118"></a>
### ケース 118: [SVGで動かす剣の決闘](https://x.com/kdnbmb/status/2120537324488450050) (投稿者 [@kdnbmb](https://x.com/kdnbmb))

**動きのタイミングとシルエットが、ベクターアニメーションの動きにどう説得力を与えるかを見る。**

作者によると、コードで描いたアニメーションはSolを1回実行して得られたもので、約18分かかった。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2120537298286608384-168cc4ec913763fba163.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-118/2120537298286608384-poster-7749116f725da65b0420.jpg" width="640" alt="ソースプレビュー 1 · SVGで動かす剣の決闘"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2120537298286608384-168cc4ec913763fba163.mp4)

Type: Demo | Date: 2026-11-11

---

<a id="case-120"></a>
### ケース 120: [SVGで写真のような風景を描く](https://x.com/kdnbmb/status/2120193707987317053) (投稿者 [@kdnbmb](https://x.com/kdnbmb))

**自然の風景をベクターで描いたとき、どの細部が残るかを確認する。**

作者は、Maxに設定したSolに写真のような自然風景のSVGを指示したと述べ、レンダリングした結果を公開した。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-120/2120193470002241536-2e471c1c74dabf15e6eb.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-120/2120193470002241536-2e471c1c74dabf15e6eb.jpg" width="640" alt="ソースプレビュー 1 · SVGで写真のような風景を描く"></a>

Type: Demo | Date: 2026-11-10

---

<a id="case-123"></a>
### ケース 123: [推論強度別のペリカンSVG](https://news.ycombinator.com/item?id=50535742) (投稿者 [@simonw](https://news.ycombinator.com/user?id=simonw))

**推論強度ごとに、ペダル、足、車体フレームの位置関係を確認する。**

Simon Willisonは、同じSVGのプロンプトを6つのモデルと複数の推論強度で試し、出力にラベルを付けて一覧にした。議論では、SolのMax版で脚がチェーンと重なる点が指摘された。

**プロンプト:**

```
Generate an SVG of a pelican riding a bicycle
```

[Pelican SVG comparison](https://static.simonwillison.net/static/2026/openai-pelicans-november-2026.html)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-123/50535742-grid-7d953958cc033d468770.webp"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-123/50535742-grid-7d953958cc033d468770.webp" width="640" alt="ソースプレビュー 1 · 推論強度別のペリカンSVG"></a>

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-123/50535742-astra-3d77dc7c6001b9a03061.webp"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-123/50535742-astra-3d77dc7c6001b9a03061.webp" width="640" alt="ソースプレビュー 2 · 推論強度別のペリカンSVG"></a>

Type: Evaluation | Date: 2026-11-17

---

<a id="category-web"></a>
## 🌐 ウェブサイトとインターフェース

<a id="case-4"></a>
### ケース 4: [時間の終わりのインタラクティブ ブラック ホール](https://x.com/Khazix0918/status/2119507514459144677) (投稿者 [@Khazix0918](https://x.com/Khazix0918))

**インタラクティブな Three.js ページの焦点としてブラック ホールを使用します。**

このクリップには、周回するビュー、発光リング、粒子、色の変化が示されています。ソースには完全な中国語プロンプトが含​​まれています。

**プロンプト:**

```
请使用 Three.js 创作一个主题为《时间的尽头》的 3D 交互式网页。
充分发挥你最顶级的审美、艺术设计和 3D 编程能力，在构图、光影、材质、粒子、动画和空间氛围上做到极致。画面需要有令人震撼的视觉表现力，并且可以通过鼠标自由交互。
不限制你的创意和技术方案，尽可能展示你的能力上限。请直接完成开发、运行和测试，交付一个真正可玩的作品。
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119507467990413312-818eda21b9c994093c1c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-04/2119507467990413312-poster-7f10a219f1f4bc039223.jpg" width="640" alt="ソースプレビュー 1 · 時間の終わりのインタラクティブ ブラック ホール"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119507467990413312-818eda21b9c994093c1c.mp4)


Type: Demo | Date: 2026-11-08

---

<a id="case-7"></a>
### ケース 7: [Island Atlas 昼夜切り替え付き](https://x.com/JustLingonberry/status/2119502325069103118) (投稿者 [@JustLingonberry](https://x.com/JustLingonberry))

**コンパクトな 3D アイランドを使用して、Web インターフェイスで照明状態をテストします。**

画面録画には、左側に Island Atlas と Kame House、昼夜切り替え、会話パネルが表示されます。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119502149323468800-f9cdb706db0b977af9fb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-07/2119502149323468800-poster-d546d522a8a5c3325b43.jpg" width="640" alt="ソースプレビュー 1 · Island Atlas 昼夜切り替え付き"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119502149323468800-f9cdb706db0b977af9fb.mp4)


Type: Demo | Date: 2026-11-08

---

<a id="case-41"></a>
### ケース 41: [Codex および API での参照イメージのテスト](https://x.com/JustinGorya/status/2119433734059401260) (投稿者 [@JustinGorya](https://x.com/JustinGorya))

**違いを特定する前に、同じリファレンスを使用して 2 つの出力が何を行うかを比較してください。**

動画には画面と 3D の出力が映っています。投稿者は、結果の違いだけでは裏で使われたモデルは特定できないと明記しています。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119433659820265472-dc037578c6e914ded9aa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-41/2119433659820265472-poster-b2e0a738009479a562c2.jpg" width="640" alt="ソースプレビュー 1 · Codex および API での参照イメージのテスト"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119433659820265472-dc037578c6e914ded9aa.mp4)


Type: Evaluation | Date: 2026-11-08

---

<a id="case-61"></a>
### ケース 61: [回転する七角形の中の重力ボール](https://x.com/VeknQAQ/status/2119613583055261907) (投稿者 [@VeknQAQ](https://x.com/VeknQAQ))

**容器が回転するとボールがどう動くか確認します。**

ブラウザーの録画では、色とりどりのボールが回転する七角形の容器の中で落下し、縁に沿って集まります。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119613276808163329-9e32891b47f58015ccd9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-61/2119613276808163329-poster-ebcefd25490e1fa11f76.jpg" width="640" alt="ソースプレビュー 1 · 回転する七角形の中の重力ボール"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119613276808163329-9e32891b47f58015ccd9.mp4)

Type: Demo | Date: 2026-11-09

---

<a id="case-69"></a>
### ケース 69: [ブガッティ・シロンの360度コンフィギュレーター](https://x.com/SahilPanhotra/status/2119692064099368967) (投稿者 [@SahilPanhotra](https://x.com/SahilPanhotra))

**カメラが車の周りを移動する様子を見ながら、塗装の仕上がりを比べます。**

録画ではスタジオ照明の下で、撮影角度を変えながら青、銀、黒の塗装を表示します。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119691929403482112-00220dfbd8a8d75a6ce7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-69/2119691929403482112-poster-645e9a72b2bb463ff65e.jpg" width="640" alt="ソースプレビュー 1 · ブガッティ・シロンの360度コンフィギュレーター"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119691929403482112-00220dfbd8a8d75a6ce7.mp4)

Type: Demo | Date: 2026-11-09

---

<a id="case-75"></a>
### ケース 75: [ブラウザー操作でGeoGuessrの場所を特定](https://x.com/nickbaumann_/status/2122805861093417220) (投稿者 [@nickbaumann_](https://x.com/nickbaumann_))

**モデル間で開始地点、制限時間、距離の基準をそろえる。**

試験者は同じ100地点を使い、各地点で5分以内に1 km圏内へピンを置くよう求めた。SolとAstraはいずれも77回成功し、試験者によるとSolの方が速かった。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122751536778387456-4ba9a30b51fd04a352fb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-75/2122751536778387456-poster-499c7bb9670c1315b38e.jpg" width="640" alt="ソースプレビュー 1 · ブラウザー操作でGeoGuessrの場所を特定"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122751536778387456-4ba9a30b51fd04a352fb.mp4)

Type: Benchmark | Date: 2026-11-17

---

<a id="case-77"></a>
### ケース 77: [Blenderのモデルを使ったチョウの展示サイト](https://x.com/DeryaTR_/status/2122814594737684568) (投稿者 [@DeryaTR_](https://x.com/DeryaTR_))

**回転できる標本に拡大表示と観察情報を組み合わせる。**

作者はSolとBlenderでサイトを制作したと報告した。映像では動きのある複数のチョウ、翅の拡大表示、生息地・分類・成長段階の情報欄を確認できる。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122813839481663488-e921dcc4253d7432553d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-77/2122813839481663488-poster-2f054c454b8ad5768090.jpg" width="640" alt="ソースプレビュー 1 · Blenderのモデルを使ったチョウの展示サイト"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122813839481663488-e921dcc4253d7432553d.mp4)

Type: Demo | Date: 2026-11-17

---

<a id="case-80"></a>
### ケース 80: [Browser Useのタスク達成率と操作ステップ数](https://x.com/browser_use/status/2122844670598488376) (投稿者 [@browser_use](https://x.com/browser_use))

**同じブラウザー評価セットで、達成率、所要時間、操作ステップ数を比較する。**

Browser UseはSol 6.2の達成率を82%、Sol 6.1を81%と報告した。公開当日の比較では、所要時間は6.2が12分、6.1が22分で、6.2の操作ステップ数は36%少なかった。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-80/2122843921776889856-e164df0ff216a1ca1693.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-80/2122843921776889856-e164df0ff216a1ca1693.jpg" width="640" alt="ソースプレビュー 1 · Browser Useのタスク達成率と操作ステップ数"></a>

Type: Benchmark | Date: 2026-11-18

---

<a id="case-82"></a>
### ケース 82: [Perplexityのエージェント評価「WANDR」](https://x.com/perplexity_ai/status/2122814545639223348) (投稿者 [@perplexity_ai](https://x.com/perplexity_ai))

**タスクのスコアと1件あたりの費用を併せて比較する。**

Perplexityによると、Solは同社の評価でWANDRスコア0.746、1タスクあたり約2.65ドルだった。スコアはGPT-6.1 Solより0.065高かった。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-82/2122814541839183872-f37a3311076b269e6032.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-82/2122814541839183872-f37a3311076b269e6032.jpg" width="640" alt="ソースプレビュー 1 · Perplexityのエージェント評価「WANDR」"></a>

Type: Benchmark | Date: 2026-11-17

---

<a id="case-108"></a>
### ケース 108: [Wikipediaの50ページから指定記事にたどり着く](https://x.com/nickbaumann_/status/2122753176113688601) (投稿者 [@nickbaumann_](https://x.com/nickbaumann_))

**移動時間を計測する際は、到達先と開始ページを固定する。**

5つのモデルすべてが、指定されたどの開始ページからもJacob Misiorowskiの記事に到達した。テスト担当者によると、Solは39秒で比較中最速だった。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122753158950555648-0e31c6a62410aad900f2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-108/2122753158950555648-poster-f3d93eef7774666a24dd.jpg" width="640" alt="ソースプレビュー 1 · Wikipediaの50ページから指定記事にたどり着く"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122753158950555648-0e31c6a62410aad900f2.mp4)

Type: Benchmark | Date: 2026-11-17

---

<a id="case-119"></a>
### ケース 119: [エージェントのセッションを管理するかんばんプラグイン](https://x.com/mspd4100/status/2120527338165465527) (投稿者 [@mspd4100](https://x.com/mspd4100))

**タスク、セッション、レビュー待ちの項目が画面上でどう結び付くかを確認する。**

Super Kanbanの開発者は、2日間のリファクタリングにSolを使ったと報告した。v0.8.0では、ワークスペースをまたいでタスクをまとめ、1つのタスクを複数のセッションに関連付けられる。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-119/2120527322340335617-06bc9b33952b11d16d33.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-119/2120527322340335617-06bc9b33952b11d16d33.jpg" width="640" alt="ソースプレビュー 1 · エージェントのセッションを管理するかんばんプラグイン"></a>

Type: Integration | Date: 2026-11-11

---

<a id="category-game"></a>
## 🎮 ゲーム開発

<a id="case-17"></a>
### ケース 17: [PELICAN PANIC ボクセルチェイスゲーム](https://x.com/Ananth7e/status/2119479157633786246) (投稿者 [@Ananth7e](https://x.com/Ananth7e))

**短い追跡ゲームを使用して、コントロール、フィードバック、および終了状態を検査します。**

このクリップには、ライダーがペリカンに乗ってジャガイモの怪物から逃げる様子が映されている。スコアとクリア画面「Escaped」が表示されます。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119478839500013568-2ec29cee42e54d0bf9c5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-17/2119478839500013568-poster-3716db2a9abc6cf0e264.jpg" width="640" alt="ソースプレビュー 1 · PELICAN PANIC ボクセルチェイスゲーム"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119478839500013568-2ec29cee42e54d0bf9c5.mp4)


Type: Demo | Date: 2026-11-08

---

<a id="case-62"></a>
### ケース 62: [ブラウザーで動くルービックキューブ](https://x.com/VeknQAQ/status/2119633751173173475) (投稿者 [@VeknQAQ](https://x.com/VeknQAQ))

**プレビューでキューブの回転とステッカーの配置を確認します。**

録画には、色をそろえた状態と崩した状態の3Dキューブ、ブラウザー上の操作ボタンが映っています。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119633608680124416-44e5b8b00d129caeba34.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-62/2119633608680124416-poster-1ea9e2acda539d582293.jpg" width="640" alt="ソースプレビュー 1 · ブラウザーで動くルービックキューブ"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119633608680124416-44e5b8b00d129caeba34.mp4)

Type: Demo | Date: 2026-11-09

---

<a id="case-67"></a>
### ケース 67: [海岸沿いのレースゲームの試作](https://x.com/Stargridcompass/status/2119683294220390638) (投稿者 [@Stargridcompass](https://x.com/Stargridcompass))

**レース中にカウントダウン、速度表示、コースマップが読み取りやすいか確認します。**

録画にはスタートグリッドからの発進とレース中の様子が映っています。投稿者によると制作には16分かかりました。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119682250472112128-81f053c6ffe2a4aae055.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-67/2119682250472112128-poster-526c85969a54c7f93833.jpg" width="640" alt="ソースプレビュー 1 · 海岸沿いのレースゲームの試作"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2119682250472112128-81f053c6ffe2a4aae055.mp4)

Type: Demo | Date: 2026-11-09

---

<a id="case-78"></a>
### ケース 78: [倉庫番の問題セットを全問クリア](https://x.com/banteg/status/2122826622638137666) (投稿者 [@banteg](https://x.com/banteg))

**クリアした部屋数を記録し、手順を再生して行き詰まる場面を確認する。**

作者はSolとAstraをmediumで試した。今回はどちらも全66部屋をクリアし、投稿時点の作者のランキングでSolは2位、Astraは3位だった。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122826155086512128-d2a8456da3a5a99263f5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-78/2122826155086512128-poster-4a2c4bee2b8d9510e347.jpg" width="640" alt="ソースプレビュー 1 · 倉庫番の問題セットを全問クリア"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122826155086512128-d2a8456da3a5a99263f5.mp4)

Type: Benchmark | Date: 2026-11-17

---

<a id="case-93"></a>
### ケース 93: [RuneScapeで2つのクエストを攻略](https://x.com/maxbittker/status/2122783334216466487) (投稿者 [@maxbittker](https://x.com/maxbittker))

**エージェントが選んだクエストと受け取った報酬を確認する。**

ベンチマークの管理者によると、SolとAstraはそれぞれ1回の実行で2つのクエストに取り組み、両方の報酬を受け取った。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-93/2122782503542960128-31be885019f467cb7472.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-93/2122782503542960128-31be885019f467cb7472.jpg" width="640" alt="ソースプレビュー 1 · RuneScapeで2つのクエストを攻略"></a>

Type: Benchmark | Date: 2026-11-17

---

<a id="case-95"></a>
### ケース 95: [タッチ操作に対応したマルチプレイヤーのブラウザーゲーム](https://x.com/VraserX/status/2122770481975837145) (投稿者 [@VraserX](https://x.com/VraserX))

**各ビルドをプレイし、操作の改善点を具体的に伝える。**

開発者は、タッチ操作を含めて各ビルドをテストしながら、16対16の試作版の実装、デバッグ、改修にSolを使ったと報告している。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122770342842077184-c89268a9c06156333c45.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-95/2122770342842077184-poster-c5a1ebf986d6362bd35d.jpg" width="640" alt="ソースプレビュー 1 · タッチ操作に対応したマルチプレイヤーのブラウザーゲーム"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122770342842077184-c89268a9c06156333c45.mp4)

Type: Demo | Date: 2026-11-17

---

<a id="case-97"></a>
### ケース 97: [村づくりのブラウザーゲーム「Lanternkeep」](https://x.com/AdamHoltererer/status/2122766741881413818) (投稿者 [@AdamHoltererer](https://x.com/AdamHoltererer))

**マップと目標パネルが村づくりの流れをどう支えるかを見る。**

作者はSolを使ったゲームとして紹介している。録画では操作できる村のマップと目標パネルが確認できる。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122766701477367808-c628e4fc3e8c14dc15d8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-97/2122766701477367808-poster-50e4bfea19c965f6d231.jpg" width="640" alt="ソースプレビュー 1 · 村づくりのブラウザーゲーム「Lanternkeep」"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122766701477367808-c628e4fc3e8c14dc15d8.mp4)

Type: Demo | Date: 2026-11-17

---

<a id="case-99"></a>
### ケース 99: [スクリーンショットだけで『ポケットモンスター ファイアレッド』を進める](https://x.com/Clad3815/status/2122763941675995209) (投稿者 [@Clad3815](https://x.com/Clad3815))

**ゲームを操作するエージェントの到達点とクリア時間を記録する。**

テスト担当者は、入力にスクリーンショットを使い、推論強度をhighに設定したと報告した。このテストでSolは15時間34分かかり、最初のジムリーダーにはAstraより先に到達した。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-99/2122763933345890304-ffe6b4053f347b1d4d5f.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-99/2122763933345890304-ffe6b4053f347b1d4d5f.jpg" width="640" alt="ソースプレビュー 1 · スクリーンショットだけで『ポケットモンスター ファイアレッド』を進める"></a>

Type: Benchmark | Date: 2026-11-17

---

<a id="category-painting"></a>
## 🖌️ パソコンの使用と絵を描くこと

<a id="case-1"></a>
### ケース 1: [Freddie Mercury の MS Paint](https://x.com/Avenoxai/status/2119569440681464296) (投稿者 [@Avenoxai](https://x.com/Avenoxai))

**ポートレートを使用して、デスクトップ描画の試行によって何が生成されるかを検査します。**

スクリーンショットは、MS Paint の Freddie Mercury ポートレートの横にある Codex の会話を示しています。著者はコンピュータ使用テストについて説明します。スクリーンショットは結果と会話の一部をキャプチャしたものです。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-01/2119569353834180609-7032bb605e364515b8ca.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-01/2119569353834180609-7032bb605e364515b8ca.jpg" width="640" alt="ソースプレビュー 1 · Freddie Mercury の MS Paint"></a>

Type: Demo | Date: 2026-11-08

---

<a id="case-100"></a>
### ケース 100: [ブラウザー上のお絵描きキャンバスに描いた肖像](https://x.com/N1njaCodex/status/2122763308491325670) (投稿者 [@N1njaCodex](https://x.com/N1njaCodex))

**描画途中のフレームを、キャンバス横に表示された参照画像と見比べる。**

作者はSolで肖像を描いたとしている。録画では白紙のキャンバスにSam Altmanの肖像が細かく描き込まれていく。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122763229021491200-68e05d85bf900b9bde8f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-100/2122763229021491200-poster-6021a21c7fa6bf0245bc.jpg" width="640" alt="ソースプレビュー 1 · ブラウザー上のお絵描きキャンバスに描いた肖像"></a>

[デモ動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/playback/2122763229021491200-68e05d85bf900b9bde8f.mp4)

Type: Demo | Date: 2026-11-17

---

<a id="category-communication"></a>
## 💬 コンピュータの使用とコミュニケーション

<a id="case-43"></a>
### ケース 43: [メッセージを中継する未完了の試み](https://x.com/SadAlbert10/status/2119428297092460613) (投稿者 [@SadAlbert10](https://x.com/SadAlbert10))

**この試みを使用して、デスクトップ ワークフローがどこで停止したかを確認します。**

スクリーンショットは、メッセージを渡す要求の後に受信者を見つけようとする試みを示しています。メッセージが送信される前にタスクが終了しました。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-43/2119428121711775744-8419b4e0c62aa252d1dc.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-43/2119428121711775744-8419b4e0c62aa252d1dc.jpg" width="640" alt="ソースプレビュー 1 · メッセージを中継する未完了の試み"></a>
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-43/2119428270945140736-f9662043dadb9a6e4b1b.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-6-2-sol-use-cases/assets/cases/case-43/2119428270945140736-f9662043dadb9a6e4b1b.jpg" width="640" alt="ソースプレビュー 2 · メッセージを中継する未完了の試み"></a>

Type: Limit | Date: 2026-11-08

---

<a id="related-repositories"></a>
## 関連リポジトリ

- [GPT-6.2 Astra · Demos & Use Cases](https://github.com/cheercheung/awesome-gpt-6-2-astra-guide-and-use-cases)
- [GPT-6.1 Terra · Guide & Use Cases](https://github.com/cheercheung/awesome-gpt-6-1-terra-guide-and-use-cases)

<a id="acknowledge"></a>
## 🙏 謝辞

これらの実験を共有してくれたクリエイターに感謝します。リンクされた作品およびメディアは、それぞれの作成者に帰属します。

[@Avenoxai](https://x.com/Avenoxai), [@kimmonismus](https://x.com/kimmonismus), [@imjustnewatai](https://x.com/imjustnewatai), [@Khazix0918](https://x.com/Khazix0918), [@marcthecreatorr](https://x.com/marcthecreatorr), [@Bhavani_00007](https://x.com/Bhavani_00007), [@JustLingonberry](https://x.com/JustLingonberry), [@Mr_Salio](https://x.com/Mr_Salio), [@aGim_asf](https://x.com/aGim_asf), [@0x0SojalSec](https://x.com/0x0SojalSec), [@pengsonal](https://x.com/pengsonal), [@GeekCatX](https://x.com/GeekCatX), [@Ananth7e](https://x.com/Ananth7e), [@EnvolDev](https://x.com/EnvolDev), [@xbquan](https://x.com/xbquan), [@SahilPanhotra](https://x.com/SahilPanhotra), [@rubenssoto_ai](https://x.com/rubenssoto_ai), [@vikktorrrre](https://x.com/vikktorrrre), [@pankajkumar_dev](https://x.com/pankajkumar_dev), [@Cayden970207](https://x.com/Cayden970207), [@HarshithLucky3](https://x.com/HarshithLucky3), [@TokenGremlin](https://x.com/TokenGremlin), [@SadAlbert10](https://x.com/SadAlbert10), [@maxt3chno](https://x.com/maxt3chno), [@karanC_12](https://x.com/karanC_12), [@JustinGorya](https://x.com/JustinGorya), [@kdnbmb](https://x.com/kdnbmb), [@VraserX](https://x.com/VraserX), [@jessexai_](https://x.com/jessexai_), [@theaidesk_](https://x.com/theaidesk_), [@gadi_neelesh](https://x.com/gadi_neelesh), [@Haleeeemahh](https://x.com/Haleeeemahh), [@SPAC89](https://x.com/SPAC89), [@VeknQAQ](https://x.com/VeknQAQ), [@Aurora0x3f](https://x.com/Aurora0x3f), [@bei351009016](https://x.com/bei351009016), [@Stargridcompass](https://x.com/Stargridcompass), [@iamtheQwen](https://x.com/iamtheQwen), [@voxelbench](https://x.com/voxelbench), [@sshayahmet](https://x.com/sshayahmet), [@TimJayas](https://x.com/TimJayas), [@lucian__03](https://x.com/lucian__03), [@camperaigg](https://x.com/camperaigg), [@nickbaumann_](https://x.com/nickbaumann_), [@thtbee_](https://x.com/thtbee_), [@DeryaTR_](https://x.com/DeryaTR_), [@banteg](https://x.com/banteg), [@Leviwoyun](https://x.com/Leviwoyun), [@browser_use](https://x.com/browser_use), [@simonw](https://x.com/simonw), [@perplexity_ai](https://x.com/perplexity_ai), [@_3912657840](https://x.com/_3912657840), [@fawnunwrap](https://x.com/fawnunwrap), [@Angaisb_](https://x.com/Angaisb_), [@jony_palino](https://x.com/jony_palino), [@notjazii](https://x.com/notjazii), [@noclipepe](https://x.com/noclipepe), [@Super_Nius](https://x.com/Super_Nius), [@maxbittker](https://x.com/maxbittker), [@morsenxxx](https://x.com/morsenxxx), [@AdamHoltererer](https://x.com/AdamHoltererer), [@Clad3815](https://x.com/Clad3815), [@N1njaCodex](https://x.com/N1njaCodex), [@CodeByNZ](https://x.com/CodeByNZ), [@DanielZambrini](https://x.com/DanielZambrini), [@RezAIT00](https://x.com/RezAIT00), [@LuminaBench](https://x.com/LuminaBench), [@Jason85885174](https://x.com/Jason85885174), [@mspd4100](https://x.com/mspd4100), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@simonw](https://news.ycombinator.com/user?id=simonw)

*帰属または削除リクエストについては、ソース修正の問題を開いてください。*
