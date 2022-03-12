import os

# 音频文本的路径
path_dir = "/root/data/mys/data/S0150/S0150_mic"

# 最终保存的路径
target_file="/root/data/mys/data/kaldi_file"


# 保存数据到文件中
def save_data(data, file_name):
  # 保存数据
  with open(os.path.join(target_file, file_name),'w',encoding="utf-8") as file:
    for item in data:
      # 一行一行的保存
      file.writelines(item)
      pass
  pass


# 生成utt2spk
"""
BAC009S0150W0500 S0150
BAC009S0252W0248 S0252
BAC009S0252W0493 S0252
"""
def get_utt2spk():
  # 用于保存结果的列表
  utt2spk = []
  
  # 遍历文件夹
  for file_name in os.listdir(path_dir):
    
    if file_name[-3:] == "wav":
      continue
    
    # 都是txt
    # 音频id
    utt = file_name.split(".")[0]
    # 说话人id
    spk = utt[-10:-6]
    # 添加到列表
    utt2spk.append(utt+" " + spk+"\n")
  
  # 保存数据
  save_data(utt2spk, "utt2spk")    



# 得到spk2utt
"""
S0150 BAC009S0150W0391 BAC009S0150W0500 BAC009S0150W0189 ...
S0252 BAC009S0252W0248 BAC009S0252W0297 BAC009S0252W0493 ...
{"S0150":[BAC009S0150W0391,BAC009S0150W0500,BAC009S0150W0189...],
"S0252":[BAC009S0252W0248,BAC009S0252W0297,BAC009S0252W0493...]
}
"""
def get_spk2utt():
  
  spk2utt = {}

  # 遍历
  for file_name in os.listdir(path_dir):
    if file_name[-3:0] == "txt":
      continue
    # 音频id
    utt = file_name.split(".")[0]
    # 说话人
    spk = utt[-10:-6]
    
    # 如果字典里面有这个人，则采用追加的方式
    if spk in spk2utt:
      spk2utt[spk].append(utt)
    # 如果字典里面没有这个人
    else:
      spk2utt[spk] = []
  
  # 最终输出打印的列表
  write_spk2utt = []
  for key in spk2utt.keys():
    # 写数据
    write_spk2utt.append(str(key)+" "+" ".join(spk2utt[key])+"\n")
  
  
  # 保存数据
  save_data(write_spk2utt, "spk2utt")



get_utt2spk()

get_spk2utt()





