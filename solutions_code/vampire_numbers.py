#The vampire numbers problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=125

#Main function
def is_vampire(num):
    num_len=len(str(num))
    if num_len%2!=0:
        return False
    return get_num(num,num_len/2,"","",num2list(num))

#Main auxiliar function
"""I've opted for a recursive function that takes digits from the original number to form all possible combinations of
   numbers of length L="original_number_length/2" with them. As it get each of these combinations of length L, the 
   function will multiply them by the possible combinations of length L that can be created with the remaining digits
   of the original number (as we had only used "original_number_length/2" digits to make the first one). If the result
   is   equal to the original number it will return True (as it would be a vampire number). If it isn't, it will continue 
   searching and checking the remaining combinations until he finds one that fits or until it validates every posible
   combination without succes (which would mean it's not a vampire number). To avoid repeating multiplications that have
   already been done, it will only multiply those in which the first combination is greater than the second one."""
def get_num(original_num,length,num1,num2,nums_left):
    total=[]
    if len(num1)==length:
        if len(num2)==length:
            return original_num==int(num1)*int(num2)
        for i in nums_left:
            if len(num2)==0 and i>num1[0] or len(num2)>0:
                num2_left_shown=""+num2
                num2_left_shown=num2_left_shown+i
                nums_left_shown=[]+nums_left
                nums_left_shown.remove(i)
                if get_num(original_num,length,num1,num2_left_shown,nums_left_shown):
                    return True
    for i in nums_left:
        num1_left_shown=""+num1
        num1_left_shown=num1_left_shown+i
        nums_left_shown=[]+nums_left
        nums_left_shown.remove(i)
        if get_num(original_num,length,num1_left_shown,num2,nums_left_shown):
            return True
    return False

#Basic auxiliar function
def num2list(num):
    num_s=str(num)
    num_list=[]
    for i in num_s:
        num_list.append(i)
    return num_list


#You can obviously print these inside the function, but i personally to keep the code "print-free"
print(is_vampire(4))      # --> False
print(is_vampire(2187))   # --> True
print(is_vampire(126))    # --> False
print(is_vampire(1122))   # --> False
print(is_vampire(536539)) # --> True
