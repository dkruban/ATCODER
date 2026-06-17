#include <bits/stdc++.h>
using namespace std;

// Structure to track contiguous blocks of the same item type
struct Block {
    int value;
    int start;
    int end;
};

void solve() {
    int n;
    if (!(cin >> n)) return;
    
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    // 1. Identify all contiguous blocks and count occurrences per type
    vector<Block> blocks;
    map<int, int> type_block_count;

    for (int i = 0; i < n; ) {
        int j = i;
        while (j < n && a[j] == a[i]) {
            j++;
        }
        blocks.push_back({a[i], i, j - 1});
        type_block_count[a[i]]++;
        i = j;
    }

    int unique_types = type_block_count.size();

    // If the number of blocks equals unique types, it's already perfectly arranged
    if ((int)blocks.size() == unique_types) {
        cout << "YES\n";
        return;
    }

    // 2. Collect candidate indices for swapping
    // We only need to check indices near the boundaries of scattered blocks
    set<int> candidate_set;
    int scattered_blocks_count = 0;

    for (const auto& b : blocks) {
        if (type_block_count[b.value] > 1) {
            scattered_blocks_count++;
            
            // Insert indices at the front and back of this broken block
            candidate_set.insert(b.start);
            if (b.start + 1 <= b.end) candidate_set.insert(b.start + 1);
            if (b.end - 1 >= b.start) candidate_set.insert(b.end - 1);
            candidate_set.insert(b.end);
        }
    }

    // A single swap can alter at most a few blocks. 
    // If there are too many scattered blocks, it's impossible to fix in 1 swap.
    if (scattered_blocks_count > 10) {
        cout << "NO\n";
        return;
    }

    vector<int> candidates(candidate_set.begin(), candidate_set.end());

    // Lambda function to check if the modified array is valid in O(N)
    auto check_valid = [&]() {
        int cnt = 0;
        for (int i = 0; i < n; ) {
            int j = i;
            while (j < n && a[j] == a[i]) {
                j++;
            }
            cnt++;
            i = j;
        }
        return cnt == unique_types;
    };

    // 3. Test all pairs of candidate indices
    for (size_t i = 0; i < candidates.size(); i++) {
        for (size_t j = i + 1; j < candidates.size(); j++) {
            swap(a[candidates[i]], a[candidates[j]]);
            
            if (check_valid()) {
                cout << "YES\n";
                return;
            }
            
            swap(a[candidates[i]], a[candidates[j]]); // Undo swap
        }
    }

    cout << "NO\n";
}

int main() {
    // Optimize standard I/O operations for competitive programming
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;
    if (cin >> t) {
        while (t--) {
            solve();
        }
    }
    return 0;
}
