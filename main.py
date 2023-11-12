from data import first_names, surnames
from datetime import datetime, timedelta
import random

#
# See the duplications in the data.py
#
#print(len(surnames))#len(first_names))

#
# Functions definitions
#
#
# Create a random Name and Surname
#

# Build person name, based on a list of first names and surnames
# uses random
def person_name(first_name_list, surname_list):
  first_name_list_len = len(first_name_list)
  surname_list_len = len(surname_list)
  random_first_name_position = random.randrange(first_name_list_len)
  random_surname_position = random.randrange(surname_list_len)
  person_name = first_name_list[random_first_name_position] + ' ' + surname_list[random_surname_position]
  return person_name
  
def show_duplicates_in_array(list):
  names_dict = {}
  names_set = set(list)
  if len(names_set) == len(list):
    print("The array has no duplicates")
  else:
    print("The array has duplicates")
  
  for name in list:
    if name in names_dict:
      names_dict[name] += 1
    else:
      names_dict[name] = 1

  for name, count in names_dict.items():
    if count > 1:
      print(name+": "+str(count))
  names_dict = {}
  #print(list(set(first_names)))

#Create a random date
def random_date_generator(first_date, second_date):
  time_between_dates = second_date - first_date
  days_between_dates = time_between_dates.days
  random_number_of_days = random.randrange(days_between_dates)
  random_date = first_date + timedelta(days=random_number_of_days)
  return random_date.strftime('%Y-%m-%d')
  #print(random_date)

def license_generator_canada(province, surname, dob):
  
  #show_duplicates_in_array(surnames)#first_names)

#  print("\nPerson Name: " + person_name(first_names, surnames))

  start_date = datetime(1950, 1, 1)
  end_date = datetime(2000, 12, 31)
  date_of_birth = random_date_generator(start_date, end_date)
  print("Date of Birth: " + date_of_birth)

data_generator=int(input("How many person data do you want to generate?: "))
for number in range(data_generator):
  print("Person Name: " + person_name(first_names, surnames))
  print("Date of Birth: " + random_date_generator(datetime(1950, 1, 1), datetime(2000, 12, 31))+"\n-------------------------")