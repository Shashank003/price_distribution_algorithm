 # Replace 10 with your desired value

#This algorithm is only for participant count 200-500

import numpy as np



entryAmount = 50

numOfParticipants = 200
rankArray = [i for i in range(1, numOfParticipants+1)]


pricePoolBeforeRunningCharges = entryAmount*numOfParticipants

print("Before charges price pool:" + str(pricePoolBeforeRunningCharges))

pricePoolToBeDistributed = pricePoolBeforeRunningCharges - ((25/100)*pricePoolBeforeRunningCharges)
totalPrizePoolRemaining = pricePoolToBeDistributed

print("Price after cut pool: "+ str(pricePoolToBeDistributed))

# print(totalPrizePool)
# print(scoreBoard)

exclude_count = int(0.25 * numOfParticipants)
fifteith_percentile = int(0.5 * numOfParticipants)

npRankArray = np.array(rankArray)

percentile_30 = np.percentile(npRankArray, 30)
percentile_50 = np.percentile(npRankArray, 50)
percentile_75 = np.percentile(npRankArray, 75)
indices_between_50_and_75 = np.where((npRankArray > percentile_50) & (npRankArray <= percentile_75))[0]

# Calculate the number of ranks between 50th and 75th percentile
num_ranks_between_50_and_75 = len(indices_between_50_and_75)

for i, rank in enumerate(npRankArray):
    

    if( rank == 1):
        yourReward = (10/100)*pricePoolToBeDistributed
        totalPrizePoolRemaining = totalPrizePoolRemaining - yourReward
        print(f"person: {i}, rank: {rank}")
        print("Your reward is:   " + str(yourReward))

    if( rank == 2):
        yourReward = (7/100)*pricePoolToBeDistributed
        totalPrizePoolRemaining = totalPrizePoolRemaining - yourReward
        print(f"person: {i}, rank: {rank}")
        print("Your reward is:   " + str(yourReward))

    if( rank == 3):
        yourReward = (2.5/100)*pricePoolToBeDistributed
        totalPrizePoolRemaining = totalPrizePoolRemaining - yourReward
        print(f"person: {i}, rank: {rank}")
        print("Your reward is:   " + str(yourReward))
    
    # if (rank > 3 and rank < npRankArray[int(percentile_30)]):
    #     yourReward = 

    if (rank >3 and rank < 11):
        yourReward = (1/100)*pricePoolToBeDistributed
        totalPrizePoolRemaining = totalPrizePoolRemaining - yourReward
        print(f"person: {i}, rank: {rank}")
        print("Your reward is:   " + str(yourReward))


    if(rank >=11 and rank < percentile_50):
        yourReward = entryAmount
        totalPrizePoolRemaining = totalPrizePoolRemaining - entryAmount
        print(f"person: {i}, rank: {rank}")
        print("Your reward is: " + str(yourReward))

print("Total Prize Pool Remaining before distributing remaining:", totalPrizePoolRemaining)
remains = totalPrizePoolRemaining
 
for i, rank in enumerate(npRankArray):
    if(rank >=percentile_50 and rank < percentile_75):
        yourReward = remains/num_ranks_between_50_and_75
        totalPrizePoolRemaining = totalPrizePoolRemaining - yourReward
        print(f"person: {i}, rank: {rank}")
        print("Your reward is: " + str(yourReward))


print("Total Prize Pool Remaining after distributing remaining:", totalPrizePoolRemaining)
         







