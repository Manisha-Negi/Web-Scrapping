import datetime
from data import data
import time
from pandas.tests.io.excel.test_openpyxl import openpyxl
import os
#import UPC_based
#from UPC_based import extractdata1
# from mainlink import mainlink
from extractdata import extractdata
from mainlink import mainlink

store_list=[]

def _main(start, end):
    global dir_path
    global _zip
    global _job_number
    global _cookie
    global _Date
    #global store_id

    store_file = "Store_Info.xlsx"
    wb_store = openpyxl.load_workbook(store_file)
    sheet_store = wb_store.active

    for row in sheet_store.iter_rows(values_only=True):
        row_list = [row[0], row[1], row[2]]
        if row_list[0] == None:
            break
        else:
            store_list.append(row_list)
    for x in range(start, end + 1):
        _Zip = str(store_list[x][0])
        _JobNumber = str(store_list[x][1])
        _Cookie = str(store_list[x][2])
        _Date = datetime.date.today().strftime("%m/%d/%Y")
        start_time = time.time()
        #print(_Date)


        mainlink(_Cookie,_Date,_Zip,_JobNumber)
        data.data(_Cookie,_JobNumber)
        extractdata.extractdata(_Zip, _JobNumber)


        end_time = time.time()
        Consumed_time = end_time - start_time
        print("Total consumed time by code", Consumed_time)




#_main(1,3)