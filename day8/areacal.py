import math
def paint_cal(height,width,cover):
    number_of_cans = (height*width)/cover
    result=math.ceil(number_of_cans)
    print(f"You'll need {result} cans of paint.")

test_h = int(input("height of wall: "))
test_w = int(input("width of wall: "))
coverage = 5
paint_cal(height=test_h, width=test_w, cover=coverage)