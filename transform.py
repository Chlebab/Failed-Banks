{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d17bf368",
   "metadata": {},
   "outputs": [],
   "source": [
    "class transform:\n",
    "    def head(self, dataset, steps): #return the top N records from the dataset\n",
    "        for step in range(steps):\n",
    "            return dataset[step]\n",
    "            \n",
    "    def tail(self, dataset, steps): #return the last N records from the dataset\n",
    "        for step in range(steps):\n",
    "            return dataset[-steps:]\n",
    "            \n",
    "    def rename_attribute(self, dataset, old_name, new_name): #rename a column in the dataset\n",
    "        new_dataset = []\n",
    "        for row in dataset:\n",
    "            new_row = row.copy()\n",
    "            if old_name in new_row:\n",
    "                row[new_name] = row.pop(old_name)\n",
    "            new_dataset.append(new_row)\n",
    "        return new_dataset\n",
    "    \n",
    "    def remove_attribute(self, dataset, column_to_remove): #remove a column from the dataset\n",
    "        return [\n",
    "            {key: value for key, value in row.items() if key != column_to_remove} for row in dataset\n",
    "        ]\n",
    "    \n",
    "    def rename_attributes(self, dataset, old_names, new_names): #rename a list of columns in the dataset\n",
    "        new_dataset = dataset.copy()\n",
    "        for row in new_dataset:\n",
    "            for old_name, new_name in zip(old_names, new_names):\n",
    "                if old_name in row:\n",
    "                    row[new_name] = row.pop(old_name)\n",
    "        return new_dataset\n",
    "    \n",
    "    def remove_attributes(self, dataset, columns_to_remove): #remove a list of columns in the dataset\n",
    "        new_dataset = [{key:value for key,value in row.items() if key not in columns_to_remove} \n",
    "                       for row in dataset]\n",
    "        return new_dataset\n",
    "            \n",
    "    def transform(self, dataset):\n",
    "        dataset_after_remove = self.remove_attributes(dataset, ['Bank Name', 'City', 'Cert', 'Acquiring Institution', 'Fund'])\n",
    "        dataset_after_rename = self.rename_attribute(dataset_after_remove, 'State', 'State Abbreviation')\n",
    "        return dataset_after_rename"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
