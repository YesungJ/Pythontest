'''kens = ["kanagawa","tokyo","END","tochigi","chiba","saitama"]

for ken in kens:
    if ken == "END":
        print("continue loop")
        continue
    print(ken)
else:
    print("End loop")
    
'''
games = ["lol", "pubg", "fgo", "maple", "diablo"]

#indexの名前もとってこれる
'''
for index,games in enumerate(games):
    print(str(index)+":"+games)
'''
titles = ["katarina", "M4", "Altoria","Arrow","mola"]

#zip関数
for (game, title)in zip(games, titles):
    print("game:"+game+"\ntitle:"+title+"\n")
