TSD_Dataset_DIR = 'TSD_Dataset'
TSD_Dataset_filepath = TSD_Dataset_DIR + '/TSD_Dataset.csv'
import csv

class TSD_Parser():

    def __init__(self):
        self.tests = {}

        with open(TSD_Dataset_filepath, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]
        id = 0
        for row in data:
            id += 1
            speech_turn = row['speech_turn']
            label = row['label']
            self.tests[id] = (speech_turn, label)


if __name__ == '__main__':
    tsd_parser = TSD_Parser()
    for id in tsd_parser.tests:
        speech_turn, label = tsd_parser.tests[id]
        print(speech_turn + " " +label)