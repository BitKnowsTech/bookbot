def get_word_count(text: str) -> int:
    return len(text.split())

def get_symbol_count(text: str) -> dict[str, int]:
    ret = {}
    for i in text.lower():
        if i not in ret:
            ret[i] = 0
        ret[i] += 1
    
    return ret

def get_sorted_dict(dictionary: dict[str, int]) -> list[dict[str, str|int]]:
    sorted_list = sorted(list(map(lambda x: {"char": x[0], "count": x[1]}, dictionary.items())), key=lambda x: x["count"], reverse=True)
    return sorted_list