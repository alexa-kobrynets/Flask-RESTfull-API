from datetime import datetime
import xml.etree.ElementTree as ET



ABBR_FILENAME = 'abbreviations.txt'
START_FILENAME = 'start.log'
END_FILENAME = 'end.log'
POS_DELIMITER = 16


def read_file(path):
    with open(path, 'r') as file_input:
        return file_input.read().splitlines()


def time_count(start_time, end_time):
    end = datetime.strptime(end_time, '%Y-%m-%d_%H:%M:%S.%f')
    start = datetime.strptime(start_time,'%Y-%m-%d_%H:%M:%S.%f')
    return end - start


def read_abbr(path_abbr):
    raw_abbr = read_file(path_abbr)
    result = {}
    for line in raw_abbr:
        result[line.split('_')[0]] = {'name': line.split('_')[1], 'team': line.split('_')[2]}
    return result


def read_log(path_log):
    raw_log = read_file(path_log)
    result = {}
    for line in raw_log:
        result[line[:3]] = line[3:]

    return result


def build_report(folder):
    abbr = read_abbr(folder / ABBR_FILENAME)
    start = read_log(folder / START_FILENAME)
    end = read_log(folder / END_FILENAME)
    for i in start:
        abbr[i]['time'] = str(time_count(start[i], end[i]))
    return abbr


def sort_report(data):
    res = dict(sorted(data.items(), key=lambda item: item[1]['time']))
    for place, team in enumerate(res, 1):
        res[team]['place_asc'] = place
        res[team]['place_desc'] = len(res) - place
    return res


def print_driver(data, abbr):
    print(data[abbr]['name'],  '|', data[abbr]['team'], '|', data[abbr]['time'])


def main_func(folder):
    data = build_report(folder)
    return data


def form_xml_drivers(data):
    results = ET.Element("results")
    for line in data:
        result = ET.SubElement(results, "result")
        abbr = ET.SubElement(result, "abbreviation")
        name = ET.SubElement(result, "name")
        name.text = data[line]['name']
        abbr.text = str(data[line]['abbreviation'])
    tree = ET.ElementTree(results)
    return tree


def form_xml_report(data, driver=None):
    results = ET.Element("results")
    for num, line in enumerate(data, 1):
        result = ET.SubElement(results, "result")
        name = ET.SubElement(result, "name")
        team = ET.SubElement(result, "team")
        time = ET.SubElement(result, "time")
        place = ET.SubElement(result, "place")
        if driver:
            name.text = line.name
            team.text = line.team
            time.text = str(line.time)
            place.text = str(num)
        else:
            name.text = line.name
            team.text = line.abbr
            time.text = str(line.time)
            place.text = str(num)
    tree = ET.ElementTree(results)
    return tree


if __name__ == '__main__':
    main_func()
