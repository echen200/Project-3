import unittest

from proj3 import (
    Node,
    MinHeap,
    heapify_up,
    heapify_down,
    insert,
    extract_min,
    count_frequency,
    create_priority_queue,
    build_tree_from_queue,
    generate_codes,
    encode,
    decode,
    huffman_encoding,
)


def is_min_heap(heap):
    data = heap.data

    for i in range(len(data)):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(data) and data[i] > data[left]:
            return False

        if right < len(data) and data[i] > data[right]:
            return False

    return True


class TestStudentHuffman(unittest.TestCase):

    def test_heapify_up(self):
        heap = MinHeap([
            Node(2, "b"),
            Node(3, "c"),
            Node(1, "a"),
        ])

        new_heap = heapify_up(heap, 2)

        self.assertEqual(new_heap.data[0], Node(1, "a"))
        self.assertTrue(is_min_heap(new_heap))

        # Original heap should not be changed
        self.assertEqual(heap.data[0], Node(2, "b"))

    def test_insert(self):
        heap = MinHeap([])
        heap = insert(heap, Node(5, "e"))
        heap = insert(heap, Node(2, "b"))
        heap = insert(heap, Node(8, "h"))
        heap = insert(heap, Node(1, "a"))

        self.assertEqual(len(heap.data), 4)
        self.assertEqual(heap.data[0], Node(1, "a"))
        self.assertTrue(is_min_heap(heap))

    def test_extract_min(self):
        heap = MinHeap([])
        heap = insert(heap, Node(5, "e"))
        heap = insert(heap, Node(2, "b"))
        heap = insert(heap, Node(8, "h"))
        heap = insert(heap, Node(1, "a"))

        new_heap, minimum = extract_min(heap)

        self.assertEqual(minimum, Node(1, "a"))
        self.assertEqual(len(new_heap.data), 3)
        self.assertTrue(is_min_heap(new_heap))

        # Original heap should still have 4 items
        self.assertEqual(len(heap.data), 4)

    def test_heapify_down(self):
        heap = MinHeap([
            Node(10, "z"),
            Node(2, "b"),
            Node(3, "c"),
            Node(4, "d"),
        ])

        new_heap = heapify_down(heap, 0)

        self.assertEqual(new_heap.data[0], Node(2, "b"))
        self.assertTrue(is_min_heap(new_heap))

    def test_count_frequency(self):
        self.assertEqual(
            count_frequency("aaabbc"),
            {"a": 3, "b": 2, "c": 1}
        )

    def test_create_priority_queue(self):
        frequency = {"a": 3, "b": 2, "c": 1}
        heap = create_priority_queue(frequency)

        self.assertEqual(len(heap.data), 3)
        self.assertEqual(heap.data[0], Node(1, "c"))
        self.assertTrue(is_min_heap(heap))

    def test_build_tree_root_frequency(self):
        frequency = count_frequency("aaabbc")
        heap = create_priority_queue(frequency)
        root = build_tree_from_queue(heap)

        self.assertEqual(root.freq, 6)
        self.assertEqual(set(root.char), {"a", "b", "c"})

    def test_generate_codes_and_encode_decode(self):
        input_string = "aaabbc"
        frequency = count_frequency(input_string)
        heap = create_priority_queue(frequency)
        root = build_tree_from_queue(heap)
        codes = generate_codes(root)

        encoded = encode(input_string, codes)
        decoded = decode(encoded, root)

        self.assertEqual(decoded, input_string)
        self.assertEqual(set(codes.keys()), {"a", "b", "c"})

    def test_huffman_encoding_repeated_characters(self):
        input_string = "aaaa"

        frequency = count_frequency(input_string)
        heap = create_priority_queue(frequency)
        root = build_tree_from_queue(heap)
        codes = generate_codes(root)

        self.assertEqual(frequency, {"a": 4})
        self.assertEqual(root, Node(4, "a"))
        self.assertEqual(codes, {"a": ""})
        self.assertEqual(encode(input_string, codes), "")

    def test_huffman_encoding_empty_string(self):
        input_string = ""
        encoded, decoded, codes = huffman_encoding(input_string)

        self.assertEqual(encoded, "")
        self.assertEqual(decoded, "")
        self.assertEqual(codes, {})

    def test_huffman_encoding_ABBA(self):
        input_string = "ABBA"
        encoded, decoded, codes = huffman_encoding(input_string)

        self.assertEqual(encoded, "0110")
        self.assertEqual(decoded, input_string)
        self.assertEqual(codes, {"A": "0", "B": "1"})


if __name__ == "__main__":
    unittest.main()