# mecab (with python3, Ubuntu 18.04)

```
sudo apt install swig
sudo apt install mecab-ipadic-utf8
sudo apt install mecab
sudo apt install libmecab-dev
pip3 install mecab-python3
```



```
$ ./main.py
庭      ニワ    庭      名詞-一般
に      ニ      に      助詞-格助詞-一般
は      ハ      は      助詞-係助詞
二      ニ      二      名詞-数
羽      ワ      羽      名詞-接尾-助数詞
、      、      、      記号-読点
鶏      ニワトリ        鶏      名詞-一般
が      ガ      が      助詞-格助詞-一般
い      イ      いる    動詞-自立       一段    連用形
ます    マス    ます    助動詞  特殊・マス      基本形
。      。      。      記号-句点
EOS
```
