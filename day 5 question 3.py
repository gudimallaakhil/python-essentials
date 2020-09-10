# Question 3
# Make a Lambda function for capitalizing the whole sentence passed using arguments.
# And map all the sentences in the List, with the lambda functions
# ["hey this is sai","l am in mumbai"...]
# o/p- ["Hey This Is Sai", "I Am In Mumbai".....]



inp_list = ["hey this is sai","I am in mumbai"]

out_list = list(map(lambda x : x.title(),inp_list))
print(out_list)
