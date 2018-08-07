import math

def format_float(val):
    num = round(val, 2)
    return ('%i' if num == int(num) else '%s') % num

def checkio(data):

    pp = []
    p = []
    for pair_string in data.replace("),(", ");(").split(";"):
        pp.append([float(s) for s in pair_string[1:-1].split(",") if s.isdigit()])

    if pp[0][1] == pp[1][1]:
        p.append(pp[1])
        p.append(pp[2])
        p.append(pp[0])
    elif pp[1][1] == pp[2][1]:
        p.append(pp[1])
        p.append(pp[0])
        p.append(pp[2])
    else:
        p = pp

    x1, y1 = p[0][0], p[0][1]
    x2, y2 = p[1][0], p[1][1]
    x3, y3 = p[2][0], p[2][1]

    x = \
        ((x3**2 - x2**2 + y3**2 - y2**2) / (2*(y3 - y2)) - \
         (x2**2 - x1**2 + y2**2 - y1**2) / (2*(y2 - y1))) /\
        ((x3 - x2)/(y3 - y2) - (x2 - x1)/(y2-y1))

    y = -(x2-x1)/(y2-y1)*x + (x2**2 - x1**2 +y2**2-y1**2)/2/(y2-y1)

    r = math.sqrt( (x1-x)**2 + (y1-y)**2)

    fx = format_float(x)

    #print(f"(x-{fx})^2+(y-{format_float(y)})^2={format_float(r)}^2" )
    #replace this for solution
    return f"(x-{fx})^2+(y-{format_float(y)})^2={format_float(r)}^2"


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"