#!/usr/bin/python

import pandas as pd

# code which can be resued
excel_writer = pd.ExcelWriter('test_excel_out.xlsx')
test_data_frame = pd.DataFrame(range(10))
test_data_frame.to_excel(excel_writer, sheet_name = 'test_sheet_name', header = False,index = False)
excel_writer.save()

