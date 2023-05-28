import hashlib

class Block:
    def __init__(self, block_id, data, previous_hash, difficulty):
        self.block_id = block_id
        self.data = data
        self.previous_hash = "0"*64 if not previous_hash else previous_hash
        self.difficulty = difficulty
        self.nonce, self.hash_value = self.calculate_nonce_and_hash_value()
    def calculate_nonce_and_hash_value(self):
        nonce = 0
        while True:
            current_hash = hashlib.sha256(f'{self.block_id}{self.data}{self.previous_hash}{nonce}'.encode('utf-8')).hexdigest()
            if current_hash.startswith("0"*self.difficulty):
                return nonce, current_hash
            else:
                nonce += 1

def print_block_chain(current_node, block_chain):
    while True:
        if not current_node:
            break
        print(f'\n\tBlock :')
        print(f'\t\tId: {current_node.block_id}')
        print(f'\t\tData: {current_node.data}')
        print(f'\t\tPrevious Hash Value: {current_node.previous_hash}')
        print(f'\t\tHash Value: {current_node.hash_value}')
        print(f'\t\tNonce: {current_node.nonce}')
        nodes_with_that_hash = list(filter(lambda x: x.hash_value == current_node.previous_hash, block_chain))
        if len(nodes_with_that_hash) == 0:
            current_node = None
        else:
            current_node = nodes_with_that_hash[0]
    return


current_node = None
block_chain = []
difficulty = int(input('\nEnter the Difficulty: '))
print('\n================================================')
while True:
    data = input('\nEnter the Data: ')
    block_id = int(input('Enter Block Id: '))
    new_node = Block(block_id, data, None if not current_node else current_node.hash_value, difficulty)
    current_node = new_node
    block_chain.append(current_node)
    print('\nBlockChain: [', end='\n')
    print_block_chain(current_node, block_chain)
    print(']')
    is_continue = int(input('\n\nDo you want to continue? (1(Y)/0(N)) '))
    print('\n------------------------------------------------')
    if not is_continue:
        print('\nProgram Ended!!!')
        break