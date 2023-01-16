from collections import deque
# Initializing a class-based dequeue queue 
queue = deque()
print(queue)

names_list = ['Bobby', 'Tom', 'Pete']
names_tuple = ('Bobby', 'Tom', 'Pete')
names_set = {'Bobby', 'Tom', 'Pete'}
names_dict = {'1': 'Bobby', '2': 'Tom', '3': 'Pete'}
#pass iterable to deque
deque_from_list = deque(names_list)
deque_from_tuple = deque(names_tuple)
deque_from_set = deque(names_set)
deque_from_dict_keys = deque(names_dict.keys())
deque_from_dict_values = deque(names_dict.values())
#Display deque
print(deque_from_list)
print(deque_from_tuple)
print(deque_from_set)
print(deque_from_dict_keys)
print(deque_from_dict_values)
# Let append John to deque(names_list) 
queue = deque(names_list)
print(queue)
queue.append('John')
print(queue)
#Let remove from that same list
queue.pop()
print(queue)