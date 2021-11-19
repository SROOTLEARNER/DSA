def recur(digits, i, str=""):
 
    # base case: all digits are processed in the current configuration
    if i == len(digits):
        # print the string
        print(str)
        return
 
    sum = 0
 
    # process the next two digits (i'th and (i+1)'th)
    for j in range(i, min(i + 1, len(digits) - 1) + 1):
 
        sum = (sum * 10) + digits[j]
 
        # if a valid character can be formed by taking one or both digits,
        # append it to the output and recur for the remaining digits
        if 0 < sum <= 26:
            recur(digits, j + 1, str + alphabet[sum - 1])
 
 
if __name__ == '__main__':
 
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = [1, 2, 2]
 
    recur(digits, 0)