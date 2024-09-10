
import pandas
data = pandas.read_csv("NATO_alphabets/nato_phonetic_alphabet.csv")
NATO_dict = {row.letter:row.code for (index, row) in data.iterrows()}
def generate_phonetic():
    user_input = input("Enter a word:").upper()
    try:
        NATO_list = [NATO_dict[n] for n in user_input]
    except KeyError:
        print("Sorry enter only letters!!")
        generate_phonetic()
    else:
        print(NATO_list)

generate_phonetic()