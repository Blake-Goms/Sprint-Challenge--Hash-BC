#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    # weight is the weights at i
    # weight_limit is the limit - weight
    # retrieve the weight_limit and set it as index_pair
    # if index_pair is not None and higher than i it will be index_pair first, 
    # else it will be i first
        # return the group once we know what order it should go in
    # insert everything into the hash table
    for i in range(length):
        weight = weights[i]
        weight_limit = limit - weight
        index_pair = hash_table_retrieve(ht, weight_limit)
        if index_pair is not None:
            group = (index_pair, i) if i < index_pair else(i, index_pair)
            return group
        hash_table_insert(ht, weight, i)

    return None

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
