import stim
from juliacall import Main as jl
from random import randint, choice
from paulie.common.pauli_string_factory import get_pauli_string as p
from pauliarray import PauliArray


def get_random(n: int) -> str:
    """ Get random Pauli String lenght n """
    return''.join([choice("IXYZ") for _ in range(n)])

def get_random_list(n:int, size: int) -> list[str]:
    """ Get random list of Pauli String lenght n """
    return [get_random(n) for _ in range(size)]

def paulistringJL():
    jl.include("paulistring.jl")
    pauli_module = jl.PauliString
    result_str = pauli_module.generate_pauli(3)
    print(f"generate_pauli(3): {result_str}")  # 
    mult_result = pauli_module.multiply_pauli("X", "Y")
    print(f"multiply_pauli('X', 'Y'): {mult_result}")  # 

def main():
    g = get_random_list(10, 10)
    stim_g = [stim.PauliString(a) for a in g]
    print(f"stim generators is {stim_g}")
    paulie_g = p(g)
    print(f"paulie generators is {paulie_g}")
    pauliarray_g = PauliArray.from_labels(g)
    print(f"pauliarray generators is {pauliarray_g}")
    paulistringJL()

    #g = p(["XX", "YY", "ZZ", "ZY"])
    #print(f"{g.get_algebra()} is {g.is_algebra('u(1)+2*su(2)')}")


if __name__ == "__main__":
    main()
