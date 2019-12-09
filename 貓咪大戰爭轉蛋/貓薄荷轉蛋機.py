import easygui, random


picture = []
rare = ["綠色貓薄荷種子","紫色貓薄荷種子","紅色貓薄荷種子","藍色貓薄荷種子","黃色貓薄荷種子","XP+100,000","加速","貓型電腦"]
epic = ["綠色貓薄荷","紫色貓薄荷","紅色貓薄荷","藍色貓薄荷","黃色貓薄荷","XP+500,000","洞悉先機","狙擊手","土豪貓"]
legendary = ["XP+1,000,000","彩虹貓薄荷","寶物雷達"]

special = (random.randint(1,100))
if special > 75:
    easygui.msgbox("SPECIAL EVENT!!!")
    c3s = 70
    c2s = 30
else:
    c3s = 85
    c2s = 55
for g in range(0,99**99):
    c3 = 0
    c2 = 0
    c1 = 0

    ans = easygui.choicebox("要抽甚麼轉蛋？",choices=["單抽","10連抽"])
    if ans == "單抽":
        per = random.randint(1,100)
        if per > c3s:
            char = "中超大獎啦!!～～"+legendary[random.randint(0,(len(legendary))-1)]
        elif per > c2s:
            char = "中大獎啦!～～"+epic[random.randint(0,(len(epic))-1)]
        else:
            char = "中獎啦～～"+rare[random.randint(0,(len(rare)-1))]
        easygui.msgbox(char)
    elif ans == "10連抽":
        for i in range(0,10):
            per = random.randint(1,100)
            if per > c3s:
                char = "中超大獎啦!!～～"+legendary[random.randint(0,(len(legendary))-1)]
                c3 += 1
            elif per > c2s:
                char = "中大獎啦!～～"+epic[random.randint(0,(len(epic))-1)]
                c2 += 1
            else:
                char = "中獎啦～～"+rare[random.randint(0,(len(rare))-1)]
                c1 += 1
            easygui.msgbox(char)
        easygui.msgbox("You got:\n    超大獎 x"+str(c3)+"\n    大獎 x"+str(c2)+"\n    中獎 x"+str(c1))
