
import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
NATO_dict = {row.letter:row.code for (index, row) in data.iterrows()}
user_input = input("Enter a word:").upper()
NATO_list = [NATO_dict[n] for n in user_input if n in NATO_dict ]
print(NATO_list)