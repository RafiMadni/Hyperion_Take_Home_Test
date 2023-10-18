# Create variable for qualifying time and let it equal to 100
qualifying_time = 100

# Create variables for each event and promt user to enter values accordingly
swimminig = int(input("How many minutes did it take the participant take to complete the swimming event?\n"))
cycling = int(input("How many minutes did it take the participant to complete the cylcing event?\n"))
running = int(input("How many minutes did it take the participant to complete the running event?\n"))
              
# Create variable called total time and let it equal to the sum of the 3 events              
total_time = (swimminig + cycling + running)
print("Total Time: ", total_time)

# Create if statement, total time to be equal and less then qualifying time
if total_time <= qualifying_time:
    print("Provincial Colours")

# Create elif statement, use <= operator
elif total_time <= 105:
    print("Provincial Half Colours")
# Create elif statement, use <= operator
elif total_time <= 110:
    print("Provincial Scroll")    

# Create else statement. If none of the above condtions are met else will activate
else:
    print("No award")


