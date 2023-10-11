################################################
##Фон
################################################
##Мануал
image manual slide1 = "images/manual/Slide (1).png"
image manual slide2 = "images/manual/Slide (2).png"
image manual slide3 = "images/manual/Slide (3).png"
image manual slide4 = "images/manual/Slide (4).png"
image manual slide5 = "images/manual/Slide (5).png"
image manual slide6 = "images/manual/Slide (6).png"
image manual slide7 = "images/manual/Slide (7).png"
image manual slide8 = "images/manual/Slide (8).png"
image manual slide9 = "images/manual/Slide (9).png"
image manual slide10 = "images/manual/Slide (10).png"
image manual slide11 = "images/manual/Slide (11).png"
image manual slide12 = "images/manual/Slide (12).png"
image manual slide13 = "images/manual/Slide (13).png"

image logo = "images/logo.png"
image logo2 = "images/logo2.png"
image sun:
    "images/bc/sun.png"
    rotate 0
    linear 6 rotate 360
    repeat
image bc = "images/bc/bc.png"
image farm spring = "images/bc/farm.png"
image farm autumn = "images/bc/farm(autumn).png"

image calendar1 = "images/calendar1.png"
image calendar2 = "images/calendar2.png"
image plant0 = "images/stage теория.png"
image plant1 = "images/stage Посадка pic1.png"
image plant2 = "images/stage Посадка pic2.png"
image plant3 = "images/stage Посадка pic3.png"
image plant4 = "images/stage Посадка pic0.png"


#Почвы
image soil peaty = "images/bc/soil(peaty).png" #Торфянник
image soil sandy = "images/bc/soil(sandy).png" #Песчаная
image soil sandyloam = "images/bc/soil(sandy loam).png" #Супесчанная
image soil clayey = "images/bc/soil(clayey).png" #Глинистая
image soil loamy = "images/bc/soil(loamy).png" #Суглинистая
image soil humus = "images/bc/soil(humus).png" #Чернозем

##Иконки
image icon_poison = "gui/icon/icon_poison.png"
image icon_nopoison = "gui/icon/icon_nopoison.png"
image icon_fungi = "gui/icon/icon_fungi.png"
image icon_insec = "gui/icon/icon_insec.png"
image icon_herbi = "gui/icon/icon_herbi.png"
image icon_plow = "gui/icon/icon_plow.png"
image icon_fert = "gui/icon/icon_fert.png"
image icon_sandyloam = "gui/icon/icon_sandyloam.png"
image icon_say = "gui/icon/icon_say.png"
image icon_teory = "gui/icon/icon_teory.png"
image icon_answer = "gui/icon/icon_answer.png"
image icon_no = "gui/icon/icon_no.png"
image icon_potato = "gui/icon/icon_potato.png"
image icon_tomato = "gui/icon/icon_tomato.png"
image icon_corn = "gui/icon/icon_corn.png"
image icon_clayey = "gui/icon/icon_clayey.png"
image icon_humus = "gui/icon/icon_humus.png"
image icon_loamy = "gui/icon/icon_loamy.png"
image icon_peaty = "gui/icon/icon_peaty.png"
image icon_sandy = "gui/icon/icon_sandy.png"
image icon_sandyloam = "gui/icon/icon_sandyloam.png"


##эффекты
image poison:
    "images/effect/poison.png" with dissolve
    0.5
    "images/effect/poison2.png" with dissolve
    repeat
image herbi:
    "images/effect/herbi.png" with dissolve
    0.5
    "images/effect/herbi2.png" with dissolve
    repeat
image insec:
    "images/effect/insec.png" with dissolve
    0.5
    "images/effect/insec2.png" with dissolve
    repeat
image fungi:
    "images/effect/fungi.png" with dissolve
    0.5
    "images/effect/fungi2.png" with dissolve
    repeat
image addN:
    "images/effect/N+.png" with dissolve
    1
    "images/effect/N+2.png" with dissolve
    1
    repeat
image addE:
    "images/effect/Е+.png" with dissolve
    1
    "images/effect/Е+2.png" with dissolve
    1
    repeat
image addK:
    "images/effect/K+.png" with dissolve
    1
    "images/effect/K+2.png" with dissolve
    1
    repeat
image addP:
    "images/effect/P+.png" with dissolve
    1
    "images/effect/P+2.png" with dissolve
    1
    repeat
image insects:
    "images/effect/insects2.png" with dissolve
    0.2
    "images/effect/insects.png" with dissolve
    0.2
    "images/effect/insects3.png" with dissolve
    0.2
    repeat
