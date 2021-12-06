people = [ "Johny", "Marry", "Francis" ]  # top 3 devs in a company
print("BEFORE", people)


f = int(input("Choose the first index: "))
s = int(input("Choose the second index: "))


if f in range(0, len(people)) and s in range(0, len(people)):
    temp = people[f]
    people[f] = people[s]
    people[s] = temp
    print("AFTER", people)

else:
    print("Wrong index")
