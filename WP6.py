# Waypoint 6: Find Cheapest Hotels
# Write a function find_cheapest_hotels that takes two arguments hotel_daily_rates and maximum_daily_rate where:
# - hotel_daily_rates: a list of hotels and their respective daily rate represented by tuples (hotel_name, daily_rate) where:
#  hotel_name: the first element of the tuple, a string, representing the name of an hotel;
#  daily_rate: the second element of the tuple, an integer or float, representing the daily rate (in USD) of this hotel.
# - maximum_daily_rate: an integer or a float representing the maximum daily rate the user is willing to pay for one day at an hotel.
# The function returns a list of names of the hotels which daily rate is least or equal to the argument maximum_daily_rate. 
# These list of hotel names is sorted by the ascending daily rate of these hotels, i.e., from the cheapest hotels to the most expensive.
# For examples:
# >>> hotel_daily_rates = [
# ...    ('Majestic Saigon Hotel', 93),
# ...    ('Hotel Grand Saigon', 80),
# ...    ('Sofitel Saigon Plaza', 123),
# ...    ('Hotel Continental', 62),
# ...    ('Caravelle Hotel', 180),
# ...    ('Sheraton Saigon Hotel', 216),
# ...    ('Park Hyatt Saigon', 209)
# ... ]
# >>> find_cheapest_hotels(hotels, 50)
# []
# >>> find_cheapest_hotels(hotels, 80)
# ['Hotel Continental', 'Hotel Grand Saigon']
# >>> find_cheapest_hotels(hotels, 150)
# ['Hotel Continental', 'Hotel Grand Saigon', 'Majestic Saigon Hotel', 'Sofitel Saigon Plaza']

# *******************************

# B1. Tạo hàm find_cheapest_hotels cho nhâp hotel_daily_rates và maximum_daily_rate

def find_cheapest_hotels(hotel_daily_rates, maximum_daily_rate):
    hotels = []
    hotel_daily_rates(hotels)

    cheapest_hotels = []
    for hotel, daily_rate in hotels:
        if daily_rate <= maximum_daily_rate:
            cheapest_hotels.append((hotel, daily_rate))

    cheapest_hotels_sorted = sorted(cheapest_hotels, key=lambda x: x[1])
    return [hotel[0] for hotel in cheapest_hotels_sorted]

# tạo hàm hotel_daily_rates chứa argument hotels. input tên hotel và daily rate
def hotel_daily_rates(hotels):
    while True:
        try:
            hotel_name = input("Enter hotel name (or 'E' to exit): ")
            if hotel_name.upper() == 'E':
                break
            daily_rate = float(input("Enter daily rate (in USD): "))
            hotels.append((hotel_name, daily_rate))
        except ValueError:
            print("Invalid input, enter a number again.")

# Tạo hàm input_maximum_daily_rate 
def input_maximum_daily_rate():
    while True:
        try:
            max_rate = float(input("Enter maximum daily rate (in USD): "))
            return max_rate
        except ValueError:
            print("Invalid input, enter a number again.")

# In kết quả
result = find_cheapest_hotels(hotel_daily_rates, input_maximum_daily_rate());
print("List of cheapest hotels is: " + str(result)) ;




















# # *****************************************************
# def find_cheapest_hotels(hotel_daily_rates, maximum_daily_rate):
# # tìm các hotel có rate nhỏ hơn maximum rate
#     filtered_hotels = [hotel for hotel in hotel_daily_rates if hotel[1] <= maximum_daily_rate]
    
# # nếu không có hotel thỏa mãn, trả về list rỗng
#     if len(filtered_hotels) == 0:
#         return []
    
# # Sắp xếp hotel trong list theo thứ tự nhỏ đến lớn theo rate
#     sorted_hotels = sorted(filtered_hotels, key=lambda x: x[1])
    
# # tạo list hotel name từ list sorted
#     hotel_names = [hotel[0] for hotel in sorted_hotels]
#     return hotel_names


# hotel_daily_rates = [
#    ('Majestic Saigon Hotel', 93),
#    ('Hotel Grand Saigon', 80),
#    ('Sofitel Saigon Plaza', 123),
#    ('Hotel Continental', 62),
#    ('Caravelle Hotel', 180),
#    ('Sheraton Saigon Hotel', 216),
#    ('Park Hyatt Saigon', 209)
# ]

# print(find_cheapest_hotels(hotel_daily_rates, 190)) 
