import random


def strategia(stan_gry):
    """To jest prosta strategia"""
    ruch = min(stan_gry, random.randint(1, 3))
    return ruch

# help(komputer.strategia)
