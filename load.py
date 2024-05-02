import csv
from extract import extract  # Import the external extract class
from transform import transform  # Import the external transform class

class load:
    """
    A class to handle the loading of data into CSV files.
    
    This class provides a method to write a dataset to a CSV file, converting each dictionary in the dataset
    into a row in the CSV file. The keys of the dictionaries are used as field names in the CSV file.
    
    Attributes:
        None
    """

    def toCSV(self, file_path, dataset):
        """
        Writes a dataset to a CSV file.
        
        This method opens the specified CSV file in write mode, creates a CSV writer object with the fieldnames
        derived from the keys of the first dictionary in the dataset, writes the header row, and then writes the rows
        of the dataset to the CSV file.
        
        Parameters:
            file_path (str): The path to the CSV file to be written.
            dataset (list): A list of dictionaries, where each dictionary represents a row in the CSV file.
            
        Returns:
            None
        """
        with open(file_path, mode='w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=dataset[0].keys())
            writer.writeheader()
            writer.writerows(dataset)