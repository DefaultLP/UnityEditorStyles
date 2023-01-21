import os
import urllib.parse

folder = "Light"
#folder = "Dark"
readme = folder + "\\README.md"
f = open(readme, "w+")

f.write("# Dark GUIStyles\n\n")
f.write("| GUIStyle name | With Text | Without Text |\n")
f.write("| --- | --- | --- |\n")

count = 0
for x in os.listdir(os.path.dirname(__file__) + "\\" + folder + "\\img"):
    if x.endswith(".png"):
        if count % 2 == 0:
            f.write("| <h3>" + x[:-9] + "</h3> | ")
            f.write("![Alt text](img/" + urllib.parse.quote(x) +") | ")
        else:
            f.write("![Alt text](img/" + urllib.parse.quote(x) + ") |\n")
        count += 1

f.write("")
f.close()