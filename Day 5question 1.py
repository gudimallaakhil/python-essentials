# Question 1
# Write a program to identify sub list [1,1,5] is there in the given list in the same order, if yes print "it's a Match" if no then print "it's Gone" in function.
# Example -
# Listy = [1,5,6,4,1,2,3,5] - it's a Match
# Listy = [1,5,6,5,1,2,3,6] - it's Gone



def checkSublist(a, b):
    if not a:
        return True
    for k in range(len(b)):
        if a[0] == b[k]:
            return sub_list(a[1:], b[k+1:])
    return False

def finAns(ans):
    if(ans==True):
        return "it's a Match"
    else:
        return "it's Gone"

sub_list = [1,1,5]

#MAIN_LIST_1
super_list1 = [1,5,6,4,1,2,3,5]
print(" Sub-list : ",sub_list,"\n","Main-list : ",super_list1)
final_ans = finAns(checkSublist(sub_list, super_list1))
print(final_ans)
print()

#MAIN_LIST_2
super_list2 = [1,5,6,4,1,2,3,6]
print(" Sub-list : ",sub_list,"\n","Main-list : ",super_list2)
final_ans = finAns(checkSublist(sub_list, super_list2))
print(final_ans)
