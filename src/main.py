# -*- coding: utf-8 -*-
import re, sys, os
import argparse, configparser

parser = argparse.ArgumentParser(description='测试')
parser.add_argument('-f', '--file', default='index.html', help='要转换的白页')

args = parser.parse_args()
print(args)

if os.path.isfile(args.file) == False:
  print('Error: %s' %('文件不存在或已删除，请选择正确的文件'))
  exit()

print(123123)


config = configparser.ConfigParser()
config.read('./conf/default.conf')

# 读取正则表达式
reges = {}
for key in config['rege']:
  reges[key] = re.compile(config['rege'][key])

# 替换白页
tpl = []
with open('./index.html', 'r', encoding="utf-8") as file:
  for i in file:
    for reguer in reges:
      i = re.sub(reges[reguer], reguer, i)
    tpl.append(i)

# 保存文件
f = open('index.tpl', 'w')
f.writelines(tpl)
f.close()




