from microbit import*
s = 500
code = 0
cod = 0
b = pin0
led = pin16
led.write_digital(cod)
sleep(s)
#These are all the letters mors codes
A = [1,0,0,0,0,0,0,1] 
B = [1,0,1,0,0,0,0,1]
C = [1,0,0,1,0,0,0,1]
D = [1,0,0,0,1,0,0,1]
E = [1,0,0,0,0,1,0,1]
F = [1,1,0,0,0,0,0,1]
G = [1,0,1,1,0,0,0,1]
H = [1,0,0,1,1,0,0,1]
I = [1,0,0,0,1,1,0,1]
J = [1,0,0,0,0,1,1,1]
K = [1,1,0,0,0,0,1,1]
L = [1,0,1,0,0,0,1,1]
M = [1,0,0,1,0,0,1,1]
N = [1,0,0,0,1,0,1,1]
O = [1,0,0,0,0,1,1,1]
P = [1,1,1,0,0,0,1,1]
Q = [1,0,1,1,0,0,1,1]
R = [1,0,0,1,1,0,1,1]
S = [1,0,0,0,1,1,1,1]
T = [1,1,1,0,0,1,1,1]
U = [1,0,1,1,0,1,1,1]
V = [1,0,0,1,1,1,1,1]
W = [1,1,1,1,1,0,0,1]
X = [1,1,1,0,1,1,1,1]
Y = [1,1,1,1,0,1,1,1]
Z = [1,1,1,1,1,1,1,1]
mors = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]
#This variable will contain the sentance that you want to send
let = hello
txt = let.upper()
text = txt.split()
num = len(text)
mun = len(A)
print(num*mun)
val = b.read_digital()
for x in range(num*mun):
    led.write_digital(let[code][cod])
    if cod == 7:
        cod -= 7
        cod = 0
        if code == 7:
            code -= 7
            code = 0
        code += 1
    cod += 1
    sleep(s)
