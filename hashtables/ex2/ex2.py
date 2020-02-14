#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    # # add Tickets to hash table
    # for ticket in tickets:
    #     hash_table_insert(hashtable, ticket.source, ticket.destination)

    # route[0] = hash_table_retrieve(hashtable, "NONE")
    
    # for i in range(1, len(route)-1):

    #     route[i] = hash_table_retrieve(hashtable, route[i-1])
    # for ticket in tickets:
    #     hash_table_insert(hashtable, ticket.source, ticket.destination)

    # route[0] = hash_table_retrieve(hashtable, 'NONE')

    # current = 0
    # while current < length - 1:
    #     route[current + 1] = hash_table_retrieve(hashtable, route[current])
    #     current += 1
    # return route

        # loop through tickets
        #check for a source = NONE
            # if so then that is the start
            # if no NONE insert source and destination to ht
    # loop through the route, 
    # next route will start with the dest from the last one ( i-1)

    for t in tickets:
        if t.source == "NONE":
            route[0] = t.destination
        else:
            hash_table_insert(hashtable, t.source, t.destination)
    for i in range(1, len(tickets)):
        route[i] = hash_table_retrieve(hashtable, route[i-1])