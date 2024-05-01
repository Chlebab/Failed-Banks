import csv
from extract import extract # import the external extract class
from transform import transform # import the external transform class

class load:
    def toCSV(self, file_path, dataset):
        try:
            with open(file_path, mode='w', newline='') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=dataset[0].keys())
                writer.writeheader()
                writer.writerows(dataset)
        except FileNotFoundError:
            print(f"Error: File not found. Please check the file path: {file_path}")
        except PermissionError:
            print(f"Error: Permission denied. Cannot write to the file at {file_path}")
        except csv.Error as e:
            print(f"Error: Issue with CSV writing. {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")