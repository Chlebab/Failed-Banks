{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "f7953020",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'actor': 'Sean Bean', 'character': 'Eddard \"Ned\" Stark', 'first_appearance': '1'}\n",
      "{'actor': 'Mark Addy', 'character': 'Robert Baratheon', 'first_appearance': '1'}\n",
      "{'actor': 'Nikolaj Coster-Waldau', 'character': 'Jaime Lannister', 'first_appearance': '1'}\n",
      "{'actor': 'Michelle Fairley', 'character': 'Catelyn Stark', 'first_appearance': '1'}\n",
      "{'actor': 'Lena Headey', 'character': 'Cersei Lannister', 'first_appearance': '1'}\n",
      "{'actor': 'Emilia Clarke', 'character': 'Daenerys Targaryen', 'first_appearance': '1'}\n",
      "{'actor': 'Iain Glen', 'character': 'Jorah Mormont', 'first_appearance': '1'}\n",
      "{'actor': 'Harry Lloyd', 'character': 'Viserys Targaryen', 'first_appearance': '1'}\n",
      "{'actor': 'Kit Harington', 'character': 'Jon Snow', 'first_appearance': '1'}\n",
      "{'actor': 'Sophie Turner', 'character': 'Sansa Stark', 'first_appearance': '1'}\n",
      "{'actor': 'Maisie Williams', 'character': 'Arya Stark', 'first_appearance': '1'}\n",
      "{'actor': 'Richard Madden', 'character': 'Robb Stark', 'first_appearance': '1'}\n",
      "{'actor': 'Alfie Allen', 'character': 'Theon Greyjoy', 'first_appearance': '1'}\n",
      "{'actor': 'Isaac Hempstead Wright', 'character': 'Bran Stark', 'first_appearance': '1'}\n",
      "{'actor': 'Jack Gleeson', 'character': 'Joffrey Baratheon', 'first_appearance': '1'}\n",
      "{'actor': 'Rory McCann', 'character': 'Sandor \"The Hound\" Clegane', 'first_appearance': '1'}\n",
      "{'actor': 'Peter Dinklage', 'character': 'Tyrion Lannister', 'first_appearance': '1'}\n",
      "{'actor': 'Jason Momoa', 'character': 'Khal Drogo', 'first_appearance': '1'}\n",
      "{'actor': 'Aidan Gillen', 'character': 'Petyr \"Littlefinger\" Baelish', 'first_appearance': '1'}\n",
      "{'actor': 'Liam Cunningham', 'character': 'Davos Seaworth', 'first_appearance': '2'}\n",
      "{'actor': 'John Bradley', 'character': 'Samwell Tarly', 'first_appearance': '1'}\n",
      "{'actor': 'Stephen Dillane', 'character': 'Stannis Baratheon', 'first_appearance': '2'}\n",
      "{'actor': 'Carice van Houten', 'character': 'Melisandre', 'first_appearance': '2'}\n",
      "{'actor': 'James Cosmo', 'character': 'Jeor Mormont', 'first_appearance': '1'}\n",
      "{'actor': 'Jerome Flynn', 'character': 'Bronn', 'first_appearance': '1'}\n",
      "{'actor': 'Conleth Hill', 'character': 'Varys', 'first_appearance': '1'}\n",
      "{'actor': 'Sibel Kekilli', 'character': 'Shae', 'first_appearance': '1'}\n",
      "{'actor': 'Natalie Dormer', 'character': 'Margaery Tyrell', 'first_appearance': '2'}\n",
      "{'actor': 'Charles Dance', 'character': 'Tywin Lannister', 'first_appearance': '1'}\n",
      "{'actor': 'Oona Chaplin', 'character': 'Talisa Maegyr', 'first_appearance': '2'}\n",
      "{'actor': 'Rose Leslie', 'character': 'Ygritte', 'first_appearance': '2'}\n",
      "{'actor': 'Joe Dempsie', 'character': 'Gendry', 'first_appearance': '1'}\n",
      "{'actor': 'Kristofer Hivju', 'character': 'Tormund Giantsbane', 'first_appearance': '3'}\n",
      "{'actor': 'Gwendoline Christie', 'character': 'Brienne of Tarth', 'first_appearance': '2'}\n",
      "{'actor': 'Iwan Rheon', 'character': 'Ramsay Bolton', 'first_appearance': '3'}\n",
      "{'actor': 'Hannah Murray', 'character': 'Gilly', 'first_appearance': '2'}\n",
      "{'actor': 'Michiel Huisman[c]', 'character': 'Daario Naharis', 'first_appearance': '3'}\n",
      "{'actor': 'Nathalie Emmanuel', 'character': 'Missandei', 'first_appearance': '3'}\n",
      "{'actor': 'Indira Varma', 'character': 'Ellaria Sand', 'first_appearance': '4'}\n",
      "{'actor': 'Dean-Charles Chapman[d]', 'character': 'Tommen Baratheon', 'first_appearance': '1'}\n",
      "{'actor': 'Tom Wlaschiha[e]', 'character': \"Jaqen H'ghar\", 'first_appearance': '1'}\n",
      "{'actor': 'Michael McElhatton', 'character': 'Roose Bolton', 'first_appearance': '2'}\n",
      "{'actor': 'Jonathan Pryce', 'character': 'The High Sparrow', 'first_appearance': '5'}\n",
      "{'actor': 'Jacob Anderson', 'character': 'Grey Worm', 'first_appearance': '3'}\n"
     ]
    }
   ],
   "source": [
    "import csv\n",
    "class extract:\n",
    "    def fromCSV(self, file_path):\n",
    "        dataset = list()\n",
    "        with open(file_path) as f:\n",
    "            csv_file = csv.DictReader(f, delimiter=',')\n",
    "            for row in csv_file:\n",
    "                dataset.append(row) \n",
    "            return dataset   \n",
    "\n",
    "e = extract()\n",
    "dataset = e.fromCSV(file_path=\"data/banklist.csv\")\n",
    "for row in dataset:\n",
    "    print(row)"
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
