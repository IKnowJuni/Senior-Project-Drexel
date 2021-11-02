# import xlwings as xw
import os
import pandas as pd

cwd = os.path.abspath('')

files = os.listdir(cwd)

df_total = pd.DataFrame()

# loop through Excel files
for file in files:
    if file.endswith('.xlsx'):
        excel_file = pd.ExcelFile(file)
        sheets = excel_file.sheet_names
        # loop through sheets inside an Excel file
        for sheet in sheets:
            df = excel_file.parse(sheet_name = sheet)
            df_total = df_total.append(df)
df_total.to_excel('combined_file.xlsx', index=False)


# file = 'inoutnetgross.xlsx'
# try:
#     excelapp = xw.App(visible=False)
#     wb = excelapp.books.open(file)
#     for i in wb.sheets:
#         i.api.Copy()
#         newwb = xw.books.active
#         newwb.save(f'{i.name}.csv')
#         newwb.close()
# finally:
#     excelapp.quit()
## Method 1 gets the first sheet of a given file
# df = pd.DataFrame()
# for file in files:
#     if file.endswith('.xlsx'):
#         df = df.append(pd.read_excel(file), ignore_index=True) 
# df.head() 
# df.to_excel('total_sales.xlsx')

# # The END.
