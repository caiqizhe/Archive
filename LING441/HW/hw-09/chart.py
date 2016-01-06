
from io import StringIO
from nltk import Production, Nonterminal, Tree


def cross_product (lists):
    if len(lists) == 1:
        for elt in lists[0]:
            yield [elt]
    else:
        for lst in cross_product(lists[:-1]):
            for elt in lists[-1]:
                yield lst + [elt]


class Edge (object):

    def __init__ (self, rule_or_edge, child):
        if isinstance(rule_or_edge, Production):
            self.prev = None
            self.rule = rule_or_edge
            self.children = [child]
        elif isinstance(rule_or_edge, Edge):
            self.prev = rule_or_edge
            self.rule = rule_or_edge.rule
            self.children = rule_or_edge.children + [child]
        else:
            raise Exception('Expected a rule or edge, got %s' % repr(child))

        rhs = self.rule.rhs()
        i = len(self.children) - 1
        if i >= len(rhs):
            raise Exception('Too many children provided, expected %d' % len(rhs))
        x = rhs[i]
        if isinstance(child, str):
            if not isinstance(x, str):
                raise Exception('Expected %s, got %s' % (repr(x), repr(child)))
        elif isinstance(child, Node):
            if child.cat != x:
                raise Exception('Expected %s, got %s' % (repr(x), repr(child.cat)))

        self.i = self.children[0].i
        self.j = self.children[-1].j

    def __repr__ (self):
        rhs = [repr(x) for x in self.rule.rhs()]
        n = len(self.children)
        return 'Edge(%d %s -> %s *%d %s)' % (
            self.i,
            self.rule.lhs(),
            ' '.join(rhs[:n]),
            self.j,
            ' '.join(rhs[n:]))

    def dot_at_end (self):
        return len(self.children) == len(self.rule.rhs())

    def after_dot (self):
        rhs = self.rule.rhs()
        n = len(self.children)
        if n < len(rhs): return rhs[n]

    def unwind (self, cat):
        treesets = []
        for child in self.children:
            if isinstance(child, Node):
                trees = child.unwind()
            elif isinstance(child, str):
                trees = [child]
            else:
                raise Exception('Bad item in edge children: %s' % repr(child))
            treesets.append(trees)
        for childset in cross_product(treesets):
            yield Tree(cat, childset)


class Node (object):

    def __init__ (self, i, cat, j, expansion=None):
        if not isinstance(cat, Nonterminal):
            raise Exception('Expected a nonterminal cat, got %s' % repr(cat))
        if not (isinstance(i, int) and isinstance(j, int)):
            raise Exception('Expected ints for i and j, got %s, %s' % (repr(i), repr(j)))

        self.cat = cat
        self.i = i
        self.j = j
        self.expansions = [] # edges, or one string
        self.add_expansion(expansion)

    def __repr__ (self):
        return 'Node(%d %s %d)' % (self.i, self.cat, self.j)

    def add_expansion (self, edge):
        if edge is None: return
        if isinstance(edge, str):
            if self.expansions:
                raise Exception('If expansion is a string, there may only be one expansion')
        elif isinstance(edge, Edge):
            if len(self.expansions) == 1 and isinstance(self.expansions[0], str):
                raise Exception('If expansion is a string, there may only be one expansion')
            if not edge.dot_at_end():
                raise Exception('Dot is not at end')
            if edge.i != self.i or edge.j != self.j:
                raise Exception('Expansion span (%d,%d) does not match node span (%d,%d)' % (edge.i, edge.j, self.i, self.j))
        else:
            raise Exception('Expected an edge, got %s' % repr(edge))
        self.expansions.append(edge)

    def unwind (self):
        if not self.expansions:
            raise Exception('No expansions: %s' % repr(self))
        if len(self.expansions) == 1 and isinstance(self.expansions[0], str):
            yield Tree(self.cat, [self.expansions[0]])
        else:
            for edge in self.expansions:
                for tree in edge.unwind(self.cat):
                    yield tree


class Chart (object):

    def __init__ (self):
        self.nodes = NodeTable()
        self.edges = EdgeTable()
        self.trace = False

    def reset (self):
        self.nodes.clear()
        self.edges.clear()

    def create_node (self, i, X, j, exp):
        node = self.nodes.add(i, X, j, exp)
        if self.trace:
            if node:
                print('Chart: created', node, 'with expansion', repr(node.expansions[0]))
            else:
                print('Chart: added expansion', exp, 'to', self.get_node(i, X, j))
        return node

    def create_edge (self, edge_or_rule, child):
        edge = self.edges.add(edge_or_rule, child)
        if self.trace:
            print('Chart: created', edge)
        return edge

    def get_node (self, i, X, j):
        return self.nodes[i, X, j]

    def get_edges_at (self, j):
        return self.edges[j]

    def __str__ (self):
        out = StringIO()
        print('Chart:', end='', file=out)
        for node in self.nodes:
            print('\n    Node', node, end='', file=out)
        for edge in self.edges:
            print('\n    Edge', edge, end='', file=out)
        s = out.getvalue()
        out.close()
        return s


class NodeTable (dict):

    def __getitem__ (self, key):
        if not (isinstance(key, tuple) and len(key) == 3):
            raise Exception('Must access nodes by i X j')
        if key in self:
            return dict.__getitem__(self, key)

    def add (self, i, X, j, expansion):
        key = (i, X, j)
        if key in self:
            node = dict.__getitem__(self, key)
            node.add_expansion(expansion)
        else:
            node = Node(i, X, j, expansion)
            dict.__setitem__(self, key, node)
            return node


class EdgeTable (object):

    def __init__ (self):
        self.lists = []

    def __iter__ (self):
        for lst in self.lists:
            for edge in lst:
                yield edge

    def __getitem__ (self, j):
        if j >= len(self.lists):
            return iter([])
        else:
            return iter(self.lists[j])

    def add (self, edge_or_rule, child):
        edge = Edge(edge_or_rule, child)
        j = edge.j
        while j >= len(self.lists):
            self.lists.append([])
        self.lists[j].append(edge)
        return edge

    def clear (self):
        self.lists.clear()
