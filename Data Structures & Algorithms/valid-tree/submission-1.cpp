class DSU {
    vector<int>parent, size;
    public:
        DSU(int n) {
            parent.resize(n);
            size.resize(n);
            for(int i=0;i<n;i++) {
                parent[i] = i;
                size[i] = 1;
            }
        }

        int find(int x) {
            if(parent[x] == x) return x;
            return parent[x] = find(parent[x]);
        }

        bool Union(int u, int v) {
            int pU = find(u);
            int pV = find(v);
            if(pU == pV) return false;
            if(size[pU] > size[pV]) {
                size[pU]+=size[pV];
                parent[pV] = pU;
            } else {
                size[pV]+=size[pU];
                parent[pU] = pV;
            }
            return true;
        }
};

class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        DSU uf(n);
        for(auto &e : edges) {
            if(!uf.Union(e[0], e[1])) {
                return false;
            }
        }
        if(abs(n-edges.size()!=1)) return false;
        return true;
    }
};
