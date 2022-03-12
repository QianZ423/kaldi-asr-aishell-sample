# 生成语言模型
# 需要指定你的语料
text="./text.txt"


# 1> 拿到语料
# awk '{for (i = 2; i <=NF; i++) printf("%s ",$i) printf("\n")}' text > xxx.lm
# 遍历列：
#   NF: 表示最后一列，
#   第0列是文本的一行内容
#   printf("")类似C语言


# 2> 统计词语出现的个数
#	-text：语料
#	-order：阶数
#	-write：写文件
ngram-count -text $text -order 3 -write text.count

# 3> 根据词语出现的个数，生成语言模型
#	-read：上面生成的write，统计词语出现的个数
#	-order：阶数
#	-lm：生成的语言模型名称
#	-interpolate：平滑
#	-kndiscount：回退概率
ngram-count -read text.count -order 3 -lm text.arpa -interpolate -kndiscount
















