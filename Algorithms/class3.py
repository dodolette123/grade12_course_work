# define your linear_search() below...
def linear_search(search_list,target_value):
  for idx in range(len(search_list)):
    print(search_list[idx])
    if search_list[idx] == target_value:
      return idx
    
  raise ValueError("{0} not in list".format(target_value))

# uncomment the lines below to test...
values = [54, 22, 46, 99]
print(linear_search(values, 22))




#Duplicate Answer
tour_locations = [ "New York City", "Los Angeles", "Bangkok", "Istanbul", "London", "New York City", "Toronto"]
target_city = "New York City"

#Linear Search Algorithm
def linear_search(search_list, target_value):
  matches = []
  for idx in range(len(search_list)):
    if search_list[idx] == target_value:
      matches.append(idx)
  if len(matches) != 0:
    return matches
  else:
   raise ValueError("{0} not in list".format(target_value))

#Function call
tour_stops = linear_search(tour_locations, target_city)
print(tour_stops)



#Duplicates Template
# Search list and target value
tour_locations = [ "New York City", "Los Angeles", "Bangkok", "Istanbul", "London", "New York City", "Toronto"]
target_city = "New York City"


#Linear Search Algorithm
def linear_search(search_list, target_value):
  for idx in range(len(search_list)):
    if search_list[idx] == target_value:
      return idx
  raise ValueError("{0} not in list".format(target_value))

#Function call
tour_stops = linear_search(tour_locations, target_city)
print(tour_stops)

