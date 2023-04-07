expected = ('john doe', '1111', 'something', True)
actual = (
    response["user"],
    response["objects"][0]["id"],
    response["objects"][0]["event"][0]["type"],
    response["reached"]
)
assert expected == actual
# Запускать pytest с ключом -v, тогда он явно покажет какие элементы в кортежах не равны.