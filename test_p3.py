import unittest
from proj3 import huffman_encoding

class TestHuffmanEncoding(unittest.TestCase):
    def test_hello(self):
        input_string = "hello"
        expected_encoded = "1111100010"
        expected_codes = {'l': '0', 'o': '10', 'e': '110', 'h': '111'}
        encoded, decoded, codes = huffman_encoding(input_string)
        self.assertEqual(encoded, expected_encoded)
        self.assertEqual(decoded, input_string)
        self.assertEqual(codes, expected_codes)

    def test_calpoly(self):
        input_string = "calpoly"
        expected_encoded = "011010101111101000"
        expected_codes = {'l': '10', 'y': '00', 'a': '010', 'c': '011', 'o': '110', 'p': '111'}
        encoded, decoded, codes = huffman_encoding(input_string)
        self.assertEqual(encoded, expected_encoded)
        self.assertEqual(decoded, input_string)
        self.assertEqual(codes, expected_codes)


    def test_ABBA(self):
        input_string = "ABBA"
        expected_encoded = "0110"
        expected_codes = {'A': '0', 'B': '1'}
        encoded, decoded, codes = huffman_encoding(input_string)
        self.assertEqual(encoded, expected_encoded)
        self.assertEqual(decoded, input_string)
        self.assertEqual(codes, expected_codes)

    def test_ABC(self):
        input_string = "ABC"
        expected_encoded = "10110"
        expected_codes = {'C': '0', 'A': '10', 'B': '11'}
        encoded, decoded, codes = huffman_encoding(input_string)
        self.assertEqual(encoded, expected_encoded)
        self.assertEqual(decoded, input_string)
        self.assertEqual(codes, expected_codes)



if __name__ == "__main__":
    unittest.main()
