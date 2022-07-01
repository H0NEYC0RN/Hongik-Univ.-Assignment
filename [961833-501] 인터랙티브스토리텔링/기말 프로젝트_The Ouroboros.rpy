init:
    #GUI / Option 정의
    $ gui.show_name = False
    $ quick_menu = False
    define gui.choice_button_text_idle_color = '#000000'
    define gui.choice_button_text_hover_color = '#ffffff'
    $ Language_change = 0

    # 캐릭터 정의
    define F = DynamicCharacter("FN",color="FF0000")
    image F Default = "woman_default.png"
    image F None = "woman_none.png"
    image F Afeared = "woman_afeared.png"
    image F Sad = "woman_sad.png"
    image F Awkward = "woman_awkward.png"
    image F Angry = "woman_angry.png"
    
    define M = DynamicCharacter("MN",color="0000FF")
    image M Default = "Man_default.png"
    image M None = "man_none.png"
    image M Awkward = "man_awkward.png"
    image M Angry = "man_angry.png"
    image M Panic = "man_panic.png"
    image M Unbreathing = "man_unbreathing.png"

    define B = DynamicCharacter("BN",color="000000")

    # 이미지 정의
    image Background = "bar.png"
    image Cuba = "Cuba_Libre.png"
    image Necklace = "Necklace.png"
    image Truth = "the_bitter_truth.png"
    image Memory = "the_memories_remains"
    image Loss = "memory_loss.png"

    #내부 변수 정의
    $ F_Memory = 0
    $ F_Loss = 0
    $ F_Truth = 0

    $ M_Memory = 0
    $ M_Loss = 0
    $ M_Truth = 0

    $ is_Skip = 0

    $ FN = ""
    $ MN = ""
    $ BN = ""

label start:
    menu: 
        "한국어":
            $ FN = "여자"
            $ MN = "남자"
            $ BN = "나"
            jump Korean
        "English":
            $ FN = "Woman"
            $ MN = "Man"
            $ BN = "Me"
            jump English

label Korean:
    centered "{color=ffffff}이 게임은 {/color}{color=ff0000}폭행, 폭언, 죽음{/color}{color=ffffff}에 대한 직/간접적인 묘사가 포함되어 있습니다.{/color}" with dissolve
    centered "{color=ffffff}게임에서 사용된 소재는 결코 현실에서 일어나서는 안되는 것이며,\n\n제작진 역시 폭력을 절대로 옹호/지지하지 않습니다.{/color}" with dissolve

    "프롤로그를 스킵할까요?"
    menu:
        "YES":
            "선택지로 바로 이동할까요?"
            menu:
                "YES":
                    play music "BGM_Main.mp3" fadein 1.5 loop
                    $ is_Skip = 2
                    jump Main_2
                "NO": 
                    play music "BGM_Main.mp3" fadein 1.5 loop
                    $ is_Skip = 1
                    jump Main_1
        "NO":
            play music "BGM_Main.mp3" fadein 1.5 loop
            call Prologue from _call_Prologue

label English:
    centered "{color=ffffff}The game includes direct and indirect descriptions of {/color}{color=ff0000}assault, verbal abuse, {/color}{color=ffffff}and {/color/}{color=ff0000}death.{/color}" with dissolve
    centered "{color=ffffff}{color=ffffff}The theme used in the game is something that should never happen in reality, \n\n and the crew also never advocates/supports violence.{/color}" with dissolve

    "Skip the Prologue?"
    menu:
        "YES":
            "Move on to the Selection?"
            menu:
                "YES":
                    play music "BGM_Main.mp3" fadein 1.5 loop
                    $ is_Skip = 2
                    jump Main_2_Eng
                "NO": 
                    play music "BGM_Main.mp3" fadein 1.5 loop
                    $ is_Skip = 1
                    jump Main_1_Eng
        "NO":
            play music "BGM_Main.mp3" fadein 1.5 loop
            call Prologue_Eng from _call_Prologue_Eng

label Prologue:
    scene Background with Fade(0.25,0.3,0.25,color="000")

    #Prologue
    play sound "SE_Japanese_furin.mp3" fadein 3
    "짤랑, 하는 방울소리와 함께 바에 한 여자가 들어왔다." with dissolve
    "여자는 입구에 서서 잠시 바의 내부를 구경한다."

    "카운터에서 여자 외의 유일한 손님으로 보이는 남자가 바텐더와 이야기를 나누고 있다."
    show M Default with dissolve

    M "…내가 꼭 찾아낼 겁니다." with dissolve
    B "그럼요. 당신이라면 충분히 그러실 수 있을 겁니다."
    B "너무 조급해하실 필요 없습니다."
    B "기회는 한 번만 있는 게 아니지 않습니까?"

    "여자가 카운터로 다가온다."
    hide M Default
    show F Default with dissolve
    F "어머, 좋은 향을 가지고 계시네요." with dissolve
    

    "남자가 주변을 잠시 두리번거린다."
    hide F Default
    show M Default with dissolve
    M "…저 말씀하시는 건가요?" with dissolve
    F "네, 향기가 아주 좋으신 분이네요."
    
    hide F Default
    show M Default with dissolve
    "남자는 무언가 허탈한 듯 작게 웃는다."
    M "…칭찬 감사합니다. 향을 좋아하시는 분이신가 보군요."

    hide M Default
    show F Default with dissolve
    F "그렇다고 해 두죠. "
    

    "여자가 남자의 술잔을 슬쩍 보고 묻는다."
    hide F Default
    show Cuba with dissolve
    F "으음…. 지금 드시고 계신 술 괜찮은가요?"
    F "사실 당장 술을 마실 생각은 없었는데…\n이 곳의 간판을 보자 마자 홀린 듯 들어오게 됐지 뭐에요?"
    M "흠, 술을 좋아하시는 편이신가요?"
    F "조금은요."
    M "가볍게 마시기엔 괜찮다고 생각합니다. 그렇게 알콜이 강하지 않아서요."
    F "그래요? 흥미가 가네요."
    hide Cuba
    show M Default at left
    show F Default at right
    with dissolve
    "여자는 남자와 두 자리 떨어진 곳에 앉았다. \n남자가 마시고 있는 술과 같은 것으로 주문한다." with dissolve

    B "쿠바 리브레입니다."
    F "감사합니다."

    call Main_1 from _call_Main_1

label Prologue_Eng:
    scene Background with Fade(0.25,0.3,0.25,color="000")

    #Prologue
    play sound "SE_Japanese_furin.mp3" fadein 3
    "A woman came into the bar with a bell sound." with dissolve
    "The woman stands at the entrance and looks around the inside of the bar for a while."

    "At the counter, a man who seem to be the only guest other than a woman is talking to a bartender."
    show M Default with dissolve

    M "…I'll find out for sure." with dissolve
    B "Of course. I'm sure you can."
    B "Don't be so impatient."
    B "You have more than one chance, right?"

    "The woman approaches the counter."
    hide M Default
    show F Default with dissolve
    F "Oh, you have a nice scent." with dissolve
    

    "The man looks around for a moment."
    hide F Default
    show M Default with dissolve
    M "…Are you talking about me?" with dissolve
    F "Yes, he smells very good."
    
    hide F Default
    show M Default with dissolve
    "The man smiles quietly as if he were in perplexed."
    M "…Thank you for the compliment. I guess you like scents."

    hide M Default
    show F Default with dissolve
    F "Maybe it is. "
    

    "The woman sneaks at the man's cup and asks."
    hide F Default
    show Cuba with dissolve
    F "Um…. Is the alcohol you're drinking okay?"
    F "Actually, I didn't mean to drink….\nAs soon as I saw this sign, I came in like I was possessed"
    M "Well, do you like to drink?"
    F "A little bit."
    M "I think it's okay to drink lightly. The alcohol isn't that strong."
    F "Really? That's interesting."
    hide Cuba
    show M Default at left
    show F Default at right
    with dissolve
    "The woman sat two seats away from the man. \nOrder the same alcohol that the man is drinking." with dissolve

    B "It's Cuban Libre."
    F "Thank you."

    call Main_1_Eng from _call_Main_1_Eng

label Main_1:
    if is_Skip == 1:
        scene Background with Fade(0.25,0.3,0.25,color="000")
        show M Default at left
        show F Default at right
        with dissolve
    
    F "으음, 시간이 꽤 늦었는데도 사람이 그렇게 많지는 않네요?"
    B "하하, 항상 오시는 분들만 오시는 편입니다."
    B "고즈넉하게 마시기 좋다고 좋아하시는 분들이 많죠."
    F "확실히요, 뭔가 시끌벅적한 분위기가 아니라 편한 분위기라 좋네요."
    F "왠지 모르게 익숙하다고 해야하나…."
    F "여기 오게 된 건 처음인데, 이상하게 편하네요."

    "여자가 웃으며 말을 건넨다."

    F "그 쪽도 여기 자주 오시는 편이신가요?"
    M "…네, 그런 편입니다."
    F "와아, 그럼 저도 오늘부터 단골이 되어야겠어요!"

    "여자는 남자가 마음에 든 눈치다. 웃으며 계속 남자에게 말을 건넨다."

    F "이렇게 동지가 되었는데.. 우리 통성명이나 할까요?"
    M "…"
    F "난 안나라고 해요. 그쪽은 이름이 뭔가요?"
    M "…제임스 입니다."
    F "아, 역시! 뭔가 그런 이름일 것 같았어요."
    F "이상한 소리긴 하지만, 최근에 보고 있는 드라마에서 당신과 닮은 사람이 나오거든요…"
    F "그래선지, 뭔가 당신 이름도 비슷할 것 같다고 생각했지 뭐에요?"
    F "뭔가, 짐이라고 불러야 할 것 같은 느낌이에요."
    M "…. 짐… 이라고요?"

    "여자가 '짐'이라는 호칭을 꺼내자, 남자가 잠시 눈에 띄게 굳는다."
    
    F "아… 혹시 제가 실례를 했을까요…?"
    M "아닙니다."
    M "…실제로도 짐이라고 부르는 사람이 있었어서 잠시 당황했네요."
    F "으음… 미안해요 제임스."
    M "편하게 부르셔도 됩니다. 짐이나, 제임스나요."
    F "그..으래요? 그럼 짐이라고 불러도 괜찮을까요?"
    M "좋으실대로."
    F "좋아요!"

    "여자가 계속 남자에게 말을 건다."
    "어느 새 여자는 자리를 옮겨 남자의 옆자리에 앉아있다."
    "남자도 계속해서 말을 거는 여자에게 어느정도 익숙해진 것 같다."
    "… …" with Fade(0.5,1,0.5,color="000000")

    F "…그랬다니까요? 내가 어이가 없어서 정말."
    M "그렇군요."

    F "좋아요, 여태까지 계속 내 얘기만 하는 것도 슬슬 힘드네요."
    F "짐, 짐의 얘기도 해줘요!"
    F "사실, 여기 처음 왔을 때 당신한테 뭔가 고민이 있어 보였거든요."
    F "마침 동지가 된 겸 내가 그 고민 들어줄까요?"
    M "…고민이요?"
    F "네에, 고민."
    F "캐모마일 향을 풍기는 사람 치고 고뇌가 없는 사람이 없거든."
    M "…내가 그렇습니까?"
    F "그럼요. 얼핏 스쳐도 느껴질 정도면 아주 가까이에 두나 봐요?"
    F "아, 나도 캐모마일 좋아해요."

    show Necklace with dissolve

    F "항상 몸에도 달고 다닐 정도로요."
    F "우와. 그러고 보면 당신과 나는 닮은 점이 아주 많군요!"
    M " …캐모마일…."
    M "내가 가져다 둔 적은 없지만, 항상 곁에 많이 있긴 했네요."

    hide Necklace

    "남자는 잠깐 상념에 빠진 듯 하다, 이윽고 대답한다."
    "여자는 남자의 눈치를 살피며 말을 건넨다."

    F "아…. 혹시 연인분이…?"
    M "아뇨, 연인이라니."
    M "그냥 알고 있는 사람입니다."

    "'연인'이라는 말에 남자의 얼굴에 잠시 불쾌감이 스친다."

    F "…그렇군요…."

    "여자는 눈치를 살피며 다른 주제로 이야기를 돌린다."
    "어쩐지 죽이 척척 맞았던 그들은 그렇게 한참을 대화했다."

    call Main_2 from _call_Main_2

label Main_1_Eng:
    if is_Skip == 1:
        scene Background with Fade(0.25,0.3,0.25,color="000")
        show M Default at left
        show F Default at right
        with dissolve
    
    F "Well, it's pretty late, but there aren't that many people?"
    B "Haha, only the people who always come come."
    B "There are regular who like it because it's good to drink quietly."
    F "Certainly, I like it because it's not a noisy atmosphere but a comfortable atmosphere."
    F "I don't know why, but I'm used to it…."
    F "It's my first time here, and it's strangely comfortable."

    "The woman talks with a smile."

    F "Do you come here often, too?"
    M "…Well, I do."
    F "Wow, then I should be a regular starting today!"

    "A woman seems to interested a man. she keeps talking to the man with a smile."

    F "We've become comrades. Can we know a name for each other's?"
    M "…"
    F "My name is Anna. What's your name?"
    M "…James."
    F "As expected! I thought it would be that kind of name."
    F "It may sound something crazy, but there is a person who looks like you in the drama I've been watching recently."
    F "So, I thought you might have a similar name."
    F "I feel like I should call you 'Jim.'"
    M "…. you say 'Jum'..?"

    "When the woman brings up the name of 'Jim,' the man becomes noticeable stuck for a while."
    
    F "Oh… Did I ever excuse myself…?"
    M "No."
    M "…I was embarrassed for a second because there was someone who actually called me Jim."
    F "Umm… Sorry James."
    M "You can sing it comfortably. It's Jim or James, I don't care."
    F "R..ight? Is it okay if I call you Jim."
    M "As you wish."
    F "Okay!"

    "The woman keeps talking to the man."
    "A new woman is sitting next to the man."
    "The man seems to have gotten somewhat used to the woman who keeps talking to him."
    "… …" with Fade(0.5,1,0.5,color="000000")

    F "…That's what happened?? I was so speechless."
    M "That's a ridiculous story."
    F "I mean so!"

    F "Good, it's getting hard to just talk about me all this whole time."
    F "Jim, tell me about Jim!"
    F "Actually, when I first came here, you seemed to have something on your mind."
    F "Do you want me to listen to your concerns?"
    M "…My concern?"
    F "Yeees, Your concern."
    F "For someone who smells like chamomile, there's no one who doesn't have concerns."
    M "…Am I?"
    F "Of course. I guess you keep it close enough to feel it"
    F "Oh, I like chamomile, too."

    show Necklace with dissolve

    F "I always carry it around on my body."
    F "Wow. Come to think of it, you and I have so many similarities!"
    M "…chamomile…."
    M "I've never brought it, but that've always been my around a lot."

    hide Necklace

    "The man seems to be lost in thought for a moment, and then he replies."
    "The woman looks at the man and speaks."

    F "Oh… Is your Darling…??"
    M "No, that's wrong."
    M "Just I know person."

    "A man is briefly displeased."

    F "…R..ight…."

    "The woman take a look at him, turning to a different subject."
    "Somehow they got along so well that they talked for a long time."

    call Main_2_Eng from _call_Main_2_Eng

label Main_2:
    if is_Skip == 2:
        scene Background with Fade(0.25,0.3,0.25,color="000")
        show M Default at left
        show F Default at right
        with dissolve
    else:
        scene Background with Fade(0.5,1,0.5,color="000")
        show M Default at left
        show F Default at right
        with dissolve

    F "후…. 오랜만에 이렇게 대화가 잘 통하는 사람을 만나서 너무 즐거웠어요."
    F "마지막 한 잔만 마시고 일어날까요?"
    M "그럼, 마지막 잔은 시그니처로 마무리하죠."
    F "흠? 시그니처 칵테일도 있었군요?"
    M "항상 마지막 잔은 시그니처 칵테일로 마무리 하는게 이 곳의 문화죠."
    F "와, 정말 그런 문화가 있나요?"
    B "하하. 별 것 아닙니다. 어쩌다보니 단골분들이 항상 마무리를 시그니처로 주문하시더군요."
    B "그러다보니 자연스럽게 문화가 되어버렸지 뭡니까."
    B "물론 강제적인 것은 아닙니다."
    B "다만 제가 자신있게 말씀드릴 수 있는 점은, 어디서든 맛보지 못한 새로운 칵테일을 보여드릴 것입니다."
    F "우와.. 그거 멋진데요? 그 잔 저도 받을 수 있나요?"
    B "물론이죠. 시그니처로 마무리 하시겠습니까?"
    F "네, 좋아요!"
    B "두분 다, 어떤 시그니처 칵테일을 내어드릴까요?"
    F "음…. 제일 자신있는 칵테일로 주세요."
    B "그렇다면, 제 미공개 시범작을 보여드려도 괜찮을까요?"
    M "언제나처럼, 당신 선택에 맡기죠."
    F "와, 물론이죠! 너무 좋아요!"
    B "좋습니다. 최선을 다하죠."

    hide F Default
    hide M Default
    with dissolve

    call Select_1 from _call_Select_1

label Main_2_Eng:
    if is_Skip == 2:
        scene Background with Fade(0.25,0.3,0.25,color="000")
        show M Default at left
        show F Default at right
        with dissolve
    else:
        scene Background with Fade(0.5,1,0.5,color="000")
        show M Default at left
        show F Default at right
        with dissolve

    F "Whew…. It was so nice to meet someone who I can communicate with after a long time."
    F "Shall we get up after one last drink?"
    M "Then, let's wrap up with a signature."
    F "Hmm? There was a signature cocktail, too?"
    M "The culture of this place is to finish the last cup with a signature cocktail."
    F "Wow, is there really such a culture?"
    B "Haha. It's nothing. It just so happens that regulars always order the finish as signature."
    B "So it became a culture naturally."
    B "Of course, it's not compulsory."
    B "But what I can tell you with confidence is that I'll show you a new cocktail that you've never tasted anywhere."
    F "Wow, that's cool! Can I get that signature?"
    B "Sure. Would you like to wrap up with a signature?"
    F "Yes, good!"
    B "What kind of signature cocktail would you like?"
    F "Um... I'd like to have the cocktail that you're most confident in."
    B "Then, can I show you my unreleased demonstration?"
    M "As always, I'll leave it up to you."
    F "Wow, of course! I love it!"
    B "All right, I'll do my best."

    hide F Default
    hide M Default
    with dissolve

    call Select_1_Eng from _call_Select_1_Eng

