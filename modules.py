def set_rank(a_dict):
    a_sort_list = sorted(a_dict.items(), key=lambda x: x[1], reverse=True)
    a_sort_dict = {}
    for n, s in a_sort_list:
        a_sort_dict[n] = s
    return a_sort_dict


d = {}
file = open("rank.txt", "r")
out = open("final/keqing.md", "a")
for s in file.readlines():
    id = s.split(":")[0]
    score = int(s.split(":")[1])
    d[id] = score
d2 = set_rank(d)

for i, s in d2.items():
    out.write(
        "## [{}](https://danbooru.donmai.us/posts/{}?q=keqing_%28genshin_impact%29) likes: {}".format(i, i, s))
    out.write("\n")

file.close()
out.close()
