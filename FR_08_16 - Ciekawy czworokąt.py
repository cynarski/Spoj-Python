from math import sin,pi
r,alfa,beta,gamma = [int(x) for x in input().split()]
delta = 360 - alfa - beta - gamma
pole = (r**2 *(sin(alfa*pi/180) + sin(beta*pi/180) + sin(gamma*pi/180) + sin(delta*pi/180)))/2
print('{:0.4f}'.format(pole))