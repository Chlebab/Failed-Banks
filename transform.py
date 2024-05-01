class transform:
    def head(self, dataset, steps): #return the top N records from the dataset
        return dataset[:steps]
            
    def tail(self, dataset, steps): #return the last N records from the dataset
        return dataset[-steps:]
            
    def rename_attribute(self, dataset, old_name, new_name): #rename a column in the dataset
        new_dataset = []
        for row in dataset:
            new_row = row.copy()
            if old_name in row:
                new_row[new_name] = new_row[old_name]
            new_dataset.append(new_row)
        return new_dataset
    
    def remove_attribute(self, dataset, column_to_remove): #remove a column from the dataset
        return [
            {key: value for key, value in row.items() if key != column_to_remove} for row in dataset
        ]
    
    def rename_attributes(self, dataset, old_names, new_names): #rename a list of columns in the dataset
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
        new_dataset = [{key:value for key,value in row.items() if key not in columns_to_remove} 
                       for row in dataset]
        return new_dataset
            
    def transform(self, dataset, columns_to_remove=None, renames=None):
        new_dataset = dataset[:]
        # Remove attributes
        if columns_to_remove is not None:
            new_dataset = self.remove_attributes(new_dataset, columns_to_remove)
        # Rename attributes
        if renames is not None:
            new_dataset = self.rename_attributes(new_dataset, list(renames.keys()), list(renames.values()))
        return new_dataset