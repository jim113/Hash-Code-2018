ka=[]
with open('example.txt','r') as f:
    f_contents = f.readlines() # gives list of each line \
    
    for j in range (0 , len (f_contents) ) :
        for i in f_contents[j].split():
            ka.append(i)

    #print ka
"""
from string import rstrip

with open('example.txt') as f:
    ka = map(rstrip, f)

for i in range(len(ka)):
        
    p=ka[i]
    p.split()
    ka[i]=p """
def matrix(ka,x):
    return[ka[i:i+x] for i in xrange(0,len(ka),x)]

ka=matrix(ka,6)
#print ka



R=int(ka[0][0])
C=int(ka[0][1])
F=int(ka[0][2])
N=int(ka[0][3])
B=int(ka[0][4])
T=int(ka[0][5])

ka.pop(0)

#print ka

#print ka[0][8] ###pada artio

def steps(a,b,x,y):
    return (abs(a-x)+abs(y-b))

"""b=[]
for i in range (int(N)):
    b1=ka[i].split(' ')
    b.append(b1)
#print b
"""
b=ka


rides=[]
for i in range(int(N)):
    rides.append([steps(int(b[i][0]),int(b[i][1]),int(b[i][2]),int(b[i][3])),i])

reversed(sorted(rides))
#print rides

fromzero=[]
for i in range(int(N)):
    fromzero.append([steps(int(b[i][0]),int(b[i][1]),0,0),i])

#print fromzero

def mergeSort(alist):
    
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    
mergeSort(fromzero)
#print fromzero

time=[]
timetostart=[]
for i in range(len(rides)):
    temp=rides[i][1]
    
    for j in range(len(fromzero)):
        
        if (fromzero[j][1]==temp):
            dist_index=j
            #print fromzero[j][0]
            break
    time.append([(fromzero[dist_index][0]+rides[i][0]+int(b[temp][4])),i])
    timetostart.append([(fromzero[dist_index][0]+int(b[temp][4])),i])


#print time
mergeSort(timetostart)
#print timetostart
diadr=[]
sums=[]
for i in range(F):
    sums.append(0)
for i in range(F):
    diadr.append(str(timetostart[i][1]))
    sums[i]=sums[i]+timetostart[i][0]
#print diadr


j=0   
for i in range(F,N):
    if ((time[j][0]+sums[j])<int(b[i][5]) or ((int(b[i][5])-time[j][0]-sums[j])<0)): #and gia to D
        (diadr[j])=str(diadr[j])+' '+str(timetostart[i][1])
    j=j+1
    if (j==F):
         j=0
#print diadr



cd=open("example2.txt",'w')
for i in range (F) :
    
    cd.write("%d" %len(diadr[i].split(' ')))
    cd.write(' ')
    cd.write ("%s" %diadr[i])
    cd.write( '\n')
cd.close()

