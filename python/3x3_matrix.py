title = "Determinant for 3x3 Matrix"


def determinant():
    print(title.upper())
    a11, a12, a13 = input("Enter values for Row 1: ").split()
    a11 = int(a11)
    a12 = int(a12)
    a13 = int(a13)
    a21, a22, a23 = input("Enter values for Row 2: ").split()
    a21 = int(a21)
    a22 = int(a22)
    a23 = int(a23)
    a31, a32, a33 = input("Enter values for Row 3: ").split()
    a31 = int(a31)
    a32 = int(a32)
    a33 = int(a33)
    x = a33*a22 - a23*a32
    y = a33*a21 - a23*a31
    z = a21*a32 - a22*a31
    Determinant = a11*x - a12*y + a13*z
    print(f"Determinant, D={Determinant}.")
    if Determinant != 0:
        print("The 3x3 matrix is Non-singular!")
    else:
        print("The 3x3 Matrix is a Singular Matrix")