image potatoplowing:
    "images/effect/potato plowing.png" with dissolve
    0.4
    "images/effect/potato plowing2.png"
    0.4
    "images/effect/potato plowing3.png"
    0.4
    repeat
image tomatoplowing:
    "images/effect/tomato plowing.png" with dissolve
    0.4
    "images/effect/tomato plowing2.png"
    0.4
    "images/effect/tomato plowing3.png"
    0.4
    repeat
################################################
##Овощи
################################################
##Картошка
image ptthermometer = "images/vegetables/potato/thermometer.png"
image potato baglow = "images/vegetables/potato/bag(low).png"
image potato bagmedium = "images/vegetables/potato/bag(medium).png"
image potato baggood = "images/vegetables/potato/bag(good).png"
image potato stage1:
    "images/vegetables/potato/Stage 1.png"
    0.3
    "images/vegetables/potato/Stage 2.png" with dissolve
image potato stage1damaged:
    "images/vegetables/potato/Stage 2.png"
    0.3
    "images/vegetables/potato/Stage 2(damaged).png" with dissolve
image potato stage2damaged:
    "images/vegetables/potato/Stage 2(damaged).png"
    0.3
    "images/vegetables/potato/Stage 3.png" with dissolve
image potato stage2:
    "images/vegetables/potato/Stage 2.png"
    0.3
    "images/vegetables/potato/Stage 3.png" with dissolve
image potato stage3low:
    "images/vegetables/potato/Stage 3.png"
    0.3
    "images/vegetables/potato/Stage 4(low).png" with dissolve
    0.5
    "images/vegetables/potato/Stage 5(low).png"with dissolve
image potato stage3medium:
    "images/vegetables/potato/Stage 3.png"
    0.3
    "images/vegetables/potato/Stage 4(medium).png" with dissolve
    0.5
    "images/vegetables/potato/Stage 5(medium).png"with dissolve
image potato stage3good:
    "images/vegetables/potato/Stage 3.png"
    0.3
    "images/vegetables/potato/Stage 4(good).png" with dissolve
    0.5
    "images/vegetables/potato/Stage 5(good).png"with dissolve

##Справочные пикчи по картофелю
image ptattach1 = "images/vegetables/potato/Attach1.png"
image ptattach2 = "images/vegetables/potato/Attach2.png"
image ptattach3 = "images/vegetables/potato/Attach3.png"
image ptattach4 = "images/vegetables/potato/Attach4.png"
image ptattach5 = "images/vegetables/potato/Attach5.png"
image ptattach6 = "images/vegetables/potato/Attach6.png"
image ptattach7 = "images/vegetables/potato/Attach7.png"
image ptattach8 = "images/vegetables/potato/Attach8.png"
image ptattach9 = "images/vegetables/potato/Attach9.png"
image ptattach10 = "images/vegetables/potato/Attach10.png"
image ptattach11 = "images/vegetables/potato/Attach11.png"
image ptattach12 = "images/vegetables/potato/Attach12.png"
image ptattach13 = "images/vegetables/potato/Attach13.png"
image ptattach14 = "images/vegetables/potato/Attach14.png"
image ptattach15 = "images/vegetables/potato/Attach15.png"
image ptattach16 = "images/vegetables/potato/Attach16.png"

##Помидор
#idt
image tmthermometer = "images/vegetables/tomato/thermometer.png"
image tomato idtstage0 = "images/vegetables/tomato/Stage 0(idt).png"
image tomato idtstage1:
    "images/vegetables/tomato/Stage 1(idt).png"
    0.3
    "images/vegetables/tomato/Stage 2(idt).png" with dissolve
image tomato idtstage1damaged:
    "images/vegetables/tomato/Stage 2(idt).png"
    0.3
    "images/vegetables/tomato/Stage 2(idt-damaged).png" with dissolve
image tomato idtstage2:
    "images/vegetables/tomato/Stage 2(idt).png"
    0.3
    "images/vegetables/tomato/Stage 3(idt).png" with dissolve
image tomato idtstage2damaged:
    "images/vegetables/tomato/Stage 2(idt-damaged).png"
    0.3
    "images/vegetables/tomato/Stage 3(idt).png" with dissolve
image tomato idtstage3low:
    "images/vegetables/tomato/Stage 3(idt).png"
    0.3
    "images/vegetables/tomato/Stage 3(idt).png" with dissolve
image tomato idtstage3medium:
    "images/vegetables/tomato/Stage 4(itdt-low).png"
    0.3
    "images/vegetables/tomato/Stage 4(itdt-medium).png" with dissolve
image tomato idtstage3good:
    "images/vegetables/tomato/Stage 3(idt).png"
    0.3
    "images/vegetables/tomato/Stage 4(itdt-good).png" with dissolve

