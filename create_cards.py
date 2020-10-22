from random import shuffle

CARD_OPTION_FILENAME = "pres_final_debate_input.txt"
CARD_COUNT = 10
card_options = []

with open(CARD_OPTION_FILENAME, "r") as input_filename:
    for count, line in enumerate(input_filename):
        card_options.append(line.strip())

print("Read in the bingo options")
print("Generating bingo cards...\n")

for card_count in range(0, CARD_COUNT):
    shuffle(card_options)
    print(card_options)
    bingo_card_name = "card_{}.html".format(card_count)

    with open(bingo_card_name, "w") as card:
        card.write("<!DOCTYPE html>\n\n")
        card.write("<html lang=\"en\">\n")
        card.write("<head>\n")
        card.write("<style>\n")
        card.write("table, th, td {\n")
        card.write("\tborder: 1px solid black;\n")
        card.write("\tborder-collapse: collapse;\n")
        card.write("}\n")
        card.write("</style>\n\n")
        card.write("\t<title>{}</title>\n".format(str(bingo_card_name)))
        card.write("</head>\n\n")
        card.write("<body>\n")
        card.write("\t<table>\n")
        for item in range(0, 25):
            if item == 12:
                card.write("\t\t\t<td>Free Space</td>\n")
            elif item % 5 == 0:
                card.write("\t\t<tr height = 20px></tr>\n")
                card.write("\t\t<tr>\n")
                card.write("\t\t\t<td>  {}  </td>\n".format(card_options[item]))
            elif (item + 1) % 5 == 0:
                card.write("\t\t\t<td>  {}  </td>\n".format(card_options[item]))
                card.write("\t\t</tr>\n")
            else:
                card.write("\t\t\t<td>  {}  </td>\n".format(card_options[item]))
        card.write("\t</table>\n")
        card.write("</body>\n\n")
        card.write("</html>\n")
