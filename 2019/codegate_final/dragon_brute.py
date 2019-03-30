def tupleadd(a1, a2):
     return (a1[0]+a2[0], a1[1]+a2[1], a1[2]+a2[2], a1[3]+a2[3], a1[4]+a2[4])



l1 = [(0, 0, 0, 0, 1), (0, 1, 0, 0, 0)]
l2 = [(1, 2, 1, 0, 1), (0, 2, 1, 1, 1)]
l3 = [(1, 1, 0, 0, 1), (1, 0, 0, 0, 0), (1, 1, 0, 0, 0), (0, 0, 0, 0, 0)]
l4 = [(1, 0, 2, 2, 1)]
l5 = [(0, 0, 1, 2, 2), (0, 1, 2, 1, 1), (0, 0, 0, 0, 0)]
l6 = [(1, 0, 1, 0, 0), (2, 0, 2, 0, 1), (0, 0, 0, 0, 0)]
l7 = [(1, 2, 0, 2, 1), (0, 0, 0, 0, 0)]
for i1 in l1:
     for i2 in l2:
             for i3 in l3:
                     for i4 in l4:
                             for i5 in l5:
                                     for i6 in l6:
                                             for i7 in l7:
                                                     c = tupleadd(tupleadd(tupleadd(tupleadd(tupleadd(tupleadd(i1, i2), i3), i4), i5), i6), i7)
                                                     if c == (5, 5, 5, 5, 5):
                                                             print "found!"
                                                             print i1, i2, i3, i4, i5, i6, i7
