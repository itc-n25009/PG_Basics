answer_num = [1,2,3,4,5]
while True:
    num = input("type a number or string:")
    if num == "q":
        break
    try:
        num = int(num)
    except ValueError:
        print("type a number or q to retire")
    if num in answer_num:
        print("correct!")        
    elif num not in answer_num:
        print("incorrect")
