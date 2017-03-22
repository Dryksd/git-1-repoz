def checkPalindrome(inputString):
    if len(inputString) == 1:
        return True
    
    M = len(inputString) / 2
    if len(inputString) % 2 == 0 :
        M_1 = len(inputString) // 2
        R = inputString[(M_1) :]
        R_list = list(R)
        R_list.reverse()
        C = ''.join(R_list)
        X = inputString[:(M_1)]
        if C == X :
            return True
        
    if len(inputString) % 2 != 0 :
        M_1 = len(inputString) // 2
        R = inputString[(M_1 + 1) :]
        R_list = list(R)
        R_list.reverse()
        C = ''.join(R_list)
        X = inputString[:(M_1)]
        if C == X :
            return True
    else :
        return False
    


    
