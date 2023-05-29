#  A linked list of length n is given such that each node contains an additional random pointer,
# which could point to any node in the list, or null.
#  Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes,
# where each new node has its value set to the value of its corresponding original node.
#  Both the next and random pointer of the new nodes should point to new nodes in the copied list
# such that the pointers in the original list and copied list represent the same list state.
#  None of the pointers in the new list should point to nodes in the original list.
# ------------------
# For example, if there are two nodes X and Y in the original list, where X.random --> Y,
# then for the corresponding two nodes x and y in the copied list, x.random --> y.
# ------------------
# Return the head of the copied linked list.
#   The linked list is represented in the input/output as a list of n nodes.
#   Each node is represented as a pair of [val, random_index] where:
#      - val: an integer representing Node.val
#      - random_index: the index of the node (range from 0 to n-1) that the random pointer points to,
#        or null if it does not point to any node.
# Your code will only be given the head of the original linked list.
# ------------------
# 0 <= n <= 1000  ,  -104 <= Node.val <= 104
# Node.random is null or is pointing to some node in the linked list.


class Node:
    def __init__(self, x=0, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __str__(self):
        return f"{self.val} -> {self.next}"


def create_linked(to_link: list[list[int, int]]) -> Node:
    tempo = link = Node()
    all_nodes: list[Node] = []
    for index in range(len(to_link)):
        tempo.val = to_link[index][0]
        all_nodes.append(tempo)
        if index != (len(to_link) - 1):
            tempo.next = Node()
            tempo = tempo.next
    tempo = link
    for x in range(len(to_link)):
        random_index: int = to_link[x][1]
        if random_index is None:
            tempo = tempo.next
            continue
        tempo.random = all_nodes[random_index]
        tempo = tempo.next
    return link


def show_all_nodes(linked: Node) -> None:
    print("\nAll nodes:", linked)
    node_num: int = 0
    one_node: Node = linked
    while one_node:
        print("Node index:", node_num)
        print("Node.val:", one_node.val)
        print("Node.random:", one_node.random)
        print("----")
        one_node = one_node.next
        if one_node:
            node_num += 1


def copy_random_list(head: Node) -> Node:
    pass

# Well while making all this basics to see what's going on in this task. I'm already made part of what we needed.
# Hardest part is to get indexes of random_nodes, because we're just given these nodes.
# Their not unique and have no indexes, so only way I see to get where we need to place them,
# is to change every value in given list to 0...n, than read this list again, and get first .val of random_link.
# But it's changing original input_list, so we're going to traverse TWICE just to get random indexes,
# is there a better way?
# First task with this type of linked_lists, and I won't google until I hit time_limit, so let's try to
# make something like O(4) -> 1 to get indexes,
#                          -> 2 to return original values,
#                          -> 3 build new with values,
#                          -> 4 put random_links
# I could leave original changed, but it's not correct, and maybe it's allowed because there's no condition for that.
# But we're dealing DEEPCOPY, so we're obliged to return COPY and leave original as it is.
# I don't even know if we're allowed to change original in first place, but how else can we get random_indexes to put?
# Extra time to traverse, but it's 99% more correct to return the original state.
# ------------------
# Ok. Rebuild creating of linked list from before, and dunder for __str__.
# But can't make it show random, because it's trying to loop for itself and ending in a max_recursion.
# Tho it's working correct, and checking with just print, is bad. But first time I encounter something more,
# than single_linked list, so it's fine for now.


test1 = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
test1_out = [{7, None}, [13, 0], [11, 4], [10, 2], [1, 0]]
test = create_linked(test1)
show_all_nodes(test)
del test

test2 = [[1, 1], [2, 1]]
test2_out = [[1, 1], [2, 1]]
test = create_linked(test2)
show_all_nodes(test)
del test

test3 = [[3, None], [3, 0], [3, None]]
test3_out = [[3, None], [3, 0], [3, None]]
test = create_linked(test3)
show_all_nodes(test)
del test
