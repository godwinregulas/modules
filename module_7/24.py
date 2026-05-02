# observe the dictionary above and write a menu driven python program to create recipes. Once one recipe is done then the quantity of the items in pantry should also be reduced
# Eg  :  If you cook beans on toast the beans quantity and bread quantity need to decrease i.e., one from the total quantity each.

pantry = {
    "chicken": 500,
    "lemon": 2,
    "cumin": 24,
    "paprika": 18,
    "chilli powder": 7,
    "yogurt": 300,
    "oil": 450,
    "onion": 5,
    "garlic": 9,
    "ginger": 2,
    "tomato puree": 125,
    "almonds": 75,
    "rice": 500,
    "coriander": 20,
    "lime": 3,
    "pepper": 8,
    "egg": 6,
    "pizza": 2,
    "spam": 1,
}

recipes = {
    "Butter chicken": [
        "chicken",
        "lemon",
        "cumin",
        "paprika",
        "chilli powder",
        "yogurt",
        "oil",
        "onion",
        "garlic",
        "ginger",
        "tomato puree",
        "almonds",
        "rice",
        "coriander",
        "lime",
    ],
    "Chicken and chips": [
        "chicken",
        "potatoes",
        "salt",
        "malt vinegar",
    ],
    "Pizza": [
        "pizza",
    ],
    "Egg sandwich": [
        "egg",
        "bread",
        "butter",
    ],
    "Beans on toast": [
        "beans",
        "bread",
    ],
    "Spam a la tin": [
        "spam",
        "tin opener",
        "spoon",
    ],
}

is_true=1
while is_true==1:
    print("\nMENU")
    print("---------------------------------------")
    ind=1
    for i in recipes:
        print(ind,i)
        ind+=1
    print("0 Exit")
    print("---------------------------------------")
    ch=int(input("Enter your choice: "))
    if ch==0:
        break
    elif ch>6 or ch<0:
        print("Invalid choice!")
        continue

    recipes_list=list(recipes.keys())
    selected_recipes=recipes_list[ch-1]
    avl=1
    for i in recipes[selected_recipes]:
        if i not in pantry or pantry[i]<=0:
            avl=0
            print("recipie not available")
            break
    if avl==1:
        for i in recipes[selected_recipes]:
            pantry[i]-=1
        print(selected_recipes,"is cooked successfully!")
    print("---------------------------------------")
    print("---------------------------------------")
    print("---------------------------------------")