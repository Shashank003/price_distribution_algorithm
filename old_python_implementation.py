# Prompt user for total number of players and entry fee
Total_people = input("Total no of people: ")
entry_fee = eval(input("Entry fee: "))
mper = eval(input("Percentage: ")) #75 percent, the percent of users to recieve any money


# Convert input values to integers
Total_people = int(Total_people)
total_people = Total_people
# Calculate total amount based on input values
TTotal = int(total_people) * int(entry_fee)
# Print total amount, number of players, and entry fee
print("Total amount: ", TTotal)
print("Number of players: ", total_people)
print("Entry fee: ", entry_fee)
# Use loop to simulate number of iterations required to find final player count
for i in range(1000):
    Total_people = mper * Total_people
    Total_people = int(Total_people)
    # Check if there is only one player left and store number of iterations required to reach that count
    if Total_people == 1:
        no_iterations = i
        break
# Create list of player counts after each iteration
list_3 = [*range(no_iterations+1)]
for y in range(no_iterations+1):
    total_people = mper * total_people
    total_people = int(total_people)
    list_3[y] = total_people
# Create two additional lists to calculate payout structure
# list_4 is a reversed copy of list_3 and list_5 is the difference between adjacent elements in list_4
list_4 = list_3[0:len(list_3)] # list_4 is a copy of list_3
list_5 = list_4[::-1] # list_5 is a reversed copy of list_4 (more people in the end, less people in the beginning)
list_6 = [*range(len(list_3)-1)] # list_6 is a list of the difference between adjacent elements in list_5
for temp in range(len(list_3)-1):
    list_6[temp] = list_5[temp+1] - list_5[temp]
# Calculate the inverse square of the player count after each iteration
list_semi = [y**-2 for y in list_5]
# Calculate weight for each rank
weights = [*range(len(list_6))]
for y in range(len(list_6)):
    weights[y] = list_6[y] * list_semi[y]
# Calculate sum of weights
sum_weights = sum(weights)
# Create a new list containing the payout for each player
# Payout is calculated by multiplying the weight with the additional payout and dividing the result by the sum of the weights
# The entry fee is added to each payout value in the list
weights_demi = weights
minimum_distribution = mper * int(TTotal)
# minimum_distribution = 0.7 * int(TTotal)
# additional_payout = 0.3 * int(TTotal)
additional_payout = (1-mper) * int(TTotal)
weights_demi = [y * additional_payout for y in weights_demi]
weights_demi = [y / sum_weights for y in weights_demi]
for y in range(len(list_6)):
    weights_demi[y] = weights_demi[y] / list_6[y]
weights_demi = [y + int(entry_fee) for y in weights_demi]
weights_demi = [int(y) for y in weights_demi]
# Calculate payout for each rank and print it
# If there is a gap in the ranking, the payout is calculated by multiplying the difference between the adjacent ranking values
# with the weight for the higher ranking
sum = 0
weights_demi.append(entry_fee)
for y in range(len(list_5)):
    if (list_5[y] - list_5[y - 1] > 1):
        sum = sum + (list_5[y] - list_5[y - 1] - 1) * weights_demi[y]
        print("Rank: %d to %d"%(list_5[y - 1] + 1, list_5[y]), "\tPayout: %d"%(weights_demi[y]))
    else:
        sum = sum + weights_demi[y]
        print("Rank: %d"%(list_5[y]), "\tPayout: %d"%(weights_demi[y]))
print("Payout to players:", sum)
print("Payout to organizers:", TTotal - sum)
input("Press Enter to exit")