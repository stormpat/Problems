import itertools

# Demo of Python iterators

mylist = range(1,11)
mydict = { 'a': 1, 'b': 2, 'c': 3, 'd': 4 }
names = ["Leonardo", "Donatello", "Raphaello", "Michelangelo", "I wont show up"]
ages = [54,32,56,76]

# The most basic loop
def most_basic():
  '''basic loop using an accumulator'''
  i = 0
  while i < len(mylist):
    val = mylist[i]
    print(val)
    i += 1

# Slightly better
def little_better():
  '''basic loop using for-in'''
  for i in range(len(mylist)):
    v = mylist[i]
    print(v)

def much_better():
  '''loop with only for-in'''
  for v in mylist:
    print(v)

def dict_loop():
  '''iterating dicts'''
  for v in mydict.values(): # itervalues() in Py < 3
    print(v)
  for k in mydict.keys(): # iterkeys() in Py < 3
    print(k)
  for kk,vv in mydict.items(): # iteritems() in Py < 3
    print(kk,vv)

def file_iter():
  '''iterate file contents'''
  with open("proiter.f") as f:
    for line in f:
      print(repr(line))

def get_index():
  '''using enumerate to get index'''
  for i, v in enumerate(mylist): # returns an enumerate object
    print(i,v)

def array_comp():
  return [x * x for x in mylist] # For simple stuff

def array_comp_lambda():
  return [(lambda x: x * x if x % 2 == 0 else x)(x) for x in mylist] #Lambda for more complex stuff.

def make_pairs():
  return list(enumerate(names)) # [(0, 'Leonardo'), (1, 'Donatello') ... etc

def iter_over_two_lists():
  for i in range(len(names)):
    name = names[i]
    age = ages[i]
    print("%s is %d years old" % (name, age))

def iter_over_two_lists_better():
  for name, age in zip(names, ages): # (zip) will drop the k/v if thers not a match
    print("%s is %d years old" % (name, age))

def make_dict():
  return dict(zip(names, ages)) # Create a dict formm two lists

def dict_iterables_uses():
  artists = make_dict()
  oldest = max(artists.values()) # Get age of oldest
  youngest = min(artists.values()) # Get age of youngest
  name_age_oldest = max(artists.items(), key=lambda b: b[1]) # Get tuple of oldest (name, age)
  name_oldest = max(artists.items(), key=lambda b: b[1])[0] # Get just the name of the oldest
  print(artists)
  print(oldest)
  print(youngest)
  print(name_age_oldest)
  print(name_oldest)

def other_uses_for_iterables():
  total = sum(mylist) # Sum on iterable list
  new_list = list(mylist) # Create a new list on iterable
  result = array_comp_lambda() # Get the result of a iterable (lambda or not)
  smallest = min(mylist) # Get smallest
  biggest = max(mylist) # Get biggest
  combined = " ".join(["Hello", "World", "From", "A", "List"]) # Or Tuple
  print("TOTAL: " + str(total))
  print("NEW LIST: " + str(new_list))
  print("RESULT: " + str(result))
  print("SMALLEST: " + str(smallest))
  print("BIGGEST: " + str(biggest))
  print("COMBINE: " + combined)
