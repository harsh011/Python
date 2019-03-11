def main():
    fun4(s1="devo",s2="jado",s3="chotu")
    fun5(1,2,3,4,5,6,7,devo='foo',jado='genius',chotu='zoo')
    print(fun6())

def fun4(**kwargs):
    print("arguments ",kwargs['s1'],kwargs['s2'],kwargs['s3'])

def fun5(a=1,b=2,c=3,*args,**kwargs):
          print(" a,b,c = ",a, " ",b," ",c)
          for n in args:
              print(n,end=' ')
          for i in kwargs:
              print(i,' = ',kwargs[i])

def fun6():
    return 'hi hello'

main()
