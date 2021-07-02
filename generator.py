import yaml
from pprint import pprint


with open('schema.yml') as f:
    templates = yaml.safe_load(f)

# pprint(templates)

tables_list = list(templates)
# print(tables_list)
# print(list(templates.get(tables_list[0])))

for table_name in templates:
    # print(table_name)
    table_fields = templates.get(table_name).get('fields')
    # print(table_fields)
    # print(templates.get(table_name))
    # print(table_name)
    print('CREATE TABLE', table_name.lower(), '(')
    print(f'    {table_name.lower()}_id SERIAL PRIMARY KEY,')
    fields = len(table_fields)
    for field, value in table_fields.items():
        print(f'    {table_name.lower()}_{field} {value} NOT NULL', end='')
        if fields > 1:
            print(',')
            fields -= 1
    print('\n);')