#1st Select
label Select_1:
    "{color=#ff0000}{b}여자{/color}{/b}에게 내어줄 칵테일을 만들자."
    "{b}베이스{/b}는 뭘로 할까…."
    menu:

        #진실
        "리큐르를 베이스로": 
            $ F_Truth += 1
            call Select_2 from _call_Select_2
        #기억
        "위스키를 베이스로":
            $ F_Memory += 1
            call Select_2 from _call_Select_2_1
        #망각
        "브랜디를 베이스로":
            $ F_Loss += 1
            call Select_2 from _call_Select_2_2

label Select_1_Eng:
    "Let's make a cocktail for {color=#ff0000}{b}the woman{/color}{/b}."
    "What should be {b}the base{/b} of the cocktail?"
    menu:

        #진실
        "Liqueur as the base.": 
            $ F_Truth += 1
            call Select_2_Eng from _call_Select_2_Eng
        #기억
        "Whiskey as a base.":
            $ F_Memory += 1
            call Select_2_Eng from _call_Select_2_Eng_1
        #망각
        "Brandy as the base.":
            $ F_Loss += 1
            call Select_2_Eng from _call_Select_2_Eng_2

#2nd Select
label Select_2:
    "{b}추가 재료{/b}는 뭘로 할까…."

    menu:
        #기억
        "레드 와인과 리큐르를 추가한다.":
            $ F_Memory += 1
            call Select_3 from _call_Select_3
        #진실
        "에스프레소와 과일 주스를 추가한다.": 
            $ F_Truth += 1
            call Select_3 from _call_Select_3_1
        #망각
        "진과 과일 주스를 추가한다.":
            $ F_Loss += 1
            call Select_3 from _call_Select_3_2

label Select_2_Eng:
    "What about {b}the extra ingredients{/b} for the cocktail?"

    menu:
        #기억
        "Add red wine and liqueur.":
            $ F_Memory += 1
            call Select_3_Eng from _call_Select_3_Eng
        #진실
        "Add espresso and fruit juice.": 
            $ F_Truth += 1
            call Select_3_Eng from _call_Select_3_Eng_1
        #망각
        "Add gin and fruit juice.":
            $ F_Loss += 1
            call Select_3_Eng from _call_Select_3_Eng_2

#3rd Select
label Select_3:
    "{b}마무리{b}는…."

    menu:
        #망각
        "라임을 가니쉬로 사용한다.": 
            $ F_Loss += 1
            call Select_result_1 from _call_Select_result_1
        #기억
        "커피콩을 가니쉬로 사용한다.":
            $ F_Memory += 1
            call Select_result_1 from _call_Select_result_1_1
        #진실
        "계피 스틱을 가니쉬로 사용한다.":
            $ F_Truth += 1
            call Select_result_1 from _call_Select_result_1_2

label Select_3_Eng:
    "What about {b}Garnish{/b} for the cocktail?"

    menu:
        #망각
        "Use lime as garnish.": 
            $ F_Loss += 1
            call Select_result_1_Eng from _call_Select_result_1_Eng
        #기억
        "Use coffee beans as garnish.":
            $ F_Memory += 1
            call Select_result_1_Eng from _call_Select_result_1_Eng_1
        #진실
        "Use cinnamon sticks as garnish.":
            $ F_Truth += 1
            call Select_result_1_Eng from _call_Select_result_1_Eng_2

label Select_result_1:
    if F_Loss == 3:
        show M Default at left
        show F Default at right
        with dissolve

        show Loss with dissolve
        B "기억 상실, 한 잔 나왔습니다."
        F "어디…."
        F "우와…. 이거 정말 좋네요."
        F "기억 상실이라니…."
        F "확실히, 이런 칵테일이라면 계속 마시다 필름이 끊겨도 모르겠는걸요?"
        B "하하, 칭찬해주셔서 감사합니다."
        B "같은 걸로 드릴까요?"
        M "흠…. 당신 마음대로."
        B "좋습니다."
        hide Loss with dissolve

        call Select_4 from _call_Select_4
    elif F_Memory == 3:
        show M Default at left
        show F Default at right
        with dissolve
        show Memory with dissolve
        B "남겨진 기억, 한 잔 나왔습니다."
        F "어디…."
        F "우와…. 이거 정말 좋네요!"
        F "……."
        F "뭔가, 어디선가 먹어본 맛인 것 같은데…."
        F "흠, 뭐지? …."
        F "아무튼, 제 취향인건 확실 하군요."
        B "하하, 칭찬해주셔서 감사합니다."
        B "같은 걸로 드릴까요?"
        M "흠…. 당신 마음대로."
        B "좋습니다."
        hide Memory with dissolve

        call Select_4 from _call_Select_4_1
    elif F_Truth == 3:
        show M Default at left
        show F Default at right
        with dissolve
        show Truth with dissolve
        B "쓰라린 진실, 한 잔 나왔습니다."
        F "어디…."
        F "우와…. 이거 정말 좋네요!"
        F "왠지…. 그리운 맛 인 것 같기도 하고…."
        F "으음…. 이유는 모르겠지만, 가슴이 아파지는 맛?"
        F "…싫다는건 아니에요! 정말 제 취향이네요."
        B "하하, 칭찬해주셔서 감사합니다."
        B "같은 걸로 드릴까요?"
        M "흠…. 당신 마음대로."
        B "좋습니다."
        hide Truth with dissolve

        call Select_4 from _call_Select_4_2
    else :
        jump Select_fail

label Select_result_1_Eng:
    if F_Loss == 3:
        show M Default at left
        show F Default at right
        with dissolve

        show Loss with dissolve
        B "'Memory loss'. Here's a drink."
        F "Let's see…."
        F "Wow, this is really nice."
        F "'Memory loss'…."
        F "Exactly, If it's a all cocktail like this, I wouldn't know even if I kept drinking to the Memory loss."
        B "Haha, thank you for the compliment."
        B "Would you like the same one?"
        M "Hmm… as you wish. I don't mind anything else."
        B "Okay."
        hide Loss with dissolve

        call Select_4_Eng from _call_Select_4_Eng

    elif F_Memory == 3:
        show M Default at left
        show F Default at right
        with dissolve
        show Memory with dissolve
        B "'Remain Memories'. Here's a drink."
        F "Let's see…."
        F "Wow, this is really nice."
        F "……."
        F "I think I've tasted it somewhere…."
        F "Hmm, what is it?…."
        F "Anyway, I'm sure it's my cup of tea."
        B "Haha, thank you for the compliment."
        B "Would you like the same one?"
        M "Hmm… as you wish. I don't mind anything else."
        B "Okay."
        hide Memory with dissolve

        call Select_4_Eng from _call_Select_4_Eng_1

    elif F_Truth == 3:
        show M Default at left
        show F Default at right
        with dissolve
        show Truth with dissolve
        B "'Bitter Truth'. Here's a drink."
        F "Let's see…."
        F "Wow, this is really nice."
        F "It's kind of a nostalgic taste…."
        F "Um…. I don't know why, but it makes my heart ache"
        F "…I'm not saying I don't like it! It's really my cup of tea."
        B "Haha, thank you for the compliment."
        B "Would you like the same one?"
        M "Hmm… as you wish. I don't mind anything else."
        B "Okay."
        hide Truth with dissolve

        call Select_4_Eng from _call_Select_4_Eng_2
    else :
        jump Select_fail_Eng

#4st Select
label Select_4:
    "{color=#0000ff}{b}남자{/color}{/b}에게 내어줄 칵테일을 만들자."
    "{b}베이스{/b}는 뭘로 할까…."
    menu:

        #진실
        "리큐르를 베이스로": 
            $ M_Truth += 1
            call Select_5 from _call_Select_5
        #기억
        "위스키를 베이스로":
            $ M_Memory += 1
            call Select_5 from _call_Select_5_1
        #망각
        "브랜디를 베이스로":
            $ M_Loss += 1
            call Select_5 from _call_Select_5_2

label Select_4_Eng:
    "Let's make a cocktail for {color=#0000ff}{b}the man{/color}{/b}."
    "What should be {b}the base{/b} of the cocktail?"
    menu:

        #진실
        "Liqueur as the base.": 
            $ M_Truth += 1
            call Select_5_Eng from _call_Select_5_Eng
        #기억
        "Whiskey as a base.":
            $ M_Memory += 1
            call Select_5_Eng from _call_Select_5_Eng_1
        #망각
        "Brandy as the base.":
            $ M_Loss += 1
            call Select_5_Eng from _call_Select_5_Eng_2

#5nd Select
label Select_5:
    "{b}추가 재료{/b}는 뭘로 할까…."

    menu:
        #기억
        "레드 와인과 리큐르를 추가한다.":
            $ M_Memory += 1
            call Select_6 from _call_Select_6
        #진실
        "에스프레소와 과일 주스를 추가한다.": 
            $ M_Truth += 1
            call Select_6 from _call_Select_6_1
        #망각
        "진과 과일 주스를 추가한다.":
            $ M_Loss += 1
            call Select_6 from _call_Select_6_2

label Select_5_Eng:
    "What about {b}the extra ingredients{/b} for the cocktail?"

    menu:
        #기억
        "Add red wine and liqueur.":
            $ M_Memory += 1
            call Select_6_Eng from _call_Select_6_Eng
        #진실
        "Add espresso and fruit juice.": 
            $ M_Truth += 1
            call Select_6_Eng from _call_Select_6_Eng_1
        #망각
        "Add gin and fruit juice.":
            $ M_Loss += 1
            call Select_6_Eng from _call_Select_6_Eng_2

#3rd Select
label Select_6:
    "{b}마무리{/b}는…."

    menu:
        #망각
        "라임을 가니쉬로 사용한다.": 
            $ M_Loss += 1
            call Select_result_2 from _call_Select_result_2
        #기억
        "커피콩을 가니쉬로 사용한다.":
            $ M_Memory += 1
            call Select_result_2 from _call_Select_result_2_1
        #진실
        "계피 스틱을 가니쉬로 사용한다.":
            $ M_Truth += 1
            call Select_result_2 from _call_Select_result_2_2

label Select_6_Eng:
    "What about {b}Garnish{/b} for the cocktail?"

    menu:
        #망각
        "Use lime as garnish.": 
            $ M_Loss += 1
            call Select_result_2_Eng from _call_Select_result_2_Eng
        #기억
        "Use coffee beans as garnish.":
            $ M_Memory += 1
            call Select_result_2_Eng from _call_Select_result_2_Eng_1
        #진실
        "Use cinnamon sticks as garnish.":
            $ M_Truth += 1
            call Select_result_2_Eng from _call_Select_result_2_Eng_2

label Select_result_2:
    if M_Loss == 3:
        B "기억 상실, 한 잔 나왔습니다."
        M "감사합니다."
        M "…이번 주의 마무리도 이 한 잔이군요…."
        M "…앞으로 얼마나 더 마셔야할지…."
        M "…앞으로 얼마나 더 마실 수 있을지…."
        "남자가 작게 중얼거린다."
        "여자는 남자의 혼잣말을 듣지 못한 것 같다."

        call End_route from _call_End_route
    elif M_Memory == 3:
        B "남겨진 기억, 한 잔 나왔습니다."
        M "오…."
        M "다른 레시피가 있으신 줄은 몰랐습니다."
        M "이건 어쩐지…. 꼭 마셔야 할 것 같은 기분이 드는군요."

        call End_route from _call_End_route_1
    elif M_Truth == 3:
        B "쓰라린 진실, 한 잔 나왔습니다."
        M "오…."
        M "다른 레시피가 있으신 줄은 몰랐습니다."
        M "쓰라린 진실이라…."
        M "…."
        M "뭔가, 제게 암시하고 싶으신게 있으신가요?"
        B "하하, 글쎄요."
        F "칵테일 이름이 뭐 다 그렇지 않나요?"
        B "맞습니다. 의미가 있을 수도 있지만, 대체적으로는 어울리는 이름을 붙이는 편이죠."
        F "그러니까요."
        F "참, 칵테일 이름하니까 생각난게 있는데…."
        
        call End_route from _call_End_route_2
    else :
        jump Route_10

label Select_result_2_Eng:
    if M_Loss == 3:
        B "'Memory loss', here comes a drink."
        M "Thank you."
        M "…This is the end of the week, too…."
        M "…How much more do I have to drink…."
        M "…How much more can I drink…."
        "The man murmurs quietly"
        "The woman doesn't seem to have heard the man talk to himself"

        call End_route_Eng from _call_End_route_Eng
    elif M_Memory == 3:
        B "'Remain Memories'. Here's a drink."
        M "Oh…."
        M "I didn't know you had another recipe."
        M "This is something…. I feel like I must have to this drink."

        call End_route_Eng from _call_End_route_Eng_1
    elif M_Truth == 3:
        B "'Bitter Truth'. Here's a drink."
        M "Oh…."
        M "I didn't know you had another recipe."
        M "'Bitter Truth'…."
        M "…."
        M "Is there anything you want to imply to me?"
        B "Haha, I don't know."
        F "well, Isn't that the name of the many cocktail have not meaning? I think that just seem to some object or something…"
        B "That's right. It may mean something, but I tend to give it the matching name from object or something"
        F "HaHa, That's good."
        F "Oh, Speaking of cocktail names, I thought of this…."
        
        call End_route_Eng from _call_End_route_Eng_2
    else :
        jump Route_10_Eng

label End_route:
    if F_Truth == 3:
        if M_Truth == 3:
            jump Route_1
        elif M_Memory == 3:
            jump Route_2
        elif M_Loss == 3:
            jump Route_3
    elif F_Memory == 3:
        if M_Truth == 3:
            jump Route_4
        elif M_Memory == 3:
            jump Route_5
        elif M_Loss == 3:
            jump Route_6
    elif F_Loss == 3:
        if M_Truth == 3:
            jump Route_7
        elif M_Memory == 3:
            jump Route_8
        elif M_Loss == 3:
            jump Route_9

label End_route_Eng:
    if F_Truth == 3:
        if M_Truth == 3:
            jump Route_1_Eng
        elif M_Memory == 3:
            jump Route_2_Eng
        elif M_Loss == 3:
            jump Route_3_Eng
    elif F_Memory == 3:
        if M_Truth == 3:
            jump Route_4_Eng
        elif M_Memory == 3:
            jump Route_5_Eng
        elif M_Loss == 3:
            jump Route_6_Eng
    elif F_Loss == 3:
        if M_Truth == 3:
            jump Route_7_Eng
        elif M_Memory == 3:
            jump Route_8_Eng
        elif M_Loss == 3:
            jump Route_9_Eng

