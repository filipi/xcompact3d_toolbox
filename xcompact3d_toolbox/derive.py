from .param import mytype
import scipy.sparse as sp

def SecondDerivative(n, d, ncl1=2, ncln=2, npaire=1):
    '''
    f_xx = (-1*f[i-2]+16*f[i-1]-30*f[i+0]+16*f[i+1]-1*f[i+2])/(12*h**2)
    '''
    rhs = sp.diags([-1., 16., -30., 16., -1.],
                  offsets=[-2, -1, 0, 1, 2],
                  shape=(n,n),
                  dtype=mytype,
                  format="lil")

    # Boundary Conditions at i = 0
    if ncl1 == 0:
        #f_xx = (-1*f[-2]+16*f[-1]-30*f[0]+16*f[1]-1*f[2])/(12*h**2)
        rhs[0,-1] = rhs[0,1]
        rhs[0,-2] = rhs[0,2]
        #f_xx = (-1*f[-1]+16*f[0]-30*f[1]+16*f[2]-1*f[3])/(12*h**2)
        rhs[1,-1] = rhs[1,3]
    if ncl1 == 1:
        if npaire == 0:
            #f_xx = (1*f[2]-16*f[1]-0*f[0]+16*f[1]-1*f[2])/(12*h**2)
            rhs[0,0] = 0.
            rhs[0,1] = 0.
            rhs[0,2] = 0.
            #f_xx = (1*f[1]+0*f[0]-30*f[1]+16*f[2]-1*f[3])/(12*h**2)
            rhs[1,0] = 0.
            rhs[1,1] -= rhs[1,3]
        elif npaire == 1:
            #f_xx = (-1*f[2]+16*f[1]-30*f[0]+16*f[1]-1*f[2])/(12*h**2)
            rhs[0,1] *= 2.
            rhs[0,2] *= 2.
            #f_xx = (-1*f[1]+16*f[0]-30*f[1]+16*f[2]-1*f[3])/(12*h**2)
            rhs[1,1] += rhs[1,3]
    elif ncl1 == 2:
        #f_xx = (35*f[0]-104*f[1]+114*f[2]-56*f[3]+11*f[4])/(12*h**2)
        rhs[0,0] =   35.
        rhs[0,1] = -104.
        rhs[0,2] =  114.
        rhs[0,3] = - 56.
        rhs[0,4] =   11.
        #f_xx = (11*f[i-1]-20*f[i+0]+6*f[i+1]+4*f[i+2]-1*f[i+3])/(12*h**2)
        rhs[1,0] =   11.
        rhs[1,1] = - 20.
        rhs[1,2] =    6.
        rhs[1,3] =    4.
        rhs[1,4] = -  1.

    # Boundary Conditions at i = n
    if ncln == 0:
        #f_xx = (-1*f[-3]+16*f[-2]-30*f[-1]+16*f[0]-1*f[1])/(12*h**2)
        rhs[-1,0] = rhs[-1,-2]
        rhs[-1,1] = rhs[-1,-3]
        #f_xx = (-1*f[-4]+16*f[-3]-30*f[-2]+16*f[-1]-1*f[0])/(12*h**2)
        rhs[-2,0] = rhs[-2,-4]
    if ncln == 1:
        if npaire == 0:
            #f_xx = (-1*f[-3]+16*f[-2]-0*f[-1]-16*f[-2]+1*f[-3])/(12*h**2)
            rhs[-1,-1] = 0.
            rhs[-1,-2] = 0.
            rhs[-1,-3] = 0.
            #f_xx = (-1*f[-4]+16*f[-3]-30*f[-2]+0*f[-1]+1*f[-2])/(12*h**2)
            rhs[-2,-1] = 0.
            rhs[-2,-2] -= rhs[-2,-4]
        elif npaire == 1:
            #f_xx = (-1*f[-3]+16*f[-2]-30*f[-1]+16*f[-2]-1*f[-3])/(12*h**2)
            rhs[-1,-2] *= 2.
            rhs[-1,-3] *= 2.
            #f_xx = (-1*f[-4]+16*f[-3]-30*f[-2]+16*f[-1]-1*f[-2])/(12*h**2)
            rhs[-2,-2] += rhs[-2,-4]
    elif ncln == 2:
        #f_xx = (11*f[-5]-56*f[-4]+114*f[-3]-104*f[-2]+35*f[-1])/(12*h**2)
        rhs[-1,-5] =   11.
        rhs[-1,-4] = - 56.
        rhs[-1,-3] =  114.
        rhs[-1,-2] = -104.
        rhs[-1,-1] =   35.
        #f_xx = (-1*f[-5]+4*f[-4]+6*f[-3]-20*f[-2]+11*f[-1])/(12*h**2)
        rhs[-2,-5] = -  1.
        rhs[-2,-4] =    4.
        rhs[-2,-3] =    6.
        rhs[-2,-2] = - 20.
        rhs[-2,-1] =   11.

    return (rhs / (12. * d*d)).tocoo()

