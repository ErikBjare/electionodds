def p_win_over_trump(p_won_primary, p_president):
    assert 0 < p_won_primary < 1
    assert 0 < p_president < 1
    return p_president / p_won_primary


odds = [
    ('Warren', 0.366, 0.185),
    ('Biden', 0.233, 0.13),
    ('Yang', 0.052, 0.034),
    ('Buttigieg', 0.044, 0.022)
]

for name, p_won_primary, p_president in odds:
    print(f"{name:9} - Win against Trump:  {round(p_win_over_trump(p_won_primary, p_president)*100, 1)}%")