# F = Truth / M = Truth
label Route_1:
    "…" with dissolve
    "남자와 여자의 사이는 어느샌가 더 가까워진 것 같다."
    "여자는 남자가 마음에 든 듯, 적극적으로 그에게 관심을 표하고 있다."
    "남자 또한 여자에게 관심이 있는 것 같아 보인다."
    "두 사람은 시간가는 줄 모르고 이야기를 나눈다."
    "…" with dissolve
    F "정말요? 의외의 면도 가지고 있군요…."
    M "…당신 앞에서는 별 말도 다 하게 되는군요."
    M "이런 말을 남한테 할 줄은 몰랐는데…."
    F "와아, 나한테만 얘기한거에요? 기쁘네요."
    M "이런, 벌써 시간이…." with dissolve
    F "어머, 정말!"
    F "시간가는 줄도 몰랐군요…."
    M "저도 마찬가지입니다."
    F "솔직하게 말할게요, 난 당신이 마음에 들었어요."
    M "…여태까지 느낀거지만, 정말 당돌하군요…."
    M "…나도 마찬가지입니다."
    F "당신이랑 계속 연락하고 싶어요."
    F "이번 주는 이미 끝났고…."
    F "다음 주에 시간 있어요?" with dissolve
    F "이 근처에 괜찮은 레스토랑이 있는데…."
    F "술 말고 저녁 먹어요, 우리."
    M "…" with dissolve
    "남자는 잠깐 고민하더니, 작게 고개를 끄덕인다."
    M "좋습니다. 그렇게 하지요."
    F "좋아요!"
    F "연락처 알려줘요, 자세한 일정 잡게!"
    M "하하, 알겠습니다."
    hide M Default
    hide F Default
    with dissolve
    "…"
    play sound "SE_Japanese_furin.mp3" fadein 3
    "짤랑,하는 방울소리와 함께 문이 열린다."

    scene black with dissolve
    centered "{color=#ffffff}문 밖으로 발을 내딛는 순간….{/color}" with dissolve
    scene Background with dissolve

    "그들은, 무언가로 머리를 얻어맞은 듯한 충격에 빠진다." with dissolve
    "…" with dissolve

    show M Default at left
    show F Default at right
    with dissolve
    
    F "우리… 해야 할 이야기가 많은 것 같지…?"
    M "…."
    F "다음에 또 올게요, 오늘 좋은 술을 내어주셔서 감사합니다. 잘 마셨어요."
    B "그렇게 느끼셨다니 다행입니다."

    hide M Default
    hide F Default

    scene black with dissolve
    centered "{color=#ffffff}여자는 남자의 손을 이끌고 밖으로 나갔다.{/color}" with dissolve
    centered "{color=#ffffff}일주일 뒤, 두 사람은 다시 바에 찾아왔다.{/color}" with dissolve
    scene Background with dissolve
    
    show M Default at left
    show F Default at right
    with dissolve
    
    B "어서 오십시오."
    F "반가워요."
    F "…일주일 동안 정말 많은 대화를 나눴어요." with dissolve
    F "…우리의 앞으로에 대해서."
    B "그러셨군요."
    F "네, 정말 많은 고민을 했고…."
    F "최선의 방법을 찾은 듯 해, 당신에게 말해주러 왔어요."
    B "흠, 무엇이죠?"
    M "…우리. 우리는 서로만을 위해 함께 살기로 했습니다."
    B "흠…."
    B "그건 곤란하군요." with dissolve
    M "…네? 그게 무슨 말씀이신지…."
    B "내가 고작 이 따위 촌극이나 보기 위해 인과율을 거스르는 큰 힘을 사용한 줄 압니까?"
    B "나 원, 어이가 없어서…."
    F "대체 무슨 말씀을 하시는지…."
    #show 
    M "{size=35}{color=#ff0000}컥, 커억…!{/size}{/color}" with dissolve
    #
    F "{cps=20}{size=50}{color=ff0000}꺄아아악!{/cps}{/size}{/color}"
    F "이게 대체 무슨 짓이죠?!"
    B "물론, {b}{color=#0000ff}계약 조건{/b}{/color}을 이행하지 않은 채무자에게 정당한 권리를 행사하는 중이죠."
    B "제임스, 이번 선택은 정답이 아니었어."
    B "재미도 없고, 감동도 없었다고."
    B "다음에는 좀 더 현명한 선택을 하기 바라."
    
    scene black with dissolve
    centered "{color=#ffffff}바텐더와 남자가 서서히 사라져갔다.{/color}" with dissolve
    scene Background with dissolve

    show F Default
    F "이게 대체 무슨…"
    F "{size=45}바텐더 ! ! ! 제임스 ! ! !{/size}"
    F "{size=50}그이에게 대체 무슨 짓을 한거야 ! !{/size}"
    B "시끄럽게 굴긴, 공공장소에서 예의를 갖추세요."
    B "당신은 이따가 다시봅시다."
    
    hide F Default
    scene black with dissolve
    centered "{color=#ffffff}이것은, 불쌍한 남자의 이야기.{/color}" with dissolve
    scene Background with Fade(0.5,1,0.5,color="#ffffff")
    
    play sound "SE_Japanese_furin.mp3" fadein 3
    centered "{color=#ffffff}The Ouroboros, 라고 적힌 고즈넉한 바에 한 젊은 남자가 들어온다.{/color}" with dissolve
    show M Default with dissolve
    B "어서오십시오." with dissolve
    M "아무거나…." with dissolve
    M "아무거나 주십시오."
    B "…알겠습니다."
    "남자는 한참 동안이나 말 없이 술만 마셨다." with dissolve
    B "…무슨 일이 있으신가 봅니다?" with dissolve
    M "…." with dissolve
    M "10년전 오늘, 어머니가 자살하셨습니다."
    M "그러니까, 오늘이 기일이죠."
    B "아…. 죄송합니다."
    M "괜찮습니다. 별로 좋은 사람은 아니었으니까요."
    M "…오히려 최악이었죠."
    B "…. 실례가되지 않는다면, 어떤 분이셨는지 여쭤봐도 괜찮을까요?"
    M "물론이죠."
    M "…참 볼품없는 여자였습니다. 특별할 것도 없죠."
    M "…난 아버지가 없습니다."
    M "어머니 말로는, 저를 임신한 상태에서 갑자기 사라졌다더라고요. 흔적도 없이."
    M "…제가 기억하던 어머니는 처음부터 미친 여자였지만…." with dissolve
    M "주변 이야기를 들어보니, 원래는 살짝 조울증 증세가 있는, 평범한 여자였다고 합니다."
    M "그저 캐모마일 향이 나는 것은 무엇이든 병적으로 사 모은다는 점 빼고는…."
    M "딱히 특징적인 사람이 아니라고 하더군요."
    M "그러다, 어떤 남자를 만나고 나서부터 사람이 바뀌었답디다."
    M "캐모마일 향이 나는 멋진 남자라고…. 자랑을 하고 다닌 모양이에요."
    M "아마 그 사람이 제 아버지겠죠."
    M "…바에서 만난 인연으로, 결혼까지 했다더군요."
    M "결혼하고 얼마 뒤, 제가 생겼다고 해요."
    M "그리고 아버지가… 증발한거죠. 흔적도 없이."
    M "어머닌 임신한 몸으로 그 남자를 찾아다녔다고 합니다."
    M "주변에서 아무리 말려도, 미친듯 찾아다니다가…."
    M "제가 태어나니, 아버지 찾기를 멈췄다고 하더라고요."
    M "…처음엔 어머니 주변 분들도, 이제 어머니가 애를 낳고 마음을 다 잡은 줄 알았답니다." with dissolve
    M "그런데, 제 생후 4개월 째…."
    M "갑자기 미쳤다고 합니다."
    M "…문자 그대로, 사람이 미쳤다고…."
    M "갓난 아기였던 저를…."
    M "캐모마일 향유를 푼 욕조에 숨이 잠기도록 담구거나…."
    M "때리는 것은 예삿일이었죠."
    M "다행히도, 어머니 주변 분들이 어머니를 말려주셨습니다."
    M "…그러니 제가 살아있겠죠."
    M "뭐, 한 두번이 아니어서 문제였지만…."
    M "…결국, 제가 6살이 되는 해…." with dissolve
    M "외할머니가 돌아가시고 나서 부터는, 아무도 어머니를 말릴 수 없었습니다."
    M "…그 뒤, 10년 동안은 명확한 기억이 없습니다."
    M "제가 기억하는 거라고는…. 어머니에게 맞은 거나, 어머니가 그 빌어먹을 캐모마일이 엮인 물건을 사 모으는 것 밖에 없어요."
    M "…그것 마저도 지쳤는지, 제가 16살…. 중학교를 졸업하고 나서, 자살하셨습니다."
    M "남은 거라곤 캐모마일 향이 나는 물건들, 사망 보험금 말곤 없는 볼품없고 비루한 인생이었죠."
    B "…음, 오늘 이곳에 오신 이유가 있으신 것 같습니다만…."
    M "하…. 바텐더란 직업은 원래 다 그런가요? 귀신같이 알아차리시는 군요."
    B "하하, 아무래도 술 마시러 오시는 손님분들을 상대로 장사를 하다보니…."
    B "그래서, 얼추 맞았습니까?"
    M "…네. 맞습니다. 참 대단하시군요."
    M "…오늘, 마지막 술을 마시고 죽을 겁니다."
    M "다행히, 제가 참 술을 잘 마는 곳으로 골랐나 보군요."
    M "…술 상대 해주셔서 감사합니다."
    M "맛있게 잘 마셨습니다."
    B "흠…. 만약, 당신이 태어나기 전으로 돌아간다면 어떻게 하실 겁니까?"
    M "하하….술을 먹은건 전데, 왜 당신이 이상한 말을…."
    B "그래서 {b}만약{/b}이라고 하지 않았습니까?"
    B "만약 당신이 태어나기 전으로 돌아갈 기회가 있다면, 무엇을 하고 싶으십니까?"
    M "…."
    M "…어머니를,"
    M "{color=#ff0000}어머니를, 죽일겁니다.{/color}"
    B "흠…. 그렇군요, 잘 알겠습니다."
    M "대체 뭘 알겠다는 건지…."
    B "지금부터, 당신을 30년 전으로 보내드리겠습니다."
    B "그 시간 선에 당신이 머무룰 수 있는 시간은 3년."
    B "3년동안 원하는 바를 이뤄보실 수 있도록…."
    B "어떻습니까?"
    M "하, 아니… 대체 무슨…."
    B "어차피 죽을 것이라고 하지 않으셨습니까?"
    B "허황된 거짓말 같아도, 한 번 속아 넘어간다고 해서 손해볼 것도 없으시지 않나요?"
    M "하…. 맞긴 하군요."
    M "내가 참, 별…."
    B "아, 만약 당신의 어머니가 당신이 원하는 바를 이루기 전에 아이를 갖게 된다면…."
    B "3년이라는 시간은 무의미해질 겁니다."
    B "당신이란 존재가, 존재하지 않게 되는 것이니까요."
    B "그러니, 서둘러서 원하는 바룰 이루도록 하세요."
    M "…내가 치뤄야 할 대가는?"
    B "매주 일요일, 이곳에 와서 당신에게 어떤 일이 있었는지, 제게 당신의 이야기를 들려주시면 됩니다."
    B "어때요, 간단하죠?"
    M "…좋습니다. 까짓거, 한 번 속아보죠."

    hide M Default
    scene black with dissolve
    centered "{color=#ffffff}자고 일어나면 과거로 돌아가 있을겁니다.{/color}" with dissolve
    centered "{color=#ffffff}그럼, 일요일에 뵙지요.{/color}" with dissolve

    jump END_1

label Route_1_Eng:
    "…" with dissolve
    "The relationship between men and women seems to have gotten closer before I knew it."
    "The woman is actively showing interest in the man"
    "Man also seem to be interested in women."
    "The two talk without knowing the time is passing."
    "…" with dissolve
    F "Really? You have an unexpected side"
    M "…I end up saying everything in front of you."
    M "I didn't know I'd say this to others…."
    F "Wow, did you talk to only me? that's sound good."
    M "Oh, The time is already…." with dissolve
    F "Really?"
    F "I lost track of time…."
    M "I am the same"
    F "I'll be honest, I liked you."
    M "…I've been feeling this way, but yor're very bold…."
    M "…I'm.. Same here."
    F "I want to keep in touch with you."
    F "This week is already over…."
    F "Are you free next week?" with dissolve
    F "There is a good restaurant near here…."
    F "Let's have dinner instead of drinking."
    M "…" with dissolve
    "The man agonizes for a moment, then nods a little."
    M "Okay.. I'll do that."
    F "Good!"
    F "Tell me your contact information, and I'll make a detailed schedule!"
    M "Haha, I see."
    hide M Default
    hide F Default
    with dissolve
    "…"
    play sound "SE_Japanese_furin.mp3" fadein 3
    "The door opens with a bell sound."

    scene black with dissolve
    centered "{color=#ffffff}The moment that As soon as They stepped out of the door….{/color}" with dissolve
    scene Background with dissolve

    "They are in shock, as if they were hit on the head by something." with dissolve
    "…" with dissolve

    show M Default at left
    show F Default at right
    with dissolve
    
    F "I think we have a lot to talk about…?"
    M "…."
    F "I'll come back again, thank you for offering me a good drink today. I drank it well"
    B "I'm glad you felt that way"

    hide M Default
    hide F Default

    scene black with dissolve
    centered "{color=#ffffff}The woman led the man's hand outside.{/color}" with dissolve
    centered "{color=#ffffff}A week later, the two visited the bar again.{/color}" with dissolve
    scene Background with dissolve
    
    show M Default at left
    show F Default at right
    with dissolve
    
    B "Welcome."
    F "Nice to meet you."
    F "…We've had a lot of conversations over the course of the week." with dissolve
    F "…About our future."
    B "I see."
    F "Yes, I've been thinking a lot…."
    F "I think I found the best way, I'm here to tell you."
    B "Well, what is it?"
    M "…We. We decided to live together just for each other"
    B "…."
    B "That's impossible." with dissolve
    M "…What? What do you mean…."
    B "Do you think I've used a great force against causality just to see a play like this poor skit?"
    B "I'm speechless…."
    F "What the hell are you talking about…."
    #show 
    M "{size=35}{color=#ff0000}…!{/size}{/color}" with dissolve
    "The man is strangled."
    F "{cps=20}{size=50}{color=ff0000}ughhhhhhhhhhh! ! *Screaming*{/cps}{/size}{/color}"
    F "What the hell are you doing?!"
    B "Of course, I'm exercising legitimate rights to debtors who don't fulfill {b}{color=#0000ff}the terms of the contract{/b}{/color}."
    B "James, this choice wasn't the answer."
    B "It wasn't funny, it wasn't touching."
    B "Next time, I hope you make a smarter choice."
    
    scene black with dissolve
    centered "{color=#ffffff}The bartender and the man slowly disappeared.{/color}" with dissolve
    scene Background with dissolve

    show F Default
    F "What the hell is this"
    F "{size=45}Hey ! ! ! James ! ! !{/size}"
    F "{size=50}What the hell did you do to him ! !{/size}"
    B "Noisy, be polite."
    B "See you later."
    
    hide F Default
    scene black with dissolve
    centered "{color=#ffffff}This is the story of a poor man.{/color}" with dissolve
    scene Background with Fade(0.5,1,0.5,color="#ffffff")
    
    play sound "SE_Japanese_furin.mp3" fadein 3
    centered "{color=#ffffff}A young man walks into a quiet bar 'The Ouroboros.'{/color}" with dissolve
    show M Default with dissolve
    B "Welcome." with dissolve
    M "Anything…." with dissolve
    M "Anything, please."
    B "…I see."
    "The man drank for a long time without saying a word." with dissolve
    B "…What's going on?" with dissolve
    M "…." with dissolve
    M "10 years ago today, my mother killed herself."
    M "So, today is the anniversary."
    B "Oh…. I'm sorry."
    M "That's all right. she wasn't a good person."
    M "…She was rather the worst."
    B "…. If you don't mind, may I ask what kind of person she was?"
    M "Of course.."
    M "…She hasn't anyting. It's nothing special."
    M "…I don't have a father."
    M "My mother said, she was pregnant and suddenly disappeared. without a trace."
    M "…My mother, who I remember, was a crazy woman from the beginning…." with dissolve
    M "I heard that she was a normal woman who had a slight bipolar disorder."
    M "Except she buy anything that smells like chamomile morbidly…."
    M "They say she's not exactly a characteristic person."
    M "Then, she was changed since she met a guy."
    M "He's a cool guy who smells like chamomile…. she bragged about it."
    M "Maybe he's my father."
    M "…she met him at a bar and got married. That's all."
    M "Some time after she got married, she was pregnant. That's me."
    M "And my father... It evaporated. Without a trace."
    M "My mother was looking for him"
    M "No matter how hard another try to stop her, she's been looking for him like crazy…."
    M "When I was born, she stopped looking for my father."
    M "…At first, the people around her thought she had a baby and made up her mind." with dissolve
    M "By the way, 4 months after I was born…."
    M "They says, she was suddenly crazy."
    M "…Literally, crazy…."
    M "I was a baby…."
    M "she soak to me  in a tub filled with chamomile oil…."
    M "Hitting is nothing special…."
    M "Fortunately, people around her stopped her."
    M "…So I'm alive"
    M "Well, it wasn't once or twice, so it was a problem…."
    M "…In the end, the year I was 6 year old…." with dissolve
    M "Since my grandmother died, no one could stop her"
    M "…After that, I don't have a clear memory for 10 years."
    M "All I remember is.... All I was to do is get hit by mother. And she buy and collect the damn chamomile weave."
    M "…I guess she was tired of that. When I'm 16 years old.. After graduating from middle school, she committed suicide"
    M "All that was left was chamomile-scented items, an ugly, shabby life that had nothing but death insurance."
    B "…Well, I think there's a reason you're here today…."
    M "Ha…. Is other bartenders is like you? You seem to have six sense."
    B "Haha, well.. since I'm doing business with customers who come to drink…."
    B "So, did I almost get it right?"
    M "……Yes, that's right. That's amazing.."
    M "…Today, I'm gonna die after my last drink."
    M "Fortunately, I guess I chose this place where make drink very well."
    M "…Thank you for talk with me."
    M "Thank you for the drink."
    B "Hmm…. What would you do if you went back to before you were born?"
    M "Ha ha…. I'm the one who drank, but why did you say something weird…?"
    B "So, {b}'If'{/b} Didn't I say?"
    B "If you had a chance to go back before you was born, what would you do"
    M "…."
    M "…Mother,"
    M "{color=#ff0000}I'm going to kill my mother.{/color}"
    B "Hmm…. I see, I see."
    M "What do you know…."
    B "From now on, I'll send you back 30 years."
    B "The time you can stay in that time line is 3 years."
    B "I hope you can achieve what you want for 3 years…."
    B "What do you think?"
    M "Ha…. What in the world…."
    B "Didn't you say you were going to die anyway?"
    B "Even if it's a lie, isn't there anything to lose by being fooled?"
    M "Ha…. That's true."
    M "What's this…."
    B "Oh, if your mother has a child before you can achieve what you want…."
    B "3 years will be meaningless."
    B "When The Future is changed, then you don't exist."
    B "So, hurry up and Achieve what you want."
    M "…What do I have to pay?"
    B "Every Sunday, you should come here and tell me your story about what happened to you."
    B "It's simple, right?"
    M "…O,kay. I trust you just once."

    hide M Default
    scene black with dissolve
    centered "{color=#ffffff}When you wake up, you'll go back to the past.{/color}" with dissolve
    centered "{color=#ffffff}Well, See you on Sunday.{/color}" with dissolve

    jump END_1_Eng

label END_1:

    centered "{color=#ffffff}이것은, 악마에게 속아넘어간 남자의 돌고 도는 이야기….{/color}" with dissolve

    call screen ED1 with dissolve

screen ED1:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("ED01. 진실")

        textbutton "타이틀로 돌아가기" action MainMenu(confirm=False)

label END_1_Eng:

    centered "{color=#ffffff}This is a repeated story of a man who was deceived by a demon….{/color}" with dissolve

    call screen ED1_Eng with dissolve

screen ED1_Eng:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("ED01. Truth")

        textbutton "Return to Title" action MainMenu(confirm=False)

# F = Truth / M = Memory
label Route_2:
    "…" with dissolve
    "남자와 여자의 사이는 어느샌가 더 가까워진 것 같다."
    "여자는 남자가 마음에 든 듯, 적극적으로 그에게 관심을 표하고 있다."
    "남자 또한 여자에게 관심이 있는 것 같아 보인다."
    "두 사람은 시간가는 줄 모르고 이야기를 나눈다."
    "…" with dissolve
    F "정말요? 의외의 면도 가지고 있군요…."
    M "…당신 앞에서는 별 말도 다 하게 되는군요."
    M "이런 말을 남한테 할 줄은 몰랐는데…."
    F "와아, 나한테만 얘기한거에요? 기쁘네요."
    M "이런, 벌써 시간이…." with dissolve
    F "어머, 정말!"
    F "시간가는 줄도 몰랐군요…."
    M "저도 마찬가지입니다."
    F "솔직하게 말할게요, 난 당신이 마음에 들었어요."
    M "…여태까지 느낀거지만, 정말 당돌하군요…."
    M "…나도 마찬가지입니다."
    F "당신이랑 계속 연락하고 싶어요."
    F "이번 주는 이미 끝났고…."
    F "다음 주에 시간 있어요?" with dissolve
    F "이 근처에 괜찮은 레스토랑이 있는데…."
    F "술 말고 저녁 먹어요, 우리."
    M "…" with dissolve
    "남자는 잠깐 고민하더니, 작게 고개를 끄덕인다."
    M "좋습니다. 그렇게 하지요."
    F "좋아요!"
    F "연락처 알려줘요, 자세한 일정 잡게!"
    M "하하, 알겠습니다."
    hide M Default
    hide F Default
    with dissolve
    "…"
    play sound "SE_Japanese_furin.mp3" fadein 3
    "짤랑,하는 방울소리와 함께 문이 열린다."

    scene black with dissolve
    centered "{color=#ffffff}문 밖으로 발을 내딛는 순간….{/color}" with dissolve
    scene Background with dissolve

    "그들은, 무언가로 머리를 얻어맞은 듯한 충격에 빠진다." with dissolve
    "…" with dissolve

    show M Default at left
    show F Default at right
    with dissolve
    
    "남자는 분노에 찬 표정으로 여자를 바라본다."
    M "당신…."
    F "아니…."
    F "아니야…! !"
    
    hide M Default
    hide F Default

    scene black with dissolve
    centered "{color=#ffffff}남자는 여자에게 달려들어 여자의 목을 조르기 시작했다.{/color}" with dissolve
    centered "{size=50}{color=#0000ff}죽어…!{/color}{/size}" with dissolve
    centered "{size=30}{color=#ff0000}커헉…! 컥, 이… 이거 놔…!{/color}{/size}" with dissolve
    centered "{size=50}{color=#0000ff}죽어 ! {/size}{size=60}{/color}{color=#0000ff}죽어 ! !{/size}{/color}" with dissolve
    centered "{color=#ffffff}여자는 남자에게 목이 졸린 채 버둥거리다가, 이내 저항을 포기했다.{/color}" with dissolve
    centered "{color=#ff0000}미, 커헉…. 미안해요, 짐…{/color}" with dissolve
    centered "{color=#ffffff}여자는 이내 숨을 거뒀고, 남자의 몸이 부숴지기 시작했다.{/color}" with dissolve
    centered "{color=#ffffff}남자는 여자의 말에 놀라 손에서 힘을 풀었다.{/color}" with dissolve
    centered "{color=#ffffff}이어서, 자신의 몸이 부숴지고 있다는 것을 알아차렸다.{/color}" with dissolve
    centered "{color=#0000ff}대체 왜 내게? 아니, 이게 무슨…{/color}" with dissolve
    centered "{color=#ffffff}남자는 혼란스러워 보인다.{/color}" with dissolve
    centered "{color=#0000ff}설마, 당신이…{/color}" with dissolve
    centered "{color=#ffffff}남자는 혼돈과 경악에 가득 찬 얼굴로 이쪽을 바라보다가 카운터로 달려들었다.{/color}" with dissolve
    centered "{color=#ffffff}남자의 몸이 카운터에 거의 당도했을 때, 남자는 이미 흔적도 없이 사라져 있었다.{/color}" with dissolve
    scene black with dissolve

    jump END_2

