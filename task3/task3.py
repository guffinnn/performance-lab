import json
from collections import defaultdict


def read_data_from_file(file):
    with open(file, 'r') as file:
        data = json.load(file)
        return data


def main(values, tests, report):
    values_data = read_data_from_file(file=values)
    tests_data = read_data_from_file(file=tests)

    values_dict = {test_id: value for test_id, value in values_data.items()}

    report_data = defaultdict(dict)

    for test_id, test_info in tests_data.items():
        if test_id in values_dict:
            test_info['value'] = values_dict[test_id]
        report_data[test_id] = test_info

    with open(report, 'w') as report_file:
        json.dump(report_data, report_file, indent=4)


if __name__ == '__main__':
    main(values='values.json', tests='tests.json', report='report.json')
