#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print(vector<T>& nums) {
    for (const T& val: nums) {
        cout << val <<  " ";
    }
    cout << endl;
}

template <typename T>
class Sort {
private:
    vector<T> nums;
    T temp;
public:
    Sort(vector<T>& nums) : nums(nums) {};
    void selectionSort() {
        for (auto i = nums.begin(); i != nums.end(); ++i) {
            typename vector<T>::iterator min_ptr = i;
            for (auto j = i; j != nums.end(); ++j) {
                if (*j < *min_ptr) {
                    min_ptr = j;
                }
            }
            if (min_ptr != i) {
                swap(*i, *min_ptr);
            }
        }
    }

    void bubbleSort() {
        for (int i = 1; i < nums.size(); ++i) {
            for (int j = 1; j < nums.size() - i; ++j) {
                if (nums[j - 1] > nums[j]) {
                    swap(nums[j], nums[j - 1]);
                }
            }
        }
    }

    void insertionSort() {
        int v, j;
        for (int i = 1; i < nums.size(); ++i) {
            v = nums[i];
            j = i - 1;
            while (j >= 0 && nums[j] > v) {
                nums[j + 1] = nums[j];
                --j;
            }
            nums[j + 1] = v;
        }
    }

    vector<T> getSortedArray() {
        return nums;
    }
};

int main() {
    vector<int> nums = {3, 5, 1, 4, 6, 2, 7};
    vector<int> sorted;
    {
        cout << endl << "Selection Sort" << endl;
        cout << "Before sorting" << endl;
        print(nums);
        Sort<int> sorter(nums);
        sorter.selectionSort();
        cout << "After sorting" << endl;
        sorted = sorter.getSortedArray();
        print(sorted);
    }
    {
        cout << endl << "Bubble Sort" << endl;
        cout << "Before sorting" << endl;
        print(nums);
        Sort<int> sorter(nums);
        sorter.bubbleSort();
        cout << "After sorting" << endl;
        sorted = sorter.getSortedArray();
        print(sorted);
    }
    {
        cout << endl << "Insertion Sort" << endl;
        cout << "Before sorting" << endl;
        print(nums);
        Sort<int> sorter(nums);
        sorter.insertionSort();
        cout << "After sorting" << endl;
        sorted = sorter.getSortedArray();
        print(sorted);
    }
    return 0;
}
