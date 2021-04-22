import os
from os import path

os.system('rm -rf result')
os.mkdir('result')

for dirpath, dirnames, filenames in os.walk("downloads"):
    os.chdir(dirpath)
    for filename in filenames:
        # 压缩文件
        cmd = 'rar a -v1.5g -sm5 -df "{rarfile}" "{sourcefile}"'.format(
            rarfile=path.join('../result', filename + '.rar'),
            sourcefile=filename
        )
        print("[deal] %s with %s" % (path.join(dirpath, filename), cmd))
        os.system(cmd)
        # 删除原始文件
    os.chdir('..')