label Route_2_Eng:
    "…" with dissolve
    "The relationship between men and women seems to have gotten closer before I knew it."
    "The woman is actively showing interest in the man"
    "Man also seem to be interested in women."
    "The two talk without knowing the time is passing."
    "…" with dissolve
    F "Really? You have an unexpected side"
    M "…I end up saying everything in front of you."
    M "I didn't know I'd say this to others…."
    F "Wow, did you talk to only me? that's sound good."
    M "Oh, The time is already…." with dissolve
    F "Really?"
    F "I lost track of time…."
    M "I am the same"
    F "I'll be honest, I liked you."
    M "…I've been feeling this way, but yor're very bold…."
    M "…I'm.. Same here."
    F "I want to keep in touch with you."
    F "This week is already over…."
    F "Are you free next week?" with dissolve
    F "There is a good restaurant near here…."
    F "Let's have dinner instead of drinking."
    M "…" with dissolve
    "The man agonizes for a moment, then nods a little."
    M "Okay.. I'll do that."
    F "Good!"
    F "Tell me your contact information, and I'll make a detailed schedule!"
    M "Haha, I see."
    hide M Default
    hide F Default
    with dissolve
    "…"
    play sound "SE_Japanese_furin.mp3" fadein 3
    "The door opens with a bell sound."

    scene black with dissolve
    centered "{color=#ffffff}The moment that As soon as They stepped out of the door….{/color}" with dissolve
    scene Background with dissolve

    "They are in shock, as if they were hit on the head by something." with dissolve
    "…" with dissolve

    show M Default at left
    show F Default at right
    with dissolve
    
    "The man looks at the woman with an angry look on his face."
    M "You…."
    F "No…."
    F "Listen…! !"
    
    hide M Default
    hide F Default

    scene black with dissolve
    centered "{color=#ffffff}The man jumped at the woman and began to strangle her{/color}" with dissolve
    centered "{size=50}{color=#0000ff}Die…!{/color}{/size}" with dissolve
    centered "{size=30}{color=#ff0000}koff…! kof, Le.. let go of this…!{/color}{/size}" with dissolve
    centered "{size=50}{color=#0000ff}Die ! !{/size}{size=60}{/color}{color=#0000ff}Die ! !{/size}{/color}" with dissolve
    centered "{color=#ffffff}The woman struggled with a man stranging her, and soon gave up resistance.{/color}" with dissolve
    centered "{color=#ff0000}S, koff…. Sorry, Jim…{/color}" with dissolve
    centered "{color=#ffffff}The woman soon died, and the man's body began to break.{/color}" with dissolve
    centered "{color=#ffffff}The man was surprised by the woman's words and relaxed his hand.{/color}" with dissolve
    centered "{color=#ffffff}Subsequently, he noticed that his body was breaking.{/color}" with dissolve
    centered "{color=#0000ff}Why are you apologizing to me? No, what is this…{/color}" with dissolve
    centered "{color=#ffffff}The man looks confused.{/color}" with dissolve
    centered "{color=#0000ff}Don't tell me what…{/color}" with dissolve
    centered "{color=#0000ff}You lied to me.…{/color}" with dissolve
    centered "{color=#ffffff}The man looked this way with a face full of confusion and astonishment and rushed to the counter.{/color}" with dissolve
    centered "{color=#ffffff}When the man's body almost reached the counter, he had already disappeared without a trace.{/color}" with dissolve
    scene black with dissolve

    jump END_2_Eng
    
label END_2:
    call screen ED2 with dissolve

screen ED2:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("ED02. 업보")
        textbutton "타이틀로 돌아가기" action MainMenu(confirm=False)

label END_2_Eng:
    call screen ED2_Eng with dissolve

screen ED2_Eng:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("ED02. karma")
        textbutton "Return to Title" action MainMenu(confirm=False)

# F = Truth / M = Loss
label Route_3:
    "…" with dissolve
    "남자와 여자의 사이는 어느샌가 더 가까워진 것 같다."
    "여자는 남자가 마음에 든 듯, 적극적으로 그에게 관심을 표하고 있다."
    "남자 또한 여자에게 관심이 있는 것 같아 보인다."
    "두 사람은 시간가는 줄 모르고 이야기를 나눈다."
    "…" with dissolve
    F "정말요? 의외의 면도 가지고 있군요…."
    M "…당신 앞에서는 별 말도 다 하게 되는군요."
    M "이런 말을 남한테 할 줄은 몰랐는데…."
    F "와아, 나한테만 얘기한거에요? 기쁘네요."
    M "이런, 벌써 시간이…." with dissolve
    F "어머, 정말!"
    F "시간가는 줄도 몰랐군요…."
    M "저도 마찬가지입니다."
    F "솔직하게 말할게요, 난 당신이 마음에 들었어요."
    M "…여태까지 느낀거지만, 정말 당돌하군요…."
    M "…나도 마찬가지입니다."
    F "당신이랑 계속 연락하고 싶어요."
    F "이번 주는 이미 끝났고…."
    F "다음 주에 시간 있어요?" with dissolve
    F "이 근처에 괜찮은 레스토랑이 있는데…."
    F "술 말고 저녁 먹어요, 우리."
    M "…" with dissolve
    "남자는 잠깐 고민하더니, 작게 고개를 끄덕인다."
    M "좋습니다. 그렇게 하지요."
    F "좋아요!"
    F "연락처 알려줘요, 자세한 일정 잡게!"
    M "하하, 알겠습니다."
    hide M Default
    hide F Default
    with dissolve
    "…"
    play sound "SE_Japanese_furin.mp3" fadein 3
    "짤랑,하는 방울소리와 함께 문이 열린다."

    scene black with dissolve
    centered "{color=#ffffff}여자가 문 밖으로 발을 내딛는 순간….{/color}" with dissolve
    scene Background with dissolve

    "여자는, 무언가로 머리를 얻어맞은 듯한 충격에 빠진다." with dissolve
    "…"

    show F Default with dissolve
    F "…흑, 으흑…." with dissolve
    "여자는 갑자기 남자를 보며 울음을 쏟아낸다."
    hide F Default
    show M Default at left
    show F Default at right
    with dissolve
    M "왜… 왜 저를 보며 우시는거죠?" with dissolve
    F "아아…. 어째서…."
    F "우리는 대체 왜…."
    M "어…. 우, 울지 마십시오…." with dissolve
    "여자는 슬픔에 겨워, 문을 가로막고 주저앉았다."
    "남자는 여자를 한참동안 위로했다."
    F "…죄송합니다. 추태를 부렸네요…." with dissolve
    F "위로 감사합니다…. 도움이 많이 됐어요…."

    hide F Default
    hide M Default
    scene black with dissolve
    centered "{color=#ffffff}그리고 그녀는 홀연히 떠났다.{/color}" with dissolve
    centered "{color=#ffffff}한달 후 화요일, 그녀가 다시 찾아왔다.{/color}" with dissolve
    scene Background with dissolve
    
    show F Default with dissolve
    F "그이는…. 자주… 오나요…?" with dissolve
    B "…네. 매주 일요일마다 오십니다."
    F "…내 얘길… 하던가요?"
    B "…가끔 하셨습니다."
    F "그이가 나를 잊은건…."
    "여자가 물끄럼히 쳐다본다."
    F "그 음료…."
    B "…. 맞습니다."
    "여자가 허탈하게 웃는다."
    F "…." with dissolve
    F "내가 죽으면…."
    F "나만 죽으면 이 모든게 해결이 될까요?"
    B "…." with dissolve
    F "나만 없으면…. 그이가 더는 고통받지 않을까요…?"
    B "글쎄요, 잘 모르겠습니다."

    play sound "SE_Japanese_furin.mp3" fadein 3
    scene black with dissolve
    centered "{color=#ffffff}여자는 말없이 앉아있다가, 들어주셔서 감사하다는 말과 함께 바에서 떠났다.{/color}" with dissolve
    centered "{color=#ffffff}그리고, 다시는 찾아오지 않았다.{/color}" with dissolve

    jump END_3

label Route_3_Eng:
    "…" with dissolve
    "The relationship between men and women seems to have gotten closer before I knew it."
    "The woman is actively showing interest in the man"
    "Man also seem to be interested in women."
    "The two talk without knowing the time is passing."
    "…" with dissolve
    F "Really? You have an unexpected side"
    M "…I end up saying everything in front of you."
    M "I didn't know I'd say this to others…."
    F "Wow, did you talk to only me? that's sound good."
    M "Oh, The time is already…." with dissolve
    F "Really?"
    F "I lost track of time…."
    M "I am the same"
    F "I'll be honest, I liked you."
    M "…I've been feeling this way, but yor're very bold…."
    M "…I'm.. Same here."
    F "I want to keep in touch with you."
    F "This week is already over…."
    F "Are you free next week?" with dissolve
    F "There is a good restaurant near here…."
    F "Let's have dinner instead of drinking."
    M "…" with dissolve
    "The man agonizes for a moment, then nods a little."
    M "Okay.. I'll do that."
    F "Good!"
    F "Tell me your contact information, and I'll make a detailed schedule!"
    M "Haha, I see."
    hide M Default
    hide F Default
    with dissolve
    "…"
    play sound "SE_Japanese_furin.mp3" fadein 3
    "The door opens with a bell sound."

    scene black with dissolve
    centered "{color=#ffffff}The moment that As soon as They stepped out of the door….{/color}" with dissolve
    scene Background with dissolve

    "She has in shock, as if they were hit on the head by something." with dissolve
    "…" with dissolve

    show F Default with dissolve
    F "…Ha, It'.. What the…." with dissolve
    "The woman suddenly cries at the man."
    hide F Default
    show M Default at left
    show F Default at right
    with dissolve
    M "Why… Why are you crying at me?" with dissolve
    F "Ahhh…. How come…."
    F "Why are we…."
    M "Uh…. Ooh, don't cry…." with dissolve
    "She was so sad that she stood in the door and sat down."
    "The man comforted the woman for a long time."
    F "…I'm sorry. I made a fool of myself…." with dissolve
    F "Thank you for your consolation…. It helped me a lot…."

    hide F Default
    hide M Default
    scene black with dissolve
    centered "{color=#ffffff}And she left suddenly.{/color}" with dissolve
    centered "{color=#ffffff}A month later on Tuesday, she came back.{/color}" with dissolve
    scene Background with dissolve
    
    show F Default with dissolve
    F "He…. How he often… coming?" with dissolve
    B "…Yes, he comes every Sunday."
    F "…Did he tell you about me?"
    B "…He tell about you from time to me."
    F "That time, He forgot about me…."
    "The woman glances at me."
    F "That drink…."
    B "Hmm, That's right."
    "The woman laughs dejectedly."
    F "…." with dissolve
    F "If I die…."
    F "If I die, will all this work out?"
    B "…." with dissolve
    F "If Without me…. Won't he suffer any more…?"
    B "Well, I don't know."

    play sound "SE_Japanese_furin.mp3" fadein 3
    scene black with dissolve
    centered "{color=#ffffff}The woman sat silent and left the bar with thanks for listening.{/color}" with dissolve
    centered "{color=#ffffff}And she never came back.{/color}" with dissolve

    jump END_3_Eng

label END_3:
    call screen ED3 with dissolve

screen ED3:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("ED03. 체념")
        textbutton "타이틀로 돌아가기" action MainMenu(confirm=False)

label END_3_Eng:
    call screen ED3_Eng with dissolve

screen ED3_Eng:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("ED03. Resignation")
        textbutton "Return to Title" action MainMenu(confirm=False)

# F = Memory / M = Truth
label Route_4:
    "…" with dissolve
    "남자와 여자의 사이는 어느샌가 더 가까워진 것 같다."
    "여자는 남자가 마음에 든 듯, 적극적으로 그에게 관심을 표하고 있다."
    "남자 또한 여자에게 관심이 있는 것 같아 보인다."
    "두 사람은 시간가는 줄 모르고 이야기를 나눈다."
    "…" with dissolve
    F "정말요? 의외의 면도 가지고 있군요…."
    M "…당신 앞에서는 별 말도 다 하게 되는군요."
    M "이런 말을 남한테 할 줄은 몰랐는데…."
    F "와아, 나한테만 얘기한거에요? 기쁘네요."
    M "이런, 벌써 시간이…." with dissolve
    F "어머, 정말!"
    F "시간가는 줄도 몰랐군요…."
    M "저도 마찬가지입니다."
    F "솔직하게 말할게요, 난 당신이 마음에 들었어요."
    M "…여태까지 느낀거지만, 정말 당돌하군요…."
    M "…나도 마찬가지입니다."
    F "당신이랑 계속 연락하고 싶어요."
    F "이번 주는 이미 끝났고…."
    F "다음 주에 시간 있어요?" with dissolve
    F "이 근처에 괜찮은 레스토랑이 있는데…."
    F "술 말고 저녁 먹어요, 우리."
    M "…" with dissolve
    "남자는 잠깐 고민하더니, 작게 고개를 끄덕인다."
    M "좋습니다. 그렇게 하지요."
    F "좋아요!"
    F "연락처 알려줘요, 자세한 일정 잡게!"
    M "하하, 알겠습니다."
    hide M Default
    hide F Default
    with dissolve
    "…"
    play sound "SE_Japanese_furin.mp3" fadein 3
    "짤랑,하는 방울소리와 함께 문이 열린다."

    scene black with dissolve
    centered "{color=#ffffff}여자가 문 밖으로 발을 내딛는 순간….{/color}" with dissolve
    scene Background with dissolve

    "그들은, 무언가로 머리를 얻어맞은 듯한 충격에 빠진다." with dissolve
    "…"

    show F Default with vpunch
    F "{size=60}{cps=20}{color=#FF0000}{b}꺄 아 아 아 아 아 아 아 악 ! ! ! !{/b}{/color}{/cps}{/size}" with dissolve
    F "{size=50}{color=#FF0000}싫어! ! 살려주세요 ! !{/size}{/color}"
    hide F Default
    show M Default with dissolve
    M "아… 아니…." with dissolve
    "여자는 비명을 지르며 바에서 도망쳤다." with dissolve
    "남자는 여자가 떠난 자리를 망연하게 쳐다보았다."
    M "…가버렸군요." with dissolve
    M "나는…."
    M "나는 어떡해야 하죠…?"
    M "이제 앞으로 뭘 해야…."
    B "어렵게 생각하실 필요 없습니다."
    B "제임스씨가 어떤 선택을 하시던, 그것이 옳은 선택일 테니까요."
    M "제… 선택이요."
    M "…."
    M "…이대로 떠나겠습니다." with dissolve
    B "흠? 후회 안 하시겠습니까?"
    M "…지금의 그녀에게 사죄건, 무엇이건…."
    M "무엇이든, 제가 그녀를 만난다는 것 자체가… 그녀에겐…."
    M "기껏 도와주셨는데, 죄송합니다."
    M "바텐더씨, 지금까지 감사했습니다."
    M "오늘이 마지막이겠군요."
    M "안녕히 계십시오."
    B "흠…. 네, 기회가 되면 또 뵙죠."
    B "안녕히 가시길."

    play sound "SE_Japanese_furin.mp3" fadein 3
    scene black with dissolve
    centered "{color=#ffffff}남자는 그대로 나가, 다시 돌아오지 않았다.{/color}" with dissolve

    jump END_4
    
label Route_4_Eng:
    "…" with dissolve
    "The relationship between men and women seems to have gotten closer before I knew it."
    "The woman is actively showing interest in the man"
    "Man also seem to be interested in women."
    "The two talk without knowing the time is passing."
    "…" with dissolve
    F "Really? You have an unexpected side"
    M "…I end up saying everything in front of you."
    M "I didn't know I'd say this to others…."
    F "Wow, did you talk to only me? that's sound good."
    M "Oh, The time is already…." with dissolve
    F "Really?"
    F "I lost track of time…."
    M "I am the same"
    F "I'll be honest, I liked you."
    M "…I've been feeling this way, but yor're very bold…."
    M "…I'm.. Same here."
    F "I want to keep in touch with you."
    F "This week is already over…."
    F "Are you free next week?" with dissolve
    F "There is a good restaurant near here…."
    F "Let's have dinner instead of drinking."
    M "…" with dissolve
    "The man agonizes for a moment, then nods a little."
    M "Okay.. I'll do that."
    F "Good!"
    F "Tell me your contact information, and I'll make a detailed schedule!"
    M "Haha, I see."
    hide M Default
    hide F Default
    with dissolve
    "…"
    play sound "SE_Japanese_furin.mp3" fadein 3
    "The door opens with a bell sound."

    scene black with dissolve
    centered "{color=#ffffff}The moment that As soon as They stepped out of the door….{/color}" with dissolve
    scene Background with dissolve

    "They has in shock, as if they were hit on the head by something." with dissolve
    "…" with dissolve

    show F Default with vpunch
    F "{size=60}{cps=20}{color=#FF0000}{b}U g h h h h h h h h h h h ! ! ! !{/b}{/color}{/cps}{/size}" with dissolve
    F "{size=50}{color=#FF0000}NO ! ! HELP ME ! !{/size}{/color}"
    hide F Default
    show M Default with dissolve
    M "…." with dissolve
    "The woman screamed and ran away from the bar." with dissolve
    "The man stared vacantly at the place where the woman had left."
    M "…She's gone." with dissolve
    M "What…."
    M "What should I do…?"
    M "I don't know what to do…."
    B "You don't have to think too hard."
    B "Whatever you choose, it'll be the right choice"
    M "My… choice."
    M "…."
    M "…I'll leave her." with dissolve
    B "Hmm? You won't regret it?"
    M "…Apologize to her now, or whatever…."
    M "Whatever it is, the fact that I'm meeting her…."
    M "I'm sorry you helped me at the most."
    M "Mr. Bartender, thank you so far."
    M "Today must be the last day."
    M "Good bye."
    B "Hmm…. Yes, I'll see you again when I get a chance."
    B "Good bye."

    play sound "SE_Japanese_furin.mp3" fadein 3
    scene black with dissolve
    centered "{color=#ffffff}The man left, never to return.{/color}" with dissolve

    jump END_4_Eng

