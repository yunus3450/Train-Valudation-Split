import os
import random
import shutil
from sklearn.model_selection import train_test_split


data_path = "path/path/path" # resim ve .txt dosyları tek klasörde olmalı(Örneğin car(1).jpg ve car(1).txt aynı klasörde olmalı)

train_ratio = 0.8# train/val oranı

# dosya listesini oluşturun
files = os.listdir(data_path)#path'in içindeki tüm dosyaların listesini alan kod 
jpg_files = [f for f in files if f.endswith('.jpg')]
txt_files = [f for f in files if f.endswith('.txt')]

# train ve val dosya listelerini oluşturun
jpg_train, jpg_val, txt_train, txt_val = train_test_split(jpg_files, txt_files, train_size=train_ratio)

# train ve val klasörlerini oluşturun
train_path = os.path.join(data_path, 'train')
val_path = os.path.join(data_path, 'val')
os.makedirs(train_path, exist_ok=True)
os.makedirs(val_path, exist_ok=True)

# train ve val dosyalarını kopyalayın
for jpg_file, txt_file in zip(jpg_train, txt_train):
    shutil.copy(os.path.join(data_path, jpg_file), os.path.join(train_path, jpg_file))
    shutil.copy(os.path.join(data_path, txt_file), os.path.join(train_path, txt_file))

for jpg_file, txt_file in zip(jpg_val, txt_val):
    shutil.copy(os.path.join(data_path, jpg_file), os.path.join(val_path, jpg_file))
    shutil.copy(os.path.join(data_path, txt_file), os.path.join(val_path, txt_file))
