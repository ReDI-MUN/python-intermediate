import csv
import os


# TODO: Add necessary logging setup and correct log-level statements to this whole program.
# TODO: This script is designed such that you need to use each log level.

def read_csv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        data = [row for row in reader]
    return data


def write_csv(file_path, data):
    with open(file_path, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data)


def process_data(data):
    processed_data = []
    for row in data:
        if not row:
            continue
        try:
            processed_row = [int(x) * 2 for x in row]
        except ValueError:
            continue
        processed_data.append(processed_row)
    return processed_data


def main():
    input_file_path = 'input.csv'
    output_file_path = 'output.csv'

    if not os.path.exists(input_file_path):
        return

    raw_data = read_csv(input_file_path)
    processed_data = process_data(raw_data)
    write_csv(output_file_path, processed_data)


if __name__ == "__main__":
    main()
