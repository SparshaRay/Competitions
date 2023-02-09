#SWH 2022 Hackathon Q-4

m_1=float(input("enter mass of ball 1="))
m_2=float(input("enter mass of ball 2="))
u_1=float(input("enter velocity="))

v_2=u_2=0
r=0.05
x_1=10-r
x_2=r
wall=0
dt=u_1/1000
ncol=0
u_1=(-1)*u_1
v_1=u_1


running=1
while running==1:
    col=False
    x_1=x_1+(dt*v_1)
    x_2=x_2+(dt*v_2)
    if abs(x_1-x_2)<(2*r):
        col=True
        if (m_1-m_2)<0:
            x_1=x_2+(2*r)
        elif (m_2-m_1)<0:
            x_2=x_1-(2*r)
        elif m_1==m_2:
            x_2=x_1-(2*r)
        print("no")
    elif abs(x_2-wall)<=r:
        col=True
        k=2
        print("yes")
        x_2=x_2+r
    if col:
        if k==2:
            v_2=(-1)*v_2
        else:
            v_1=u_1*(m_1-m_2)/(m_2+m_1)+(u_2*2*m_2)/(m_1+m_2)
            v_2=u_2*(m_1-m_2)/(m_2+m_1)+(u_1*2*m_1)/(m_1+m_2)
        u_1=v_1
        u_2=v_2
        ncol=ncol+1
    if v_1>=v_2:
        running=0
print(ncol)
    
    

