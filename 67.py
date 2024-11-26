import time 
start = time.time()

triangles = open('triangle.txt','r')
triangle = []
for line in triangles:
    line = line.strip()
    columns = [int(i) for i in line.split(' ')]
    triangle.append(columns)
triangles.close()
#print(triangle)

def maxi(triangle,i,k):
    triangle[i][k] += max(triangle[i+1][k+1],triangle[i+1][k])

#updating the entire row
def update_row(triangle,i):
    length = len(triangle[i])
    for k in range(length):
        maxi(triangle,i,k)

def maximum(triangle):
    intitial = len(triangle)-2
    i = intitial
    while i >-1:
        update_row(triangle,i)
        i -= 1
    return triangle[0][0]
end = time.time()
print(start-end)
print(maximum(triangle))