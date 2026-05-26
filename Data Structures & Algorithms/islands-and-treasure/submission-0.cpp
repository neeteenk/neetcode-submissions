class Solution {
public:
    int maxi = 2147483647;
    void islandsAndTreasure(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        queue<pair<pair<int, int>, int>>q; //{node, distance} //treasureChest distance = 0
        
        for(int i=0;i<m;i++) {
            for(int j=0;j<n;j++) {
                if(grid[i][j] == 0) {
                    q.push({{i, j}, 0});
                }
            }
        }
        int dx[4] = {0, 0, 1, -1};
        int dy[4] = {-1, 1, 0, 0};

        while(!q.empty()) {
            auto ele = q.front();
            q.pop();
            int x = ele.first.first;
            int y = ele.first.second;
            int currDist = ele.second;
            for(int i=0;i<4;i++) {
                int newX = x + dx[i];
                int newY = y + dy[i];
                if(newX >=0 && newX<m && newY>=0 && newY < n && grid[newX][newY] == maxi) {
                    grid[newX][newY] = currDist+1;
                    q.push({{newX, newY}, currDist+1});
                }
            }
        }
    }
};
