import csv
class extract:
    def fromCSV(self, file_path):
        dataset = list()
        with open(file_path) as f:
            csv_file = csv.DictReader(f, delimiter=',')
            for row in csv_file:
                dataset.append(row) 
            return dataset   