label END_4:
    call screen ED4 with dissolve

label END_4_Eng:
    call screen ED4_Eng with dissolve

screen ED4:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("ED04. 포기")
        textbutton "타이틀로 돌아가기" action MainMenu(confirm=False)

screen ED4_Eng:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("ED04. give up")
        textbutton "Return to Title" action MainMenu(confirm=False)

# F = Memory / M = Memory
label Route_5:
    "…" with dissolve
    "남자와 여자의 사이는 어느샌가 더 가까워진 것 같다."
    "여자는 남자가 마음에 든 듯, 적극적으로 그에게 관심을 표하고 있다."
    "남자 또한 여자에게 관심이 있는 것 같아 보인다."
    "두 사람은 시간가는 줄 모르고 이야기를 나눈다."
    "…" with dissolve
    F "정말요? 의외의 면도 가지고 있군요…."
    M "…당신 앞에서는 별 말도 다 하게 되는군요."
    M "이런 말을 남한테 할 줄은 몰랐는데…."
    F "와아, 나한테만 얘기한거에요? 기쁘네요."
    M "이런, 벌써 시간이…." with dissolve
    F "어머, 정말!"
    F "시간가는 줄도 몰랐군요…."
    M "저도 마찬가지입니다."
    F "솔직하게 말할게요, 난 당신이 마음에 들었어요."
    M "…여태까지 느낀거지만, 정말 당돌하군요…."
    M "…나도 마찬가지입니다."
    F "당신이랑 계속 연락하고 싶어요."
    F "이번 주는 이미 끝났고…."
    F "다음 주에 시간 있어요?" with dissolve
    F "이 근처에 괜찮은 레스토랑이 있는데…."
    F "술 말고 저녁 먹어요, 우리."
    M "…" with dissolve
    "남자는 잠깐 고민하더니, 작게 고개를 끄덕인다."
    M "좋습니다. 그렇게 하지요."
    F "좋아요!"
    F "연락처 알려줘요, 자세한 일정 잡게!"
    M "하하, 알겠습니다."
    hide M Default
    hide F Default
    with dissolve
    "…"
    play sound "SE_Japanese_furin.mp3" fadein 3
    "짤랑,하는 방울소리와 함께 문이 열린다."

    scene black with dissolve
    
    centered "{color=#ffffff}문 밖으로 발을 내딛는 순간….{/color}" with dissolve
    scene Background with dissolve

    "그들은, 무언가로 머리를 얻어맞은 듯한 충격에 빠진다." with dissolve
    "…" with dissolve

    show M Default at left
    show F Default at right
    with dissolve
    
    "남자는 분노에 찬 표정으로 여자를 바라본다."
    M "당신…."
    F "{size=50}{color=#ff0000}{cps=20}꺄 아 아 악 !{/color}{/cps}{/size}" with dissolve
    
    scene black with dissolve
    centered "{color=#ffffff}남자는 도망가려는 여자의 팔을 우악스럽게 잡아채, 넘어뜨린다.{/color}" with dissolve
    centered "{color=#ffffff}비명을 지르며 넘어진 여자를 잡아채 가게 안 쪽으로 던졌다.{/color}" with dissolve
    scene Background with dissolve

    M "{size=50}{color=#ff0000}{cps=20}X발, 뒤져! 뒤지라고! ! ! !{/color}{/cps}{/size}" with dissolve
    M "{size=50}{color=#ff0000}{cps=20}이번엔 네가 맞아 뒤지는거야 ! ! !{/color}{/cps}{/size}" with dissolve
    F "{size=50}{color=#ff0000}{cps=20}아 아 아 악 !{/color}{/cps}{/size}" with dissolve
    F "{size=50}{color=#ff0000}{cps=20}아파 ! 살려주세요 !{/color}{/cps}{/size}" with dissolve
    F "{size=60}{color=#ff0000}{cps=20}죽고 싶지 않아! ! !{/color}{/cps}{/size}" with dissolve
    M "{size=50}{color=#ff0000}아파? X발 아프다고?{/size}{/color}"
    M "{size=50}{color=#ff0000}그 주둥이에서 아프다는 소리가 나와?{/size}{/color}"
    M "{size=50}{color=#ff0000}평생을 애새끼 쳐 패는 재미에 살더니, 이제와서 아파? !{/size}{/color}"
    M "{size=50}{color=#ff0000}X발, 나는 더 아팠어! 이 개같은…! !{/size}{/color}"
    F "{size=50}{color=#ff0000}{cps=20}아 아 아 악 !{/color}{/cps}{/size}" with dissolve
    #피격음

    scene black with dissolve
    centered "{color=#ffffff}남자는 괴성을 지르며 쉬지 않고 폭력을 행사했다.{/color}" with dissolve
    centered "{color=#ffffff}여자는 비명을 지르며 저항하려고 헀다.{/color}" with dissolve
    centered "{color=#ffffff}어느순간, 여자의 비명이 멈췄다. 남자는 멈추지 않았다.{/color}" with dissolve
    centered "{color=#ffffff}남자의 몸은 부숴지고 있었다.{/color}" with dissolve
    centered "{color=#ffffff}그럼에도, 남자는 그의 몸이 전부 사라질 때 까지, 미친 듯이 웃으며….{/color}" with dissolve
    centered "{color=#ffffff}이미 곤죽이 된 여자를 때리고, 때리고, 또 때렸다...{/color}" with dissolve

    jump END_5

label Route_5_Eng:
    "…" with dissolve
    "The relationship between men and women seems to have gotten closer before I knew it."
    "The woman is actively showing interest in the man"
    "Man also seem to be interested in women."
    "The two talk without knowing the time is passing."
    "…" with dissolve
    F "Really? You have an unexpected side"
    M "…I end up saying everything in front of you."
    M "I didn't know I'd say this to others…."
    F "Wow, did you talk to only me? that's sound good."
    M "Oh, The time is already…." with dissolve
    F "Really?"
    F "I lost track of time…."
    M "I am the same"
    F "I'll be honest, I liked you."
    M "…I've been feeling this way, but yor're very bold…."
    M "…I'm.. Same here."
    F "I want to keep in touch with you."
    F "This week is already over…."
    F "Are you free next week?" with dissolve
    F "There is a good restaurant near here…."
    F "Let's have dinner instead of drinking."
    M "…" with dissolve
    "The man agonizes for a moment, then nods a little."
    M "Okay.. I'll do that."
    F "Good!"
    F "Tell me your contact information, and I'll make a detailed schedule!"
    M "Haha, I see."
    hide M Default
    hide F Default
    with dissolve
    "…"
    play sound "SE_Japanese_furin.mp3" fadein 3
    "The door opens with a bell sound."

    scene black with dissolve
    
    centered "{color=#ffffff}The moment they stepped out the door....{/color}" with dissolve
    scene Background with dissolve

    "They are in shock, as if they were hit on the head by something." with dissolve
    "…" with dissolve

    show M Default at left
    show F Default at right
    with dissolve
    
    "The man looks at the woman with an angry expression."
    M "You…."
    F "{size=50}{color=#ff0000}{cps=20}A A A A A A A ! ! ! *Screaming*{/color}{/cps}{/size}" with dissolve
    
    scene black with dissolve
    centered "{color=#ffffff}The man grasps the woman's arm trying to run away and knocks it over.{/color}" with dissolve
    centered "{color=#ffffff}Screaming, he grabbed the woman, who fell and threw her into the store.{/color}" with dissolve
    scene Background with dissolve

    M "{size=50}{color=#ff0000}{cps=20}FXXk ! ! Die ! ! !{/color}{/cps}{/size}" with dissolve
    M "{size=50}{color=#ff0000}{cps=20}It's the time that you are beaten to death ! ! !{/color}{/cps}{/size}" with dissolve
    F "{size=50}{color=#ff0000}{cps=20}A A A A A A A ! ! ! *Screaming*{/color}{/cps}{/size}" with dissolve
    F "{size=50}{color=#ff0000}{cps=20}It hurts! ! ! Help me! ! !{/color}{/cps}{/size}" with dissolve
    F "{size=60}{color=#ff0000}{cps=20}I don't want to die! ! !{/color}{/cps}{/size}" with dissolve
    M "{size=50}{color=#ff0000}Does it hurt? Did you just say you fXXking hurt?!{/size}{/color}"
    M "{size=50}{color=#ff0000}Is 'it hurts' coming out of your fXXking snout?{/size}{/color}"
    M "{size=50}{color=#ff0000}You've lived your whole life for the fun of beating kids, but now you are saying 'it hurts'? !{/size}{/color}"
    M "{size=50}{color=#ff0000}FXXk!! I was more painful, you fucking shit ! !{/size}{/color}"
    F "{size=50}{color=#ff0000}{cps=20}A A A A ! ! ! *Screaming*{/color}{/cps}{/size}" with dissolve
    #피격음

    scene black with dissolve
    centered "{color=#ffffff}The man screamed and used violence nonstop.{/color}" with dissolve
    centered "{color=#ffffff}The woman screamed and tried to resist.{/color}" with dissolve
    centered "{color=#ffffff}At one point, the woman's scream stopped. But the man didn't stop.{/color}" with dissolve
    centered "{color=#ffffff}The man's body was breaking.{/color}" with dissolve
    centered "{color=#ffffff}Still, the man laughed frantically until his whole body was gone….{/color}" with dissolve
    centered "{color=#ffffff}Beating, beating, and beating the already muddled woman...{/color}" with dissolve

    jump END_5_Eng

label END_5:

    call screen ED5 with dissolve

label END_5_Eng:
    call screen ED5_Eng with dissolve

screen ED5:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("ED05. 복수")
        textbutton "타이틀로 돌아가기" action MainMenu(confirm=False)

screen ED5_Eng:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("ED05. Revenge")
        textbutton "Return to Title" action MainMenu(confirm=False)

# F = Memory / M = Loss
label Route_6:
    "…" with dissolve
    "남자와 여자의 사이는 어느샌가 더 가까워진 것 같다."
    "여자는 남자가 마음에 든 듯, 적극적으로 그에게 관심을 표하고 있다."
    "남자 또한 여자에게 관심이 있는 것 같아 보인다."
    "두 사람은 시간가는 줄 모르고 이야기를 나눈다."
    "…" with dissolve
    F "정말요? 의외의 면도 가지고 있군요…."
    M "…당신 앞에서는 별 말도 다 하게 되는군요."
    M "이런 말을 남한테 할 줄은 몰랐는데…."
    F "와아, 나한테만 얘기한거에요? 기쁘네요."
    M "이런, 벌써 시간이…." with dissolve
    F "어머, 정말!"
    F "시간가는 줄도 몰랐군요…."
    M "저도 마찬가지입니다."
    F "솔직하게 말할게요, 난 당신이 마음에 들었어요."
    M "…여태까지 느낀거지만, 정말 당돌하군요…."
    M "…나도 마찬가지입니다."
    F "당신이랑 계속 연락하고 싶어요."
    F "이번 주는 이미 끝났고…."
    F "다음 주에 시간 있어요?" with dissolve
    F "이 근처에 괜찮은 레스토랑이 있는데…."
    F "술 말고 저녁 먹어요, 우리."
    M "…" with dissolve
    "남자는 잠깐 고민하더니, 작게 고개를 끄덕인다."
    M "좋습니다. 그렇게 하지요."
    F "좋아요!"
    F "연락처 알려줘요, 자세한 일정 잡게!"
    M "하하, 알겠습니다."
    hide M Default
    hide F Default
    with dissolve
    "…"
    play sound "SE_Japanese_furin.mp3" fadein 3
    "짤랑,하는 방울소리와 함께 문이 열린다."

    scene black with dissolve
    centered "{color=#ffffff}여자가 문 밖으로 발을 내딛는 순간….{/color}" with dissolve
    scene Background with dissolve

    "여자는, 무언가로 머리를 얻어맞은 듯한 충격에 빠진다." with dissolve
    "…"

    show F Default with vpunch
    F "{size=60}{cps=20}{color=#FF0000}{b}아 아 아 아 아 아 아 악 ! ! ! !{/b}{/color}{/cps}{/size}" with dissolve
    hide F Default
    show M Default with dissolve
    M "뭐야?"
    M "이봐요, 당신 왜 이러는 겁니까?!"
    "남자는 갑자기 자신을 바라보며 소리를 지르는 여자를 보고 당황한다." with dissolve
    hide M Default
    show F Default with vpunch
    F "{size=60}{cps=20}{color=#FF0000}{b}살려주세요살려주세요살려주세요살려주세요살려주세요살려주세요살려주세요살려주세요살려주세요살려주세요살려주세요살려주세요살려주세요살려주세요살려주세요살려주세요살려주세요{/b}{/color}{/cps}{/size}" with dissolve
    hide F Default
    show M Default with dissolve
    M "아니, 이봐요 당신! 왜 이러는 겁니까?!" with dissolve
    hide M Default
    show F Default with vpunch
    F "{size=60}{color=#FF0000}{b}아 아 아 아 ! ! ! !{/b}{/color}{/size}" with dissolve
    F "{size=60}{color=#FF0000}{b}죽고 싶지 않아 ! ! ! !{/b}{/color}{/size}" with dissolve
    hide F Default with vpunch

    scene black with dissolve
    centered "{color=#ffffff}여자는 무언가에 쫓기듯, 문을 박차고 도망쳤다.{/color}" with dissolve
    centered "{color=#ffffff}남자는 문 앞에서 황망히 서 있었다.{/color}" with dissolve
    scene Background with dissolve


    show M Default with dissolve
    M "아니…." with dissolve
    M "저 사람, 대체 왜 저러는지 아십니까?"
    B "글쎄요, 무슨일인지…."
    M "…혹시, 저 사람이 '그녀'인가요?"
    B "흠…. 모르겠습니다. 대체 무슨 일인지…."
    B "왜 그런 생각이 드셨죠?"
    M "캐모마일…." with dissolve
    M "그놈의 지긋긋한 캐모마일 향이 났습니다."
    hide M Default

    scene black with dissolve
    centered "{color=#ffffff}남자 잠시 무언가를 생각하더니, 나중에 다시 오겠다며 떠났다.{/color}" with dissolve
    centered "{color=#ffffff}이틀뒤, 여자가 찾아왔다.{/color}" with dissolve
    scene Background with dissolve

    show F Default with dissolve
    F "…." with dissolve
    B "…어서오십시오." with dissolve
    F "…." with dissolve
    F "…그 사람…." with dissolve
    F "…왔나요?"
    B "…네?"
    F "…그 남자…. 나를 찾던가요?"
    B "무슨… 말씀이신지…."
    F "…도와주세요, 그 남자가 날 죽이려해요…."
    F "{size=60}{color=#FF0000}{cps=20}그 악귀 같은 낯을 하고 날 찢어 죽이려고 한다고! !{/size}{/color}{/cps}"
    B "흠…. 제가 어떻게 도와드리면 될까요?"
    F "그 남자가 나를 찾거든…"
    F "…모르는 척 해주세요."
    F "제발… 도와주세요…."
    "여자가 흐느끼며 부탁한다." with dissolve

    scene black with dissolve
    centered "{color=#ffffff}여자는 자신이 찾아왔다는 것을 알리지 말라고 몇 번이나 당부하곤 떠났다.{/color}" with dissolve
    centered "{color=#ffffff}그 이후, 여자는 다시 돌아오지 않았다.{/color}" with dissolve
    centered "{color=#ffffff}남자는 일요일마다 간간히 바를 찾았다.{/color}" with dissolve
    centered "{color=#ffffff}그에게도 이제 시간이 얼마 남지 않았다.{/color}" with dissolve

    jump END_6

label Route_6_Eng:
    "…" with dissolve
    "The relationship between men and women seems to have gotten closer before I knew it."
    "The woman is actively showing interest in the man"
    "Man also seem to be interested in women."
    "The two talk without knowing the time is passing."
    "…" with dissolve
    F "Really? You have an unexpected side"
    M "…I end up saying everything in front of you."
    M "I didn't know I'd say this to others…."
    F "Wow, did you talk to only me? that's sound good."
    M "Oh, The time is already…." with dissolve
    F "Really?"
    F "I lost track of time…."
    M "I am the same"
    F "I'll be honest, I liked you."
    M "…I've been feeling this way, but yor're very bold…."
    M "…I'm.. Same here."
    F "I want to keep in touch with you."
    F "This week is already over…."
    F "Are you free next week?" with dissolve
    F "There is a good restaurant near here…."
    F "Let's have dinner instead of drinking."
    M "…" with dissolve
    "The man agonizes for a moment, then nods a little."
    M "Okay.. I'll do that."
    F "Good!"
    F "Tell me your contact information, and I'll make a detailed schedule!"
    M "Haha, I see."
    hide M Default
    hide F Default
    with dissolve
    "…"
    play sound "SE_Japanese_furin.mp3" fadein 3
    "The door opens with a bell sound."

    scene black with dissolve
    centered "{color=#ffffff}The moment a woman steps out the door....{/color}" with dissolve
    scene Background with dissolve

    "The woman is in shock, as if she was hit on the head by something." with dissolve
    "…"

    show F Default with vpunch
    F "{size=60}{cps=20}{color=#FF0000}{b}A A A A A A A A A A A ! ! ! *Screaming*{/b}{/color}{/cps}{/size}" with dissolve
    hide F Default
    show M Default with dissolve
    M "What the...?"
    M "Hey, what's wrong with you?!"
    "The man is embarrassed to see the woman screaming at him all of a sudden." with dissolve
    hide M Default
    show F Default with vpunch
    F "{size=60}{cps=20}{color=#FF0000}{b}Please save me. Please don't kill me.Please save me. Please don't kill me.Please save me. Please don't kill me.Please save me. Please don't kill me.Please save me. Please don't kill me.{/b}{/color}{/cps}{/size}" with dissolve
    hide F Default
    show M Default with dissolve
    M "What the...Hey!! What's going on?!" with dissolve
    hide M Default
    show F Default with vpunch
    F "{size=60}{color=#FF0000}{b}A A A A A A ! ! ! *Screaming*{/b}{/color}{/size}" with dissolve
    F "{size=60}{color=#FF0000}{b}Please, I don't wanna die ! ! ! !{/b}{/color}{/size}" with dissolve
    hide F Default with vpunch

    scene black with dissolve
    centered "{color=#ffffff}The woman, kicked the door and ran away like she is chased by something.{/color}" with dissolve
    centered "{color=#ffffff}The man stood in a blankly at the door.{/color}" with dissolve
    scene Background with dissolve


    show M Default with dissolve
    M "What is this….?" with dissolve
    M "Do you know what's hell wrong with her?"
    B "I have no idea…."
    M "…Is she, by any chance, 'That' woman?"
    B "Hmm... I don't know. What is going on…."
    B "What made you think like that?"
    M "Chamomile…." with dissolve
    M "She smelled like a sickening chamomile."
    hide M Default

    scene black with dissolve
    centered "{color=#ffffff}The man thought about something for a while and left the bar, saying he'd come back next time.{/color}" with dissolve
    centered "{color=#ffffff}Two days later, the woman came to visit.{/color}" with dissolve
    scene Background with dissolve

    show F Default with dissolve
    F "…." with dissolve
    B "…Welcome back, Miss." with dissolve
    F "…." with dissolve
    F "…Did that guy…." with dissolve
    F "…come here..?"
    B "…Pardon?"
    F "…Was he…. looking for me?"
    B "I'm sorry… I don't know what you're talking about…."
    F "…Please help me, he's trying to kill me…."
    F "{size=60}{color=#FF0000}{cps=20}He is going to rip me off with that evil face! ! !{/size}{/color}{/cps}"
    B "Hmm...How can I help you?"
    F "If he's looking for me…"
    F "…please pretend you don't know."
    F "Please… please help me…."
    "The woman sobbed out a request." with dissolve

    scene black with dissolve
    centered "{color=#ffffff}The woman left after repeatedly telling her not to let her know she had come.{/color}" with dissolve
    centered "{color=#ffffff}Since then, the woman never visit the bar again.{/color}" with dissolve
    centered "{color=#ffffff}The man occasionally visited the bar every Sunday.{/color}" with dissolve
    centered "{color=#ffffff}...He doesn't have much time left either.{/color}" with dissolve

    jump END_6_Eng

