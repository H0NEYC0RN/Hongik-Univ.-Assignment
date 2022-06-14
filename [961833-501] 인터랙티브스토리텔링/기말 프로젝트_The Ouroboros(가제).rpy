
# 캐릭터 정의
define F = Character('여자', color="FF0000")
define M = Character('남자', color="0000FF")
define B = Character('나', color="000000")

init:

    $ Fst = 0
    $ Scd = 0
    $ Trd = 0

label start:
    #Prologue
    F "프롤로그 라인"
    call Select_1

#1st Select
label Select_1:


    M "레시피 1번 선택"

    menu:

        "A": 
            $ Fst = 1
            call Select_2
        "B":
            $ Fst = 2
            call Select_2
        "C":
            $ Fst = 3
            call Select_2

#2nd Select
label Select_2:
    M "레시피 2번 선택"

    menu:
        "A": 
            $ Scd = 1
            call Select_3
        "B":
            $ Scd = 2
            call Select_3
        "C":
            $ Scd = 3
            call Select_3

#3rd Select
label Select_3:
    M "레시피 3번 선택"

    menu:

        "A": 
            $ Trd = 1
            call Select_result
        "B":
            $ Trd = 2
            call Select_result
        "C":
            $ Trd = 3
            call Select_result

label Select_result:
    B "어디보자.."

    if Fst == 1:
        if Scd == 1 :
            if Trd == 1:
                jump Route_1
            if Trd == 2:
                jump Select_fail
            if Trd == 3:
                jump Select_fail
        if Scd == 2 :
            if Trd == 1:
                jump Select_fail
            if Trd == 2:
                jump Route_2
            if Trd == 3:
                jump Select_fail
        if Scd == 3 :
            if Trd == 1:
                jump Select_fail
            if Trd == 2:
                jump Select_fail
            if Trd == 3:
                jump Route_3

    if Fst == 2:
        if Scd == 1 :
            if Trd == 1:
                jump Route_4
            if Trd == 2:
                jump Select_fail
            if Trd == 3:
                jump Select_fail
        if Scd == 2 :
            if Trd == 1:
                jump Select_fail
            if Trd == 2:
                jump Route_5
            if Trd == 3:
                jump Select_fail
        if Scd == 3 :
            if Trd == 1:
                jump Select_fail
            if Trd == 2:
                jump Select_fail
            if Trd == 3:
                jump Route_6

    if Fst == 3:
        if Scd == 1 :
            if Trd == 1:
                jump Route_7
            if Trd == 2:
                jump Select_fail
            if Trd == 3:
                jump Select_fail
        if Scd == 2 :
            if Trd == 1:
                jump Select_fail
            if Trd == 2:
                jump Route_8
            if Trd == 3:
                jump Select_fail
        if Scd == 3 :
            if Trd == 1:
                jump Select_fail
            if Trd == 2:
                jump Select_fail
            if Trd == 3:
                jump Route_9


# F : 1 / M : 1
label Route_1:
    B "대사출력"
    call screen ED1

screen ED1:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("ED1 : 엔딩명")
        textbutton _("메인 화면으로 돌아가기") action ShowMenu("main_menu")

# F : 2 / M : 1
label Route_2:
    B "대사출력"
    call screen ED2

screen ED2:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("ED2 : 엔딩명")
        textbutton _("메인 화면으로 돌아가기") action ShowMenu("main_menu")

# F : 3 / M : 1
label Route_3:
    B "대사출력"
    call screen ED3

screen ED3:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("ED3 : 엔딩명")
        textbutton _("메인 화면으로 돌아가기") action ShowMenu("main_menu")

# F : 1 / M : 2
label Route_4:
    B "대사출력"
    call screen ED4

screen ED4:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("ED4 : 엔딩명")
        textbutton _("메인 화면으로 돌아가기") action ShowMenu("main_menu")

# F : 2 / M : 2
label Route_5:
    B "대사출력"
    call screen ED5

screen ED5:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("ED5 : 엔딩명")
        textbutton _("메인 화면으로 돌아가기") action ShowMenu("main_menu")

# F : 3 / M : 2
label Route_6:
    B "대사출력"
    call screen ED6

screen ED6:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("ED6 : 엔딩명")
        textbutton _("메인 화면으로 돌아가기") action ShowMenu("main_menu")

# F : 1 / M : 3
label Route_7:
    B "대사출력"
    call screen ED7

screen ED7:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("ED7 : 엔딩명")
        textbutton _("메인 화면으로 돌아가기") action ShowMenu("main_menu")

# F : 2 / M : 3
label Route_8:
    B "대사출력"
    call screen ED8

screen ED8:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("ED8 : 엔딩명")
        textbutton _("메인 화면으로 돌아가기") action ShowMenu("main_menu")

# F : 3 / M : 3
label Route_9:
    B "대사출력"
    call screen ED9

screen ED9:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("ED9 : 엔딩명")
        textbutton _("메인 화면으로 돌아가기") action ShowMenu("main_menu")


# Game Over Scean
label Select_fail:
    F "실패 대사"
    call screen Game_over
    return

screen Game_over:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("Game Over")
        textbutton _("메인 화면으로 돌아가기") action ShowMenu("main_menu")
