# 天気予報アプリケーション

シンプルで使いやすい天気予報 Web アプリケーションです。OpenWeatherMap API を使用して、世界中の都市の最新の天気情報と 3 時間ごとの予報を提供します。

## 機能

- 都市名による天気検索（日本語対応）
- 現在の天気状況の詳細表示（温度、湿度、風速、気圧など）
- 3 時間ごとの天気予報
- レスポンシブデザイン（モバイル、タブレット、デスクトップに対応）
- ダークモード UI で目に優しい表示

- ## 初期画面
![Image](https://github.com/user-attachments/assets/eae77dea-1502-4407-a700-51f5006ceee9)

##  検索後
![Image](https://github.com/user-attachments/assets/51b7e36b-8c6f-4db8-9d04-84ee8e105de8)

## 技術スタック

- **バックエンド**: Django 4.2.4
- **フロントエンド**: HTML, CSS (カスタムデザイン)
- **API**: OpenWeatherMap API
- **翻訳**: Google Translate API (日本語 → 英語の都市名変換)
- **コンテナ化**: Docker, Docker Compose

## 処理の流れ

1. **ユーザー入力**:

   - ユーザーが検索フォームに都市名（例: 「東京」、「ニューヨーク」）を入力
   - フォームが送信されると、POST リクエストが`weather/views.py`の`result`関数に送られる

2. **言語変換**:

   - 入力された都市名を`googletrans`ライブラリを使用して英語に変換
   - 例: 「東京」→「Tokyo」（OpenWeatherMap API は主に英語の都市名に対応）

3. **API 通信**:

   - 変換された都市名をパラメータとして OpenWeatherMap API にリクエスト
   - 3 時間ごとの天気予報データを取得
   - URL フォーマット: `api.openweathermap.org/data/2.5/forecast?q={都市名}&appid={APIキー}&lang=ja&units=metric`

4. **データ処理**:

   - API からのレスポンス JSON を解析
   - 現在の天気情報（温度、湿度、風速、気圧など）を抽出
   - 各日の最高気温・最低気温を計算
   - 適切な天気アイコンを選択

5. **データ集約**:

   - 3 時間ごとの予報データを日ごとにグループ化
   - 各日の代表的な天気状態とアイコンを決定
   - 各日の最高/最低気温を算出

6. **レンダリング**:

   - 処理されたデータをコンテキスト変数としてテンプレートに渡す
   - `results.html`テンプレートがデータを受け取り、HTML 形式で表示

7. **エラー処理**:
   - 都市が見つからない場合や通信エラーの場合は「見つかりませんでした」と表示
   - 例外発生時にはエラーログを記録

## フォルダ構造
<pre>
.
├── myproject
│ ├── **init**.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── static
│ └── css
│ └── style.css
├── templates
│ ├── weather
│ │ ├── home.html
│ │ └── results.html
│ └── base.html
├── weather
│ ├── migrations
│ │ └── **init**.py
│ ├── **init**.py
│ ├── admin.py
│ ├── apps.py
│ ├── key.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
├── compose.yaml
├── Dockerfile
├── manage.py
├── README.md
├── requirements.txt
└── .env
</pre>
## 主要ファイル

## weather/views.py - メインの処理ロジック

## templates/base.html - ベーステンプレート

## templates/weather/results.html - 天気結果表示テンプレート