label END_6:
    call screen ED6 with dissolve

label END_6_Eng:
    call screen ED6_Eng with dissolve

screen ED6:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("ED06. 도망")
        textbutton "타이틀로 돌아가기" action MainMenu(confirm=False)

screen ED6_Eng:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("ED06. Runaway")
        textbutton "Return to Title" action MainMenu(confirm=False)

# F = Loss / M = truth
label Route_7:
    "…" with dissolve
    "남자와 여자의 사이는 어느샌가 더 가까워진 것 같다."
    "여자는 남자가 마음에 든 듯, 적극적으로 그에게 관심을 표하고 있다."
    "남자 또한 여자에게 관심이 있는 것 같아 보인다."
    "두 사람은 시간가는 줄 모르고 이야기를 나눈다."
    "…" with dissolve
    F "정말요? 의외의 면도 가지고 있군요…."
    M "…당신 앞에서는 별 말도 다 하게 되는군요."
    M "이런 말을 남한테 할 줄은 몰랐는데…."
    F "와아, 나한테만 얘기한거에요? 기쁘네요."
    M "이런, 벌써 시간이…." with dissolve
    F "어머, 정말!"
    F "시간가는 줄도 몰랐군요…."
    M "저도 마찬가지입니다."
    F "솔직하게 말할게요, 난 당신이 마음에 들었어요."
    M "…여태까지 느낀거지만, 정말 당돌하군요…."
    M "…나도 마찬가지입니다."
    F "당신이랑 계속 연락하고 싶어요."
    F "이번 주는 이미 끝났고…."
    F "다음 주에 시간 있어요?" with dissolve
    F "이 근처에 괜찮은 레스토랑이 있는데…."
    F "술 말고 저녁 먹어요, 우리."
    M "…" with dissolve
    "남자는 잠깐 고민하더니, 작게 고개를 끄덕인다."
    M "좋습니다. 그렇게 하지요."
    F "좋아요!"
    F "연락처 알려줘요, 자세한 일정 잡게!"
    M "하하, 알겠습니다."
    hide M Default
    hide F Default
    with dissolve
    "…"
    play sound "SE_Japanese_furin.mp3" fadein 3
    "짤랑,하는 방울소리와 함께 문이 열린다."

    scene black with dissolve
    centered "{color=#ffffff}남자가 문 밖으로 발을 내딛는 순간….{/color}" with dissolve
    scene Background with dissolve

    "남자는, 무언가로 머리를 얻어맞은 듯한 충격에 빠진다."
    "…"

    hide F Default
    show M Default with dissolve
    M "…내가 당신을…." with dissolve
    M "나는…"
    M "…당신의…."
    "남자는 여자의 얼굴을 보더니, 갑자기 혼란스러워 하기 시작했다."
    "여자는 주변을 두리번거리다가, 이읃고 남자가 자신을 말하는 것이라는 것을 깨닫는다."
    hide M Default
    show F Default with dissolve
    F "저요..? 제가 왜요?" with dissolve
    F "음…. 혹시, 저를 아시는 분이신가요?"
    M "…" with dissolve
    hide F Default
    show M Default with dissolve
    F "…고민이 많은 얼굴이네요." with dissolve
    F "음….괜찮다면 나한테 얘기해줄래요?"
    F "저 고민 들어주는 거 되게 잘하는데."
    "여자가 밝게 웃는다."
    
    #발소리 SE
    scene black with dissolve
    scene Background with dissolve
    hide M Default with dissolve
    "남자는 여자의 얼굴을 한참 바라보다, 망연한 표정으로 바에서 나갔다." with dissolve
    show F Default with dissolve
    F "으음…." with dissolve
    F "무슨 일이실까…."
    F "깜짝이야! 바텐더씨, 언제부터 거기 계셨나요?"
    F "아… 내가 뭐하고 있었더라?" with dissolve
    "여자는 잠시 고민하더니, 다시 밝은 얼굴로 돌아와 질문한다."
    F "…저 분 여기 단골이신가요?"
    B "네, 매주 오시곤 한답니다."
    F "어머…. 주로 언제쯤 오시는 편이신가요?"
    B "음…. 일요일에 주로 오시는 편이죠."
    F "일요일…."
    F "감사합니다."
    "여자는 홀가분하게 바를 나갔다."
    hide F Default with dissolve

    scene black with dissolve
    centered "{color=#ffffff}일주일 뒤, 다시 일요일.{/color}" with dissolve
    centered "{color=#ffffff}다시 남자가 찾아왔다..{/color}" with dissolve
    scene Background with dissolve

    show M Default with dissolve
    M "바텐더씨, 제가 도대체 어떻게 해야할까요…?" with dissolve
    M "내가, 내가…."
    M "당최 뭘 해야…."
    M "…나는…."
    "남자는 아직도 혼란스러워 보인다."
    B "어렵게 생각하실 필요 없습니다."
    B "제임스씨가 어떤 선택을 하시든, 그것이 옳은 선택일테니."

    play sound "SE_Japanese_furin.mp3" fadein 3
    "짤랑, 하는 방울소리와 함께 바에 한 여자가 들어왔다." with dissolve

    hide M Default with dissolve
    show F Default with dissolve
    F "어라, 진짜 계시네!" with dissolve
    hide F Default

    show M Default at left
    show F Default at right
    with dissolve
    F "안녕하세요, 우리 구면이죠?"
    M "…" with dissolve
    F "나는 안나라고 해요."
    F "우리 이것도 인연인데, 그 쪽은 이름이 뭔지 물어봐도 되나요?"
    M "…" with dissolve
    M "…제임스…입니다."
    F "어머, 그러시구나!"
    F "제임스씨, 아직도 고민이 해결이 안된 것 같은데…."
    F "내가 고민 들어줄까요?"
    hide M Default
    hide F Default

    scene black with dissolve
    centered "{color=#ffffff}남자는 재잘거리는 여자의 말을 한참을 잠자코 듣고 있었다.{/color}" with dissolve
    centered "{color=#ffffff}여자는 한참을 떠들더니, 다음 주에 또 오겠다며 작별을 고하고 바를 떠났다.{/color}" with dissolve
    scene Background with dissolve

    show M Default with dissolve
    M "…" with dissolve
    M "바텐더씨…."
    M "저는…."
    M "…저는, 그녀 곁에 남겠습니다."
    B "그것이 당신의 선택입니까?"
    M "…네."
    B "…이제 시간이 얼마 남지 않은 것은 아시죠?"
    B "…압니다."
    B "그래도…. 그러고 싶어요."
    B "알겠습니다. 당신의 선택을 존중합니다."
    scene black with dissolve

    centered "{color=#ffffff}남자와 여자는 매 주 일요일마다 바에서 서로의 말동무가 되어주었다.{/color}" with dissolve
    centered "{color=#ffffff}그러길 14개월, 남자는 다시는 바를 찾아오지 못했다. 아쉽게도.{/color}" with dissolve

    jump END_7

label Route_7_Eng:
    "…" with dissolve
    "The relationship between men and women seems to have gotten closer before I knew it."
    "The woman is actively showing interest in the man"
    "Man also seem to be interested in women."
    "The two talk without knowing the time is passing."
    "…" with dissolve
    F "Really? You have an unexpected side"
    M "…I end up saying everything in front of you."
    M "I didn't know I'd say this to others…."
    F "Wow, did you talk to only me? that's sound good."
    M "Oh, The time is already…." with dissolve
    F "Really?"
    F "I lost track of time…."
    M "I am the same"
    F "I'll be honest, I liked you."
    M "…I've been feeling this way, but yor're very bold…."
    M "…I'm.. Same here."
    F "I want to keep in touch with you."
    F "This week is already over…."
    F "Are you free next week?" with dissolve
    F "There is a good restaurant near here…."
    F "Let's have dinner instead of drinking."
    M "…" with dissolve
    "The man agonizes for a moment, then nods a little."
    M "Okay.. I'll do that."
    F "Good!"
    F "Tell me your contact information, and I'll make a detailed schedule!"
    M "Haha, I see."
    hide M Default
    hide F Default
    with dissolve
    "…"
    play sound "SE_Japanese_furin.mp3" fadein 3
    "The door opens with a bell sound."

    scene black with dissolve
    centered "{color=#ffffff}As soon as the man steps out the door….{/color}" with dissolve
    scene Background with dissolve

    "The man is shocked as if he had been hit on the head by something."
    "…"

    hide F Default
    show M Default with dissolve
    M "…What ever I done to you…?" with dissolve
    M "I am…"
    M "…your…."
    "The man looked at the woman's face and suddenly began to be confused."
    "The woman looks around and eventually realizes that the man is talking about her."
    hide M Default
    show F Default with dissolve
    F "Me..? Why do you call me like that?" with dissolve
    F "Hmm…. Do you happen to know me?"
    M "…" with dissolve
    hide F Default
    show M Default with dissolve
    F "…You look worried." with dissolve
    F "….If you don't mind, can you tell me what is it?"
    F "I am really good at listening."
    "The woman smiles brightly."
    
    #발소리 SE
    scene black with dissolve
    scene Background with dissolve
    hide M Default with dissolve
    "The man looked at the woman's face for a long time, and left the bar with a abstracted look on his face." with dissolve
    show F Default with dissolve
    F "Hmm…." with dissolve
    F "What's the matter with him…."
    F "What the..!!! Hey, mr.Bartender, sice when have you been there?"
    F "Uh... What was I doing here..?" with dissolve
    "The woman agonizes for a while, then returns to her bright face and asks questions."
    F "…Is he a regular here?"
    B "Yes, he comes every week."
    F "Oh, really? When do you usually come?"
    B "Well, he usually comes on Sundays."
    F "Sunday…."
    F "Thank you."
    "The woman walked out of the bar airily."
    hide F Default with dissolve

    scene black with dissolve
    centered "{color=#ffffff}On the next Sunday.{/color}" with dissolve
    centered "{color=#ffffff}The man came again..{/color}" with dissolve
    scene Background with dissolve

    show M Default with dissolve
    M "Mr. Bartender, what should I do...?" with dissolve
    M "How, how…."
    M "How do I supposed to do…."
    M "…I…I am…."
    "The man still looks confused."
    B "Just take it easy."
    B "Whatever you choose, it will be right thing, James."

    play sound "SE_Japanese_furin.mp3" fadein 3
    "The woman came into the bar with a bell ring." with dissolve

    hide M Default with dissolve
    show F Default with dissolve
    F "Wow, he's really here!" with dissolve
    hide F Default

    show M Default at left
    show F Default at right
    with dissolve
    F "Hi. We've met before, right?"
    M "…" with dissolve
    F "My name is Anna."
    F "It seems like we are in fate, so could you tell me what is your name?"
    M "…" with dissolve
    M "…James."
    F "Oh, you are!"
    F "Hey, mr. James. You don't look like the problem is solved yet…."
    F "If you don't mind, can you let me hear it?"
    hide M Default
    hide F Default

    scene black with dissolve
    centered "{color=#ffffff}The man listened in silence to the chattering the woman for a long time.{/color}" with dissolve
    centered "{color=#ffffff}After a long chat, the woman said goodbye and left the bar, saying she would come again next week.{/color}" with dissolve
    scene Background with dissolve

    show M Default with dissolve
    M "…" with dissolve
    M "Mr. Bartender…."
    M "I…."
    M "…I, I will stay with her."
    B "Is that your choice?"
    M "…Yes."
    B "…You know you don't have much time left, right?"
    M "…I know."
    M "But…. I want it."
    B "All right, I respect your choice."
    scene black with dissolve

    centered "{color=#ffffff}The man and the woman were company to each other at the bar every Sunday.{/color}" with dissolve
    centered "{color=#ffffff}After 14 months, the man couldn't visit the bar ever again... Saddly.{/color}" with dissolve

    jump END_7_Eng

label END_7:
    call screen ED7 with dissolve

label END_7_Eng:
    call screen ED7_Eng with dissolve

screen ED7:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("ED07. 희생")
        textbutton "타이틀로 돌아가기" action MainMenu(confirm=False)

screen ED7_Eng:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("ED07. Sacrifice")
        textbutton "Return to Title" action MainMenu(confirm=False)

# F = Loss / M = Memory
label Route_8:
    "…" with dissolve
    "남자와 여자의 사이는 어느샌가 더 가까워진 것 같다."
    "여자는 남자가 마음에 든 듯, 적극적으로 그에게 관심을 표하고 있다."
    "남자 또한 여자에게 관심이 있는 것 같아 보인다."
    "두 사람은 시간가는 줄 모르고 이야기를 나눈다."
    "…" with dissolve
    F "정말요? 의외의 면도 가지고 있군요…."
    M "…당신 앞에서는 별 말도 다 하게 되는군요."
    M "이런 말을 남한테 할 줄은 몰랐는데…."
    F "와아, 나한테만 얘기한거에요? 기쁘네요."
    M "이런, 벌써 시간이…." with dissolve
    F "어머, 정말!"
    F "시간가는 줄도 몰랐군요…."
    M "저도 마찬가지입니다."
    F "솔직하게 말할게요, 난 당신이 마음에 들었어요."
    M "…여태까지 느낀거지만, 정말 당돌하군요…."
    M "…나도 마찬가지입니다."
    F "당신이랑 계속 연락하고 싶어요."
    F "이번 주는 이미 끝났고…."
    F "다음 주에 시간 있어요?" with dissolve
    F "이 근처에 괜찮은 레스토랑이 있는데…."
    F "술 말고 저녁 먹어요, 우리."
    M "…" with dissolve
    "남자는 잠깐 고민하더니, 작게 고개를 끄덕인다."
    M "좋습니다. 그렇게 하지요."
    F "좋아요!"
    F "연락처 알려줘요, 자세한 일정 잡게!"
    M "하하, 알겠습니다."
    hide M Default
    hide F Default
    with dissolve
    "…" with dissolve
    play sound "SE_Japanese_furin.mp3" fadein 3
    "짤랑,하는 방울소리와 함께 문이 열린다."

    scene black with dissolve
    
    centered "{color=#ffffff}남자가 문 밖으로 발을 내딛는 순간….{/color}" with dissolve
    
    scene Background with dissolve
    "남자는, 무언가로 머리를 얻어맞은 듯한 충격에 빠진다."
    "…"

    show F Default with dissolve
    F "짐?"
    F "왜그래요, 어디 아파요?"
    hide F Default
    show M Default with dissolve
    M "…당신."
    M "…당신이었구나…."
    hide M Default
    show F Default with dissolve
    F "…네?"
    hide F Default
    show M Default with dissolve
    M "당신이… 그 여자였어…."
    hide M Default
    show F Default with dissolve
    F "도대체 무슨 말을…."
    hide F Default
    show M Default with dissolve
    M "네가…"
    M "{size=60}{cps=20}네가 {color=#FF0000}{b}그 년{/b}{/color}이었다고 네가 ! ! ! !{/cps}{/size}" with dissolve
    hide M Default with vpunch

    scene black with dissolve    
    centered "{size=50}{color=#ff0000}{cps=20}꺄 아 아 악 !{/color}{/cps}{/size}" with dissolve

    centered "{color=#ffffff}남자는 여자를 밀쳐 넘어뜨렸다.{/color}" with dissolve
    centered "{color=#ffffff}그리고 품에서 잭나이프를 꺼내들어 여자에게 휘둘렀다.{/color}" with dissolve
    centered "{size=60}{color=#0000ff}죽어 ! 죽으라고 !{/color}{/size}" with dissolve
    centered "{size=60}{color=#0000ff}너 때문에 내가…! {/color}{/size}" with dissolve
    centered "{size=50}{color=#ff0000}{cps=20}살려주세요 ! 아아아악 !{/color}{/cps}{/size}" with dissolve
    centered "{color=#ffffff}남자는 넘어진 여자에게 올라타, 여자를 찔렀다.{/color}" with dissolve
    centered "{color=#ffffff}여자는 끔찍한 비명을 지르며 저항했지만, 흘러나온 피 만큼이나 점차 힘을 잃어갔다.{/color}" with dissolve
    centered "{color=#ffffff}곧이어, 여자의 숨이 완전이 멎었다.{/color}" with dissolve
    centered "{color=#0000ff}바텐더씨, 내가 드디어 해냈습니다…!{/color}" with dissolve
    centered "{color=#0000ff}내가 드디어 찾았어요…!{/color}" with dissolve
    centered "{color=#0000ff}하하…!{/color}" with dissolve
    centered "{color=#0000ff}{cps=20}{size=50}아 하 하 하 하 하 학 ! ! !{/cps}{/color}{/size}" with dissolve
    centered "{color=#ffffff}곧이어, 남자의 몸이 서서히 부숴지기 시작했다.{/color}" with dissolve
    centered "{color=#ffffff}남자는 자신의 몸이 부숴지고 있는 것 조차 모른채\n미친듯이 웃으며, 그렇게 사라졌다.{/color}" with dissolve
    centered "{color=#ffffff}문 앞에 비치된 러그에 수십, 수백 번 찔린 여자의 혈액이 화려하게 물들었다.{/color}" with dissolve
    
    jump ED8

