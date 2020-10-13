num = input("请输入一个奇数：")
for topRow in range((int(num)-1)//2,0,-1): #循环打印上半部分
    for leftBlack in range(topRow):#循环打印上半部分的每一行的左边的空格
        print(" ",end="")
    for midStar in range(int(num)-2*topRow):#循环打印上半部分每一行的中间的星星
        print("*",end="")
    for top in range(topRow):#循环打印上半部分的每一行的右边的空格
        print(" ", end="")
    print()#上半部分每一行打印结束后行进换行
for midStar in range(int(num)): #打印最中间行的星星
    print("*",end="")
print()#最中间行打印结束后进行换行
for bottomRow in range(1,int(num)//2+1):#循环打印下半部分
    for leftBlack in range(bottomRow):#循环打印下半部分的每一行的左边的空格
        print(" ",end="")
    for midStar in range(int(num)-2*bottomRow):#循环打印下半部分每一行的中间的星星
        print("*",end="")
    for rightBlack in range(bottomRow):#循环打印下半部分每一行的右边的空格
        print(" ",end="")
    print()#下半部分每一行打印结束后换行
    ##我在这里修改了Github