def computepay(hr, rt):
    if hr > 40:
        return ((hr - (hr - 40)) * rt) + (hr - 40) * (rt * 1.5)
    else:
        return hr * rt

hrs = input("Enter Hours:")
rate = input("Enter Rate:")

h = float(hrs)
r = float(rate)
p = computepay(h, r)
print("Pay", p)