# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    digits = 10**7
    contacts = [None] * digits
    for cur_query in queries:
        index = cur_query.number
        if cur_query.type == 'add':
            if contacts[index] == None:
                contacts[index] = cur_query
            else:
                contacts[index].name = cur_query.name
        elif cur_query.type == 'del':
            contacts[index] = None
        else:
            if contacts[index] == None:
                result.append('not found')
            else:
                result.append(contacts[index].name)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
