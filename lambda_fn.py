'''Using Python3'''
# lambda argument: manipulate(argument)

square = lambda x : x*x
print (square(5.5))

add2val = lambda x,y : x+y
print (add2val(10,5))

lst = [x for x in range(20)]
even_number = list(filter(lambda x : x%2==0, lst))
print (even_number)

lst = [(1,3),(-5,10),(77,-3)]
lst.sort(key = lambda x:x[1])
print (lst)

print ("-----Using lambda as if condion-----")
#Syntax 
# function_name = lambda parameters:(false outcome,true outcome)[condition]
# def love(ucl):
# 	if ucl>=11:
# 		return "Real Madrid"
# 	else:
# 		return "Some Farmers Club"
love = lambda ucl:("Some Farmers Club","Real Madrid")[ucl>=11] # Equivalent of above function
best_in_spain = lambda ucl,league:("Barcelona: not bettar than Real Madrid","Real Madrid")[ucl>=11 and league>=32]
print(love(11))
print(best_in_spain(5,23))
