TSD_Dataset_DIR = 'TSD_Dataset'
TSD_Dataset_filepath = TSD_Dataset_DIR + '/MI Dataset_650_with_ITSD_and_NITSD.csv'
import csv

class TSD_MI_Dataset():

    def __init__(self):
        self.tests = {}

        with open(TSD_Dataset_filepath, 'r', encoding="utf8") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]

        for row in data:
            id = row['id']
            speech_turn = row['text']
            label = row['final agreed label']
            self.tests[id] = (id, speech_turn, label)


    def print_to_file(self, file_name):
        for id in self.tests:
            print(self.tests[id])
        # Specify the CSV file name
        csv_file = file_name

        with open(csv_file, 'w', newline='', encoding="utf8") as file:
            writer = csv.writer(file)

            # Writing rows
            for id in self.tests:
                try:
                    writer.writerow(self.tests[id])
                except:
                    writer.writerow("")

        print(f"CSV file '{csv_file}' has been created.")

if __name__ == '__main__':
    mi_dataset = TSD_MI_Dataset()
    for id in mi_dataset.tests:
        id, speech_turn, label = mi_dataset.tests[id]
        #print(speech_turn + " " +label)

    mi_dataset.print_to_file("out.csv")

