# Create a list of your 5 favourite programming languages. Print the first and the 
# last one using both positive and negative indexing.

# l1 = ["python","c","c++","java","R"]

# #first one
# print(l1[0])
# print(l1[4])

# #last one
# print(l1[-5])
# print(l1[-1])


# SLICE THE LIST:-
# marks = [45, 67, 89, 23, 90, 56, 78] 
# Print the first 3 marks
# print(marks[0:3])
# Print the last 2 marks
# print(marks[5:7])
# print(marks[-2:])
# # Print every alternate mark
# print(marks[::2])
# # Print the list in reverse
# print(marks[::-1])



# Todo List Manager
# Start with 
# todos = ["wake up", "study"] 

# #  Add
# #  "exercise" at the end
# todos.append("exersice")

# # Add 
# # "meditate" at the very beginning
# todos.insert(0,"meditate")
# # Remove "study" 
# todos.remove("study")
 
# # Replace the last item with "sleep"
# todos[2]= "sleep"

# # Print the final list
# print(todos)

#student record(NESTED):-
# create a nested list where each inner list is [name,marks] for 3 students.
#   print the name of second student and marks of 3rd student.

# s1 = [1,["rahul",33],2,["vishal",75],3,["Ankit",98]]
# # Name of second student
# print(s1[3][0])
# # Marks of third student
# print(s1[5][1])

# You have data = [101, "Varanasi", 25.3, 82.9] = id, city, lat, lon. Unpack it
# into four named variables in a single line and print a sentence using them:-

# data = [101, "Varanasi", 25.3, 82.9]
# id,city,lat,lon = data
# print(f"ID is {id}, City is {city},Lat is {lat},Lon is {lon}")

# Create original = [1,2,3] . make a copy called backup. append 99 to backup. print both lists and explain(in n comment)
# why original didn't change? . then delibirately create the bug using = and observe the both outputs.

# original = [1,2,3]
# backup = original.copy()
# backup.append(99)
# print(original)
# print(backup)

# here original did not change because of we use correct mehod of copying by using this method only backup is appended original did not change , if we use = it will change the original because the backup  aquires the address of original in the memory.

# given scores = [40,80,65,95,70] without using sort() , yet - find the
# highest and lowest using slicing tricks after you learn them, OR rearrange
# manually using index assignment. Print "Winner is at position X". 

# score = [40,80,65,95,70]
# score[0]=40
# score[1]=65
# score[2]=70
# score[3]=80
# score[4]=95
# print(score)


