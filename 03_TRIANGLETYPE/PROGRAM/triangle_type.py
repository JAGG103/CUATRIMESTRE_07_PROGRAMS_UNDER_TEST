def triangle_type(a,b,c):
    if(a<b+c and b<a+c and c<a+b and a==c and b==c):
        return 'Equilatero'
    elif(a<b+c and b<a+c and c<a+b and a==b and b!=c) or (a<b+c and b<a+c and c<a+b and a==c and c!=b) or (a<b+c and b<a+c and c<a+b and c==b and b!=a):
        return 'Isosceles'
    elif(a<b+c and b<a+c and c<a+b and a!=b and b!=c and c!=a):
        return 'Escaleno'
    return 'NonTriangle'