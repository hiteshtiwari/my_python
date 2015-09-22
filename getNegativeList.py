def getNegativeList(positiveAndNegativesList): # If the positiveAndNegativesList is None, returns an error.
    negativesList = []  # Creating de list
    for value in positiveAndNegativesList: # for each value in the 'positiveAndNegativesList' list:
        if value < 0:
            negativesList.append(value) # append to the list
    return negativesList # returns the list just one time.
 
 
 
