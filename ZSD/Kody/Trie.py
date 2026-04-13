
class Node:
    def __init__(self):
        self.children = [None] * 26
        self.isLeaf = False

class Trie:
    def __init__(self):
        self.root = Node()

    def _char_to_index(self, c):
        return ord(c) - ord('a')

    def insert(self, key):
        curr = self.root
        for c in key:
            index = self._char_to_index(c)
            if curr.children[index] is None:
                curr.children[index] = Node()
            curr = curr.children[index]
        curr.isLeaf = True

    def _traverse(self, string):
        curr = self.root
        for c in string:
            index = self._char_to_index(c)
            if curr.children[index] is None:
                return None
            curr = curr.children[index]
        return curr

    def search(self, key):
        node = self._traverse(key)
        return node is not None and node.isLeaf

    def isPrefix(self, prefix):
        return self._traverse(prefix) is not None

    def startsWith(self, prefix):
        return self.isPrefix(prefix)

    def words_with_prefix(self, prefix):
        result = []
        node = self._traverse(prefix)
        if not node:
            return result
        self._dfs(node, prefix, result)
        return result

    def _dfs(self, node, path, result):
        if node.isLeaf:
            result.append(path)

        for i in range(26):
            if node.children[i] is not None:
                ch = chr(i + ord('a'))
                self._dfs(node.children[i], path + ch, result)


trie = Trie()

words = ["and", "ant", "do", "dad"]
for w in words:
    trie.insert(w)

print(trie.search("do"))                # True
print(trie.search("hi"))                # False

print(trie.startsWith("an"))            # True
print(trie.startsWith("he"))            # False

print(trie.words_with_prefix("a"))      # ['and', 'ant']
print(trie.words_with_prefix("d"))      # ['dad', 'do']

trie.insert("hi")
trie.insert("hello")
print(trie.search("hi"))                # True
print(trie.startsWith("h"))             # True