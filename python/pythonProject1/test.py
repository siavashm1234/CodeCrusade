import openpyxl as xl
wb = xl.load_workbook("1000.xlsx")
sheet = wb['Sheet1']
cell =sheet['b1']
for row in range(4, 17):
    cell = sheet.cell(row , 3)
    print(cell)