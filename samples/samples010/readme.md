## ログファイルの作成方法

```
$ python3 sample010.py > tmp.txt
```

## 100Mbps のファイルの作成方法

```
$ for ii in `seq 0 4`; do echo $ii; (python3 sample010.py > tmp$ii.txt &); done
$ kill ??? ??? ??? ??? ???
$ cat tmp?.txt | LC_ALL=C sort > tmp.txt
```
