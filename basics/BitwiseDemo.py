print('Zealous wishes you to get best career')

# Bit wise operator: & | ^ >> <<
# 65, 34
'''
2048 1024 512 256 128 64 32 16 8 4 2 1
0    0    0   0   1   0  0  0  1 1 0 0  >> 140
0    0    1   0   0   0  1  1  0 0 0 0  >> 560
0    0    0   0   1   0  0  0  1 1 0 0  >> 140
0    0    0   0   0   1  1  1  1 0 0 0  >> 120
0    0    0   0   1   0  0  0  0 0 0 1  >> 129
0    1    0   0   0   0  0  0  1 0 0 0  >>  1032
0    0    0   0   0   0  0  0  0 0 1 1  >>  3
0    0    0   0   0   1  0  0  1 1 1 0  >> 78
1 0  0    1   1   1   0  0  0  0 0 0 0
0    0    0   0   0   1  0  0  0 0 0 1  >> 65
0    0    0   0   0   0  1  0  0 0 1 0  >> 34

0    0    0   0   0   1  1  0  0 0 1 0  >> 98
0    0    0   0   0   0  0  0  1 1 0 0  >> 12
0    0    0   0   0   1  1  0  1 1 1 0  >> 110
0    0    0   0   1   1  0  0  1 0 0 0  >> 200
0    0    1   0   1   0  0  0  0 1 0 1  >> 645
0    0    1   0   1   1  0  0  1 1 0 1  >> 717

0    0    0   0   0   1  0  0  0 0 0 0  >> 64
'''
'''
cosmo=98
delta=200

print(cosmo&delta)
print(delta|645)
print(cosmo^12)

print("Cosmo is",cosmo,"DElta is",delta)

# swap by ^
cosmo^=delta#cosmo=cosmo^delta
delta^=cosmo#delta=delta^cosmo
cosmo^=delta#cosmo=cosmo^delta

print("Cosmo is",cosmo,"DElta is",delta)'''

tony=120
pepper=78

print(tony)

print(tony>>5)
print(tony)

print(pepper)

print(pepper<<6)
print(pepper)