import os

# 音频文件的位置
target_dir = "/root/data/mys/data/S0150/S0150_mic"

# wav.scp文件保存的路径
save_path = "/root/data/mys/data/kaldi_file"

# wav_scp的数据
wav_scp = []

# 遍历音频
for file_name in os.listdir(target_dir):
  # 判断后缀名是否为wav
  if file_name[-3:] == "wav":
    # wav_scp放置数据
    wav_scp.append([file_name.split(".")[0],os.path.join(target_dir, file_name)])

# 保存wav_scp
with open(os.path.join(save_path,'wav.scp'),'w',encoding="utf-8") as file:
  # 遍历wav_scp一个一个保存
  for item in wav_scp:
    file.writelines(item[0]+" "+item[1]+"\n")














