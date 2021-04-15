'''
with open("Study20Data02.csv","a",encoding="utf_8") as file:
    file.write("ABC")
    file.write("DEF\n")
    file.write("GHI\n")
'''
'''
#writeLinesメソッド
wdays = ("sun\n","mon\n","the\n","wed\n","thu\n")
with open("Study20Data03.csv","a",encoding="utf_8") as file:
    file.writelines(wdays)

'''

#ファイルの確認
import os
file_name = "Study20Data04.csv"
if os.path.exists(file_name):
    print(file_name+"は存在します")

else:
    print(file_name+"は存在しません")