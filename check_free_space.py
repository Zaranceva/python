import shutil
from pathlib import Path
# вычесляем свободное место на диске.
# вычесляем размер директории
# копируем если есть свободное место.

# start config
dst_path = Path('c:/usr/') # папка назначения
src_path = Path('c:/kx/')  # папка что копируем
dest_disk_free_size = 0 # сколько должно остатся места.
folder_size = 0
disk_buffer = 0 # сколько свободного места должно остаться на диске
# end config

# свободное место на диске назначения
dest_disk_free_size = shutil.disk_usage(dst_path).free//1024//1024


def c_s_d (src_path):
    """ 
    Принемает Path объект места назначения и считает сумму всех файлов в директории
    и поддиректории.
    Возвращает размер папки в байтах.
    """
    total_size = 0
    for i in src_path.iterdir(): 
        if i.is_dir() :  total_size += c_s_d (i)
        if i.is_file() : total_size += i.stat().st_size
    return total_size

folder_size = c_s_d(src_path)//1024//1024

if dest_disk_free_size - disk_buffer - folder_size <0 :
    print ('нет свободного места на диске')
else:
    print('начинаем копирование папки', src_path, 'размером', folder_size,'mb' , 'в ', dst_path)
    shutil.copytree(src_path, dst_path, dirs_exist_ok=True)
print('копирование завершено')
