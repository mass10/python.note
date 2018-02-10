# Python 2

改行文字を付けずに文字列だけを出力する。

```
sys.stdout.write("文字列")
sys.stdout.write("\n")
```

# Python 3

タプルなどを表示した際の空白を付けないようにするには sep=""

```
print("文", "字", "列", sep="", end="")
```

終端の改行を付けたくないときは end=""

```
print("文字列を", end="")
```
