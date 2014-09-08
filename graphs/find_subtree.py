"""
Determine if one tree is subtree of another
Note that we are given a breadth-first representation. If we change it into
a depth-first representation, the question will be one of string matching.

"""
import sys
from collections import deque


def main():
    with open(sys.argv[1], 'r') as o:
        t1 = o.readline().strip()
        t2 = o.readline().strip()

        if len(t1) > len(t2):
            t1, t2 = t2, t1

        tree1 = build_tree(t1)
        tree2 = build_tree(t2)

    ans = is_subtree(tree1, tree2)
    sys.stdout.write("{}\n".format(ans))


def build_tree(line):
    """build a tree from the string description"""
    line = deque(line.split(','))
    heads = deque([line.popleft()])
    tree = {}
    node_index = deque([0])

    while line:

        head = heads.popleft()

        if head != '':
            lchild, rchild, node_index, head_add = find_children(line,
                                                                 node_index)

            tree[node_index.popleft()] = {'lchild': lchild,
                                          'rchild': rchild,
                                          'value': int(head),
                                          }
            heads += head_add
        else:
            heads += deque([line.popleft(), line.popleft()])

    for head in heads:
        if head != '':
            tree[node_index.popleft()] = {'lchild': None,
                                          'rchild': None,
                                          'value': int(head),
                                          }

    return tree


def find_children(line, node_index):
    """find the children to the present node and assign proper indices"""
    head_add = deque([])
    lchild = None
    rchild = None

    head = line.popleft()
    if head:
        node_index.append(node_index[-1] + 1)
        lchild = node_index[-1]

    head_add.append(head)

    head = line.popleft()
    if head:
        node_index.append(node_index[-1] + 1)
        rchild = node_index[-1]

    head_add.append(head)

    return lchild, rchild, node_index, head_add


def is_subtree(t1, t2):
    """find if t1 is a subtree of t2"""
    # find node in t2 with same value as root(t1)
    common_nodes = get_common_nodes(t1, t2)
    # for each such node, check if the trees are equivalent
    for node in common_nodes:
        if tree_diff(0, node, t1, t2):
            return True
    return False


def get_common_nodes(t1, t2):
    """find nodes in t2 with same value as root(t1)"""

    root_value = t1[0]['value']
    for node in t2.keys():
        if t2[node]['value'] == root_value:
            yield node


def tree_diff(node1, node2, t1, t2):
    """find if t1 is a subtree of t2 with the help of root nodes
    node1 and node2"""

    if node1 == node2 is None:  # leaf node
        return True
    elif node1 is None:  # reached end of t1
        return True
    elif node2 is None:  # reached end of t2
        return False

    if t1[node1]['value'] == t2[node2]['value']:
        return (tree_diff(t1[node1]['lchild'], t2[node2]['lchild'], t1, t2) and
                tree_diff(t1[node1]['rchild'], t2[node2]['rchild'], t1, t2)
                )
    else:
        return False


if __name__ == "__main__":
    main()
