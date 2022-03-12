

# 0> 可视化fst
#    1：可以查看/root/data/mys/data/G/normal_learn/transforfst2jpg.sh


path="/root/data/mys/data"
# 1> 生成L.fst
# 用到这个prepare_lang.sh工具
# 用到四个参数：
#    1：准备的四个文件（fix_data_dir.sh ./local/dict）
#    2：词典里没有的词，识别成什么（SIL）
#    3：临时会生成的一些东西
#    4：F.fst
# 必须在kaldi环境下跑，不然会报错的，所以先进入kaldi下样例的目录下
cd /root/data/mys/kaldi/egs/wsj/s5
utils/prepare_lang.sh ${path}/local/dict '<SIL>' ${path}/temp/01 ${path}/L/lang





# 生成G.fst
# 首先需要生成arpa格式的语言模型，再使用下面的命令，将arpa格式的语言模型转化为G.fst
#	1：cd /root/data/mys/data/G/normal/
#	2：ls一下，里面有一个get_lm.sh，里面会有很详细的注释
#	3：sh /root/data/mys/data/G/normal/get_lm.sh

# 语言模型的事儿了
#	1：是你上一步生成的lang文件夹，主要用的就是那个word.txt，意义不明
#	2：是你的arpa格式的语言模型
#	3：是你的输出的路径，会把第一个参数中对应的文件夹里的东西全部复制一份输出到你的输出
cd /root/data/mys/data
utils/format_lm_sri.sh L/lang/ G/normal/text.arpa G/normal/lang/


# 提取特征
# 提取特征：steps/make_mfcc.sh（需要在kaldi环境中跑）
# 	1：nj表示线程数量
#	2：mfcc的配置文件
#	3：kaldi前期准备的那四个文件
cd /root/data/mys/kaldi/egs/wsj/s5
steps/make_mfcc.sh --nj 1 --mfcc-config ./conf/mfcc.conf /root/data/mys/data/kaldi_file/


# CMVN
#
cd /root/data/mys/data
steps/compute_cmvn_stats.sh ./kaldi_file/




