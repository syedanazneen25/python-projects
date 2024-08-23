with open("mail-custom-script/names.txt", mode="r") as names:
    name_list = names.readlines()

with open("mail-custom-script/starting_letter.txt", mode="r") as letter:
    letter_txt = letter.read()
new_names = []
for name in name_list:
    x = name.strip("\n").split()[0]
    new_names.append(x)

for new_name in new_names:
    x = letter_txt.replace("[name]", new_name)
    y = x.replace("[host]", "Nazneen")
    with open(f"mail-custom-script/Ready_to_send/letter_for_{new_name}.txt", mode="w") as final_letter:
        final_letter.write(y)
