

# 得到语言模型的语料->使用txt生成
file_name = "/root/data/mys/data/kaldi_file/text"

# 读取文件
with open(file_name, 'r', encoding="utf-8") as file:
  
  for item in file.readlines():

    print(" ".join(item.strip("\n").strip().split(" ")[1:]))
    
    pass
  


  pass










