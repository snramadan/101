def poly_add2(poly1, poly2):
    new0 = poly1[0] + poly2[0]
    new1 = poly1[1] + poly2[1]
    new2 = poly1[2] + poly2[2]
    new = [new0, new1, new2]
    return new

def poly_mult2(x, y):
    a0 = x[0] * y[0]
    a1 = (x[0] * y[1]) + (x[1] * y[0])
    a2 = (x[0] * y[2]) + (x[1] * y[1]) + (x[2] * y[0])
    a3 = (x[1] * y[2]) + (x[2] * y[1])
    a4 = x[2] * y[2] 
    new = [a4, a3, a2, a1, a0]
    return new

