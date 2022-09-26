class Solution:
    def equationsPossible(self, equations):
        # lee's ans
        def find(x):
            if x not in self.uf:
                self.uf[x] = x
                return x
            if x != self.uf[x]: self.uf[x] = find(self.uf[x])
            return self.uf[x]
        self.uf = {}
        for a, e, _, b in equations:
            if e == "=":
                self.uf[find(a)] = find(b)
        return not any(e == "!" and find(a) == find(b) for a, e, _, b in equations)