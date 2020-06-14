import numpy as np 

def decrypt(cipher,key):
	flag=""
	for i in cipher:
		to_work_with=i.split(' ')
		first_mat=np.zeros((3,3))
		l=0
		c=0
		for j in to_work_with:
			first_mat[l][c]=j
			c+=1
			if c>2:
				c=0
				l+=1
				if l>2:
					break
		original_matrix=np.matmul(np.transpose(first_mat),key)
		for line in range(3):
			for col in range(3):
					flag+=chr(int(round(original_matrix[line,col])))
	return flag



Ciphertext ="578.0 642.0 690.0 861.0 978.0 1017.0 653.0 807.0 734.0----710.0 579.0 360.0 1067.0 826.0 576.0 837.0 504.0 553.0----425.0 363.0 583.0 685.0 625.0 892.0 680.0 736.0 750.0----670.0 585.0 612.0 985.0 874.0 893.0 705.0 666.0 620.0----697.0 423.0 688.0 1028.0 657.0 939.0 744.0 576.0 441.0"

different_matrix=Ciphertext.split('----')
key=np.matrix("1 2 3;0 1 4;5 6 0")

key_inv=np.linalg.inv(key)
decrypt(different_matrix,key_inv)
print decrypt(different_matrix,key_inv)
