__author__ = 'ShinyA'

us = {'us', 'usa', 'u.s.a', 'united states', 'u.s.a.', 'u.s', 'u.s.'}
states = dict()
other_countries = dict()

for line in open("state_rates.txt", "r").readlines():
    items = line.split("\t")
    states[items[0].lower()] = float(items[4][:-1])

for line in open("taxes_other.txt", "r").readlines():
    items = line.split("\t")
    other_countries[items[0].lower()] = float(items[1][:-2])

price = float(input("Input your price "))
country = (input("Input your country ")).lower()

if country not in us:
    if country in other_countries:
        tax = other_countries[country]
        print("Tax is ", tax,"%")
        total_price = price + price*(tax/100)
        print("Your total price is ", total_price, "u.e.")
else:
    state = input("Input your full state name ")
    state = state.lower()
    if state in states:
        tax = states[state]
        print("Tax is ", tax,"%")
        total_price = price + price*(tax/100)
        print("Your total price is ", total_price, "dollars")
 