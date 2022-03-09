"""
start
get the numbers of sheets
sheet / 5
round answer to next number
output the results to the user
end
"""
def calculate(sheet):
    answer = sheet / 5
    rounded = round(answer, 1)
    print("sheet is: ", sheet)
    print("The answer is: ", answer)
    print("rounded is: ", rounded)
    return rounded # this return is 
    
output = calculate (80085)

print("the return statement is: ", output)