#dt
image tomato stage1:
    "images/vegetables/tomato/Stage 1.png"
    0.3
    "images/vegetables/tomato/Stage 2.png" with dissolve
image tomato stage1damaged:
    "images/vegetables/tomato/Stage 2.png"
    0.3
    "images/vegetables/tomato/Stage 2(damaged).png" with dissolve
image tomato stage2:
    "images/vegetables/tomato/Stage 2.png"
    0.3
    "images/vegetables/tomato/Stage 3(nobelt).png" with dissolve
image tomato stage2damaged:
    "images/vegetables/tomato/Stage 2(damaged).png"
    0.3
    "images/vegetables/tomato/Stage 3(nobelt).png" with dissolve
image tomato stage3low:
    "images/vegetables/tomato/Stage 4(nobelt-low).png"
    0.3
    "images/vegetables/tomato/Stage 4(nobelt-low).png" with dissolve
image tomato stage3medium:
    "images/vegetables/tomato/Stage 3(nobelt).png"
    0.3
    "images/vegetables/tomato/Stage 4(nobelt-medium).png" with dissolve
image tomato stage3good:
    "images/vegetables/tomato/Stage 3(nobelt).png"
    0.3
    "images/vegetables/tomato/Stage 4(nobelt-good).png" with dissolve
##подвяз
image tomato stage2belt:
    "images/vegetables/tomato/Stage 3(nobelt).png"
    0.3
    "images/vegetables/tomato/Stage 3(belt).png" with dissolve
image tomato stage3beltlow:
    "images/vegetables/tomato/Stage 3(belt).png"
    0.3
    "images/vegetables/tomato/Stage 4(belt-low).png" with dissolve
image tomato stage3beltmedium:
    "images/vegetables/tomato/Stage 3(belt).png"
    0.3
    "images/vegetables/tomato/Stage 4(belt-medium).png" with dissolve
image tomato stage3beltgood:
    "images/vegetables/tomato/Stage 3(belt).png"
    0.3
    "images/vegetables/tomato/Stage 3(belt-good).png" with dissolve

##Справочные пикчи по помидору
image tmattach1 = "images/vegetables/tomato/Attach1.png"
image tmattach2 = "images/vegetables/tomato/Attach2.png"
image tmattach3 = "images/vegetables/tomato/Attach3.png"
image tmattach4 = "images/vegetables/tomato/Attach4.png"
image tmattach5 = "images/vegetables/tomato/Attach5.png"
image tmattach6 = "images/vegetables/tomato/Attach6.png"
image tmattach7 = "images/vegetables/tomato/Attach7.png"
image tmattach8 = "images/vegetables/tomato/Attach8.png"
image tmattach9 = "images/vegetables/tomato/Attach9.png"
image tmattach10 = "images/vegetables/tomato/Attach10.png"
image tmattach11 = "images/vegetables/tomato/Attach11.png"
image tmattach12 = "images/vegetables/tomato/Attach12.png"
image tmattach13 = "images/vegetables/tomato/Attach13.png"
image tmattach14 = "images/vegetables/tomato/Attach14.png"
image tmattach15 = "images/vegetables/tomato/Attach15.png"
image tmattach16 = "images/vegetables/tomato/Attach16.png"
################################################
##Спрайты
################################################
image sv angry:
    "images/sprite/Sveta/angry.png"
    choice:
        pause 3
    choice:
        pause 5
    choice:
        pause 7
    "images/sprite/Sveta/angry2.png"
    0.25
    repeat
image sv smile:
    "images/sprite/Sveta/smile.png"
    choice:
        pause 3
    choice:
        pause 5
    choice:
        pause 7
    "images/sprite/Sveta/smile2.png"
    0.25
    repeat
image sv sad:
    "images/sprite/Sveta/sad.png"
    choice:
        pause 3
    choice:
        pause 5
    choice:
        pause 7
    "images/sprite/Sveta/sad2.png"
    0.25
    repeat
image sv doubt:
    "images/sprite/Sveta/doubt.png"
    choice:
        pause 3
    choice:
        pause 5
    choice:
        pause 7
    "images/sprite/Sveta/calm3.png"
    0.25
    repeat
image sv calm:
    "images/sprite/Sveta/calm.png"
    choice:
        pause 3
    choice:
        pause 5
    choice:
        pause 7
    "images/sprite/Sveta/calm3.png"
    0.25
    repeat
image sv calm2:
    "images/sprite/Sveta/calm2.png"
    choice:
        pause 3
    choice:
        pause 5
    choice:
        pause 7
    "images/sprite/Sveta/smile2.png"
    0.25
    repeat
