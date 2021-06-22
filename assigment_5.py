test_list = ["bob", "jimmy", "max b" , "bernie", "jordan", "future hendrix"]
 

print("The original list : " + str(test_list))
 

res = test_list[::2] + test_list[1::2]
 
print("Separated odd and even index list : " + str(res))
