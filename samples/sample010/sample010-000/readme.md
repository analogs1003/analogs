# テキスト形式のログファイルを生成する

## 手法

- 英数文字をランダムに連結して単語を生成
- 単語を連結して文を生成

## ログファイルの作成方法

```
$ python3 sample010.py > tmp.txt
```

## 100Mbps のログファイルの作成方法

```
$ for ii in `seq 0 4`; do echo $ii; (python3 sample010.py > tmp$ii.txt &); done
$ kill ??? ??? ??? ??? ???
$ cat tmp?.txt | LC_ALL=C sort > tmp.txt
```
