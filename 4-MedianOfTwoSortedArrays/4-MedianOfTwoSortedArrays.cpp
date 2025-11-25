// Last updated: 11/25/2025, 5:01:57 PM
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
    vector<int> merged;
    int i = 0, j = 0;

    // Merge elements in sorted order
    while (i < nums1.size() && j < nums2.size()) {
        if (nums1[i] < nums2[j]) {
            merged.push_back(nums1[i]);
            i++;
        } else {
            merged.push_back(nums2[j]);
            j++;
        }
    }

    // Append remaining elements from nums1
    while (i < nums1.size()) {
        merged.push_back(nums1[i]);
        i++;
    }

    // Append remaining elements from nums2
    while (j < nums2.size()) {
        merged.push_back(nums2[j]);
        j++;
    }
    
        if (merged.size()%2==0){
            return (merged[(merged.size()/2)-1]+merged[(merged.size()/2)])/2.0;
        }
        else {
        return merged[(merged.size()/2.0)];
        }
    
    }
};