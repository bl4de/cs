def swap_case(s):
    return''.join([c.upper() if ord(c) > 0x60 else c.lower() for c in s])

print(swap_case("Audi A4")) # aUDI a4
