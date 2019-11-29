from pyDatalog import pyDatalog


pyDatalog.create_terms('croakes, eatflies, frog, chrips, sings, canary, green, yellow, P, X')

pyDatalog.load("""
frog(X) <= croakes(X) & eatflies(X)
canary(X) <= sings(X) & chrips(X)
green(X) <= frog(X)
yellow(X) <= canary(X)
                """)

pyDatalog.assert_fact('croakes', 'Fritz')
pyDatalog.assert_fact('eatflies', 'Fritz')

pyDatalog.assert_fact('sings', 'Paul')
pyDatalog.assert_fact('chrips', 'Paul')

query = 'yellow(X)'
answers = pyDatalog.ask(query).answers

print(answers)

print(pyDatalog.ask('green(X)'))
