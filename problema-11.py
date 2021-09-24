n=int(input('Dati numarul de elemente din vector='))
if 0<n<10:    
    a=[]
for i in range(n):
    int=(input('Dati elementul='))
    a.append(i)
print('a:  afişează pe ecran componentele tabloului la un interval de 5 poziţii;')
print(a[::5])
print('b:  afişează pe ecran numerele în ordinea inversă a introducerii în calculator;')
print(a[::-1])
print('c:  sortează componentele tabloului în ordine descrescătoare;')
b=sorted(a)
b.sort(reverse=True)
print(b)
print('d:  afişează pe ecran doar componentele pare;')
pare=[]
for i in range(0,len(a)):
    if a[i]%2==0:
        y=a[i]
        pare.extend([y])
print(pare)
print('e:  afişează pe ecran media aritmetică a componentelor pare;')
print(round(sum(pare)/len(pare),2))
print('f:  afişează pe ecran doar componentele impare;')
impare=[]
for i in range(0,len(a)):
    if a[i]%2!=0:
        ia=a[i]
        impare.extend([ia])
print(impare)
print('g:  afişează pe ecran doar componentele care sunt mai mari ca x şi nu sunt divizibile cu y (valorile x şi y se citesc de la tastatură);')
x=int(input("x="))
y=int(input("y="))
v=[]
for i in a:
    if ((i>x)and(i%y!=0)):
        z=i
        v.extend([z])
print(v)
print('h:  afişează pe ecran doar componentele care sunt mai mari ca x şi mai mici decât y (valorile x şi y se citesc de la tastatură);')
val=[]
for i in a:
    if ((i>x)and(i<y)):
        y=i
        val.extend([y])
print(val)
print('i:  afişează pe ecran poziţiile (indicii) componentelor impare negative;')
o=[]
for i in im:
    if i<0:
        o.extend([a.index(i)])
print(o)
print('j:  afişează pe ecran poziţiile (indicii) componentelor ce conţin doar două cifre semnificative;')
r=[]
for i in range(0,n):
    if ((a[i]>9)and(a[i]<100))or((a[i]>-100)and(a[i]<-9)):
        r.extend([i])
print(r)
print('k:  înlocuieşte prima componentă a tabloului cu componenta de valoare minimă din tabloul respectiv;')
m=a.copy()
m[0]=min(m)
print(m)
print('l)  înlocuieşte componenta de valoare minimă din tabloul respectiv cu prima componentă a acestuia;')
l=a.copy()
l[l.index(min(l))]=l[0]
print(l)