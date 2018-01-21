import json
import random

if __name__ == "__main__":
    restaurants = json.loads(open("restaurants.json", "r").read())
    tags = dict()
    tags_ls = []
    for r in restaurants:
        for t in r["tags"]:
            if t not in tags:
                tags[t] = set()
                tags_ls.append(t)
            tags[t].add(json.dumps(r))
    print "available tags:"
    print ", ".join(tags_ls)
    ts = map(lambda x: x.strip(), raw_input("? ").strip().split(","))
    draw = set()
    ts_rm = filter(lambda x: x[0] == "!", ts)
    ts = filter(lambda x: x[0] != "!", ts)
    ts = tags_ls if len(ts) == 0 else ts
    for t in ts:
        for r in tags[t]:
            draw.add(r)
    for t in ts_rm:
        for r in tags[t[1:]]:
            if r in draw:
                draw.remove(r)
    ls = []
    for r in draw:
        ls.append(r)
    print "Your restaurant today is:"
    print json.dumps(json.loads(ls[random.randint(0, len(ls) - 1)]), indent=4)
