from typing import List

class TrieNode:
    def __init__(self):
        self.letters = [None] * 26
        self.is_word = False

def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    head = TrieNode()
    for word in words:
        curr_node = head
        for char_idx in range(len(word)):
            if not curr_node.letters[ord(word[char_idx]) - ord('a')]:
                curr_node.letters[ord(word[char_idx]) - ord('a')] = TrieNode()
            curr_node = curr_node.letters[ord(word[char_idx]) - ord('a')]
            if char_idx == len(word) - 1:
                curr_node.is_word = True
    
    answer = []
    ROWS, COLS = len(board), len(board[0])
    def check_cell(curr_node, cell, visited, curr_word):
        visited.add(cell)
        curr_word.append(board[cell[0]][cell[1]])
        if curr_node.is_word:
            answer.append(''.join(curr_word))
            curr_node.is_word = False
        def valid_cell(cell):
            if (0 <= cell[0] < ROWS and 0 <= cell[1] < COLS and cell not in visited 
            and curr_node.letters[ord(board[cell[0]][cell[1]]) - ord('a')]):
                return True
            else:
                return False
        next_cells = [(cell[0]-1, cell[1]), (cell[0]+1, cell[1]), (cell[0], cell[1]-1), (cell[0], cell[1]+1)]
        for next_cell in next_cells:
            if valid_cell(next_cell):
                new_node = curr_node.letters[ord(board[next_cell[0]][next_cell[1]]) - ord('a')]
                check_cell(new_node, next_cell, visited, curr_word)
        curr_word.pop()
        visited.remove(cell)
    
    for row in range(ROWS):
        for col in range(COLS):
            if head.letters[ord(board[row][col]) - ord('a')]:
                check_cell(head.letters[ord(board[row][col]) - ord('a')], (row, col), set(), [])
    return answer