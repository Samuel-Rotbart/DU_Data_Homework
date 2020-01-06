# ## PyPoll

import os
import csv

# open and create csvreader
pypoll_csv_path = os.path.join("Resources/election_data.csv")

with open (pypoll_csv_path,newline="") as pypollreader:
    pypollreader = csv.reader(pypollreader,delimiter=",")
    header = next(pypollreader)
#   setting up initial lists and vote counter
    vote_count = 0
    candidate_list = []
    county_list = []
    voterid_list = []
    candidate_set = []
    
    # count votes and create lists for each column in the csv file 
    for row in pypollreader:
        vote_count = vote_count + 1
        voterid = row[0]
        county = row[1]
        candidate = row [2]
        voterid_list.append(voterid)
        county_list.append(county)
        candidate_list.append(candidate)

    # print initial lines of output
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes:{vote_count}")
    print("-------------------------")

    # get unique list of candidates
    candidate_set = set(candidate_list)

    #create lists for vote counting
    candidate_name_list = []
    total_vote_list = []
    total_vote_list_sort = []
    percent_vote_list = []
    
    # create lists for total votes, candidates and percent of vote
    for x in candidate_set:
        total_votes = candidate_list.count(x)
        total_vote_list.append(total_votes) 
        candidate_name = x
        candidate_name_list.append(candidate_name)
        percent_votes = round(total_votes / vote_count *100,4)
        percent_vote_list.append(percent_votes)
    
    # create a copy of the total vote list in order to sort and get the proper order every time the code is run using a list of indexes
    total_vote_list_sort = total_vote_list.copy()
    total_vote_list_sort.sort(reverse=True)

    index_list = []

    for i in total_vote_list_sort:
        index_list.append(total_vote_list.index(i))
    # use the index list just created to print the correct values in order
    print_value1 = index_list[0]
    print_value2 = index_list[1]
    print_value3 = index_list[2]
    print_value4 = index_list[3]
    
    print(candidate_name_list[print_value1]+": "+str(percent_vote_list[print_value1]) + "% (" + str(total_vote_list[print_value1])+")")        
    print(candidate_name_list[print_value2]+": "+str(percent_vote_list[print_value2]) + "% (" + str(total_vote_list[print_value2])+")")        
    print(candidate_name_list[print_value3]+": "+str(percent_vote_list[print_value3]) + "% (" + str(total_vote_list[print_value3])+")")        
    print(candidate_name_list[print_value4]+": "+str(percent_vote_list[print_value4]) + "% (" + str(total_vote_list[print_value4])+")")        
    print("-------------------------")
    print(f"Winner: {candidate_name_list[print_value1]}")
    print("-------------------------")
    print("```")

#print to csv file
output_data = os.path.join("Resources/new_data.txt")
with open (output_data,'w') as txtfile:
    print("Election Results",file=txtfile)
    print("-------------------------",file=txtfile)
    print(f"Total Votes:{vote_count}",file=txtfile)
    print("-------------------------",file=txtfile)    
    print(candidate_name_list[print_value1]+": "+str(percent_vote_list[print_value1]) + "% (" + str(total_vote_list[print_value1])+")",file=txtfile)        
    print(candidate_name_list[print_value2]+": "+str(percent_vote_list[print_value2]) + "% (" + str(total_vote_list[print_value2])+")",file=txtfile)        
    print(candidate_name_list[print_value3]+": "+str(percent_vote_list[print_value3]) + "% (" + str(total_vote_list[print_value3])+")",file=txtfile)        
    print(candidate_name_list[print_value4]+": "+str(percent_vote_list[print_value4]) + "% (" + str(total_vote_list[print_value4])+")",file=txtfile)        
    print("-------------------------",file=txtfile)
    print(f"Winner: {candidate_name_list[print_value1]}",file=txtfile)
    print("-------------------------",file=txtfile)
    print("```",file=txtfile)
