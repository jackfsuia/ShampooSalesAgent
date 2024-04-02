import csv
from utils.file_decoding import custom_open as custom_open
def count_order_lines_in_csv(file_path ):
    line_count=0
    with custom_open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for _ in csvfile:
            line_count += 1
        csvfile.close()
    return line_count-1

    