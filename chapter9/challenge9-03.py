import csv

with open("im.csv", "w", newline='') as p:
    w = csv.writer(p, delimiter=",")
    w.writerow(["Top Gun","Risky Business"])
    w.writerow(["Tintail","Obama","Choco"])
    w.writerow(["Man on Fire","level 5"])
