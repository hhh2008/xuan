from time import ctime,sleep

def music():
    for i in range(2):
        print ("I was listening to music. %s" %ctime())
        sleep(1)

def move():
    for i in range(2):
        print ("I was at the movies! %s" %ctime())
        sleep(5)

if __name__ == '__main__':
    music()
    move()
    print ("all over %s" %ctime())
###https://www.cnblogs.com/antis/p/5275600.html
###Python多线程就这么简单
