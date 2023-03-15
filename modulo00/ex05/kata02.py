#import sys

#kata = (2019, 9, 25, 3, 30)

#try:
#    assert len(kata) == 5, "wrong nums of elements"
#    for i in kata: 
#        assert int(i) >= 0, "Only positive nums"
#    assert len(str(kata[0])) == 4, "First num must be 4 digits or less"
#    for s in kata:
#        assert all(len(str(s)) <= 2 for s in kata[1::]), "The num must be 2 digits or less"
#except AssertionError as msg:
#    print ("AsertionError:", msg)
#    sys.exit()
#except:
#    print("Only integers")
#    sys.exit()


#print(f"{kata[1]}/{kata[2]}/{kata[0]} {kata[3]}:{kata[4]}")


import datetime
kata = datetime.datetime(2019, 9, 25, 3, 30)

print('{:%Y/%m/%d %H:%M}'.format(kata))
