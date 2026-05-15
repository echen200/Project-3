# **Project 3: Huffman Encoding (Functional Design)**

## **Overview**

In this project, you'll implement Huffman Encoding—a classic algorithm for data compression. You'll walk through each core component of the process: counting character frequencies, constructing a priority queue, building a Huffman tree, generating binary codes, and decoding.

This version differs slightly from previous labs:

> ✅ **You are responsible for all core functions.**
> ⚠️ **You must return new objects or values from each function**—**do not use mutation** (no in-place updates of lists or objects).

You may find this Huffman encoder helpful for testing or intuition:
👉 [https://asecuritysite.com/calculators/huff](https://asecuritysite.com/calculators/huff)

## **Provided to You**

We provide:
### 1. **Data Structures** (DO NOT MODIFY):

```python
from __future__ import annotations
from dataclasses import dataclass, field

@dataclass(order=True, frozen=True)
class Node:
    freq: int
    char: str
    left: Node | None = None
    right: Node | None = None

    def __str__(self):
        return f"Node: {self.char}, Freq: {self.freq}"

@dataclass(frozen=True)
class MinHeap:
    data: list[Node] = field(default_factory=list)
```

These structures form the basis for your tree and heap logic. They are frozen (immutable), so you'll need to return new versions when changing the heap or creating new trees.

### 2. **Starter Code with Empty Function Definitions**

Each function is defined but unimplemented — you must complete all of them.

### 3. **Test Harness**

* `test_p3.py`: The autograder. You must pass all tests.
* `test_student.py`: Your sandbox. Write your own tests here. Again don't help your grade but absense will be penalized. 

---

## **Implementation Contract (You MUST Implement These)**

You are responsible for implementing **all** of the following functions in a **functional** style (no in-place modification of objects or lists).

### 🔧 Heap Functions

These manage a functional `MinHeap` and should always return new `MinHeap` objects.

| Function                                             | Description                                                                       |
| ---------------------------------------------------- | --------------------------------------------------------------------------------- |
| `heapify_up(heap: MinHeap, index: int) -> MinHeap`   | Bubble up the element at `index` to restore heap property. Return new `MinHeap`.  |
| `heapify_down(heap: MinHeap, index: int) -> MinHeap` | Push down the element at `index` to its correct place. Return new `MinHeap`.      |
| `insert(heap: MinHeap, element: Node) -> MinHeap`    | Insert a `Node` and restore heap property via `heapify_up`. Return new `MinHeap`. |
| `extract_min(heap: MinHeap) -> tuple[MinHeap, Node]` | Remove and return the smallest node along with the new heap.                      |

---

### 🔄 Huffman Workflow Functions

| Function Signature                                                                        | Description                                                                                                                    |
| ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `count_frequency(s: str) -> dict[str, int]`                                               | Count how many times each character appears in the input string `s`. Return a frequency dictionary.                            |
| `create_priority_queue(frequency: dict[str, int]) -> MinHeap`                             | Build a `MinHeap` from the frequency dictionary. Each character-frequency pair becomes a `Node`.                               |
| `build_tree_from_queue(priority_queue: MinHeap) -> Node`                                  | Repeatedly combine the two lowest-frequency nodes from the heap into a new node, reinserting until a single root node remains. |
| `generate_codes(node: Node \| None, prefix: str = "", code: dict \| None = None) -> dict` | Recursively traverse the Huffman tree to assign binary codes to each character. Left edges add `"0"`, right edges add `"1"`.   |
| `encode(s: str, codes: dict) -> str`                                                      | Replace each character in the string `s` with its corresponding Huffman code. Return the encoded binary string.                |
| `decode(encoded_string: str, root: Node) -> str`                                          | Use the Huffman tree to decode the binary string. Traverse from the root based on each bit, resetting at each leaf.            |



### ✅ `huffman_encoding(s: str)` — DO NOT MODIFY

This function ties it all together and will be used by our tests. You don’t need to call it manually — your job is to ensure everything it uses works.

---

## 📋 Sample Workflow

To encode `"hello"`:

1. `count_frequency("hello")` → `{'h': 1, 'e': 1, 'l': 2, 'o': 1}`
2. `create_priority_queue(...)` → `MinHeap([...])`
3. `build_tree_from_queue(...)` → Root of Huffman tree.
4. `generate_codes(root)` → `{'h': '00', 'e': '01', 'l': '1', 'o': '10'}`
5. `encode("hello", codes)` → `"000111110"`
6. `decode("000111110", root)` → `"hello"`

---

## 🔍 Functional Design Constraints

This project enforces **pure functional programming** rules:

| ❌ Mutation                                 | ✅ Functional Alternative                               |
| ------------------------------------------ | ------------------------------------------------------ |
| Modifying lists in-place                   | Use slicing, list comprehensions, or return a new list |
| Changing objects                           | Return new `MinHeap`, `Node`, or other data            |
| Using `.append()`, `.pop()` on shared data | Avoid — create new versions instead                    |

For example, `insert(heap, node)` **must return** a new heap — do **not** call `.append()` on the original list.

---

## ✅ Testing Requirements

* All tests in `test_p3.py` must pass.
* You must add your own tests to `test_student.py`:

  * Test `heapify_up`, `insert`, and `extract_min` independently.
  * Test trees and encoding/decoding with edge cases (e.g., empty strings, single characters, repeated characters).
  * Use assertions to check both return values and structural properties (e.g., length of heap, code lengths, tree shape).

---

## 🧪 Examples and Debugging Tools

* Use [https://asecuritysite.com/calculators/huff](https://asecuritysite.com/calculators/huff) to check your outputs.
* Try small strings like `"aaabbc"` or `"hello"` for quick tests.
