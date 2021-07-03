import yaml


def create_table_sql(schema):
    table_fields = templates.get(table_name).get('fields')
    print(f'CREATE TABLE {table_name.lower()} (')
    print(f'    {table_name.lower()}_id SERIAL PRIMARY KEY,')
    print(f'    {table_name.lower()}_created timestamp DEFAULT CURRENT_TIMESTAMP NOT NULL,')
    print(f'    {table_name.lower()}_updated timestamp,')
    fields = len(table_fields)
    for field, value in table_fields.items():
        print(f'    {table_name.lower()}_{field} {value} NOT NULL', end='')
        if fields > 1:
            print(',')
            fields -= 1
    print('\n);')


def create_function_sql(schema):
    pass


def create_trigger_sql(schema):
    pass


# add UI as 'Please type the file name in format ".yml" (For example: "schema.yml")
with open('schema.yml') as f:
    templates = yaml.safe_load(f)

for table_name in templates:
    create_table_sql(table_name)
