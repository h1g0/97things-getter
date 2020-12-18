# 97things-getter

[プログラマが知るべき97のこと](https://ja.wikisource.org/wiki/%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9E%E3%81%8C%E7%9F%A5%E3%82%8B%E3%81%B9%E3%81%8D97%E3%81%AE%E3%81%93%E3%81%A8)というエッセイ集から、掲載されている107個のエッセイのタイトルとURLを取得してファイルに出力します。

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
