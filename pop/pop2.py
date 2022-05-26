#Remove "broccoli" from the list using .pop and .index methods.

lst=["milk", "banana", "eggs", "bread", "broccoli", "lemons"]

indexed_item = lst.index("broccoli")

item = lst.pop(indexed_item)

print(lst, item)