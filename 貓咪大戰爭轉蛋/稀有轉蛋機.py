import easygui, random


picture = []
rare = ["跳跳貓","美容貓","魔劍士貓","車輪貓","搖滾貓",
        "超能力貓","高蹺貓","人魚貓","海盜貓","薩滿貓","僧侶貓",
        "占卜貓","拳擊手貓","樹剪貓","魔女貓","侏羅貓","弓箭手貓",
        "鬥士貓","小偷貓","發條貓","神槍手貓","貓咪陰陽師","貓咪探測器"]
epic = ["地底戰隊。地殼鑽","地底戰隊。木椿釘","地底戰隊。大力鉗",
        "地底戰隊。貓怪手","地底戰隊。電鋸手","菩薩貓","貓咪蕃長",
        "放浪貓弟","暖桌貓","御宅貓","快泳貓","蘋果貓","浴缸貓","壽司貓",
        "貓咪城mini","窗邊少女貓","舉重貓","冰刀二人組","麵包機貓",
        "衝浪貓","洞悉先機貓","土豪弟","狙擊手學徒","業餘撐桿跳貓",
        "擊劍貓","鋼鐵貓","黃金貓","萌萌貓"]
legendary = ["機器貓","貓護士","貓baby","冰雪女王貓","神鬼喵魔","貓咪鬥惡龍","巨劍騎士貓","拉斯沃斯",
             "不明貓","甩手貓","異能貓","刺骨貓","踢腳貓","頭錘貓","卷卷貓",
             "輝夜姬","蒲島太郎","猴蟹大戰貓","嘎擦嘎擦山崽子","桃太郎","白鶴貓","斗笠地藏",
             "冥界卡莉法","雙掌星西兒＆小毬","雷神珊迪亞","風神溫蒂","召喚。八戒貓","猿帝。悟空貓","寶杖使者。悟淨貓","英雄令孃蜜絲",
             "地龍索多姆","聖龍梅基多拉","龍騎士巴魯斯","霸龍迪拉姆斯","龍戰機雷電","神龍卡梅庫拉","古龍剛格利昂","角龍格拉迪歐斯",
             "真田幸村","織田信長","武田信玄","前田慶次","伊達政中","金川億元","上衫謙信","成田甲斐",
             "時空神克莉諾絲","繁榮神加納薩","海王神波賽頓","美女神阿芙蘿黛蒂","太陽神天照","天空神宙斯","守護神阿奴比斯",
             "貓俠大帝","阿激拉","天株飛隼","咒術師死亡小丑","白兔女俠","死亡偵探吳仲力","西園寺機器子",
             "帝國陸軍。石砲隊","溫泉天國。浴場隊","古代軍船。船槳隊","飛空襲擊。轟炸隊","觀測兵器。探天隊",
             "火精靈","風精靈","雷精靈","水精靈",
             "黑傑達太貓","小小瓦爾基麗貓","巫女姬御靈","黑獸牙王","黑無垢御靈","幼獸加歐","幼傑達太貓","貓飯拳派派","閃電機兵飛雷","風隼櫻","酷黑瓦爾基麗貓",
             "機器貓","貓護士","貓baby","冰雪女王貓","神鬼喵魔","貓咪鬥惡龍","巨劍騎士貓","拉斯沃斯",
             "不明貓","甩手貓","異能貓","刺骨貓","踢腳貓","頭錘貓","卷卷貓",
             "輝夜姬","蒲島太郎","猴蟹大戰貓","嘎擦嘎擦山崽子","桃太郎","白鶴貓","斗笠地藏",
             "冥界卡莉法","雙掌星西兒＆小毬","雷神珊迪亞","風神溫蒂","召喚。八戒貓","猿帝。悟空貓","寶杖使者。悟淨貓","英雄令孃蜜絲",
             "地龍索多姆","聖龍梅基多拉","龍騎士巴魯斯","霸龍迪拉姆斯","龍戰機雷電","神龍卡梅庫拉","古龍剛格利昂","角龍格拉迪歐斯",
             "真田幸村","織田信長","武田信玄","前田慶次","伊達政中","金川億元","上衫謙信","成田甲斐",
             "時空神克莉諾絲","海王神波賽頓","繁榮神加納薩","美女神阿芙蘿黛蒂","太陽神天照","天空神宙斯","守護神阿奴比斯",
             "貓俠大帝","阿激拉","天株飛隼","咒術師死亡小丑","白兔女俠","死亡偵探吳仲力","西園寺機器子",
             "帝國陸軍。石砲隊","溫泉天國。浴場隊","古代軍船。船槳隊","飛空襲擊。轟炸隊","觀測兵器。探天隊",
             "火精靈","風精靈","雷精靈","水精靈"]
