user_input_breath = int(input("please enter breath"))
user_input_length = int(input("please enter length"))

if user_input_breath == user_input_length:
    square_area = user_input_breath * user_input_breath
    square_perimeter = 4 * user_input_breath
    print("The square has perimeter", square_perimeter ,"and area", square_area )
else:
    rectangle_area = user_input_breath * user_input_length
    rectangle_perimeter = 2 * user_input_breath + user_input_length
    print("The rectangle has perimeter" , rectangle_perimeter ,"and area", rectangle_area)


