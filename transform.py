import csv
class transform:
    def head(self, dataset, steps):  # Return the top N records from the dataset
        try:
            return dataset[:steps]
        except TypeError as e:
            print(f"Error in head method: {e}")
            return dataset

    def tail(self, dataset, steps):  # Return the last N records from the dataset
        try:
            return dataset[-steps:]
        except TypeError as e:
            print(f"Error in tail method: {e}")
            return dataset

    def rename_attribute(self, dataset, old_name, new_name):  # Rename a column in the dataset
        try:
            new_dataset = []
            for row in dataset:
                new_row = row.copy()
                if old_name in row:
                    new_row[new_name] = new_row[old_name]
                new_dataset.append(new_row)
            return new_dataset
        except KeyError as e:
            print(f"Error in rename_attribute method: {e}")
            return dataset

    def remove_attribute(self, dataset, column_to_remove):  # Remove a column from the dataset
        try:
            return [
                {key: value for key, value in row.items() if key!= column_to_remove} for row in dataset
            ]
        except KeyError as e:
            print(f"Error in remove_attribute method: {e}")
            return dataset

    def rename_attributes(self, dataset, old_names, new_names):  # Rename a list of columns in the dataset
        try:
            new_dataset = []
            for row in dataset:
                new_row = row.copy()
                for i, (old_name, new_name) in enumerate(zip(old_names, new_names)):
                    if old_name in row:
                        new_row[new_name] = new_row[old_name]
                        del new_row[old_name]
                new_dataset.append(new_row)
            return new_dataset
        except KeyError as e:
            print(f"Error in rename_attributes method: {e}")
            return dataset

    def remove_attributes(self, dataset, columns_to_remove):  # Remove a list of columns in the dataset
        try:
            new_dataset = [{key:value for key,value in row.items() if key not in columns_to_remove} 
                           for row in dataset]
            return new_dataset
        except KeyError as e:
            print(f"Error in remove_attributes method: {e}")
            return dataset

    def transform(self, dataset, columns_to_remove=None, renames=None):
        try:
            new_dataset = dataset[:]
            # Remove attributes
            if columns_to_remove is not None:
                new_dataset = self.remove_attributes(new_dataset, columns_to_remove)
            # Rename attributes
            if renames is not None:
                new_dataset = self.rename_attributes(new_dataset, list(renames.keys()), list(renames.values()))
            return new_dataset
        except Exception as e:
            print(f"Error in transform method: {e}")
            return dataset

    def add_full_state_name(self, dataset, states_path): # Add a a new column with full state name
        try:
            with open(states_path, newline='') as csv_file:
                reader = csv.DictReader(csv_file)
                state_dict = {row['Abbreviation'] : row['State'] for row in reader}
                
                for row in dataset:
                    state = row.get('State')
                    if state in state_dict:
                        row['State Name'] = state_dict[state]     
            return dataset
        except FileNotFoundError as e:
            print(f"Error in add_full_state_name method: {e}")
            return dataset
        except csv.Error as e:
            print(f"Error in add_full_state_name method: {e}")
            return dataset