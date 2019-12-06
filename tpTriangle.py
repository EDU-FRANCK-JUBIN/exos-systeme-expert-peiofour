from pyDatalog import pyDatalog

pyDatalog.create_terms('triangle'
                       'angle'
                       'angle_droit'
                       'nbcotes'
                       'cotes_egaux'
                       'isocele'
                       'rectangle'
                       'equilateral'
                       'rectangle_isocele'
                       't1'
                       't2'
                       't3'
                       't4'
                       'X'
                       'Y')

pyDatalog.load("""
triangle(X) <= nb_cote(X, Y) & (Y==3)
isocele(X) <= triangle(X) & cotes_egaux(X, Y) & (Y==2)
equilateral(X) <= triangle(X) & cotes_egaux(X, Y) & (Y==3)
rectangle(X) <= triangle(X) & angle_droit(X)
rectangle_isocele(X) <= rectangle(X) & isocele(X)
""")

pyDatalog.assert_fact('nb_cote', 't1', 3)
pyDatalog.assert_fact('nb_cote', 't2', 3)
pyDatalog.assert_fact('nb_cote', 't3', 3)
pyDatalog.assert_fact('nb_cote', 't4', 3)

pyDatalog.assert_fact('cotes_egaux', 't2', 3)
pyDatalog.assert_fact('cotes_egaux', 't3', 2)
pyDatalog.assert_fact('angle_droit', 't4')
pyDatalog.assert_fact('angle_droit', 't2')

print(pyDatalog.ask('rectangle(X)'))
