"""Some dictionary utility functions."""

__author__ = "730526509"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Inverts dict key and vaule."""
    none: dict[str, str] = dict()
    ix = {v: k for k, v in x.items()}
    x_index = len(x)
    ix_index = len(ix)
    if x_index == ix_index:
        print(ix) 
    else:
        raise KeyError("Error")
    return none   


def favorite_color(x: dict[str, str]):
    """Chooses most repeated color."""
    count: dict[str, int] = {}
    for key in x:
        value = x[key]
        if value in count:
            count[value] += 1 
        else:
            count[value] = 1 
    h_count = list(count.values())
    top = max(h_count)
    for key in x:
        if count[x[key]] == top:
            return x[key]


def count(x: list[str]) -> dict[str, int]:
    """Turns list in to dict and vaule them base on times of appearnce."""
    dic: dict[str, int] = {}
    for num in x:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1 
    return(dic)
    

  





   

    
    
    
    
        