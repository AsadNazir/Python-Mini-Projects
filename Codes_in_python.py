import os


# Bubble Sort
# num_list = [2, 4, 0, -9, 39, 2, 2, 2, -9, 6, 7]

# length=int(len(num_list))


# for i in range(length):

#     for j in range (length-1-i):

#         if(num_list[j]>num_list[j+1]):

#             #Swapping Procedure
#             tmp=num_list[j]
#             num_list[j]=num_list[j+1]
#             num_list[j+1]=tmp

# print(num_list)

# -----------------------------------------------------------------------------------------

# Selection Sort

# num_list = [2, 4, 0, -9, 39, 2, 2, 2, -9, 6, 7]
# length = int(len(num_list))

# for i in range(length):

#     for j in range(i, length, 1):
#         if(num_list[i]>num_list[j]):
              
#             # Swapping Procedure
#             tmp = num_list[i]
#             num_list[i] = num_list[j]
#             num_list[j] = tmp
      
# print(num_list)

# -----------------------------------------------------------------------------------------
       
num_list = [2, 4, 0, -9, 39, 2, 2, 2, -9, 6, 7]
length = int(len(num_list))

for i in range(1,length):
    
    key=num_list[i]
    j=i-1

    while (j>=0 and num_list[j]>key):
        #Swapping Over Here
        num_list[j+1]=num_list[j]
        j-=1

    num_list[j+1]=key
    
print(num_list)


    

