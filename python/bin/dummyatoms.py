import numpy as np
import sys
class CAVPOINT3D():
	def __init__(self,  array,id):
		self.id = id
		self.coord = array  



class DUMMYATOMPAIR():
	def __init__(self, gc_id, ms_id):
		self.groundcavid = gc_id
		self.methodspecid = ms_id


U = []
V = []
D = []



#FILE *fU, *fV;



distance = 2.0; 	#reference distance between dummy atoms

gt_file = str(sys.argv[1])
ms_file = str(sys.argv[2])
fU = open(gt_file, "r"); 	#first input file <gt-file.csv> 

fptrU=[]
# for cur in fU.readlines():
# 	cur=cur.replace("\n","")
# 	for ii in cur.split():
# 		fptrU.append(ii) # in string format
# print(fptrU)
# l = len(fptrU)
for cur in fU.readlines():
	# print(cur)
	fptrU=cur.split()
	x=float(fptrU[0])
	y=float(fptrU[1])
	z=float(fptrU[2])
	iden=int(fptrU[3])
	p=CAVPOINT3D([x,y,z],iden)
	# p.coord[0] = x
	# p.coord[1] = y
	# p.coord[2] = z
	# p.id = iden
	U.append(p);

fU.close()
fV = open(ms_file, "r"); 	#second input file <ms-file.csv> 

# fptrV = read_file().split(" "); # in string format

fptrV=[]
# for cur in fV.readlines():
# 	cur=cur.replace("\n","")
# 	for ii in cur.split():
# 		fptrV.append(ii) # in string format
# print(fptrV)

for cur in fV.readlines():
	# print(cur)
	fptrV=cur.split()
	x=float(fptrV[0])
	y=float(fptrV[1])
	z=float(fptrV[2])
	iden=int(fptrV[3])
	p=CAVPOINT3D([x,y,z],iden)
	# p.coord[0] = x
	# p.coord[1] = y
	# p.coord[2] = z
	# p.id = iden
	V.append(p);

fV.close()
#print("U size:",str(len(U)))
#print("V size:",str(len(V)))

for i in range(len(U)):
	for j in range(len(V)):
		a = (U[i].coord[0] - V[j].coord[0])**2 + (U[i].coord[1] - V[j].coord[1])**2 + (U[i].coord[2] - V[j].coord[2])**2-distance
		if(a < 0):
			#print(a)
			d = DUMMYATOMPAIR(U[i].id,V[j].id)
			# d.i = U[i].id
			# d.j = V[j].id
			D.append(d)


#writing pairs of dummy atoms (cavity spheres) to the output file 
for i in range(len(D)): 
	print(D[i].groundcavid," ",D[i].methodspecid);

