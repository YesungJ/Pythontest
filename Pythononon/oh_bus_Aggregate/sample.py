import pandas as pd
import numpy as np
import datetime as dt
import os, tkinter, tkinter.filedialog, tkinter.messagebox

#01_外国語サイト予約数
#ファイル読み込み
csv01_data_sheet1  = pd.read_excel('./2020/original/04/01_外国語サイト予約数（予約日・路線・便・言語別）_20200401-20200430.xlsx',sheet_name=0)
csv01_data_sheet2  = pd.read_excel('./2020/original/04/01_外国語サイト予約数（予約日・路線・便・言語別）_20200401-20200430.xlsx',sheet_name=1)
csv01_data_sheet3  = pd.read_excel('./2020/original/04/01_外国語サイト予約数（予約日・路線・便・言語別）_20200401-20200430.xlsx',sheet_name=2)
csv01_data_sheet4  = pd.read_excel('./2020/original/04/01_外国語サイト予約数（予約日・路線・便・言語別）_20200401-20200430.xlsx',sheet_name=3)

#日付指定
csv01_sheet1_cal=csv01_data_sheet1[(csv01_data_sheet1['予約日'] >= dt.datetime(2020,4,1))&(csv01_data_sheet1['予約日'] < dt.datetime(2020,5,1))]
csv01_sheet2_cal=csv01_data_sheet2[(csv01_data_sheet2['予約日'] >= dt.datetime(2020,4,1))&(csv01_data_sheet2['予約日'] < dt.datetime(2020,5,1))]
csv01_sheet3_cal=csv01_data_sheet3[(csv01_data_sheet3['予約日'] >= dt.datetime(2020,4,1))&(csv01_data_sheet3['予約日'] < dt.datetime(2020,5,1))]
csv01_sheet4_cal=csv01_data_sheet4[(csv01_data_sheet4['予約日'] >= dt.datetime(2020,4,1))&(csv01_data_sheet4['予約日'] < dt.datetime(2020,5,1))]

#予約数の総数
csv01_sheet1_sum=csv01_sheet1_cal['予約数'].sum()
csv01_sheet2_sum=csv01_sheet2_cal['予約数'].sum()
csv01_sheet3_sum=csv01_sheet3_cal['予約数'].sum()
csv01_sheet4_sum=csv01_sheet4_cal['予約数'].sum()

print("------------------------------------------------------------")
print("01_外国語サイト予約数[予約日・路線・便・言語別](sheet1):"+str(csv01_sheet1_sum))
print("01_外国語サイト予約数[予約日・路線・便・言語別](sheet2):"+str(csv01_sheet2_sum))
print("01_外国語サイト予約数[予約日・路線・便・言語別](sheet3):"+str(csv01_sheet3_sum))
print("01_外国語サイト予約数[予約日・路線・便・言語別](sheet4):"+str(csv01_sheet4_sum))

#02_外国語サイト予約数
#ファイル読み込み
csv02_data_sheet1  = pd.read_excel('./2020/original/04/02_外国語サイト予約数（乗車日・路線・便・言語別）_20200401-20200430.xlsx',sheet_name=0)
csv02_data_sheet2  = pd.read_excel('./2020/original/04/02_外国語サイト予約数（乗車日・路線・便・言語別）_20200401-20200430.xlsx',sheet_name=1)
csv02_data_sheet3  = pd.read_excel('./2020/original/04/02_外国語サイト予約数（乗車日・路線・便・言語別）_20200401-20200430.xlsx',sheet_name=2)
csv02_data_sheet4  = pd.read_excel('./2020/original/04/02_外国語サイト予約数（乗車日・路線・便・言語別）_20200401-20200430.xlsx',sheet_name=3)

#日付指定
csv02_sheet1_cal=csv02_data_sheet1[(csv02_data_sheet1['運行日'] >= dt.datetime(2020,4,1))&(csv02_data_sheet1['運行日'] < dt.datetime(2020,5,1))]
csv02_sheet2_cal=csv02_data_sheet2[(csv02_data_sheet2['運行日'] >= dt.datetime(2020,4,1))&(csv02_data_sheet2['運行日'] < dt.datetime(2020,5,1))]
csv02_sheet3_cal=csv02_data_sheet3[(csv02_data_sheet3['運行日'] >= dt.datetime(2020,4,1))&(csv02_data_sheet3['運行日'] < dt.datetime(2020,5,1))]
csv02_sheet4_cal=csv02_data_sheet4[(csv02_data_sheet4['運行日'] >= dt.datetime(2020,4,1))&(csv02_data_sheet4['運行日'] < dt.datetime(2020,5,1))]

#予約数の総数
csv02_sheet1_sum=csv02_sheet1_cal['乗車人数'].sum()
csv02_sheet2_sum=csv02_sheet2_cal['乗車人数'].sum()
csv02_sheet3_sum=csv02_sheet3_cal['乗車人数'].sum()
csv02_sheet4_sum=csv02_sheet4_cal['乗車人数'].sum()

print("------------------------------------------------------------")
print("02_外国語サイト予約数[乗車日・路線・便・言語別](sheet1):"+str(csv02_sheet1_sum))
print("02_外国語サイト予約数[乗車日・路線・便・言語別](sheet2):"+str(csv02_sheet2_sum))
print("02_外国語サイト予約数[乗車日・路線・便・言語別](sheet3):"+str(csv02_sheet3_sum))
print("02_外国語サイト予約数[乗車日・路線・便・言語別](sheet4):"+str(csv02_sheet4_sum))

