from extract import extract # import the external extract class
import csv

class transform:
    """
    A class to perform transformations on datasets.

    Attributes:
        None

    Methods:
        head(dataset, steps): Returns the top N records from the dataset.
        tail(dataset, steps): Returns the last N records from the dataset.
        rename_attribute(dataset, old_name, new_name): Renames a column in the dataset.
        remove_attribute(dataset, column_to_remove): Removes a column from the dataset.
        rename_attributes(dataset, old_names, new_names): Renames a list of columns in the dataset.
        remove_attributes(dataset, columns_to_remove): Removes a list of columns in the dataset.
        transform(dataset, columns_to_remove=None, renames=None): Transforms the dataset by removing and/or renaming attributes.
        add_full_state_name(dataset, states_path): Adds full state names to the dataset using an external CSV file.
    """
    def head(self, dataset, steps): #return the top N records from the dataset
        """
        Returns the top N records from the dataset.

        Args:
            dataset (list[dict]): The dataset to be transformed.
            steps (int): The number of records to return from the top.

        Returns:
            list[dict]: The top N records from the dataset.
        """
        return dataset[:steps]
            
    def tail(self, dataset, steps): #return the last N records from the dataset
        """
        Returns the last N records from the dataset.

        Args:
            dataset (list[dict]): The dataset to be transformed.
            steps (int): The number of records to return from the end.

        Returns:
            list[dict]: The last N records from the dataset.
        """
        return dataset[-steps:]
            
    def rename_attribute(self, dataset, old_name, new_name): #rename a column in the dataset
        """
        Renames a column in the dataset.

        Args:
            dataset (list[dict]): The dataset to be transformed.
            old_name (str): The current name of the column.
            new_name (str): The new name for the column.

        Returns:
            list[dict]: The dataset with the renamed column.
        """
        new_dataset = []
        for row in dataset:
            new_row = row.copy()
            if old_name in row:
                new_row[new_name] = new_row[old_name]
            new_dataset.append(new_row)
        return new_dataset
    
    def remove_attribute(self, dataset, column_to_remove): #remove a column from the dataset
        """
        Removes a column from the dataset.

        Args:
            dataset (list[dict]): The dataset to be transformed.
            column_to_remove (str): The name of the column to remove.

        Returns:
            list[dict]: The dataset with the specified column removed.
        """
        return [
            {key: value for key, value in row.items() if key != column_to_remove} for row in dataset
        ]
    
    def rename_attributes(self, dataset, old_names, new_names): #rename a list of columns in the dataset
        """
        Renames a list of columns in the dataset.

        Args:
            dataset (list[dict]): The dataset to be transformed.
            old_names (list[str]): The current names of the columns to be renamed.
            new_names (list[str]): The new names for the columns.

        Returns:
            list[dict]: The dataset with the specified columns renamed.
        """
        new_dataset = []
        for row in dataset:
            new_row = row.copy()
            for i, (old_name, new_name) in enumerate(zip(old_names, new_names)):
                if old_name in row:
                    new_row[new_name] = new_row[old_name]
                    del new_row[old_name]
            new_dataset.append(new_row)
        return new_dataset
    
    def remove_attributes(self, dataset, columns_to_remove): #remove a list of columns in the dataset
        """
        Removes a list of columns in the dataset.

        Args:
            dataset (list[dict]): The dataset to be transformed.
            columns_to_remove (list[str]): The names of the columns to remove.

        Returns:
            list[dict]: The dataset with the specified columns removed.
        """
        new_dataset = [{key:value for key,value in row.items() if key not in columns_to_remove} 
                       for row in dataset]
        return new_dataset
            
    def transform(self, dataset, columns_to_remove=None, renames=None):
        """
        Transforms the dataset by removing and/or renaming attributes.

        Args:
            dataset (list[dict]): The dataset to be transformed.
            columns_to_remove (list[str], optional): The names of the columns to remove. Defaults to None.
            renames (dict, optional): A dictionary mapping old column names to new column names. Defaults to None.

        Returns:
            list[dict]: The transformed dataset.
        """
        new_dataset = dataset[:]
        # Remove attributes
        if columns_to_remove is not None:
            new_dataset = self.remove_attributes(new_dataset, columns_to_remove)
        # Rename attributes
        if renames is not None:
            new_dataset = self.rename_attributes(new_dataset, list(renames.keys()), list(renames.values()))
        return new_dataset
    
    def add_full_state_name(self, dataset, states_path):
        """
        Adds full state names to the dataset using an external CSV file.

        Args:
            dataset (list[dict]): The dataset to be transformed.
            states_path (str): The path to the CSV file containing state abbreviations and full names.

        Returns:
            list[dict]: The dataset with full state names added.
        """
        with open(states_path, newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            state_dict = {row['Abbreviation'] : row['State'] for row in reader}
            
            for row in dataset:
                state = row.get('State')
                if state in state_dict:
                    row['State Name'] = state_dict[state]     
        return dataset