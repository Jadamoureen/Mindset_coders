#Below is a nested data.
# Find out the length of the item: 'raincoat'.
# You can use reverse indexing.

gift_list=['4K drone', 'wine', 'jam', ['socks', 'pajamas', 'raincoat']]

ans_1 = len(gift_list[-1][-1])

print(ans_1)
