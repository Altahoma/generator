import yaml


def create_table_sql(table_name, templates):
    table = (
        'CREATE TABLE {table_name} (\n'
        '    {table_name}_id SERIAL PRIMARY KEY,\n'
        '    {table_name}_created timestamp DEFAULT CURRENT_TIMESTAMP NOT NULL,\n'
        '    {table_name}_updated timestamp,\n'
    ).format(table_name=table_name.lower())
    table_fields = templates.get(table_name).get('fields')
    fields = len(table_fields)
    for field, value in table_fields.items():
        table += '    {table_name}_{field} {value} NOT NULL'.format(
            table_name=table_name.lower(),
            field=field,
            value=value
        )
        if fields > 1:
            table += ',\n'
            fields -= 1
    table += '\n);'
    return table


def create_function_sql(table_name):
    function = (
        'CREATE OR REPLACE FUNCTION update_{table_name}_updated() RETURNS trigger AS $$\n'
        '    BEGIN\n'
        '        new.{table_name}_updated = CURRENT_TIMESTAMP;\n'
        '    BEGIN\n'
        '$$ LANGUAGE plpgsql;'
    ).format(table_name=table_name.lower())
    return function


def create_trigger_sql(table_name):
    trigger = (
        'CREATE TRIGGER tr_{table_name}_updated BEFORE UPDATE ON article\n'
        '    FOR EACH ROW EXECUTE FUNCTION update_{table_name}_updated();'
    ).format(table_name=table_name.lower())
    return trigger


def parser():
    print('Please enter the file name in the format ".yml" (For example: "schema.yml")')
    schema = input()
    with open(schema) as file:
        templates = yaml.safe_load(file)

        for table in templates:
            print(create_table_sql(table, templates))
            print(create_function_sql(table))
            print(create_trigger_sql(table))


parser()
