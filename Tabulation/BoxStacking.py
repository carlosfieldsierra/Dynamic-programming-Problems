#  Find height of heighest box stack 
# L < L_Below, W < W_Below 

# My Sloution
def boxStack(BoxLst):
    L = BoxLst[:]
    for i in range(1,len(BoxLst)):
        possibleBottomBoxes = [L[k] for k in range(i) if validPlacement(L[k],L[i])]
        if len(possibleBottomBoxes):
            maxBoxOnBottom = max(possibleBottomBoxes, key=lambda item:item[2])
            newVal = (L[i][0],L[i][1],maxBoxOnBottom[2]+L[i][2]) 
            L[i] = newVal
    return max(L,key=lambda item:item[2])[2]

def validPlacement(bottom,top):
    return (bottom[0]>top[0]) and (bottom[1]>top[1])

# Reducible Solution
def tallestStack(boxes):
    boxes.sort(key=lambda x:x[0])
    heights = {box:box[2] for box in boxes}
    for i in range(1,len(boxes)):
        box = boxes[i]
        S = [boxes[j] for j in range(i) if validPlacement(box,boxes[j])]
        heights[box] = box[2] + max([heights[box] for box in S],default=0)
    return max(heights.values(),default=0)


print(tallestStack([
    (4,5,3),
    (2,3,2),
    (3,6,2),
    (1,5,4),
    (2,4,1),
    (1,2,2)
]))