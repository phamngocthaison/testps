# -*- coding: utf-8 -*-

df_Word = ['dictionary', 'necessarily clear']

df_Sentence = ['For example, the data <b>dictionary</b> gives the following information about the cp column:<div><br></div><div>_từ điển</div>',
               "Based on this information, it’s not <b>necessarily</b> <b>clear</b> whether the data is going to be coded as numerical values (eg., 1, 2, 3, or 4) or with strings (eg., 'typical angina'). <div><br></div><div>_cần thiết xóa</div>"]

result = ['For example, the data <b>**********</b> gives the following information about the cp column:<div><br></div><div>_từ điển</div>',
          "Based on this information, it’s not <b>***********</b> <b>*****</b> whether the data is going to be coded as numerical values (eg., 1, 2, 3, or 4) or with strings (eg., 'typical angina'). <div><br></div><div>_cần thiết xóa</div>"]


res = []
for line in df_Sentence:
    for words in df_Word:
        for w in words.split():
            line = line.replace(w, '*'*len(w))
    res.append(line)
print res
