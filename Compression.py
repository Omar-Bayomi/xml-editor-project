import heapq
import os


class BinaryTree:
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        return self.freq == other.freq


class HuffmanCompression:

    def __init__(self, path):
        self.path = path
        self.__heap = []
        self.__code = {}
        self.__reversecode = {}

    def __frequecy_from_text(self, text):
        frequency_dict = {}
        for char in text:
            if char not in frequency_dict:
                frequency_dict[char] = 0
            frequency_dict[char] += 1
        return frequency_dict

    def __build_heap(self, frequency_dict):
        for key in frequency_dict:
            frequency = frequency_dict[key]
            binary_tree_node = BinaryTree(key, frequency)
            heapq.heappush(self.__heap, binary_tree_node)

    def __Build_Binary_Tree(self):
        while len(self.__heap) > 1:
            node1 = heapq.heappop(self.__heap)
            node2 = heapq.heappop(self.__heap)
            freq_sum = node1.freq + node2.freq
            newnode = BinaryTree(None, freq_sum)
            newnode.left = node1
            newnode.right = node2
            heapq.heappush(self.__heap, newnode)
        return

    def __Build_tree_codeHelper(self, root, current_bits):
        if root is None:
            return
        if root.value is not None:
            self.__code[root.value] = current_bits
            self.__reversecode[current_bits] = root.value
            return
        self.__Build_tree_codeHelper(root.left, current_bits + '0')
        self.__Build_tree_codeHelper(root.right, current_bits + '1')

    def __Build_tree_code(self):
        root = heapq.heappop(self.__heap)
        self.__Build_tree_codeHelper(root, '')

    def __Build_encoded_text(self, text):
        encoded_text = ''
        for char in text:
            encoded_text += self.__code[char]
        return encoded_text

    def __build_padded_text(self, encoded_text):
        padding = 8 - len(encoded_text) % 8
        for i in range(padding):
            encoded_text += '0'
        padded_info = "{0:08b}".format(padding)
        padded_text = padded_info + encoded_text
        return padded_text

    def __build_byte_array(self, padded_text):
        byte_array = []
        for i in range(0, len(padded_text), 8):
            byte = padded_text[i:i + 8]
            byte_array.append(int(byte, 2))
        return byte_array

    def Compression(self):
        # text = 'fdhkjsjfjbsknfhdjklsfjhgirjeodkfvbhjgrefjd'
        filename, file_extension = os.path.splitext(self.path)
        output_path = filename + '.bin'
        with open(self.path, 'r+') as file, open(output_path, 'wb') as output:
            text = file.read()
            text = text.rstrip()
            frequency_dict = self.__frequecy_from_text(text)
            self.__build_heap(frequency_dict)
            self.__Build_Binary_Tree()
            self.__Build_tree_code()
            encoded_text = self.__Build_encoded_text(text)
            padded_text = self.__build_padded_text(encoded_text)
            byte_array = self.__build_byte_array(padded_text)
            final_bytes = bytes(byte_array)
            output.write(final_bytes)
        print("succesfully done")
        return output_path


        return
