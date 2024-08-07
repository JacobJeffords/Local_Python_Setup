def hello():
  print("Hello!")

hello()

# ------------------------------

def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]

result = pack(1, 2, 3)
print(result)

# ------------------------------

def eat_lunch(food_list):
    if not food_list:
        print("My lunchbox is empty!")
    else:
        for i in range(len(food_list)):
            if i == 0:
                print(f"First I eat {food_list[i]}")
            else:
                print(f"Next I eat {food_list[i]}")

eat_lunch(["sandwich", "apple", "chips"])
eat_lunch([])