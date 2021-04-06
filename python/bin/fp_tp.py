import sys

tp=0
fp=0
fn=0

try:
    file=open(sys.argv[1],"r")
except:
    print("Error in opening file",sys.argv[1])

ngc=int(sys.argv[2])
nmc=int(sys.argv[3])

overlappingmatrix=[]
# for i in range(nmc):
#     temp=[]
#     for j in range(ngc):
#         temp.append(0)
#     overlappingmatrix.append(temp)

for cur in file:        
    x=list(map(float,cur.split()))
    overlappingmatrix.append(x);

# print(overlappingmatrix)   
# for j in range(ngc):
#     for i in range(nmc):
#         print(overlappingmatrix[i][j],end=" ")
#     print()

for i in overlappingmatrix:
    for j in i:
        if(j>0):
            tp+=1
# print("TP",tp)
counter=0
for j in range(ngc):
    sum1=0
    for i in range(nmc):
        # if (overlappingmatrix[i][j]==0.0):
        #     counter+=1
        sum1+=overlappingmatrix[i][j]
    if(sum1==0):
        fn+=1
# print(fn)

counter=0
for i in range(nmc):
    sum1=0
    for j in range(ngc):
        # if (overlappingmatrix[i][j]==0.0):
        #     counter+=1
        sum1+=overlappingmatrix[i][j]
    if(sum1==0):
        fp+=1
# print("FP",fp)
# file2=open("fp_tp_fn.txt","w")

print(str(nmc)+"\t"+str(tp)+"\t"+str(fp)+"\t"+str(fn))



# file.close()