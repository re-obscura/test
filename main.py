import pandas as pd

def get_records(table_name, field_name):
    # Читаем таблицу
    df = pd.read_csv(table_name)

    # Возвращаем все записи по полученному полю
    return df[field_name].tolist()

# Пример использования функции
records = get_records('table.csv', 'Имя')
print(records)
