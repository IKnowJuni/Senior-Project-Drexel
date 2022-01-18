import xlwings as xw

file = 'county-to-county-2015-2019-current-residence-sort.xlsx'

try:
    excelapp = xw.App(visible=False)
    wb = excelapp.books.open(file)
    for i in wb.sheets:
        i.api.Copy()
        newwb = xw.books.active
        newwb.save(f'{i.name}.xlsx')
        newwb.close()
finally:
    excelapp.quit()
