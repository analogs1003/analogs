# 検索用のログファイルを作成する

## 手法

ファイルをコピー

## usage

```
$ cp logfile outfile
```

## result

### 生成にかかった時間

```
$ time cp ../../../input/test.log ../../../output/outfile.dat

real    0m0.034s
user    0m0.000s
sys     0m0.016s
```

### 生成されたファイルのサイズ(byte 数)

```
$ wc -lc ../../../input/test.log
   10056 11334473 ../../../input/test.log
```

```
$ wc -lc ../../../output/outfile.dat
   10056 11334473 ../../../output/outfile.dat
```
