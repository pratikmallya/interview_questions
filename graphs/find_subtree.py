"""
Determine if one tree is subtree of another
Note that we are given a breadth-first representation. If we change it into
a depth-first representation, the question will be one of string matching.

"""
import sys
from operator import concat
from functools import reduce


def main():
    with open(sys.argv[1], 'r') as o:
        t1 = o.readline().strip()
        t2 = o.readline().strip()

        if len(t1) > len(t2):
            t1, t2 = t2, t1

        tree1 = build_tree(t1)
        tree2 = build_tree(t2)

    print(tree1)
    print(tree2)

    ans = is_subtree(tree1, tree2)
    sys.stdout.write("{}\n".format(ans))

def build_tree(line):
    """build a tree from the string description"""
    line = line.split(',')
    heads = [line.pop(0)]
    tree = {}
    node_index = [0]

    while line:

        head = heads.pop(0)

        if head != '':
            lchild, rchild, node_index, head_add = find_children(line, node_index)

            tree[node_index.pop(0)] = {'lchild': lchild,
                                'rchild': rchild,
                                 'value': int(head),
                                }
            heads += head_add
        else:
            heads += [line.pop(0), line.pop(0)]

    for head in heads:
        if head != '':
            tree[node_index.pop(0)] =  {'lchild': None,
                           'rchild': None,
                           'value': int(head),
                           }

    return tree

def find_children(line, node_index):
    head_add = []
    lchild = None
    rchild = None

    head = line.pop(0)
    if head:
        node_index.append(node_index[-1] + 1)
        lchild = node_index[-1]

    head_add.append(head)

    head = line.pop(0)
    if head:
        node_index.append(node_index[-1] + 1)
        rchild = node_index[-1]

    head_add.append(head)

    return lchild, rchild, node_index, head_add


def is_subtree(t1, t2):

    # find node in t2 with same value as root(t1)
    common_nodes = get_common_nodes(t1, t2)
    # for each such node, check if the trees are equivalent
    for node in common_nodes:
        if tree_diff(0, node, t1, t2):
            return True
    return False

def get_common_nodes(t1, t2):
    """find node in t2 with same value as root(t1)"""
    root_value = t1[0]['value']
    for node in t2.keys():
        if t2[node]['value'] == root_value:
            yield node


def tree_diff(node1, node2, t1, t2):

    # if both are None, return True
    if node1 == node2 == None:
        return True
    # if either one is None, return False
    if node1 == None or node2 == None:
        print("node1:{} node2:{}".format(node1, node2))
        return False

    if t1[node1]['value'] == t2[node2]['value']:
        return (tree_diff(t1[node1]['lchild'], t2[node2]['lchild'], t1, t2) and
                tree_diff(t1[node1]['rchild'], t2[node2]['rchild'], t1, t2)
                )


if __name__ == "__main__":
    main()
