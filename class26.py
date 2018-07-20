#file IO
# file = open('sample.txt','w')
# file.write('Sushilx')
# file.close()

# file = open('sample.txt','a')
# file.write('Sushil KC')
# file.write('\n')
# file.close()

from class23 import Point

def writeP2file(p1,p2):
    xyz = open('result.txt', 'a')
    xyz.write("Point1 = ")
    pf = str(p1)
    xyz.write(pf)
    xyz.write('\n')
    xyz.write("Point2 = ")
    ps =str(p2)
    xyz.write(ps)
    xyz.write('\n')
    xyz.write("Distance = ")
    dis = p1.distance(p2)
    distance = '%.2f'%(dis)
    xyz.write(distance)
    xyz.write('\n')

# writeP2file(Point(2,3),Point(4,5))

#creating a diary 

# import time as tm 
# t1 = tm.time()
# t2 = tm.localtime(t1)
# t3 = tm.asctime(t2)

# with open('diary.txt','a') as file:
#     file.write(input())
#     file.write('\n')
#     file.write(t3)
#     file.write('\n')
#     file.write('\n')


#file reading
# file = open('diary.txt','r')
# txt = file.read()
# print(txt)
# file.close()

# with open('diary.txt', 'r') as file:
#     txt = file.read(10)
#     print(file.tell())
#     print(txt)
#     file.seek(20,0)
#     txt = file.read(10)
#     print(file.tell())
#     print(txt)


# file = open('sample.txt', 'r')
# print(file.tell())
# print(file.read())
# print(file.tell())
# file.seek(10,0)
# print(file.read())
# file.close()

# file = open('sample2.txt', 'a')
# file.write(input())
# file.close()


# try:
#     file = open('sample3.txt', 'r+')
#     print(file.read())
# except FileNotFoundError:
#     file = open('sample3.txt', 'w+')
#     file.write('a=12\nb=23')
#     print('a=12\nb=23')
# finally:    
#     file.close()

# with open('sample.txt', 'r') as file:
#     print(file.read())

# import time
# with open('diary.txt', 'a') as file:
#     file.write(input())
#     file.write('\n')
#     localtime = time.asctime( time.localtime(time.time()) )
#     file.write(localtime)
#     file.write('\n\n')


#Exercise
# file = open("table.txt", 'w')
# for i in range(2,11):
#     for j in range(1,11):
#         print(i,"X",j,"=",i*j)
#         val = str(i)+" X "+str(j)+" = "+str(i*j)
#         file.write(val)
#         file.write('\n')
#     print()
#     file.write('\n')
# file.close()


#pickel: serialize python object to save to file or send as dataStream

import pickle

dogs_dict = { 'Ozzy': 3, 'Filou': 8, 'Luna': 5,
 'Skippy': 10, 'Barco': 12, 'Balou': 9, 'Laika': 16 }

# filename = 'dogs.txt'
# outfile = open(filename,'wb')
# pickle.dump(dogs_dict,outfile)
# outfile.close()

# infile = open(filename,'rb')
# new_dict = pickle.load(infile)
# infile.close()
# print(new_dict)
# print(new_dict==dogs_dict)
# print(type(new_dict))


#Storing object in file using pickel
# with open('point.txt','wb') as file:
#     p1 = Point(2,3)
#     pickle.dump(p1,file)

# with open('point.txt','rb') as file:
#     p2 = pickle.load(file)
#     print(p2)

#Storing array of objects in file
# points_array = (Point(2,3), Point(5,4))
# with open('point_array.txt','wb') as file:
#     pickle.dump(points_array,file)

# with open('point_array.txt','rb') as file:
#     p = pickle.load(file)

# distance = p[0].distance(p[1])
# print("The distance is %.2f"%(distance))