def main():
    # Define a list of fruits
    fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
    
    # Print all fruits
    
    
    print (fruits)
    print ("After Print" )

    print("List of fruits:")
    for fruit in fruits:
        print(fruit)

    # Add a fruit to the list
    
    fruits.append("Fig")
    print("\nAdded 'Fig' to the list:")

    for fruit in fruits:
        print(fruit)



    fruits.append("Fig")
    fruits.append("Fig")
    fruits.append("Fig")

    # Print all fruits using enumerate for index and value
        # Variables     enumerate(collection)
    for index, fruit in enumerate(fruits):
        print(f"{index + 1}: {fruit}")

    # # Remove a fruit from the list
    # fruits.remove("Fig")
    # fruits.remove("Fig")
    # fruits.remove("Fig")
    # fruits.remove("Fig")
    print("\nRemoved 'Banana' from the list:")
    for fruit in fruits:
        print(fruit)

    # Access fruits by index
    #print("\nFruit at position 3:")
    x = 3
    print( f" Thie Fruit is {fruits[x]}")  # remember, list indexing starts at 0

    # # Slicing the list
    # print("\nFirst three fruits:")
    # print(fruits[:3])

if __name__ == "__main__": # Program Entry Point 
    main()
