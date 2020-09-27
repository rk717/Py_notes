import pickle

d = {
    "name":"lin",
    "role":"king",
    "blood": 12,
    "weapon": "Key"
}

alive_players = ["alex", "james", "lin"]

d_dump = pickle.dumps(d) #序列化
print(pickle.loads(d_dump)) #反序列化

f = open("game.pkl","wb")
#f.write(d_dump)
pickle.dump(d,f) #First in first out FIFO #first in last out
pickle.dump(alive_players,f)

dump 写入文件
dumps 生成序列化的字符串

load 从文件加载
loads 把序列化的字符串反向解析


pickle vs json

    pickle 
    只支持 python
    支持python里的所有数据类型

    json
    所有语言都支持
    只支持常规数据类型 str， int， dict set list， tuple
