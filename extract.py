import csv
class extract:
    def fromCSV(self, file_path):
        dataset = list()
        try:
            with open(file_path, newline='') as f:
                csv_file = csv.DictReader(f, delimiter=',')
                for row in csv_file:
                    dataset.append(row)
            return dataset
        except FileNotFoundError:
            print(f"Error: File not found. Please check the file path: {file_path}")
            return []
        except csv.Error as e:
            print(f"Error: Issue with CSV parsing. {e}")
            return []
        except Exception as e:
            print(f"Unexpected error: {e}")
            return []