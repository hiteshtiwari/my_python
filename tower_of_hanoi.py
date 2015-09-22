def printMove(frm, to):
    print ('move from ' + str(frm) + ' to ' + str(to))


def Towers(n, frm, to, spare):
    if n == 1:
        printMove(frm, to)
    else:
        Towers(n-1, frm , spare , to)
        Towers(1, frm , to , spare)
        Towers(n-1, spare , to , frm)


Towers(4, 'f', 't', 's')
