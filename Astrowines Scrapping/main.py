from datetime import date
from scrapinghelp import htmlhelper
from pandas.tests.io.excel.test_openpyxl import openpyxl
import os
from Mainlink import mainlink

from data import data
from extractdata import extractdata
# from Extractnew import Extractdata
store_list = []


def main(start, end):
    global dir_path
    global _zip
    global _job_number
    global store_id

    store_file = "Store_Info.xlsx"
    wb_store = openpyxl.load_workbook(store_file)
    sheet_store = wb_store.active

    for row in sheet_store.iter_rows(values_only=True):
        row_list = [row[0], row[1], row[2]]
        if row_list[0] is None:
            break
        else:
            store_list.append(row_list)
    for x in range(start, end + 1):
        _website = str(store_list[x][0])
        _Zip = str(store_list[x][1])
        _JobNumber = str(store_list[x][2])
        today = date.today()
        _Date = today.strftime("%m/%d/%Y")
        print(_Date)


        mainlink(_Zip, _JobNumber, _Date)
        data.data(_Zip,_JobNumber)
        extractdata.extractdata(_Zip,_JobNumber)






