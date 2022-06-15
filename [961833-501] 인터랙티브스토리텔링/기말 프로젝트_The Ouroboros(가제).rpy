
# 캐릭터 정의
define F = Character('여자', color="FF0000")
define M = Character('남자', color="0000FF")
define B = Character('나', color="000000")

init:

    $ F_Fst = 0
    $ F_Scd = 0
    $ F_Trd = 0

    $ M_FST = 0
    $ M_SCT = 0
    $ M_TRD = 0

    $ F_End = 0
    $ M_End = 0

label start:
    #Prologue
    F "프롤로그 라인"
    call Main_1

label Main_1:
    F "메인 스토리 도입"
    call Select_1


#1st Select
label Select_1:


    F "레시피 1번 선택"

    menu:

        "A": 
            $ F_Fst = 1
            call Select_2
        "B":
            $ F_Fst = 2
            call Select_2
        "C":
            $ F_Fst = 3
            call Select_2

#2nd Select
label Select_2:
    F "레시피 2번 선택"

    menu:
        "A": 
            $ F_Scd = 1
            call Select_3
        "B":
            $ F_Scd = 2
            call Select_3
        "C":
            $ F_Scd = 3
            call Select_3

#3rd Select
label Select_3:
    F "레시피 3번 선택"

    menu:

        "A": 
            $ F_Trd = 1
            call Select_result_1
        "B":
            $ F_Trd = 2
            call Select_result_1
        "C":
            $ F_Trd = 3
            call Select_result_1

label Select_result_1:
    B "F_레시피 결과"

    if F_Fst == 1:
        if F_Scd == 1 :
            if F_Trd == 1:
                $ F_End = 1
                jump Main_2
            if F_Trd == 2:
                jump Select_fail
            if F_Trd == 3:
                jump Select_fail
        if F_Scd == 2 :
            if F_Trd == 1:
                jump Select_fail
            if F_Trd == 2:
                jump Select_fail
            if F_Trd == 3:
                jump Select_fail
        if F_Scd == 3 :
            if F_Trd == 1:
                jump Select_fail
            if F_Trd == 2:
                jump Select_fail
            if F_Trd == 3:
                jump Select_fail

    if F_Fst == 2:
        if F_Scd == 1 :
            if F_Trd == 1:
                jump Select_fail
            if F_Trd == 2:
                jump Select_fail
            if F_Trd == 3:
                jump Select_fail
        if F_Scd == 2 :
            if F_Trd == 1:
                jump Select_fail
            if F_Trd == 2:
                $ F_End = 2
                jump Main_1
            if F_Trd == 3:
                jump Select_fail
        if F_Scd == 3 :
            if F_Trd == 1:
                jump Select_fail
            if F_Trd == 2:
                jump Select_fail
            if F_Trd == 3:
                jump Select_fail

    if Fst == 3:
        if Scd == 1 :
            if Trd == 1:
                jump Select_fail
            if Trd == 2:
                jump Select_fail
            if Trd == 3:
                jump Select_fail
        if Scd == 2 :
            if Trd == 1:
                jump Select_fail
            if Trd == 2:
                jump Select_fail
            if Trd == 3:
                jump Select_fail
        if Scd == 3 :
            if Trd == 1:
                jump Select_fail
            if Trd == 2:
                jump Select_fail
            if Trd == 3:
                $ F_End = 3
                jump Main_2

#Main_2
label Main_2:
    M "메인 스토리2 도입"
    call Select_4

    #1st Select
label Select_4:
    M "레시피 1번 선택"

    menu:

        "A": 
            $ M_Fst = 1
            call Select_5
        "B":
            $ M_Fst = 2
            call Select_5
        "C":
            $ M_Fst = 3
            call Select_5

#2nd Select
label Select_5:
    M "레시피 2번 선택"

    menu:
        "A": 
            $ M_Scd = 1
            call Select_6
        "B":
            $ M_Scd = 2
            call Select_6
        "C":
            $ M_Scd = 3
            call Select_6

#3rd Select
label Select_6:
    M "레시피 3번 선택"

    menu:

        "A": 
            $ M_Trd = 1
            call Select_result_2
        "B":
            $ M_Trd = 2
            call Select_result_2
        "C":
            $ M_Trd = 3
            call Select_result_2


label Select_result_2:
    B "M_레시피 결과"

    if M_Fst == 1:
        if M_Scd == 1 :
            if M_Trd == 1:
                $ M_End = 1
                call Main_3
            if M_Trd == 2:
                jump Select_fail
            if M_Trd == 3:
                jump Select_fail
        if M_Scd == 2 :
            if M_Trd == 1:
                jump Select_fail
            if M_Trd == 2:
                jump Select_fail
            if M_Trd == 3:
                jump Select_fail
        if M_Scd == 3 :
            if M_Trd == 1:
                jump Select_fail
            if M_Trd == 2:
                jump Select_fail
            if M_Trd == 3:
                jump Select_fail

    if M_Fst == 2:
        if M_Scd == 1 :
            if M_Trd == 1:
                jump Select_fail
            if M_Trd == 2:
                jump Select_fail
            if M_Trd == 3:
                jump Select_fail
        if M_Scd == 2 :
            if M_Trd == 1:
                jump Select_fail
            if M_Trd == 2:
                $ M_End = 2
                call Main_3
            if M_Trd == 3:
                jump Select_fail
        if M_Scd == 3 :
            if M_Trd == 1:
                jump Select_fail
            if M_Trd == 2:
                jump Select_fail
            if M_Trd == 3:
                jump Select_fail

    if M_Fst == 3:
        if M_Scd == 1 :
            if M_Trd == 1:
                jump Select_fail
            if M_Trd == 2:
                jump Select_fail
            if M_Trd == 3:
                jump Select_fail
        if M_Scd == 2 :
            if M_Trd == 1:
                jump Select_fail
            if M_Trd == 2:
                jump Select_fail
            if M_Trd == 3:
                jump Select_fail
        if M_Scd == 3 :
            if M_Trd == 1:
                jump Select_fail
            if M_Trd == 2:
                jump Select_fail
            if M_Trd == 3:
                $ M_End = 3
                call Main_3

label Main_3:
    B "메인 스토리 3 도입"
 
    if F_End == 1:
        if M_End == 1:
            jump Route_1
        if M_End == 2:
            jump Route_4
        if M_End == 3:
            jump Route_7
    if F_End == 2:
        if M_End == 1:
            jump Route_2
        if M_End == 2:
            jump Route_5
        if M_End == 3:
            jump Route_8
    if F_End == 3:
        if M_End == 1:
            jump Route_3
        if M_End == 2:
            jump Route_6
        if M_End == 3:
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
