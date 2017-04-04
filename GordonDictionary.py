#Laurel Gordon
#3/30/17
#dictionaries

dictionary = {"cat": "a fluffy animal that can also be a pet.",
              "party": "a gathering of people together in one place where they have fun.",
              "friends": "people that you enjoy talking with and being with them.",
              "party pooper": "a person that brings the party to a lower level of fun.",
              "muffin": "a baked good with fruit and/or chocolate. Usually eaten for breakfast."}

#words
print("The words are cat, party, friends, party pooper, and muffin")


choice = None
while choice != "0":

    print(
    """
    Words!!

    0 - quit
    1- look up a word
    2- add a word
    """
    )


    choice = input("Choice: ")
    print()

    #exit
    if choice == "0":
        print("Good bye")

    #get a definition
    elif choice == "1":
        word = input("what word do you want me to translate?\n")
        if word in dictionary:
            definition = dictionary[word]
            print("\n", word, "means", definition)
        else:
            print("sorry that was not a choice")

    #add a word/definition
    elif choice == "2":
        word = input("what word do you want to add?: ")
        if word not in dictionary:
            definition = input("\nWhat is the defintion?: ")
            dictionary[word] = definition
            print("\n", word, "has been added.")
        else:
            print("\nThat word already exists in the dictionary! \n")

            

    #Exit

    input("Press enter to continue")
    
                     
