class Fcp:
    ffl = []
    txt_nrw = ''
    def __init__(self, sr):
        self.pl = []
        for i in range(sr):
            for f in range(i):
                if (i /(f+1)) == int(i /(f+1)):
                    if (f+1 != 1) and (f+1 != i):
                        self.ffl += [f+1]
            if len(self.ffl) > 0:
                self.ffl = []
                pass
            elif i != 0 and i != 1:
                self.pl += [i]
        for i in range(len(self.pl)):
            self.txt_nrw = self.txt_nrw + ' , ' + ''.join(str(self.pl[i]))
        self.txt_nrw = self.txt_nrw[1::]
        self.save_txt = open('saved_primes.txt', 'w' , 1)
        self.save_txt.write(self.txt_nrw)
        self.save_txt.close()

hot_pot,end_pot,pal_pot = [],[],[]
iff = Fcp(600000)
pr_ls = iff.pl[::-1]
for i in pr_ls:
    hot_pot+=[str(i)]
for x in range(100):
    for i in hot_pot:
        if (i.startswith('2')== 1 
            or i.startswith('4')==1 
            or i.startswith('5')==1
            or i.startswith('6')==1 
            or i.startswith('8')==1):
            hot_pot.remove(i)
for i in range(len(hot_pot)):
    chunk_ls = [''.join([*(hot_pot[i][0:int((len(hot_pot[i]))/2)])]), 
                ''.join([*(hot_pot[i][0:int((len(hot_pot[i]))/2)])][::-1])]
    if (hot_pot[i].startswith(chunk_ls[0]) == 1)  and (hot_pot[i].endswith(chunk_ls[1])==1):
        pal_pot += [hot_pot[i]]
save_txt2 = open('saved_palindromic_primes.txt', 'w' , 1)
save_txt2.write(" , ".join(pal_pot))
save_txt2.close()