import random
#Part A
weeks = 16
classes = 5
tuition = 6000

classes_per_week = 3
cost_per_week = ((tuition / classes) / weeks)
cost_per_class = ((cost_per_week)/(classes_per_week))

print(weeks, type(weeks))
print(classes, type(classes))
print(tuition, type(tuition))
print(classes_per_week, type(classes_per_week))
print(cost_per_week, type(cost_per_week))
print(cost_per_class, type(cost_per_class))

print("Cost per week: $", cost_per_week)
print ("Cost per class: $", cost_per_class)
#Part B
my_list = ["computer", "science", 41, 5.6, 2022, "cs110", 9.3 ]
print (random.choice(my_list))
