import csv

class extract:
    """
    A class to handle the extraction of data from CSV files.
    
    This class provides a method to read data from a CSV file and convert it into a list of dictionaries,
    where each dictionary represents a row in the CSV file.
    
    Attributes:
        None
    """

    def fromCSV(self, file_path):
        """
        Reads data from a CSV file and returns it as a list of dictionaries.
        
        This method opens the specified CSV file, reads its contents using the csv.DictReader,
        and appends each row as a dictionary to a list. The resulting list of dictionaries is then returned.
        
        Parameters:
            file_path (str): The path to the CSV file to be read.
            
        Returns:
            list: A list of dictionaries, where each dictionary represents a row in the CSV file.
        """
        dataset = list()
        with open(file_path) as f:
            csv_file = csv.DictReader(f, delimiter=',')
            for row in csv_file:
                dataset.append(row)
            return dataset