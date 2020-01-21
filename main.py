f = open('pars.txt')
x = f.read(-100)
x = x.replace('0','').replace('1','').replace('2','').replace('3','').replace('4','').replace('5','').replace('6','').replace('7','').replace('8','').replace('9','').replace('0','').replace(':','')
d = open('res.txt', 'w')
d.writelines(x)
d.close()
f.close()



    
  
    
 



 