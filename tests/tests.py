

def make_dict(chave, valor):
    return {chave: valor}

def test_make_dict():
    assert make_dict('chave', 'valor') == {'chave': 'valor'}

def turn_list_into_str(list_items: list):
    """"""
    return "".join(list_items)

def test_turn_list_into_str():
    assert turn_list_into_str(['123']) == '123'
