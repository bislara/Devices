from math import *
from sympy import *


# funct to return the value of funct at a particuar value
def func(Vgb, Shi_s, Vfb, NA, ND, Phi_t, q, Es, Cox, No, Po):
    try:
        p = Vfb + Shi_s + ((sqrt(2*q*Es))/(Cox)) * (sqrt(Po*Phi_t*(e**(-Shi_s/Phi_t)-1) +
                                    (NA-ND)*Shi_s + No*Phi_t*(e**(Shi_s/Phi_t)-1))) - Vgb
        print("p is ", p)
        return p

    except ZeroDivisionError:
        print("Error!!!!!!!!!!!", Shi_s)
        return 0


# funct to find derivative at a particular value
def derivFunc(Shi_s, Vgb, Vfb, NA, ND, Phi_t, q, Es, Cox, No, Po):
    # main function with variable t
    t = Symbol('t')
    f = Vfb + Shi_s + ((sqrt(2*q*Es))/(Cox))*(sqrt(Po*Phi_t*(e**(-t/Phi_t)-1) +
                              (NA-ND)*t + No*Phi_t*(e**(t/Phi_t)-1))) - Vgb

    deriv = Derivative(f, t)

    # this puts the value of t as Shi_s in the derivative of the main function
    k = deriv.doit().subs({t: Shi_s})
    print("k is ", k)
    if k == 0:
        return 1
    else:
        return k


# Newton_Raphson to find the root of the function
def newtonRaphson(Vgb, Shi_s, Vfb, NA, ND, Phi_t, q, Es, Cox, No, Po):

    err = 1
    count = 0
    # x(i+1) = x(i) - f(x) / f'(x)
    while abs(err) >= 0.001:
        count = count+1
        try:
            err = (func(Vgb, Shi_s, Vfb, NA, ND, Phi_t, q, Es, Cox, No, Po)) / \
                (derivFunc(Shi_s, Vgb, Vfb, NA, ND, Phi_t, q, Es, Cox, No, Po))
            Shi_s = Shi_s - (err)
            print("Shi_s is ", Shi_s)
        except ZeroDivisionError:
            print("Error! - derivative zero for x = ", Shi_s)

    print("The value of the root is : ",
          "%.4f" % Shi_s)
    # no of iterations for each value of vgb
    print("the no of iterations is ", count)
    return Shi_s
