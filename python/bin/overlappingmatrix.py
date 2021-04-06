
# //---------------------------------------------------------------------------------------
# // DESCRIPTION:
# // -----------
# // This program computes the overlapping matrix for a protein, i.e. the percentages of 
# // its cavities that are intersected by cavities of a specific method.
# //
# // SYNOPSIS:
# // --------
# //  overlappingmatrix.exe <gt-file.csv>  <da-file.txt> <n> <m> 
# //
# // where:
# //      gt-file.csv: ground-truth .csv file describing the cavities of a protein;
# //      ms-file.csv: method-specific .csv file describing the cavities of a protein;
# //      <n>:         the number of ground-truth cavities of a protein
# //      <m>:         the number of method-specific cavities of a protein
# // 
# // INPUT FILE FORMAT of <gt-file.csv>:
# // -----------------
# //  x y z id
# //
# //  where
# //       (x,y,z): Cartesian coordinates of each dummy atom center
# //       id:      cavity identifier
# //
# // INPUT FILE FORMAT of <da-file.txt>:
# // -----------------
# //  i j 
# //
# //  where
# //      i: identifier of the ground-truth cavity
# //      j: identifier of the method-specific cavity


# //---------------------------------------------------------------------------------------

import sys,csv
class CAVPOINT3D:
    def __init__(self, coord, id1):
        self.coord = coord
        self.id1 = id1  #CAVITY ID
    

# class DUMMYATOMPAIR:
#     def __init__(self, i, j):
#         self.i=i                     #ground-truth cavity id 
#         self.j=j                   #method-specific cavity id



ids=[]
dummies=[]
try:
    f1=open(sys.argv[1],"r")
except:
    print("Error opening file with name: ",sys.argv[1])


try:
    f2=open(sys.argv[2],"r")
except:
    print("Error opening file with name: ",sys.argv[2])


ngc=int(sys.argv[3])
nmc=int(sys.argv[4])


# csv_reader1=csv.reader(f1,delimiter=" ")
for cur in f1:
    cur=cur.split()
    # print(cur[3])
    # print(cur)
    ids.append(int(cur[3]))
# print(ids)
# csv_reader2=csv.reader(f2,delimiter=" ")
for cur in f2:
    cur=cur.split()
    cur=list(map(int,cur))
    # print(type(cur[0]))
    # print(cur,type(cur))
    dummies.append(cur)
# print(dummies)

count=[]
for i in range(ngc):
    count.append(0)

for i in ids:
    for j in range(ngc):
        # print(type(i),type(j))
        if(i==j):
            count[j]+=1

overlappingmatrix=[]
# print(ngc,count)
for i in range(nmc):
    temp=[]
    for j in range(ngc):
        temp.append(0)
    overlappingmatrix.append(temp)
# overlappingmatrix=[[0]*ngc]*nmc
# print(overlappingmatrix)
# print(len(overlappingmatrix))
# print(len(overlappingmatrix[0]))
# print(overlappingmatrix)
# print(dummies)
for arr in dummies:
    overlappingmatrix[arr[1]][arr[0]]+=1
# print(overlappingmatrix)

for i in range(nmc):
    for j in range(ngc):
        if(overlappingmatrix[i][j]>0):
                # print(count[j])
                # print(overlappingmatrix[i][j],count[j],i,j,(overlappingmatrix[i][j] * 100) / count[j])
                overlappingmatrix[i][j] = (overlappingmatrix[i][j] * 100) / count[j];

# print(overlappingmatrix)


# f3=open("output_overlappingmatrix.txt","w")
for i in range(nmc):
        for j in range(ngc):
            # f3.write("%0.3f \t" % overlappingmatrix[i][j]);
            print("%0.3f  " % overlappingmatrix[i][j], end="")
        print()
        # f3.write("\n");
