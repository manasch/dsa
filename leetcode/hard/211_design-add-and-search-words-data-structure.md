[[211] - Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure)

---

- Medium
- [Submission](https://leetcode.com/problems/design-add-and-search-words-data-structure/submissions/991054296/)
- string, depth-first-search, design, trie

---

## Problem Statement

<p>Design a data structure that supports adding new words and finding if a string matches any previously added string.</p>

<p>Implement the <code>WordDictionary</code> class:</p>

<ul>
	<li><code>WordDictionary()</code>&nbsp;Initializes the object.</li>
	<li><code>void addWord(word)</code> Adds <code>word</code> to the data structure, it can be matched later.</li>
	<li><code>bool search(word)</code>&nbsp;Returns <code>true</code> if there is any string in the data structure that matches <code>word</code>&nbsp;or <code>false</code> otherwise. <code>word</code> may contain dots <code>&#39;.&#39;</code> where dots can be matched with any letter.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example:</strong></p>

<pre>
<strong>Input</strong>
[&quot;WordDictionary&quot;,&quot;addWord&quot;,&quot;addWord&quot;,&quot;addWord&quot;,&quot;search&quot;,&quot;search&quot;,&quot;search&quot;,&quot;search&quot;]
[[],[&quot;bad&quot;],[&quot;dad&quot;],[&quot;mad&quot;],[&quot;pad&quot;],[&quot;bad&quot;],[&quot;.ad&quot;],[&quot;b..&quot;]]
<strong>Output</strong>
[null,null,null,null,false,true,true,true]

<strong>Explanation</strong>
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord(&quot;bad&quot;);
wordDictionary.addWord(&quot;dad&quot;);
wordDictionary.addWord(&quot;mad&quot;);
wordDictionary.search(&quot;pad&quot;); // return False
wordDictionary.search(&quot;bad&quot;); // return True
wordDictionary.search(&quot;.ad&quot;); // return True
wordDictionary.search(&quot;b..&quot;); // return True
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 25</code></li>
	<li><code>word</code> in <code>addWord</code> consists of lowercase English letters.</li>
	<li><code>word</code> in <code>search</code> consist of <code>&#39;.&#39;</code> or lowercase English letters.</li>
	<li>There will be at most <code>2</code> dots in <code>word</code> for <code>search</code> queries.</li>
	<li>At most <code>10<sup>4</sup></code> calls will be made to <code>addWord</code> and <code>search</code>.</li>
</ul>


---

## Solution

```cpp
class Node {
public:
    vector<Node *> data;
    bool flag;

    Node() : data(26, nullptr), flag(false) {}
};

class WordDictionary {
private:
    Node *root = new Node();
    bool dfs(Node* root, string word, int j) {
        Node *curr = root;
        int index;
        char x;
        for (int i = j; i < word.size(); ++i) {
            x = word[i];
            if (x == '.') {
                for (int c = 0; c < 26; ++c) {
                    if (curr && dfs(curr->data[c], word, i + 1)) {
                        return true;
                    }
                }
                return false;
            }
            else {
                index = x - 'a';
                if (!curr) {
                    return false;
                }
                else {
                    curr = curr->data[index];
                    if (!curr) {
                        return false;
                    }
                }
            }
        }
        if (!curr) {
            return false;
        }
        return curr->flag;
    }
public:
    WordDictionary() {
        
    }
    
    void addWord(string word) {
        Node *curr = root;
        int index;
        for (char x: word) {
            index = x - 'a';
            if (curr->data[index] == nullptr) {
                curr->data[index] = new Node();
            }
            curr = curr->data[index];
        }
        curr->flag = true;
    }
    
    bool search(string word) {
        return dfs(root, word, 0);
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */
```

---

## Notes

- This is similar to the implementation of a trie, but the twist lies in traversing each of the possible characters when the character to be matched is a ".".
- This can be achieved both by BFS and DFS, this method involves using DFS.
