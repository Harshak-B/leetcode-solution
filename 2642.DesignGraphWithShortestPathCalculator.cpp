#include <vector>
#include <queue>
#include <limits>

using namespace std;

class Graph {
public:
    Graph(int n, vector<vector<int>>& edges) {
        graph.resize(n);
        for (const vector<int>& edge : edges)
            addEdge(edge);
    }
    
    void addEdge(vector<int> edge) {
        const int u = edge[0];
        const int v = edge[1];
        const int w = edge[2];
        graph[u].emplace_back(v, w);
    }
    
    int shortestPath(int node1, int node2) {
        // Initialize distances to infinity
        vector<int> dist(graph.size(), numeric_limits<int>::max());
        
        // Min heap to store {distance, node} pairs
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap;
        
        // Start from node1 with distance 0
        minHeap.emplace(0, node1);
        dist[node1] = 0;

        while (!minHeap.empty()) {
            const auto [d, u] = minHeap.top();
            minHeap.pop();

            if (u == node2)
                return d;

            for (const auto& [v, w] : graph[u]) {
                if (dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                    minHeap.emplace(dist[v], v);
                }
            }
        }
        
        // If node2 is not reachable from node1
        return -1;
    }

private:
    vector<vector<pair<int, int>>> graph;
};
