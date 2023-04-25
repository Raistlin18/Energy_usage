import csv
import sys

def get_dicts_from_csv(file_name):
    csv_list = []
    try:
        with open(file_name, 'r', encoding='utf-8') as forras:
            for i in csv.DictReader(forras):
                csv_list.append(i)

    except OSError:
        sys.exit('Hiba a fájl kezelése közben!')

    else:
        csv_list = sorted(csv_list, key=lambda x: float(x['Primary energy consumption per capita (kWh/person)']), reverse=True)
        return tuple(csv_list)