label Route_8_Eng:
    "…" with dissolve
    "The relationship between men and women seems to have gotten closer before I knew it."
    "The woman is actively showing interest in the man"
    "Man also seem to be interested in women."
    "The two talk without knowing the time is passing."
    "…" with dissolve
    F "Really? You have an unexpected side"
    M "…I end up saying everything in front of you."
    M "I didn't know I'd say this to others…."
    F "Wow, did you talk to only me? that's sound good."
    M "Oh, The time is already…." with dissolve
    F "Really?"
    F "I lost track of time…."
    M "I am the same"
    F "I'll be honest, I liked you."
    M "…I've been feeling this way, but yor're very bold…."
    M "…I'm.. Same here."
    F "I want to keep in touch with you."
    F "This week is already over…."
    F "Are you free next week?" with dissolve
    F "There is a good restaurant near here…."
    F "Let's have dinner instead of drinking."
    M "…" with dissolve
    "The man agonizes for a moment, then nods a little."
    M "Okay.. I'll do that."
    F "Good!"
    F "Tell me your contact information, and I'll make a detailed schedule!"
    M "Haha, I see."
    hide M Default
    hide F Default
    with dissolve
    "…"
    play sound "SE_Japanese_furin.mp3" fadein 3
    "The door opens with a bell sound."

    scene black with dissolve
 
    centered "{color=#ffffff}As soon as the man steps out the door….{/color}" with dissolve
    scene Background with dissolve
    "The man is shocked as if he had been hit on the head by something."
    "…"

    show F Default with dissolve
    F "Jim?"
    F "What's wrong with you? Do you get sick soemwhere? "
    hide F Default
    show M Default with dissolve
    M "…You.."
    M "…It was you…."
    hide M Default
    show F Default with dissolve
    F "…Pardon?"
    hide F Default
    show M Default with dissolve
    M "You… You was that woman…."
    hide M Default
    show F Default with dissolve
    F "What are you talking about?"
    hide F Default
    show M Default with dissolve
    M "You…"
    M "{size=60}{cps=20}You {color=#FF0000}{b}were that{/b}{/color} bXXch ! ! ! !{/cps}{/size}" with dissolve
    hide M Default with vpunch

    scene black with dissolve    
    centered "{size=50}{color=#ff0000}{cps=20}A A A A A A A !!! *Screaming*{/color}{/cps}{/size}" with dissolve

    centered "{color=#ffffff}The man pushed the woman down.{/color}" with dissolve
    centered "{color=#ffffff}Then he took the jackknife out of his arms and swung it at the woman.{/color}" with dissolve
    centered "{size=60}{color=#0000ff}Die!! Die!!!{/color}{/size}" with dissolve
    centered "{size=60}{color=#0000ff}Because of you...!!! I..!!{/color}{/size}" with dissolve
    centered "{size=50}{color=#ff0000}{cps=20}Help me!!! Please don't kill me!!! A A A A A A !! *Screaming*{/color}{/cps}{/size}" with dissolve
    centered "{color=#ffffff}The man climbed on the fallen woman and stabbed her.{/color}" with dissolve
    centered "{color=#ffffff}The woman resisted with a terrible scream, but then stopped breathing.{/color}" with dissolve
    centered "{color=#0000ff}Mr. Bartender, I finally made it...!{/color}" with dissolve
    centered "{color=#0000ff}I finally found her..!!{/color}" with dissolve
    centered "{color=#0000ff}Haha…!{/color}" with dissolve
    centered "{color=#0000ff}{cps=20}{size=50}Ha Ha Ha Ha Ha Ha Ha Ha ! ! !{/cps}{/color}{/size}" with dissolve
    centered "{color=#ffffff}Soon after, the man's body slowly began to crumble.{/color}" with dissolve
    centered "{color=#ffffff}The man laughed crazily without even knowing that his body was breaking, and so disappeared.{/color}" with dissolve
    centered "{color=#ffffff}The blood of the woman who was stabbed dozens or hundreds of times in the lug placed at the door was coloured.{/color}" with dissolve
    
    jump ED8_Eng

label ED8:
    call screen ED08

label ED8_Eng:
    call screen ED8_Eng

screen ED08:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("ED08. 복수")
        textbutton "타이틀로 돌아가기" action MainMenu(confirm=False)

screen ED8_Eng:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("ED08. Revenge")
        textbutton "Return to Title" action MainMenu(confirm=False)

#F - Loss / M - Loss
label Route_9:
    show M Default
    show F Default
    with dissolve

    B "두 분께서 만족스럽게 즐겨 주시니 몸 둘 바를 모르겠군요."
    B "괜찮으시다면 제가 연구 중인 레시피에 조언 부탁드려도 될까요?"
    F "어머…. 전 따로 전문적으로 배운 적이 없는데…."
    F "제가 도움이 될까요?"
    B "물론입니다. 언제나 객관적 평가는 중요한 법이니까요."
    F "좋아요. 우리 바텐더 씨께서 어떤 마법을 부리고 계셨을까요?"
    B "{b}리큐르를 베이스{/b}로, {b}과일주스와 에스프레소{/b}를 추가한 칵테일에 대해 구상 중 입니다."
    B "가니쉬를 계피 스틱으로 할지, 라임을 할 지 고민이 됩니다."
    F "듣기만 해도 다채로운 향기가 느껴지는 칵테일이군요?"
    F "음, 저라면 가니쉬를 {b}계피 스틱{/b}으로 선택하겠어요."
    F "커피 향과 계피 향은 항상 잘 어울리니까요."
    F "짐, 당신의 생각은 어떤가요?"
    M "…저도 같은 생각입니다."
    B "큰 도움이 됐습니다. 손님들께서 좋아하셨으면 좋겠군요."
    F "흠, 레시피가 완성되면 한 잔 마셔볼 수 있을까요?"
    B "하하. 물론이죠. 레시피가 완성되면 가장 먼저 두 분께 선보이겠습니다."

    "…" with dissolve
    "남자와 여자의 사이는 어느샌가 더 가까워진 것 같다."
    "여자는 남자가 마음에 든 듯, 적극적으로 그에게 관심을 표하고 있다."
    "남자 또한 여자에게 관심이 있는 것 같아 보인다."
    "두 사람은 시간가는 줄 모르고 이야기를 나눈다."
    "…" with dissolve
    F "정말요? 의외의 면도 가지고 있군요…."
    M "…당신 앞에서는 별 말도 다 하게 되는군요."
    M "이런 말을 남한테 할 줄은 몰랐는데…."
    F "와아, 나한테만 얘기한거에요? 기쁘네요."
    M "이런, 벌써 시간이…." with dissolve
    F "어머, 정말!"
    F "시간가는 줄도 몰랐군요…."
    M "저도 마찬가지입니다."
    F "솔직하게 말할게요, 난 당신이 마음에 들었어요."
    M "…여태까지 느낀거지만, 정말 당돌하군요…."
    M "…나도 마찬가지입니다."
    F "당신이랑 계속 연락하고 싶어요."
    F "이번 주는 이미 끝났고…."
    F "다음 주에 시간 있어요?" with dissolve
    F "이 근처에 괜찮은 레스토랑이 있는데…."
    F "술 말고 저녁 먹어요, 우리."
    M "…" with dissolve
    "남자는 잠깐 고민하더니, 작게 고개를 끄덕인다."
    M "좋습니다. 그렇게 하지요."
    F "좋아요!"
    F "연락처 알려줘요, 자세한 일정 잡게!"
    M "하하, 알겠습니다."
    hide M Default
    hide F Default
    with dissolve
    "…"
    play sound "SE_Japanese_furin.mp3" fadein 3
    "짤랑,하는 방울소리와 함께 문이 열린다."

    scene black with dissolve
    centered "{color=#ffffff}그들은 당연한 것 처럼, 사랑에 빠졌다.{/color}" with dissolve
    centered "{color=#ffffff}남자는 여자의 밝고 활기찬 모습을 사랑했고,{/color}" with dissolve
    centered "{color=#ffffff}여자는 남자의 자상하고 진중한 모습을 사랑했다.{/color}" with dissolve
    centered "{color=#ffffff}시간이 꽤 지나고, 남자는 여자와 결혼을 약속했다.{/color}" with dissolve
    centered "{color=#ffffff}남자는 긴장한 듯 보였고, 여자는 행복에 벅차 눈물을 흘렸다.{/color}" with dissolve
    centered "{color=#ffffff}결혼식부터, 신혼여행, 신혼생활….{/color}" with dissolve
    centered "{color=#ffffff}모든게 행복했다.{/color}" with dissolve
    centered "{color=#ffffff}두 사람은 그린듯한 행복한 부부였다.{/color}" with dissolve
    centered "{color=#ffffff}그리고 몇 개월 뒤….{/color}" with dissolve
    
    scene Background with dissolve
    show F Default with dissolve
    play sound "SE_Japanese_furin.mp3" fadein 3
    "짤랑,하는 방울소리와 함께 여자가 들어온다." with dissolve
    "여자는 급하게 나온건지, 약간 어수선해 보인다."
    "여자가 카운터로 다가온다."
    F "…혹시 그이가 여길 찾아오지 않았나요?" with dissolve
    B "아뇨, 결혼하신 이후에는 한 번도 찾질 않으셨습니다."
    B "무슨 일이 있으십니까?"
    F "아아, 짐!"
    "여자가 갑자기 흐느끼기 시작한다."
    "시간이 지나자, 여자가 진정하고 말을 이어나간다." with dissolve
    F "제발, 어딜 간거야…." with dissolve
    F "말도 없이 사라질 사람이 아닌데.…."
    F "어젯 밤, 포도를 사러 나갔다가 돌아오질 않았어요….."
    F "무슨 일이라도 당한걸까요?"
    F "어디서 쓰러지기라도 한건 아니겠죠?"
    F "괜히 먹고 싶다고 했나봐요, 내가…."
    F "조심해야 할 시기라고, 아이가 먹는거라면 무엇이든 구해주겠다고…."
    F "이것저것 챙겨주고, 다정하게 대해주는 그이가 좋아서…."
    F "아아, 제발…. 어쩌면 좋죠?"
    B "진정하세요, 부인…."
    F "제발, 그이가 어딨는지 알게되면 제게 말해주세요…."
    B "…알겠습니다. 제임스를 보게되면 바로 연락드리겠습니다."
    F "아아, 짐…."

    hide F Default with dissolve
    scene black with dissolve

    centered "{color=#ffffff}이후로도 여자는 불러오는 배를 부여잡고,\n몇 번이나 더 찾아왔다.{/color}" with dissolve
    centered "{color=#ffffff}안타깝게도 제임스의 소식은 그 어디에서도 들을 수 없었다.{/color}" with dissolve
    centered "{color=#ffffff}시간이 갈수록, 여자는 점점 불안해져갔다.\n자신의 삶을 송두리채 빼앗긴 느낌이었다.{/color}" with dissolve
    centered "{color=#ffffff}여자는 이전의 밝고 활발한 모습을 잃었다.{/color}" with dissolve
    centered "{color=#ffffff}착실하게 미쳐가던 여자는,\n6개월 이후 더 이상 이 곳에 찾아오지 않게 되었다….{/color}" with dissolve
    
    jump End_9

label Route_9_Eng:
    show M Default
    show F Default
    with dissolve

    B "I'm so glad you guys to enjoy it satisfactorily."
    B "If you don't mind, could you give me some advice on the recipe I'm working on?"
    F "Oh…. I've never learned it professionally…."
    F "Could I be of help?"
    B "Of course you are. Objective evaluation is always important."
    F "Okay than. So... I wonder what kind of magic our bartender was using."
    B "I am thinking about a cocktail with {b}liquor as base{/b}, {b}added fruit juice and espresso{/b}."
    B "I wonder which one would go well with the garnish, cinnamon stick or lime."
    F "It sounds that it might give me a variety of scents."
    F "Well, If I were you, I'll choose {b}cinnamon stick{/b} as garnish."
    F "Coffee and cinnamon always go well together."
    F "How about you, Jim? What do you think about it?"
    M "…I agree with you."
    B "It's been a great help. I hope everyone likes it. Thank you."
    F "Hmm, I hope that I could have a drink when the recipe is completed."
    B "Haha. Of course. When the recipe is complete, I'll show it to you two first."

    "…" with dissolve
    "The relationship between men and women seems to have gotten closer before I knew it."
    "The woman is actively showing interest in the man"
    "Man also seem to be interested in women."
    "The two talk without knowing the time is passing."
    "…" with dissolve
    F "Really? You have an unexpected side"
    M "…I end up saying everything in front of you."
    M "I didn't know I'd say this to others…."
    F "Wow, did you talk to only me? that's sound good."
    M "Oh, The time is already…." with dissolve
    F "Really?"
    F "I lost track of time…."
    M "I am the same"
    F "I'll be honest, I liked you."
    M "…I've been feeling this way, but yor're very bold…."
    M "…I'm.. Same here."
    F "I want to keep in touch with you."
    F "This week is already over…."
    F "Are you free next week?" with dissolve
    F "There is a good restaurant near here…."
    F "Let's have dinner instead of drinking."
    M "…" with dissolve
    "The man agonizes for a moment, then nods a little."
    M "Okay.. I'll do that."
    F "Good!"
    F "Tell me your contact information, and I'll make a detailed schedule!"
    M "Haha, I see."
    hide M Default
    hide F Default
    with dissolve
    "…"
    play sound "SE_Japanese_furin.mp3" fadein 3
    "The door opens with a bell sound."

    scene black with dissolve
    centered "{color=#ffffff}They fell in love, like it should be.{/color}" with dissolve
    centered "{color=#ffffff}The man loved the brightness and energetic of the woman,{/color}" with dissolve
    centered "{color=#ffffff}and the woman loved the man's caring and seriousness.{/color}" with dissolve
    centered "{color=#ffffff}After a while, the man promised to marry the woman.{/color}" with dissolve
    centered "{color=#ffffff}The man looked nervous, while the woman was overwhelmed with happiness and wept.{/color}" with dissolve
    centered "{color=#ffffff}Weddings, honeymoon, honeymoon period….{/color}" with dissolve
    centered "{color=#ffffff}Everything was happy.{/color}" with dissolve
    centered "{color=#ffffff}They looked like they were a perfectly happy couple.{/color}" with dissolve
    centered "{color=#ffffff}And a few months later….{/color}" with dissolve
    
    scene Background with dissolve
    show F Default with dissolve
    play sound "SE_Japanese_furin.mp3" fadein 3
    "The woman is entering with the bell ring." with dissolve
    "The woman looks a little cluttered, like she came out in a hurry."
    "The woman approaches the counter."
    F "…Didn't he come here by any chance?" with dissolve
    B "No, he hasn't looked for here since you got married."
    B "Is there any problem with you?"
    F "Oh my god, Jim..!"
    "The woman suddenly begins to sob."
    "As time passes, the woman calms down and continues to speak." with dissolve
    F "Please, where did you go…." with dissolve
    F "He is not the person who disappears without saying anything to me.…."
    F "Last night, he went out to buy some grapes and didn't come back yet….."
    F "Did something happen to him?"
    F "Did he fall down somewhere?"
    F "I shouldn't have said I wanted to eat it…."
    F "He said it's time to be careful, and he will get anything for kid…."
    F "I...I was just excited because he..he took caore of me and..and he..he was so nice to me..."
    F "God...please...what should I do?"
    B "Calm down, ma'am…."
    F "Please...please tell me if you know where he is…."
    B "…I got it. If I meet him I'll tell you. I promise."
    F "Oh..Jim…."

    hide F Default with dissolve
    scene black with dissolve

    centered "{color=#ffffff}Since then, the woman has come to visit \nagain and again, with her growing baby in womb.{/color}" with dissolve
    centered "{color=#ffffff}Unfortunately, no one could know where James is.{/color}" with dissolve
    centered "{color=#ffffff}As time went by, the woman became more and more anxious.\nThe woman felt like she was robbed of her life.{/color}" with dissolve
    centered "{color=#ffffff}The woman has lost her former brightness and energetic.{/color}" with dissolve
    centered "{color=#ffffff}Little by, the woman who was steadily going mad. \n6 months later, the woman stopped visiting the bar….{/color}" with dissolve
    
    jump End_9_Eng
    
label End_9:
    call screen ED9 with dissolve

label End_9_Eng:
    call screen ED9_Eng with dissolve

screen ED9:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("ED9. 상실")
        textbutton "타이틀로 돌아가기" action MainMenu(confirm=False)

screen ED9_Eng:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("ED9. Loss")
        textbutton "Return to Title" action MainMenu(confirm=False)

