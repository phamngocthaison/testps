# -*- coding: utf-8 -*-
import xlrd
import json
import xlsxwriter

wb = xlrd.open_workbook("fresh_config.xls")
sheet = wb.sheet_by_index(0)
out = []
for r in range(1, sheet.nrows):
    row = sheet.row(r)
    seller_id = int(row[0].value)
    seller_name = row[1].value
    wr = [seller_id, seller_name]
    datas = json.loads(row[2].value)
    for d in datas:
        if d.get('city_id') == 294:
            leadtime_items = filter(lambda x: int(x['leadtime']) > 0, d.get('leadtime_item'))
            districts = ','.join(map(lambda x: x.get('district_name'), leadtime_items))
            wr.extend([len(d.get('leadtime_item', [])), districts])
            out.append(wr)
            if seller_id == 200702:
                pass
workbook = xlsxwriter.Workbook('config.xlsx')
worksheet = workbook.add_worksheet()

for r, data in enumerate(out):
    print r, data
    worksheet.write_row(r, 0, data)
workbook.close()
