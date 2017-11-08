# 日本語フォント ##########################################

日本語フォントを入れて

```
$ sudo apt install fonts-ipafont
```

それでも↓こうなったら

```
/usr/local/lib/python3.5/dist-packages/matplotlib/font_manager.py:1316: UserWarning: findfont: Font family ['IPAPGothic'] not found. Falling back to DejaVu Sans
  (prop.get_family(), self.defaultFamily[fontext]))
```

↓こうして再試行

```
$ rm -fr ~/.cache/matplotlib/
```
