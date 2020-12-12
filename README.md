# 97things-getter

[プログラマが知るべき97のこと](https://xn--97-273ae6a4irb6e2hsoiozc2g4b8082p.com/)というサイトから、掲載されている107個のエッセイのタイトルとURLを取得してファイルに出力します。

また、bit.lyを使用し、URLを短縮して出力することも可能です。

## 動作に必要な環境

- Python3.6以上
- requests-html（`pip3 install requests_html`でインストール）

## 使用法

```bash
$ python main.py
```

を実行すると、`result.txt`に結果が出力されます。

## URLを短縮する場合

1. bit.lyでアカウントを作り、access tokenを取得しておく
2. `main.py`と同じディレクトリに`access_token.txt`を作成し、中に取得したaccess_tokenを記述しておく
3. `main.py`の`make_url_short = False`を`True`に変える
4. `main.py`を実行