#11_新外国語サイト予約数
#ファイル読み込み
csv11_data_sheet1  = pd.read_excel('./2020/original/04/11_新外国語サイト予約数（予約日・路線・便・言語別）_20200401-20200430.xlsx',sheet_name=0)
csv11_data_sheet2  = pd.read_excel('./2020/original/04/11_新外国語サイト予約数（予約日・路線・便・言語別）_20200401-20200430.xlsx',sheet_name=1)
csv11_data_sheet3  = pd.read_excel('./2020/original/04/11_新外国語サイト予約数（予約日・路線・便・言語別）_20200401-20200430.xlsx',sheet_name=2)
csv11_data_sheet4  = pd.read_excel('./2020/original/04/11_新外国語サイト予約数（予約日・路線・便・言語別）_20200401-20200430.xlsx',sheet_name=3)

#日付指定
csv11_sheet1_cal=csv11_data_sheet1[(csv11_data_sheet1['予約日'] >= dt.datetime(2020,4,1))&(csv11_data_sheet1['予約日'] < dt.datetime(2020,5,1))]
csv11_sheet2_cal=csv11_data_sheet2[(csv11_data_sheet2['予約日'] >= dt.datetime(2020,4,1))&(csv11_data_sheet2['予約日'] < dt.datetime(2020,5,1))]
csv11_sheet3_cal=csv11_data_sheet3[(csv11_data_sheet3['予約日'] >= dt.datetime(2020,4,1))&(csv11_data_sheet3['予約日'] < dt.datetime(2020,5,1))]
csv11_sheet4_cal=csv11_data_sheet4[(csv11_data_sheet4['予約日'] >= dt.datetime(2020,4,1))&(csv11_data_sheet4['予約日'] < dt.datetime(2020,5,1))]

#予約数の総数
csv11_sheet1_sum=csv11_sheet1_cal['予約数'].sum()
csv11_sheet2_sum=csv11_sheet2_cal['予約数'].sum()
csv11_sheet3_sum=csv11_sheet3_cal['予約数'].sum()
csv11_sheet4_sum=csv11_sheet4_cal['予約数'].sum()

print("------------------------------------------------------------")
print("11_新外国語サイト予約数[予約日・路線・便・言語別](sheet1):"+str(csv11_sheet1_sum))
print("11_新外国語サイト予約数[予約日・路線・便・言語別](sheet2):"+str(csv11_sheet2_sum))
print("11_新外国語サイト予約数[予約日・路線・便・言語別](sheet3):"+str(csv11_sheet3_sum))
print("11_新外国語サイト予約数[予約日・路線・便・言語別](sheet4):"+str(csv11_sheet4_sum))


#12_新外国語サイト予約数
#ファイル読み込み
csv12_data_sheet1  = pd.read_excel('./2020/original/04/12_新外国語サイト予約数（乗車日・路線・便・言語別）_20200401-20200430.xlsx',sheet_name=0)
csv12_data_sheet2  = pd.read_excel('./2020/original/04/12_新外国語サイト予約数（乗車日・路線・便・言語別）_20200401-20200430.xlsx',sheet_name=1)
csv12_data_sheet3  = pd.read_excel('./2020/original/04/12_新外国語サイト予約数（乗車日・路線・便・言語別）_20200401-20200430.xlsx',sheet_name=2)
csv12_data_sheet4  = pd.read_excel('./2020/original/04/12_新外国語サイト予約数（乗車日・路線・便・言語別）_20200401-20200430.xlsx',sheet_name=3)

#日付指定
csv12_sheet1_cal=csv12_data_sheet1[(csv12_data_sheet1['運行日'] >= dt.datetime(2020,4,1))&(csv12_data_sheet1['運行日'] < dt.datetime(2020,5,1))]
csv12_sheet2_cal=csv12_data_sheet2[(csv12_data_sheet2['運行日'] >= dt.datetime(2020,4,1))&(csv12_data_sheet2['運行日'] < dt.datetime(2020,5,1))]
csv12_sheet3_cal=csv12_data_sheet3[(csv12_data_sheet3['運行日'] >= dt.datetime(2020,4,1))&(csv12_data_sheet3['運行日'] < dt.datetime(2020,5,1))]
csv12_sheet4_cal=csv12_data_sheet4[(csv12_data_sheet4['運行日'] >= dt.datetime(2020,4,1))&(csv12_data_sheet4['運行日'] < dt.datetime(2020,5,1))]

#予約数の総数
csv12_sheet1_sum=csv12_sheet1_cal['乗車人数'].sum()
csv12_sheet2_sum=csv12_sheet2_cal['乗車人数'].sum()
csv12_sheet3_sum=csv12_sheet3_cal['乗車人数'].sum()
csv12_sheet4_sum=csv12_sheet4_cal['乗車人数'].sum()

print("------------------------------------------------------------")
print("12_新外国語サイト予約数[乗車日・路線・便・言語別](sheet1):"+str(csv12_sheet1_sum))
print("12_新外国語サイト予約数[乗車日・路線・便・言語別](sheet2):"+str(csv12_sheet2_sum))
print("12_新外国語サイト予約数[乗車日・路線・便・言語別](sheet3):"+str(csv12_sheet3_sum))
print("12_新外国語サイト予約数[乗車日・路線・便・言語別](sheet4):"+str(csv12_sheet4_sum))
print("------------------------------------------------------------")

# データフレームを作成
df = pd.DataFrame([["0001", "John", "Engineer"],["0002", "Lily", "Sales"]],columns=['id', 'name', 'job'])

# CSV ファイル 4月集計 として出力
df.to_csv("keio_April".csv")

#korekara
