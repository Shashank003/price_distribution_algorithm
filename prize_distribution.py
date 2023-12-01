 # Replace 10 with your desired value

entryAmount = 100

numOfParticipants = 1000
scoreBoard = [i for i in range(1, numOfParticipants+1)]

reversed_scoreBoard = scoreBoard[::-1]

originalPricePool = entryAmount*numOfParticipants
totalPrizePoolRemaining = entryAmount*numOfParticipants

# print(totalPrizePool)
# print(scoreBoard)

exclude_count = int(0.25 * numOfParticipants)
fifteith_percentile = int(0.5 * numOfParticipants)


# for i, person in enumerate(reversed_scoreBoard):


#     if(person<76 and person>50):
#         print("You are supposed to get half ur participation amount back person number: " + str(person))
#         totalPrizePoolRemaining = totalPrizePoolRemaining - (entryAmount/2)

#     if(person<40 and person > 4):
#         print("You are supposed to get  your participation: " + str(person))
#         totalPrizePoolRemaining = totalPrizePoolRemaining - 2 * entryAmount

#     if(person == 3):
#         print("You are supposed to get")
    

for i, person in enumerate(scoreBoard):
    # print(f"Index: {i}, Person: {person}")

    if(person == 1):
        print("Rank 1 should get: ")
        totalPrizePoolRemaining = totalPrizePoolRemaining - ((5/100)*originalPricePool)
        print(((5/100)*originalPricePool))

    if(person == 2):
        print("Rank 2 should get: ")
        totalPrizePoolRemaining = totalPrizePoolRemaining - ((2.5/100)*originalPricePool)
        print(((2.5/100)*originalPricePool))


    if(person == 2):
        print("Rank 2 should get: ")
        totalPrizePoolRemaining = totalPrizePoolRemaining - ((1/100)*originalPricePool)
        print(((1/100)*originalPricePool))





print("Total Prize Pool Remaining:", totalPrizePoolRemaining)

