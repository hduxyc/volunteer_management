import pandas as pd
from service.models.volunteers import db

excel_path = '../../data/volunteer.xlsx'

def get_excel_info(path = excel_path):
    rows_reader = pd.read_excel(path).iterrows()
    return rows_reader

def get_insert_sql():
    items = []
    for item in get_excel_info():
        #item = [db.escape_string(_) for _ in item]
        items.append(f"('{item[1][0]}', '{item[1][1]}', '{item[1][2]}', '{item[1][3]}', '{item[1][4]}', '{item[1][5]}', '{item[1][6]}', '{item[1][7]}')")

    valus = ', '.join(items)

    sql = f'''
    INSERT INTO
        volunteer_records(`id`, `name`, `class_no`, `sex`, `card_id`, `task`, `date`, `duration`)
    VALUES 
        {valus}
    '''

    row_id = db.insert(sql)
    print(f'{row_id}条数据插入完成')


if __name__ == '__main__':
    get_insert_sql()

