class transform:
    def head(self, dataset, steps): #return the top N records from the dataset
        for step in range(steps):
            return dataset[step]
            
    def tail(self, dataset, steps): #return the last N records from the dataset
        for step in range(steps):
            return dataset[-steps:]
            
    def rename_attribute(self, dataset, old_name, new_name): #rename a column in the dataset
        new_dataset = []
        for row in dataset:
            new_row = row.copy()
            if old_name in new_row:
                row[new_name] = row.pop(old_name)
            new_dataset.append(new_row)
        return new_dataset
    
    def remove_attribute(self, dataset, column_to_remove): #remove a column from the dataset
        return [
            {key: value for key, value in row.items() if key != column_to_remove} for row in dataset
        ]
    
    def rename_attributes(self, dataset, old_names, new_names): #rename a list of columns in the dataset
        new_dataset = dataset.copy()
        for row in new_dataset:
            for old_name, new_name in zip(old_names, new_names):
                if old_name in row:
                    row[new_name] = row.pop(old_name)
        return new_dataset
    
    def remove_attributes(self, dataset, columns_to_remove): #remove a list of columns in the dataset
        new_dataset = [{key:value for key,value in row.items() if key not in columns_to_remove} 
                       for row in dataset]
        return new_dataset
            
    def transform(self, dataset):
        dataset_after_remove = self.remove_attributes(dataset, ['Bank Name', 'City', 'Cert', 'Acquiring Institution', 'Fund'])
        dataset_after_rename = self.rename_attribute(dataset_after_remove, 'State', 'State Abbreviation')
        return dataset_after_rename