def FirstDerivative(n, d, ncl1=2, ncln=2, npaire=1):
    '''
    f_x = (1*f[i-2]-8*f[i-1]+0*f[i+0]+8*f[i+1]-1*f[i+2])/(12*h**1)
    '''
    rhs = sp.diags([1., -8., 8., -1],
                  offsets=[-2, -1, 1, 2],
                  shape=(n,n),
                  dtype=mytype,
                  format="lil")

    # Boundary Conditions at i = 0
    if ncl1 == 0:
        #f_x = (1*f[-2]-8*f[-1]+0*f[0]+8*f[1]-1*f[2])/(12*h**1)
        rhs[0,-1] = -rhs[0,1]
        rhs[0,-2] = -rhs[0,2]
        #f_x = (1*f[-1]-8*f[0]+0*f[1]+8*f[2]-1*f[3])/(12*h**1)
        rhs[1,-1] = -rhs[1,3]
    if ncln == 1:
        if npaire == 0:
            #f_x = (-1*f[2]+8*f[1]+0*f[0]+8*f[1]-1*f[2])/(12*h**1)
            rhs[0,1] *= 2.
            rhs[0,2] *= 2.
            #f_x = (-1*f[1]-8*f[0]+0*f[1]+8*f[2]-1*f[3])/(12*h**1)
            rhs[1,1] += rhs[1,3]
        elif npaire == 1:
            #f_x = (1*f[2]-8*f[1]+0*f[0]+8*f[1]-1*f[2])/(12*h**1)
            rhs[0,1] = 0.
            rhs[0,2] = 0.
            #f_x = (1*f[1]-8*f[0]+0*f[1]+8*f[2]-1*f[3])/(12*h**1)
            rhs[1,1] -= rhs[1,3]
    elif ncl1 == 2:
        #f_x = (-25*f[0]+48*f[1]-36*f[2]+16*f[3]-3*f[4])/(12*h**1)
        rhs[0,0] = - 25.
        rhs[0,1] =   48.
        rhs[0,2] = - 36.
        rhs[0,3] =   16.
        rhs[0,4] = -  3.
        #f_x = (-3*f[0]-10*f[1]+18*f[2]-6*f[3]+1*f[4])/(12*h**1)
        rhs[1,0] = -  3.
        rhs[1,1] = - 10.
        rhs[1,2] =   18.
        rhs[1,3] = -  6.
        rhs[1,4] =    1.

    # Boundary Conditions at i = n
    if ncln == 0:
        #f_x = (1*f[-3]-8*f[-2]+0*f[-1]+8*f[0]-1*f[1])/(12*h**1)
        rhs[-1,0] = -rhs[-1,-2]
        rhs[-1,1] = -rhs[-1,-3]
        #f_x = (1*f[-4]-8*f[-3]+0*f[-2]+8*f[-1]-1*f[0])/(12*h**1)
        rhs[-2,0] = -rhs[-2,-4]
    elif ncln == 1:
        if npaire == 0:
            #f_x = (1*f[-3]-8*f[-2]+0*f[-1]-8*f[-2]+1*f[-3])/(12*h**1)
            rhs[-1,-2] *= 2.
            rhs[-1,-3] *= 2.
            #f_x = (1*f[-4]-8*f[-3]+0*f[-2]+8*f[-1]+1*f[-2])/(12*h**1)
            rhs[-2,-2] += rhs[-2,-4]
        elif npaire == 1:
            #f_x = (1*f[-3]-8*f[-2]+0*f[-1]+8*f[-2]-1*f[-3])/(12*h**1)
            rhs[-1,-2] = 0.
            rhs[-1,-3] = 0.
            #f_x = (1*f[-4]-8*f[-3]+0*f[-2]+8*f[-1]-1*f[-2])/(12*h**1)
            rhs[-2,-2] -= rhs[-2,-4]
    elif ncln == 2:
        #f_x = (3*f[-5]-16*f[-4]+36*f[-3]-48*f[-2]+25*f[-1])/(12*h**1)
        rhs[-1,-5] =    3.
        rhs[-1,-4] = - 16.
        rhs[-1,-3] =   36.
        rhs[-1,-2] = - 48.
        rhs[-1,-1] =   25.
        #f_x = (-1*f[-5]+6*f[-4]-18*f[-3]+10*f[-2]+3*f[-1])/(12*h**1)
        rhs[-2,-5] = -  1.
        rhs[-2,-4] =    6.
        rhs[-2,-3] = - 18.
        rhs[-2,-2] =   10.
        rhs[-2,-1] =    3.

    return (rhs / (12. * d)).tocoo()
