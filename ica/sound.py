import mdp
x = {0.09, 0.04, 0.94, 0.94, 0.26, 0.46}
y = mdp.pca(x)
print(y)
y = mdp.fastica(x, dtype='float32')
print(y)
