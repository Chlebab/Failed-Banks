import csv
from extract import extract # import the external extract class
from transform import transform # import the external transform class

class load:
    def toCSV(self, file_path, dataset):
        with open(file_path, mode='w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames = dataset[0].keys())
            writer.writeheader()
            writer.writerows(dataset)