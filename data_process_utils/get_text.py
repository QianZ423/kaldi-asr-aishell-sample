import os
import jieba


# 数据文件目录
target_dir = "/root/data/mys/data/S0150/S0150_mic"

# 保存的text文件路径
#save_path = "/root/data/mys/data/kaldi_file"
save_path = "/root/data/mys/data/G/normal"

"""
BAC009S0252W0246 确保基金管理人与托管人风险准备金的合规管理运作
"""
# 分词的函数
def segment_item(data):
  return " ".join(jieba.cut(data))
  pass

# 文本列表
text = []

# 遍历所有文件
for filename in os.listdir(target_dir):
  # 判断文件是否以txt结尾
  if filename[-3:] != "txt":
    continue

  # 读取文本文件
  with open(os.path.join(target_dir,filename),'r',encoding='utf-8') as file:
    
    # 按行读取
    for line in file.readlines():
      # 去掉换行符号，以及去掉前后的空格
      line = line.strip("\n").strip()
      
      text.append([filename.split(".")[0], line])
 
    pass
  
  
  pass

#print(text)

with open(os.path.join(save_path,"text.segment"),'w',encoding='utf-8') as file:
  # 遍历列表，一个一个的保存
  for item in text:
    # 分词
    segment_list = segment_item(item[1])
    print(segment_list)

    # 一行一行的写
    #file.writelines(item[0] + " " + item[1] + "\n")
    # 语言模型的语料
    file.writelines(item[1] + "\n")




