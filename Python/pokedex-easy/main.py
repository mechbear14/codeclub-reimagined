from utilities import get_props_by_no, print_chars

number = input("Pokemon number: ")
pokemon = get_props_by_no(number)
print("\n", end="")
try:
    print_chars(pokemon.name)
    length = len(pokemon.name) * 6 - 1
    padding = int((length - 1) / 2 - 15)
    padding = padding if padding > 0 else 0
    hr = f"\n{'=' * length}\n"
    spaces = f"{' ' * padding}"
    print(hr)
    print(f"{spaces}             HP: {pokemon.hp}")
    print(f"{spaces}         Attack: {pokemon.attack}")
    print(f"{spaces}        Defence: {pokemon.defence}")
    print(f"{spaces} Special attack: {pokemon.special_attack}")
    print(f"{spaces}Special defence: {pokemon.special_defence}")
except AttributeError:
    print_chars("error")
    print(f"\n{'=' * 29}\n")
    reason = pokemon
    padding = int((29 - len(reason)) / 2)
    padding = padding if padding > 0 else 0
    spaces = f"{' ' * padding}"
    print(f"{spaces}{reason}")
finally:
    print("")
