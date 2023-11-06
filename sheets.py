import gspread
gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key('1vcdiUoWDiJk5Zbs7SqEijrRloykhbVPiVFxBO5DVhZc')
worksheet =sh.sheet1

# res = worksheet.get_all_records()
# res = worksheet.col_values(1)
# res = worksheet.row_values(1)
# res = worksheet.get('A2:C2')

user = ["Susan", 25, "Sydney"]
worksheet.append_row(user)

# worksheet.update_cell(6,2,30)

# worksheet.delete_rows(3)