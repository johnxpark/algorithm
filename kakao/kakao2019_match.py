import re

def solution(word, pages):
    word = word.lower()

    res = {}
    for page in pages:
        page = page.lower()

        url_raw = re.search('<meta property=\\"og:url\\" content=\\"http\S+\\"', page)
        url = page[url_raw.start():url_raw.end()].split("=")[-1]

        link_raw = re.findall('<a href=\\"http\S+\\"', page)
        link = [l.split("=")[-1] for l in link_raw]

        score = re.findall('(?=((?:[^a-z]|\s)' + word + '(?:[^a-z]+|\s)))', page)

        res[url] = {"score": len(score), "link": link, "link_score": 0.0}

    for key, value in res.items():
        for link in value["link"]:
            if link in res:
                res[link]["link_score"] += res[key]["score"] / len(res[key]["link"])

    max_idx, max_score = 0, 0.0
    for i, r in enumerate(res.values()):
        score = r["score"] + r["link_score"]
        if score > max_score:
            max_idx = i
            max_score = score

    return max_idx

if __name__ == "__main__":
    print(solution("blind", \
        ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", \
         "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", \
         "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"])) # 0
    print(solution("Muzi", \
         ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", \
          "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https:/hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"])) # 1
