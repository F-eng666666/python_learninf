my_list = [
    ('a',7),
    ('b',1),
    ('c',12),
    ('w',3),
    ('e',6),
]

print(sorted(my_list, key = lambda x: x[0], reverse=True))