class Trie:
    def __init__(self):
        self.root = {}
    def insert(self, nums):
        current_node = self.root
        for i, num in enumerate(nums):
            if num not in current_node:
                current_node[num] = {}
            else:
                if i == len(nums) - 1:
                    return False
            current_node = current_node[num]
            if "*" in current_node:
                return False
        current_node["*"] = "*"
        return True

def solution(phone_book):
    trie = Trie()
    for nums in phone_book:
        res = trie.insert(nums)
        if not res:
            return False
    return True

if __name__ == "__main__":
    print(solution(["12", "123"])) # False
    print(solution(["123", "12"])) # False
    print(solution(["119", "97674223", "1195524421"])) # False
    print(solution(["123","456","789"])) # True
    print(solution(["12","123","1235","567","88"])) # False