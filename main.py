import math
def CircleCollision(x1,x2,y1,y2, radius):
    if (math.sqrt((x2 - x1)^2 + (y2- y1)^2))<radius:
        return True
    else:
        return False
    
print("Enter x position")
x1=int(input())
print("Enter second x position")
x2=int(input())
print("Enter y position")
y1=int(input())
print("Enter second y position")
y2=int(input())
print("Enter radius")
radius=int(input())

print("did you click on the circle?", CircleCollision(x1, x2, y1, y2, radius))


