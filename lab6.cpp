
// WAP to create a pile and apply ky merging
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

// Structure to store heap node
struct Node {
    int value, arrayIndex, elementIndex;

    Node(int v, int ai, int ei) : value(v), arrayIndex(ai), elementIndex(ei) {}

    // Min-heap comparator
    bool operator>(const Node &other) const {
        return value > other.value;
    }
};

// Function to merge k sorted arrays using a min-heap (priority queue)
vector<int> mergeKSortedArrays(vector<vector<int>> &arrays) {
    priority_queue<Node, vector<Node>, greater<Node>> minHeap;
    int totalSize = 0;

    // Push the first element of each array into the heap
    for (int i = 0; i < arrays.size(); i++) {
        if (!arrays[i].empty()) {
            minHeap.push(Node(arrays[i][0], i, 0));
            totalSize += arrays[i].size();
        }
    }

    vector<int> result;
    result.reserve(totalSize);

    // Process the heap
    while (!minHeap.empty()) {
        Node current = minHeap.top();
        minHeap.pop();

        result.push_back(current.value);

        int nextIndex = current.elementIndex + 1;
        if (nextIndex < arrays[current.arrayIndex].size()) {
            minHeap.push(Node(arrays[current.arrayIndex][nextIndex], current.arrayIndex, nextIndex));
        }
    }

    return result;
}

int main() {
    vector<vector<int>> arrays = {
        {1, 4, 7},
        {2, 5, 8},
        {3, 6, 9}
    };

    vector<int> mergedArray = mergeKSortedArrays(arrays);

    cout << "Merged Sorted Array:\n";
    for (int num : mergedArray) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
