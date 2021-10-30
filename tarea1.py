print("Roses are #ff0000, Violets are #0000ff why my code´s working" + "I haven´t a clue")
import colorama
from colorama import Fore, init colorama.init()
print((Fore.red + "roses are red")+(Fore.blue + "violets are blue")+(Fore.white + "my code´s working"))