very_legendary = ["天空城巴比貓塔","聖女貓會長貞德","宮本武藏","貓若丸","大地女神蓋亞","花樣桃子","奇幻貓","終末兵器。異滅堂","奇幻精靈露米納","超越科學者天域博士"]

special = (random.randint(1,100))
if special > 50: # special event??
    easygui.msgbox("SPECIAL EVENT!!!\n傳說稀有:0.3%\n超激稀有:9%\n激稀有:25%\n稀有:65.7%")
    c4s = 997
    c3s = 907
    c2s = 657
    choice_two = "10+1連抽(超激必中)"
else:
    easygui.msgbox("SPECIAL EVENT!!!\n傳說稀有:0.3%\n超激稀有:5%\n激稀有:25%\n稀有:69.7%")
    c4s = 997
    c3s = 947
    c2s = 697
    choice_two = "10+1連抽"

vl = 0
l = 0
e = 0
r = 0

while True:#start gacha!!
    c3 = 0
    c2 = 0
    c1 = 0
    c4 = 0
    ans = easygui.choicebox(("要抽甚麼轉蛋？\n(超激稀有x"+str(l)+"  激稀有x"+str(e)+"  稀有 x"+str(r)+")"),choices=["單抽",choice_two])
    if ans == "單抽":#only 1 time
        per = random.randint(1,1000)
        if per > c4s:
            char = "傳說稀有--"+very_legendary[random.randint(0,(len(very_legendary))-1)]
            vl += 1
            c4 += 1
        elif per > c3s:
            char = "超激稀有--"+legendary[random.randint(0,(len(legendary))-1)]
            l += 1
        elif per > c2s:
            char = "激稀有--"+epic[random.randint(0,(len(epic))-1)]
            e += 1
        else:
            char = "稀有--"+rare[random.randint(0,(len(rare)-1))]
            r += 1
        easygui.msgbox(char)
    elif ans == "10+1連抽":#10 +1 times
        for i in range(0,11):
            per = random.randint(1,1000)
            if per > c4s:
                char = "傳說稀有--"+very_legendary[random.randint(0,(len(very_legendary))-1)]
                vl += 1
                c4 += 1
            elif per > c3s:
                char = "超激稀有--"+legendary[random.randint(0,(len(legendary))-1)]
                l += 1
                c3 += 1
            elif per > c2s:
                char = "激稀有--"+epic[random.randint(0,(len(epic))-1)]
                e += 1
                c2 += 1
            else:
                char = "稀有--"+rare[random.randint(0,(len(rare))-1)]
                r += 1
                c1 += 1
            easygui.msgbox(char)
        easygui.msgbox("You got:\n    超激稀有 x"+str(c3)+"("+str(l)+")\n    激稀有 x"+str(c2)+"("+str(e)+")\n    稀有 x"+str(c1)+"("+str(r)+")")
    elif ans == "10+1連抽(超激必中)": # 10+1 times(100% get legendary)
        for i in range(0,10):
            per = random.randint(1,1000)
            if per > c4s:
                char = "傳說稀有--"+very_legendary[random.randint(0,(len(very_legendary))-1)]
                c4 += 1
                vl += 1
            elif per > c3s:
                char = "超激稀有--"+legendary[random.randint(0,(len(legendary))-1)]
                c3 += 1
                l += 1
            elif per > c2s:
                char = "激稀有--"+epic[random.randint(0,(len(epic))-1)]
                c2 += 1
                e += 1
            else:
                char = "稀有--"+rare[random.randint(0,(len(rare))-1)]
                c1 += 1
                r += 1
            easygui.msgbox(char)
        char = "超激稀有--"+legendary[random.randint(0,(len(legendary))-1)]
        c3 += 1
        l += 1
        easygui.msgbox(char)
        easygui.msgbox("You got:\n    傳說稀有x"+str(c4)+"("+str(vl)+")\n"+"超激稀有 x"+str(c3)+"("+str(l)+")\n    激稀有 x"+str(c2)+"("+str(e)+")\n    稀有 x"+str(c1)+"("+str(r)+")")
