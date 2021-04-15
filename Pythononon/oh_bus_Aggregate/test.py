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
csv01_sheet1_cal=csv01_data_sheet1[(csv01_data_sheet1.iloc[:,2] >= dt.datetime(2020,4,1))&(csv01_data_sheet1.iloc[:,2] < dt.datetime(2020,5,1))]
csv01_sheet2_cal=csv01_data_sheet2[(csv01_data_sheet2.B >= dt.datetime(2020,4,1))&(csv01_data_sheet2.B < dt.datetime(2020,5,1))]
csv01_sheet3_cal=csv01_data_sheet3[(csv01_data_sheet3.B >= dt.datetime(2020,4,1))&(csv01_data_sheet3.B < dt.datetime(2020,5,1))]
csv01_sheet4_cal=csv01_data_sheet4[(csv01_data_sheet4.B >= dt.datetime(2020,4,1))&(csv01_data_sheet4.B < dt.datetime(2020,5,1))]
#予約数の総数
csv01_sheet1_sum=csv01_sheet1_cal.D.sum()
csv01_sheet2_sum=csv01_sheet2_cal.D.sum()
csv01_sheet3_sum=csv01_sheet3_cal.D.sum()
csv01_sheet4_sum=csv01_sheet4_cal.D.sum()

print("------------------------------------------------------------")
print("01_外国語サイト予約数[予約日・路線・便・言語別](sheet1):"+str(csv01_sheet1_sum))
print("01_外国語サイト予約数[予約日・路線・便・言語別](sheet2):"+str(csv01_sheet2_sum))
print("01_外国語サイト予約数[予約日・路線・便・言語別](sheet3):"+str(csv01_sheet3_sum))
print("01_外国語サイト予約数[予約日・路線・便・言語別](sheet4):"+str(csv01_sheet4_sum))