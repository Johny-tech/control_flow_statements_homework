def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """

    countNeg=0
    if a<0:
        countNeg+=1
    
    if b<0:
        countNeg+=1
    
    if c<0:
        countNeg+=1
    
    countPos=0
    if a>0:
        countPos+=1
    
    if b>0:
        countPos+=1
    
    if c>0:
        countPos+=1

    if countNeg>countPos:

        return "there are a lot of negative numbers"
    else:
        return "there are a lot of positive numbers"