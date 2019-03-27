# This is the programme to find first ten most common words in the file.
# I have practice Tuple and dictionary in this programme.

#opening file 'mbox.txt' and if not open then print the statement in except block.
try :
    current_file = open('mbox.txt')
except :
    print('file not open')

current_dictionary = dict() # creat empty dictionary
for line in current_file :  # read file line by line
    line = line.lower()     # make line in lower character olny
    line = line.rstrip()    # strip line from rightside
    if not line.startswith('received:') :
        continue            # Skip lines not start with 'Received:'
    refference_pos = line.find('from')  # just refference index to find position of 'from'
    start_pos = line.find(' ',refference_pos) # starting position index
    end_pos = line.find(' ',start_pos+2)  # take the index of ' ' after the index of start_pos
    username = line[start_pos+1:end_pos]
    current_dictionary[username] = current_dictionary.get(username,0) + 1 # creating histogram of key-value pair of current_dictionary

#making a list of tupple and interchanging the value of key and value.
#sort the tupple in reverse order and store in list ls
ls = sorted([(v,k) for k,v in current_dictionary.items()],reverse = True)
ls = ls[ :10]  # slicing the list to just 10 element to get top 10.
for x in ls :
    print(x)    #printing line by line.

# Code outcome :
    # by this programme we get top 10 username from which maximum mails received.
    # the outcome indicate username coresponding to number of times mail received from that username.
    #the list is in sorted order from higher to lower frequency.
