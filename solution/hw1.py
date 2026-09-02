# Skeleton file for HW1 - Winter 2017-2018 - extended intro to CS

# Add your implementation to this file

# you may NOT change the signature of the existing functions.

# Change the name of the file to include your ID number (hw1_ID.py).


# Question 3
def avg_word_len(filename):
    inFile = open(filename, "r")  #inFile = file object
    outFile = open("output.txt", "w")
    file_string = inFile.readlines()  #file_string contains a list of the lines in the file
    sum = 0  #word length sum
    word_cnt = 0  #word counter
    for line in file_string:  #iterating the lines in file_string
        word_list = line.split()  #word_list contains a list of words in a line
        for word in word_list:  #iterating the words in word_list
            word_cnt += 1
            sum += len(word)
        if sum != 0:
            outFile.write(str(sum / word_cnt))
            sum = 0
            word_cnt = 0
        else:  #Handle divide by zero error
            outFile.write("0")
        outFile.write("\n")  #new line in file
    inFile.close()  #close read and write files
    outFile.close()


# **************************************************************
# Question 5
def k_boom(n, k):
    rtrn_str = ""  #string to be returned
    for current_num in range(1, n + 1):  #iterate from 1 to n(including)
        if str(k) in str(current_num):  #containing the digit k
            if current_num % k == 0:  #dividable by k
                rtrn_str += 'boom-boom! '
            else:
                rtrn_str += 'boom! '
        elif current_num % k == 0:  #only dividable by k
            rtrn_str += 'boom! '

        else:
            rtrn_str += str(current_num) + ' '  #regular number
    return rtrn_str[:len(rtrn_str)-1]  #remove excess space at the end


# **************************************************************
# Question 6
def max_even_seq(n, k):
    max_digits = 0  #saves maximum sequence of dividable numbers
    cnt = 0  #saves current sequence of dividable numbers
    for digit in str(n):
        if int(digit) % k == 0:  #if current digit is dividable by k
            cnt += 1  #add 1 to current sequence counter
            if cnt > max_digits:  #if current sequence is larger than max_digits
                max_digits = cnt  #save the biggest sequence in max_digits
        else:
            cnt = 0  #current sequence stopped
    return max_digits  #return biggest sequence


########
# Tester
########

def test():
    #########################Vcdghdghd
    # testing Q5
    s = k_boom(15, 7)
    if s != "1 2 3 4 5 6 boom-boom! 8 9 10 11 12 13 boom! 15":
        print("error in k_boom()")