# F = Loss / M = Fail
label Route_10:
    scene black with dissolve
    show M Default at left
    show F Default at right
    with dissolve
    B "……. 아직, 이름은 없는 시험작입니다." with dissolve
    M "감사합니다."
    M "…" with dissolve
    M "…" with dissolve
    M "으음…." with dissolve
    "남자는…." with dissolve
    M "으음…." with dissolve
    "…남자는 미묘한 표정으로 칵테일을 내려놓더니, 아무 말도 하지 않고있다."
    M "…." with dissolve
    B "…." with dissolve
    B "취향이 아니군요…?" with dissolve
    M "…불행하게도, 네." with dissolve
    B "…." with dissolve
    B "제 단골의 마지막 잔을 좋지 않은 기억으로 내버려 둘 순 없죠."
    B "다시 내어드리겠습니다."
    M "아, 아닙니다. 그러실 필요는…."
    "…남자의 잔은 거의 비지 않았다."
    B "잠시만 기다리십시오."
    "…." with dissolve
    B "…남겨진 기억 한 잔 나왔습니다."
    M "아…. 감사합니다."
    "남자가 조심스레 잔을 홀짝인다."
    B "{b}위스키를 베이스{/b}로, {b}레드 와인과 리큐르를 추가{/b}한 칵테일입니다."
    F "와아, {b}커피콩 가니쉬{/b}네요? 귀여워라."
    M "와, 이거…. 정말 맛있군요."
    B "그렇습니까? 다행이군요."
    M "뭔가, 이 칵테일을 마시니…."
    M "그리우면서, 슬픈 것 같기도 하고…."
    M "으음, 뭔가가 기억날 것 같기도 한데…."
    F "이전에 비슷한 술을 먹어본 적 있나봐요?"
    M "그런 걸지도 모르겠습니다."

    "…" with dissolve
    "남자와 여자의 사이는 어느샌가 더 가까워진 것 같다."
    "여자는 남자가 마음에 든 듯, 적극적으로 그에게 관심을 표하고 있다."
    "남자 또한 여자에게 관심이 있는 것 같아 보인다."
    "두 사람은 시간가는 줄 모르고 이야기를 나눈다."
    "…" with dissolve
    F "정말요? 의외의 면도 가지고 있군요…."
    M "…당신 앞에서는 별 말도 다 하게 되는군요."
    M "이런 말을 남한테 할 줄은 몰랐는데…."
    F "와아, 나한테만 얘기한거에요? 기쁘네요."
    M "이런, 벌써 시간이…." with dissolve
    F "어머, 정말!"
    F "시간가는 줄도 몰랐군요…."
    M "저도 마찬가지입니다."
    F "솔직하게 말할게요, 난 당신이 마음에 들었어요."
    M "…여태까지 느낀거지만, 정말 당돌하군요…."
    M "…나도 마찬가지입니다."
    F "당신이랑 계속 연락하고 싶어요."
    F "이번 주는 이미 끝났고…."
    F "다음 주에 시간 있어요?" with dissolve
    F "이 근처에 괜찮은 레스토랑이 있는데…."
    F "술 말고 저녁 먹어요, 우리."
    M "…" with dissolve
    "남자는 잠깐 고민하더니, 작게 고개를 끄덕인다."
    M "좋습니다. 그렇게 하지요."
    F "좋아요!"
    F "연락처 알려줘요, 자세한 일정 잡게!"
    M "하하, 알겠습니다."
    hide M Default
    hide F Default
    with dissolve
    "…"
    play sound "SE_Japanese_furin.mp3" fadein 3
    "짤랑,하는 방울소리와 함께 문이 열린다."

    scene black with dissolve
    centered "{color=#ffffff}남자가 문 밖으로 발을 내딛는 순간….{/color}" with dissolve
    scene Background with dissolve
    "남자는, 무언가로 머리를 얻어맞은 듯한 충격이 빠진다."
    "…"

    show F Default with dissolve
    F "짐?"
    F "왜그래요, 어디 아파요?"
    hide F Default
    show M Default with dissolve
    M "…당신."
    M "…당신이었구나…."
    hide M Default
    show F Default with dissolve
    F "…네?"
    hide F Default
    show M Default with dissolve
    M "당신이… 그 여자였어…."
    hide M Default
    show F Default with dissolve
    F "도대체 무슨 말을…."
    hide F Default
    show M Default with dissolve
    M "네가…"
    M "{size=60}{cps=20}네가 {color=#FF0000}{b}그 년{/b}{/color}이었다고 네가 ! ! ! !{/cps}{/size}" with dissolve
    hide M Default with vpunch

    scene black with dissolve    
    centered "{size=50}{color=#ff0000}{cps=20}꺄 아 아 악 !{/color}{/cps}{/size}" with dissolve

    centered "{color=#ffffff}남자는 여자를 밀쳐 넘어뜨렸다.{/color}" with dissolve
    centered "{color=#ffffff}그리고 품에서 잭나이프를 꺼내들어 여자에게 휘둘렀다.{/color}" with dissolve
    centered "{size=60}{color=#0000ff}죽어! 죽으라고!{/color}{/size}" with dissolve
    centered "{size=60}{color=#0000ff}너 때문에 내가…!{/color}{/size}" with dissolve
    centered "{size=50}{color=#ff0000}{cps=20}살려주세요! 아아아악!{/color}{/cps}{/size}" with dissolve
    centered "{color=#ffffff}남자는 넘어진 여자에게 올라타, 여자를 찔렀다.{/color}" with dissolve
    centered "{color=#ffffff}여자는 끔찍한 비명을 지르며 저항헀지만, 이읃고 숨을 멈췄다.{/color}" with dissolve
    centered "{color=#0000ff}바텐더씨, 내가 드디어 해냈습니다…!{/color}" with dissolve
    centered "{color=#0000ff}내가 드디어 찾았어요…!{/color}" with dissolve
    centered "{color=#0000ff}하하…!{/color}" with dissolve
    centered "{color=#0000ff}{cps=20}{size=50}아 하 하 하 하 하 하 ! ! !{/cps}{/color}{/size}" with dissolve
    centered "{color=#ffffff}곧이어, 남자의 몸이 서서히 부숴지기 시작했다.{/color}" with dissolve
    centered "{color=#ffffff}남자는 자신의 몸이 부숴지고 있는 것 조차 모른채\n미친듯이 웃으며, 그렇게 사라졌다.{/color}" with dissolve
    centered "{color=#ffffff}문 앞에 비치된 러그에 수십, 수백 번 찔린 여자의 혈액이 화려하게 물들었다.{/color}" with dissolve

    jump END_10

label Route_10_Eng:
    scene black with dissolve
    show M Default at left
    show F Default at right
    with dissolve
    B "…….It's a test work that doesn't have a name yet.” with dissolve." with dissolve
    M "Thank you."
    M "…" with dissolve
    M "…" with dissolve
    M "Umm…." with dissolve
    "The man…." with dissolve
    M "Hmm…." with dissolve
    "The man put down the cocktail with a subtle expression, and said nothing."
    M "…." with dissolve
    B "…." with dissolve
    B "It's not your type, right...?" with dissolve
    M "…Unfortunately, it's not my type." with dissolve
    B "…." with dissolve
    B "I can't leave the last cup of my regular as a bad memory."
    B "I'll give it back to you."
    M "Oh, no. You don't have to...."
    "…The man's glass was hardly empty."
    B "Wait a second."
    "…." with dissolve
    B "…Here's the cup of 'The Memories Remains'."
    M "Oh...Thank you.."
    "The man sips the glass carefully."
    B "It's the cocktail with {b}Whiskey as base{/b}, {b}added red wine and liqueur{/b}."
    F "Wow, {b}coffee bean garnish{/b}? How cute it is."
    M "Oh.. It tastes really nice."
    B "Really? Thank you."
    M "Well, after drinking this cocktail…."
    M "I think, I'll miss something... Why I feel sad of it…."
    M "Hmm, something is tip of my mind…."
    F "Have you ever had a similar drink before?"
    M "Maybe..."

    "…" with dissolve
    "The relationship between men and women seems to have gotten closer before I knew it."
    "The woman is actively showing interest in the man"
    "Man also seem to be interested in women."
    "The two talk without knowing the time is passing."
    "…" with dissolve
    F "Really? You have an unexpected side"
    M "…I end up saying everything in front of you."
    M "I didn't know I'd say this to others…."
    F "Wow, did you talk to only me? that's sound good."
    M "Oh, The time is already…." with dissolve
    F "Really?"
    F "I lost track of time…."
    M "I am the same"
    F "I'll be honest, I liked you."
    M "…I've been feeling this way, but yor're very bold…."
    M "…I'm.. Same here."
    F "I want to keep in touch with you."
    F "This week is already over…."
    F "Are you free next week?" with dissolve
    F "There is a good restaurant near here…."
    F "Let's have dinner instead of drinking."
    M "…" with dissolve
    "The man agonizes for a moment, then nods a little."
    M "Okay.. I'll do that."
    F "Good!"
    F "Tell me your contact information, and I'll make a detailed schedule!"
    M "Haha, I see."
    hide M Default
    hide F Default
    with dissolve
    "…"
    play sound "SE_Japanese_furin.mp3" fadein 3
    "The door opens with a bell sound."

    scene black with dissolve
    centered "{color=#ffffff}As soon as the man steps out the door….{/color}" with dissolve
    scene Background with dissolve
    "The man is shocked as if he had been hit on the head by something."
    "…"

    show F Default with dissolve
    F "Jim?"
    F "What's wrong with you? Do you get sick soemwhere? "
    hide F Default
    show M Default with dissolve
    M "…You.."
    M "…It was you…."
    hide M Default
    show F Default with dissolve
    F "…Pardon?"
    hide F Default
    show M Default with dissolve
    M "You… You was that woman…."
    hide M Default
    show F Default with dissolve
    F "What are you talking about?"
    hide F Default
    show M Default with dissolve
    M "You…"
    M "{size=60}{cps=20}You {color=#FF0000}{b}were that{/b}{/color} bXXch ! ! ! !{/cps}{/size}" with dissolve
    hide M Default with vpunch

    scene black with dissolve    
    centered "{size=50}{color=#ff0000}{cps=20}A A A A A A A !!! *Screaming*{/color}{/cps}{/size}" with dissolve

    centered "{color=#ffffff}The man pushed the woman down.{/color}" with dissolve
    centered "{color=#ffffff}Then he took the jackknife out of his arms and swung it at the woman.{/color}" with dissolve
    centered "{size=60}{color=#0000ff}Die!! Die!!!{/color}{/size}" with dissolve
    centered "{size=60}{color=#0000ff}Because of you...!!! I..!!{/color}{/size}" with dissolve
    centered "{size=50}{color=#ff0000}{cps=20}Help me!!! Please don't kill me!!! A A A A A A !! *Screaming*{/color}{/cps}{/size}" with dissolve
    centered "{color=#ffffff}The man climbed on the fallen woman and stabbed her.{/color}" with dissolve
    centered "{color=#ffffff}The woman resisted with a terrible scream, but then stopped breathing.{/color}" with dissolve
    centered "{color=#0000ff}Mr. Bartender, I finally did it...!{/color}" with dissolve
    centered "{color=#0000ff}I finally found her..!!{/color}" with dissolve
    centered "{color=#0000ff}Haha…!{/color}" with dissolve
    centered "{color=#0000ff}{cps=20}{size=50}Ha Ha Ha Ha Ha Ha Ha Ha ! ! !{/cps}{/color}{/size}" with dissolve
    centered "{color=#ffffff}Soon after, the man's body slowly began to crumble.{/color}" with dissolve
    centered "{color=#ffffff}The man laughed crazily without even knowing that his body was breaking, and so disappeared.{/color}" with dissolve
    centered "{color=#ffffff}The blood of the woman who was stabbed dozens or hundreds of times in the lug placed at the door was coloured.{/color}" with dissolve

    jump END_10_Eng

label END_10:
    call screen ED10 with dissolve

screen ED10:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("ED10. 발견")
        textbutton "타이틀로 돌아가기" action MainMenu(confirm=False)

label END_10_Eng:
    call screen ED10_Eng with dissolve

screen ED10_Eng:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("ED10.Discover")
        textbutton "Return to title" action MainMenu(confirm=False)

# Game Over Scean
label Select_fail:
    show M Default at left
    show F Default at right
    with dissolve
    B "……. 아직, 이름은 없는 시험작입니다." with dissolve
    F "어디…."with dissolve
    F "…"with dissolve
    F "…"with dissolve
    F "으음…."with dissolve
    F "…죄송해요, 생각보다 취향은 아니네요…."
    M "…으음, 사람마다 취향이라는게 있으니…."
    M "…저는 그냥, 기억 상실로 내어주십시오."with dissolve
    F "기억 상실? 그런 시그니처는 메뉴판에 없었는데…."
    B "아직 미출시 시험작입니다."
    F "와아, 미출시 시험작이 꽤 많은가 보군요!"
    F "으음…. 새 잔을 시키기엔 너무 배가 부르네요…."
    B "망각, 한 잔 나왔습니다."
    F "와, 예쁘게 생긴 칵테일!"
    M "드셔보시겠습니까?"
    F "으음…. 괜찮아요."
    F "어떤 칵테일인지 물어봐도 괜찮을까요?"
    B "그럼요."
    B "{b}브랜디를 베이스{/b}로, {b}진과 과일주스, 라임 가니쉬{/b}를 사용한 칵테일입니다."
    B "…다음번에 오시면, 취향에 맞는 칵테일을 드리도록 노력하겠습니다."
    F "그렇구나…. 네에, 기회가 되면요."
        
    "여자가 시계를 쳐다본다."with dissolve

    F "아, 벌써 시간이 이렇게!"
    F "으음, 먼저 일어나봐도 될까요?"
    M "당연하죠."
    F "오늘 즐거웠어요. 기회가 되면 또 볼 수 있으면 좋겠네요."
    M "조심히 들어가십시오."
    F "안녕히!"

    hide F Default
    hide M Default
    with dissolve
    show M Default with dissolve
    play sound "SE_Japanese_furin.mp3" fadein 3
    "짤랑, 소리를 내며 여자가 떠났다." with dissolve

    B "…따라가 보지 않아도 괜찮습니까?"with dissolve
    M "내가 여기 온 목적이 겨우 여자 따위가 아니란걸 알잖습니까."

    "남자가 칵테일을 홀짝인다."with dissolve
    M "…아, 역시…."
    M "이 곳의 칵테일은 항상 마법같이 느껴지는군요…."
    B "하하, 그렇습니까?"
    M "아무리 힘든 일도 이 칵테일 하나면 감쪽같이 잊을 수 있죠…."
    M "지금 당장, 아까 떠난 여자의 이름도 헷갈릴 정도니…"
    M "많이 취했나봅니다. …이제 가봐야겠습니다."
    B "하하…. 조심히 들어가십시오."
    B "조만간 다시 뵙겠습니다."
    M "안녕히."

    hide M Default with dissolve
    scene black with dissolve
    centered "{color=#ffffff}남자와 약속한 3년이 지났다.{/color}" with dissolve
    centered "{color=#ffffff}여자는 다시 가게를 찾아오지 않았다.{/color}" with dissolve
    centered "{color=#ffffff}남자는 자신이 찾던 사람을 찾지 못했다.{/color}" with dissolve
    
    scene Background with dissolve
    show M Default with dissolve
    B "오늘이 마지막 날입니다." with dissolve
    B "뜻하신 바는 이루셨는지요?"
    M "…."with dissolve
    M "아뇨, 복수는 커녕 그 여자를 찾지도 못했습니다."
    B "저런…. 안타까운 일이군요."
    M "…"with dissolve
    B "허나 약속된 시간이 다 되었습니다."with dissolve
    B "이번엔 저도 더 도와드릴 수가 없군요."
    B "다시 한 번, 기회를 드리겠습니다."
    M "…감사합니다."with dissolve
    M "제임스, 이번에는 부디 목표를 이루길 바랍니다."
    
    hide Man_default with vpunch
    scene black with pixellate

    centered "{color=#ffffff}직후 남자의 몸이 부숴져갔다.{/color}" with dissolve
    centered "{color=#ffffff}나는 손을 그러쥐어 남자의 파편을 흩뿌렸다.{/color}" with dissolve
    centered "{color=#ffffff}…{/color}"
    centered "{color=#ffffff}…흐음.{/color}"
    centered "{color=#ffffff}이번에는 얼마나 가려나….{/color}" with dissolve

    jump Game_over 

label Select_fail_Eng:
    show M Default at left
    show F Default at right
    with dissolve
    B "……. It's a test work that doesn't have a name yet." with dissolve
    F "Let me try." with dissolve
    F "…"with dissolve
    F "…"with dissolve
    F "Umm…"with dissolve
    F "I’m sorry. It's not my type as much as I thought."
    M "…Well, everyone has their own taste…."
    M "...Can you give me a glass of 'Memory Loss', please?"with dissolve
    F "'Memory Loss'? That's not on the menu."
    B "It's also a test work that hasn't been released yet."
    F "Wow, you have a lot of unreleased recipes."
    F "Unfortunately, I am too full to order a new cup…"
    B "Here’s the cup of ‘Memory Loss’, you ordered"
    F "Oh my god! It looks so pretty!"
    M "Would you like to try some?"
    F "Umm…I’m okay. Thank you."
    F "Instead, can I ask what kind of cocktail it is?"
    B "Sure."
    B "{b}Brand as base{/b}, it's a cocktail with {b}Gin, fruit juice{/b}and {b}lime garnish{/b}"
    B "…If you come next time, I will try to give you a cocktail that suits your taste."
    F "Oh…Sure, if I have a chance. Thank you."
        
    "The woman looks at the clock."with dissolve

    F "Oh my, we spent too much time!"
    F "…I’m so sorry but I should go."
    M "Never mind."
    F "I had a great time today. I hope to see you again later."
    M "Take care of yourself on your way home."
    F "Good bye!"

    hide F Default
    hide M Default
    with dissolve
    show M Default with dissolve
    play sound "SE_Japanese_furin.mp3" fadein 3
    "The woman left with the chime ringing." with dissolve

    B "…Are you okay if you won't follow her?"with dissolve
    M "You know I'm not here for a woman."

    "The man sips the cocktail."with dissolve
    M "…Oh, as pxpected…."
    M "Your cocktails always make me feel like magical…."
    B "Haha. Oh, really?"
    M "No matter how hard anything was, with this cocktail, I can forget it…."
    M "Right now, I'm even confused witht the name of the woman who left earlier…"
    M "…I think I'm very drunk… I've got to go."
    B "Haha…. Be careful on your way back home."
    B "See you soon."
    M "Good bye."

    hide M Default with dissolve
    scene black with dissolve
    centered "{color=#ffffff}It's been 3 years since I promised the man.{/color}" with dissolve
    centered "{color=#ffffff}The woman never visit this bar again.{/color}" with dissolve
    centered "{color=#ffffff}The man failed at find who he was finding.{/color}" with dissolve
    
    scene Background with dissolve
    show M Default with dissolve
    B "Today is the last day." with dissolve
    B "Did you accomplish what you meant?"
    M "…."with dissolve
    M "No, I couldn't even find that woman, left alone my revenge."
    B "Oh…. I'm sorry to hear that."
    M "…"with dissolve
    B "But, the time is over."with dissolve
    B "I can not help you any more in this time."
    B "I'll give you one more chance."
    M "…Thank you."with dissolve
    M "I home you achieve your goal this time, James."
    
    hide Man_default with vpunch
    scene black with pixellate

    centered "{color=#ffffff}Right after that, the man's body was brocken as dust.{/color}" with dissolve
    centered "{color=#ffffff}I clasped my hand and scatered the man's debris.{/color}" with dissolve
    centered "{color=#ffffff}…{/color}"
    centered "{color=#ffffff}…Hmm.{/color}"
    centered "{color=#ffffff}I wonder how long it takes in this time….{/color}" with dissolve

    jump Game_over_Eng

label Game_over:

    call screen Game_over with dissolve

screen Game_over:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("ED0. 회귀")
        textbutton "타이틀로 돌아가기" action MainMenu(confirm=False)

label Game_over_Eng:

    call screen Game_over_Eng with dissolve

screen Game_over_Eng:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("ED0. Return")
        textbutton "Return to title" action MainMenu(confirm=False)
