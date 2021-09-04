import re

def solution(new_id: str) -> str:
    new_id = new_id.lower()
    new_id = re.sub('[^0-9a-z._-]', '', new_id)
    new_id = re.sub('[.]+', '.', new_id)
    new_id = re.sub('(^[.]|[.]$)', '', new_id)
    new_id = new_id if new_id else 'a'
    new_id = re.sub('[.]$', '', new_id[:15])
    new_id = new_id if len(new_id) > 3 else new_id + new_id[-1] * (3 - len(new_id))
    return new_id

if __name__ == "__main__":
    print(solution("...!@BaT#*..y.abcdefghijklm")) # "bat.y.abcdefghi"
    print(solution("z-+.^.")) # "z--"
    print(solution("=.=")) # "aaa"
    print(solution("123_.def")) # "123_.def"
    print(solution("abcdefghijklmn.p")) # "abcdefghijklmn