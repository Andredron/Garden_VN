label potato_route:
    $ t = 0
    $ soil= ""
    $ cult=""
    $ err = 0
    $ Ur=0
    $ taste=0
    $ month = "???"
    $ it = 0
    $ point = 0
    $ stage_name = "???"
    $ wee = 0
    $ herbi = 0
    $ insec = 0
    $ fungi = 0
    $ fert = 0
    $ renpy.block_rollback()
    nvl clear
    show screen staty
    $ cult = "Картофель"
    $ Ur = 0
    show sv smile at centre with ease
##Блок для объяснений
##Что такое картошка?
##Рассказ о том какой месяц
##При какой температуре лучше садить картофель
    sv "О, значит картофель. Хороший выбор!"
    show sv at right2 with ease
    play sound picturebuzzer
    show ptattach4 behind sv at attach with easeinright
    sv "{color=#ffd040}Картофель{/color} одна из важнейших культур, буквально второй хлеб."
    sv "Это крахмалистый овощ из семейства пасленовых."
    sv "Она занимает первое место наряду с пшеницей, рисом и кукурузой, а её применение очень широкое."
    sv "Картофель помимо употребления в пище так же служит сырьем для спирта, крахмала, глюкозы и так далее."
    hide ptattach4
    show sv at centre with ease
    sv "Хочешь послушать историю данной культуры?"
    hide sv
    menu:
        "{image=icon_say}Да{image=icon_say}":
            $ renpy.block_rollback()
            $ stage_name = "История"
            $ svFrendship +=10
            show sv smile
            sv "О, неужели и вправду интересно? Тогда слушай."
            sv "Картофель родом из Лантинской америки и являлся одним из основных продуктов питания у латиноамериканских индейцев."
            show sv at right2 with ease
            play sound picturebuzzer
            show ptattach2 behind sv at attach4 with easeinright
            sv "В Европу он попал в 1551 году, когда испанский путешественник Сьеса де Леон возвратился на родину из Перу."
            hide ptattach2
            play sound picturebuzzer
            show ptattach3 behind sv at attach4 with easeinright
            sv "В России же картофель появился благодаря Петору I."
            sv "Он велел сажать картофель как и крупным владельцам, так и крестьянам в надежде хоть как-то победить голод и уменьшить последствия зерновой неурожайности."
            hide ptattach3
            show sv calm at centre with ease
            sv "Но по итогу народ был в ярости. Они сопротивлялись и протестовали, говоря, что картофель проклят и ядовит."
            sv "Скорее всего из-за того, что они не выкапывали его, а ели ягоды наверху."
            show sv at right2 with ease
            play sound picturebuzzer
            show ptattach1 behind sv at attach with easeinright
            sv "Они и вправду ядовитые. {color=#ffd040}2-3 штуки могут справоцировать серьезное отравление{/color}, а если съесть больше то можешь сразу собирать всех родствеников на поминках!"
            sv "Так что не надо даже пробывать их есть. Я не одобряю самоубийство."
            hide ptattach1
            show sv smile at centre with ease
            sv "Однако сейчас картофель едят почти во всех странах мира, однако особую любовь к нему питают Белорусы."
            show sv at right2 with ease
            play sound picturebuzzer
            show ptattach16 behind sv at attach with easeinright
            sv "В Беларуси картофель появился примерно в середине XVII века, благодаря Станиславу Августу Понятовскому, который в то время был королем Речи Посполитой."
            hide ptattach16
            show sv at centre with ease
            sv "Сейчас трудно представить свою жизнь без варенной картошечки с укропом и маслецем или же той самой, что жарят на масле во всяких дешевых забегаловках в городе."
            sv "Надеюсь тебе было интересно это послушать."
        "{image=icon_no}Нет{image=icon_no}":
            $ renpy.block_rollback()
            show sv calm
            sv "Ну как хочешь."
    $ renpy.block_rollback()
    show sv smile
    sv "Тогда время начинать!"
    $ stage_name = "Месяц"
    sv "Первым этапом является {u}выбор месяца для посадки{/u}."
    label ptref1:
        sv "Лучшим месяцем для посадки картофеля является {color=#ffd040}май{/color}. Можно сказать идеал."
        sv "Будет отлично если температура почвы на глубине заделки клубней будет от +7 до +8, но самым идеальным вариантом будет являться от +10 и выше."
        show sv calm
        sv "Можно попытаться посадить и в {color=#ffd040}апреле{/color}, но может случиться так, что резко начнуться холода, а картофель не любит холод."
        sv "По этой же причине {color=#ffd040}март{/color} является наихудшим вариантом для посадки. Холод, грязь и слякоть."
        sv "Если посадишь в марте - считай семена на ветер. А семена сейчас не самое дешевое удовольствие."
        hide sv
        menu:
            "{image=icon_answer}А можно ли посадить картофель в июне?{image=icon_answer}":
                show sv calm
                sv "Крайне не советую."
                sv "Из-за наступившей жары клубни не успеют сформироваться, и по итогу урожая не будет."
                sv "Касаемо жары, если температура превысит за +30, то урожая не будет."
                sv "Будь внимателен к температуре."
        sv "Надеюсь ты все понял или тебе повторить?"
        hide sv
        menu:
            "{image=icon_say}Все понятно!{image=icon_say}":
                $ renpy.block_rollback()
                show sv calm2
                sv "Я ж надеюсь, ты сделаешь правильный выбор."
                hide sv
                jump ptmenumount
            "{image=icon_answer}Можешь ещё раз повторить, пожалуйста?{image=icon_answer}":
                $ renpy.block_rollback()
                show sv smile at centre
                sv "Хорошо, но в этот раз слушай внимательно."
                jump ptref1
    label ptmenumount:
        show screen staty
        scene bc
        show sun at sunfarm
        show farm spring
        show soil peaty
        show calendar1 at left2
        menu:
            "Март":
                hide screen staty
                scene black with fade2
                play sound badend
                show text "Поздравляю, ваш урожай замерз!"
                $ renpy.pause(3, hard=True)
                hide text
                $ renpy.block_rollback()
                jump ptmenumount
            "Апрель":
                $ renpy.block_rollback()
                hide calendar1
                $ month="Апрель"
                show sv calm
                sv "Апрель значит? Тогда будь внимателен к температуре."
            "Май":
                $ renpy.block_rollback()
                hide calendar1
                play sound wow
                $ month="Май"
                show sv smile
                sv "Отличный выбор!"
            "Июнь":
                hide screen staty
                scene black with fade2
                play sound badend
                show text "Поздравляю, ваша картошка не смогла прорости!"
                $ renpy.pause(3, hard=True)
                hide text
                $ renpy.block_rollback()
                jump ptmenumount
    show sv smile
    sv "Чтож с месяцем посадки мы определелились!"
    label ptmenut:
        $ renpy.block_rollback()
        $ stage_name = "Температура"
        show screen staty
        scene bc
        show sun at sunfarm
        show farm spring
        show soil peaty
        show sv calm2
        show ptthermometer at left2 with easeinright
        $ t=renpy.input(_("{color=#ffd040}Как думаешь какая сейчас температура?{/color}"),length=3, default= 0, allow = "1234567890-+").strip()
        $ t=int(t)
        if t>=30:
            hide screen staty
            scene black with fade2
            play sound badend
            show text "Поздравляю, вы сожгли свой урожай!"
            $ renpy.pause(3, hard=True)
            hide text
            $ t=0
            $ renpy.block_rollback()
            jump ptmenut
        if t<30 and t>=7:
            hide ptthermometer
            play sound wow
            show sv smile
            sv "Я тоже так думаю!"
            jump potato_stage2
        if t<7 and month=="Май":
            hide ptthermometer
            play sound gloom
            show sv doubt
            sv "Ты чего? В мае не может быть так холодно!"
            $ t=0
            jump ptmenut
        if t<7 and month=="Апрель":
            hide screen staty
            scene black with fade2
            play sound badend
            show text "Поздравляю, ваш урожай замерз!"
            $ renpy.pause(3, hard=True)
            $ t=0
            hide text
            $ renpy.block_rollback()
            jump ptmenut

label potato_stage2:
##Блок для объяснений
##Пояснение за почвы
    $ renpy.block_rollback()
    $ stage_name = "Почва"
    sv "Следующим этапом является {u}почва{/u}."
    label ptref2:
        show sv smile
        sv "Картошку можно сажать почти где угодно, главное грамотно подойти к обработке почвы."
        sv "Картофелю не подходят тяжелые {color=#ffd040}глинистые{/color} и {color=#ffd040}суглинистые почвы{/color} с кучей влаги. Картофель не любит переизбыток влаги."
        show sv calm
        sv "В таких условиях он будет крайне плохо расти."
        sv "Если уже не где, то можно слегка улучшить ситуацию добавив в почву немного золы, песка, а ещё навоза и компоста."
        sv "Возможно что-то да и будет."
        show sv smile
        sv "Однако самая идеальная почва для картофеля это легкие почвы - {color=#ffd040}песчанные{/color} или {color=#ffd040}супечасные почвы{/color}."
        sv "{color=#ffd040}Дерновая{/color} и {color=#ffd040}торфянник{/color} тоже сойдет."
        sv"Будет отлично если это будет ровная и сухая почва."
        hide sv
        menu:
            "{image=icon_say}Все понятно!{image=icon_say}":
                jump menusoil
            "{image=icon_answer}Можешь ещё раз объяснить?{image=icon_answer}":
                show sv smile at centre
                sv "Хорошо, но в этот раз слушай внимательно."
                jump ptref2
label menusoil:
    show sv smile
    sv "Какая твоя почва на огороде?"
    hide sv
    menu:
        "{image=icon_clayey}Суглинистая почва{image=icon_clayey}":
            $ renpy.block_rollback()
            show soil loamy behind sv with dissolve
            $ soil = "Суглинистая"
            $ taste +=1
            show sv doubt
            sv "Ты уверен? Ладно."
            jump potato_stage3
        "{image=icon_sandyloam}Супесчанная почва{image=icon_sandyloam}":
            $ renpy.block_rollback()
            show soil sandyloam behind sv with dissolve
            play sound wow
            $ soil = "Супесчанная"
            $ taste += 12
            show sv calm2
            sv "Отличный выбор!"
            jump potato_stage3
        "{image=icon_sandy}Песчаная почва{image=icon_sandy}":
            $ renpy.block_rollback()
            show soil sandy behind sv with dissolve
            play sound wow
            $ soil = "Песчаная"
            $ taste += 12
            show sv calm2
            sv "Отличный выбор!"
            jump potato_stage3
        "{image=icon_peaty}Торфянная почва{image=icon_peaty}":
            $ renpy.block_rollback()
            show soil peaty behind sv with dissolve
            play sound wow
            $ soil = "Торфянник"
            $ taste += 12
            show sv calm2
            sv "Отличный выбор!"
            jump potato_stage3
        "{image=icon_humus}Дерновая почва{image=icon_humus}":
            $ renpy.block_rollback()
            show soil humus behind sv with dissolve
            play sound wow
            $ soil = "Дерновая"
            $ taste += 12
            show sv calm2
            sv "Отличный выбор!"
            jump potato_stage3

label potato_stage3:
    $ renpy.block_rollback()
    $ stage_name = "Удобрение"
    show sv smile
    sv "Теперь давай займемся {u}удобрением{/u}."
##Блок для объяснений
##Объяснение про удобрения, их соотношение и т.д
label ptref3:
    sv "Картофель удобряют для хорошего урожая и увелечения срока его хранения."
    sv "Почва может не всегда содержать достаточное количество пиательных веществ, чтобы взошла хорошая картошка."
    sv "Самыми {u}основными пительными элементами{/u} для картофеля являются: {color=#ffd040}азот{/color}, {color=#ffd040}фосфор{/color} и {color=#ffd040}калий{/color}."
    show sv sad
    sv "Картошка довольно требовательна к составу грунта."
    sv "Она быстро высывает все питательные вещества из земли, тем самым истощая её."
    sv "Если не использовать специальные удобрения для картофеля, урожайность с каждым годом будет снижаться."
    show sv smile
    sv "Так же нужно соблюдать дозы внесения удобрений в почву."
    sv "Если азот больше 120 килограмм на гектар, то урожай станет загрязненным нитрарами и непригодным для пищи."
    sv "Остальные удобрения не навредят почве никак."
    show sv at right3 with ease
    play sound picturebuzzer
    show ptattach5 behind sv at attach with easeinright
    sv "Вот таблица которая тебе поможет."
    sv "Если будешь следовать ей, то получишь примерно такие результаты."
    sv "Надеюсь все понятно?"
    hide ptattach5
    hide sv
    menu:
        "{image=icon_say}Все понятно!{image=icon_say}":
            jump ptfert
        "{image=icon_answer}Можешь ещё раз повторить, пожалуйста?{image=icon_answer}":
            show sv smile at centre
            sv "Хорошо, но в этот раз слушай внимательно."
            jump ptref3
label ptfert:
    show sv smile
    $ Nu = renpy.input(_("{color=#ffd040}Введите количество азотного удобрения(кг/га).{/color}"),length=3, default= 0, allow = "1234567890").strip()
    $ Nu = int(Nu)
    $ renpy.block_rollback()
    if Nu>=299:
        show sv angry
        play sound shout
        sv "[pl_name], что ты творишь? Хочешь уничтожить урожай?" with hpunch
        jump ptfert
    else:
        if Nu==0:
            $ Nu=0
        else:
            window hide
            hide screen staty
            hide sv
            play sound addfert
            show addN
            $ renpy.pause(1.5, hard=True)
            hide addN
            show screen staty
            show sv smile
            ##Подсчет урожайности по азотному удобрению
            if 120>Nu>80:
                $Ur+=125
            elif 21>Nu>5:
                $Ur+=12
            elif 81>Nu>49:
                $Ur+=25
            elif Nu<6:
                $Ur+=3
            elif 300>Nu>119:
                $Ur+=45
                $ taste-=12
            elif 50>Nu>20:
                $Ur+=16
    ##Подсчет урожайности по азотному удобрению
        $ Ku = renpy.input(_("{color=#ffd040}Введите количество калийного удобрения(кг/га).{/color}"),length=3, default= 0, allow = "1234567890").strip()
        $ Ku = int(Ku)
        $ renpy.block_rollback()
        if Ku>0:
            window hide
            hide screen staty
            hide sv
            play sound addfert
            show addK
            $ renpy.pause(1.5, hard=True)
            hide addK
            show screen staty
            show sv smile
    ##Подсчет урожайности по калийному удобрению
        if Ku>119:
            $Ur+=125
        elif 21>Ku>5:
            $Ur+=12
        elif 120>Ku>79:
            $Ur+=25
        elif Ku<6:
            $Ur+=3
        elif 80>Ku>20:
            $Ur+=16
        $ Pu = renpy.input(_("{color=#ffd040}Введите количество фосфорного удобрения(кг/га).{/color}"),length=3, default= 0, allow = "1234567890").strip()
        $ Pu = int(Ku)
        $ renpy.block_rollback()
        if Pu>0:
            window hide
            hide screen staty
            hide sv
            play sound addfert
            show addP
            $ renpy.pause(1.5, hard=True)
            hide addP
            show screen staty
            show sv smile
        ##Подсчет урожайности по фосфорному удобрению
            if Pu>80:
                $Ur+=125
            elif 21>Pu>5:
                $Ur+=12
            elif 81>Pu>49:
                $Ur+=25
            elif Pu<6:
                $Ur+=3
            elif 50>Nu>20:
                $Ur+=16
        $ Eu = renpy.input(_("{color=#ffd040}Введите количество органического удобрения(т/га).{/color}"),length=3, default= 0, allow = "1234567890").strip()
        $ Eu = int(Eu)
        $ renpy.block_rollback()
        if Eu>0:
            window hide
            hide screen staty
            hide sv
            play sound addfert
            show addE
            $ renpy.pause(1.5, hard=True)
            hide addE
            show screen staty
            show sv smile
    ##Подсчет урожайности по естественному удобрению
        if 61>Eu>49:
            $Ur+=125
        elif 51>Eu>5:
            $Ur+=12
        elif 41>Eu>29:
            $Ur+=25
        elif 0<Eu<10:
            $Ur+=3
        elif Eu>120:
            $Ur+=100
        elif 30>Eu>9:
            $Ur+=16
        elif Eu==0:
            $Ur+=1
    jump potato_stage5
label potato_stage5:
    $ renpy.block_rollback()
    show screen staty
    $ stage_name = "Посадка"
    with fade2
    show sv smile
    sv "Отличненько!"
    sv "Теперь поговорим о тонкостях посадки картофеля."
##Блок для объяснений
##Расстояние для посадки картошки между рядами и друг другом
label ptref5:
    sv "То на какую глубину, на каком расстоянии будут ряды друг от друга и расстояние между самими клубнями закрывать глаза не стоит."
    sv "Не нужно думать, что если ты посадишь картошку до ядра земли - то и так сойдет."
    sv "Глубина посадки картофеля зависит от того в какой почве ты его посадил."
    sv "Если твоя почва - это {color=#ffd040}торфянник{/color} и {color=#ffd040}дерновая{/color} то садить картофель нужно на глубине {u}12-14 сантиметра{/u}."
    sv "Если {color=#ffd040}суглинистая{/color} или {color=#ffd040}легкосуглинистая{/color}, то лучше её садить на глубине {u}6-8{/u} сантиметра."
    sv "Если же {color=#ffd040}песчанная{/color} или {color=#ffd040}супесчанная{/color}, то {u}10-14 сантиметра{/u}."
    sv "Так же картофель нельзя сажать достаточно близко друг другу. Например, если между рядами будет меньше 75 сантиметров, то для картошки будет мало места."
    sv "Конечно, если ты не садил картофель на {color=#ffd040}суглинистых{/color} и {color=#ffd040}легкосуглинистых{/color}."
    sv "При 50 сантимиетрах между рядами, а между самими клубнями 40 сантиметров - более менее сгладит ситуацию."
    sv "Самым идеальным расстоянием между клубнями будет 30-40 сантиметров."
    sv "Надеюсь ты все понял."
    hide sv
    menu:
        "{image=icon_say}Все понятно!{image=icon_say}":
            $ renpy.block_rollback()
            jump wd1
        "{image=icon_answer}Можешь ещё раз повторить, пожалуйста?{image=icon_answer}":
            $ renpy.block_rollback()
            show sv smile at centre
            sv "Хорошо, но в этот раз слушай внимательно."
            jump ptref5
label wd1:
    show sv smile at centre
    sv "Расстояние междурядий картофеля?"
    hide sv
    show plant1 at left4 with easeinright
    play sound picturebuzzer
    menu:
        "50 см":
            hide plant1
            $ taste=0
            $ q=50
        "70 см":
            hide plant1
            $ taste=6
        "75 см":
            $ q=75
            play sound wow
            hide plant1
            $ taste+=12
            $ q=75

    show sv smile at centre
    sv "На каком расстоянии друг от друга ты посадишь картошку?"
    hide sv
    show plant2 at left4 with easeinright
    play sound picturebuzzer
    menu:
        "20 см":
            hide plant2
            if q==75:
                play sound wow
                $taste+=12
            else:
                $ taste=0
        "30 см":
            hide plant2
            if q==75:
                play sound wow
                $taste+=12
            else:
                $ taste+=6
        "40 см":
            hide plant2
            play sound wow
            if q==50 and (soil=="Суглинистая" or soil=="Легкосуглинистая"):
                $ taste +=24
            else:
                $ taste+=0
            $ taste +=12
    show sv smile at centre
    sv "На какую глубину посадишь картошку?"
    hide sv
    show plant3 at left5 with easeinright
    play sound picturebuzzer
    menu:
        "7 см":
            hide plant3
            if soil=="Суглинистая" or soil=="Легкосуглинистая":
                play sound wow
                $taste+=12
            else:
                $taste+=6
        "10 см":
            hide plant3
            if soil=="Супесчанная" or soil=="Песчаная":
                play sound wow
                $taste+=12
            else:
                $taste+=6
        "13 см":
            hide plant3
            if soil=="Торфянник" or soil=="Дерновая" or soil=="Супесчанная" or soil=="Песчаная":
                play sound wow
                $taste+=12
            else:
                $taste+=6
        "20 см":
            hide plant3
            $taste =0
        "3 см":
            hide plant3
            $taste -=5
            jump potato_stage6
label potato_stage6:
    $ renpy.block_rollback()
    hide screen staty
    hide sv
    with fade2
    show potato stage1
    play sound grow
    $ renpy.pause(1, hard=True)
    show sv smile
    sv"Вооот, смотри! Как выросла!"
    show screen staty
    $ stage_name = "Уход"
    show sv smile
    sv "И так следующий этап, это уход за посадками."
    label ptref6:
        sv "В уход за ними входит прополка от сорняков и защита от насекомых и болезней."
        show sv sad
        sv "Картофель повреждают свыше 60-ти видов насекомых и 23 вида вирусов."
        show sv angry at right2 with ease
        play sound picturebuzzer
        show ptattach6 at attach2 with easeinright
        sv "Говоря о насекомых я имею ввиду таких как {color=#ffd040}короладский жук{/color}!"
        sv "Самый живучий вредитель огорода!"
        show ptattach10 at attach3 with easeinright
        sv "Питается листьями, молодыми побегами и даже клубнями растений!"
        sv "Помимо картофеля так же обитает на баклажанах, сладком перце и помидор."
        sv "Из-за поврежедений листьев фотосинтез снижается и развитие клубней по итогу останавливается."
        sv "Уничтожив один куст, они моментально перебираются на следующий."
        hide ptattach6
        hide ptattach10
        play sound picturebuzzer
        show ptattach14 at attach4 with easeinright
        sv "Так же его личинки отличаются особой прожорливостью! Они могут уничтожить всю делянку за несколько дней!"
        hide ptattach14
        play sound picturebuzzer
        show ptattach7 at attach4 with easeinright
        sv "Так же есть такой вредитель как {color=#ffd040}картофельная тля{/color}."
        sv "Тля поселяется на нижней стороне листьев и высасывает из них сок."
        sv "Из-за чего растения отстают в росте, цветки мелкие, цветение происходит не одновременно. По итогу урожай мельче обычного."
        sv "Так же тля является разносчиком вирусных болезней."
        hide ptattach7
        play sound picturebuzzer
        show ptattach15 at attach2 with easeinright
        sv "Ещё одним вредителем картофеля является {color=#ffd040}провлочник{/color}."
        play sound picturebuzzer
        show ptattach9 at attach3 with easeinright
        sv "Широко распространенный вредитель корнеплодов, и, особенно, картофеля. Повреждают корни и клубни."
        show sv sad
        sv "Потеря урожая составляет аж 30-50%%! К тому же такая картошка теряет свой товарный вид."
        sv "Это ужасно!"
        hide ptattach15
        hide ptattach9
        show sv angry
        play sound picturebuzzer
        show ptattach8 at attach4 with easeinright
        sv "Ещё хочу рассказать тебе про {color=#ffd040}картофельную моль{/color}."
        sv "Карантинный вредитель. Повреждает листья, стебли и клубни."
        show sv sad
        sv "При огромной числености потеря урожая аж 80%%!"
        show sv calm2
        sv "Однако при температуре почвы от -4 и ниже, они погибают."
        hide ptattach8
        show sv sad at centre with ease
        sv "Так же хочу тебе рассказать о некоторых болезнях картофеля."
        show sv at right2 with ease
        play sound picturebuzzer
        show ptattach11 behind sv at attach with easeinright
        sv "Самая распространенная болезнь картофеля - это {color=#ffd040}фитофтороз{/color}."
        sv "Он появляется в середине лета от сушественного перепада температуры и сильной влажности."
        sv "Его признаками является появление темных пятен с нижней стороны листа."
        sv "Вскоре на этом месте образуется грязно-белый налет, а через некоторое время на стебле появляеться бурый оттенок."
        sv "Происходит прекращение фотосинтеза, клубни перестают расти и растение усыхает."
        show sv calm
        sv "В серьезном случае необходимо немедленно удалить растение с грядки. Самый лучший вариант - это сжечь."
        show sv calm2
        sv "Кстати, интересный факт. Если рядом с картофелем посадить горчицу, то она не даст развиться фитофторозу."
        show sv sad
        hide ptattach11
        play sound picturebuzzer
        show ptattach12 behind sv at attach with easeinright
        sv "Ещё одной грибковой болезнью является {color=#ffd040}парша{/color}."
        sv "Её признаками яляются серо-белые пятна на листьях и стебле, а так же на корне. Сама картошка покрывается язвами красноватого цвета."
        hide ptattach12
        play sound picturebuzzer
        show ptattach13 behind sv at attach with easeinright
        sv "Так же есть {color=#ffd040}рак картофеля{/color}."
        sv "На картофеле появляются наросты, а если ничего не предпринимать то на наземной части появляются новообразования."
        show sv angry
        sv "Употреблять такой картофель в пищу - опасно для здоровья! Такое даже животным давать нельзя!"
        show sv smile
        sv "Лучше выбирать сорта, которые устойчивы к раку картофеля, как например «Палац», «Вектор», «Лад» и так далее."
        hide ptattach13
        show sv calm at centre with ease
        sv "И это только малая часть того, чем может болеть картофель!"
        sv "Вроде и рассказала мало, но даже этого набора хватит чтобы уничтожить огород."
        show sv smile
        sv "Для того что бы избежать всех этих неприятностей картофель нужно {color=#ffd040}гербицидами{/color}, {color=#ffd040}инсектицидами{/color}, {color=#ffd040}фунгицидами{/color}."
        show sv smile
        sv "Для идеала нужно 3 раза прополоть, 2 раза использовать гербециды, 2 раза использовать инстекциды, и 2 раза использовать фунгициды."
        sv "Не больше не меньше."
        sv "Конечно, есть вероятность, что караладский жук и его собратья по вредительству появятся, но он крайне мал."
        sv "Отнесись к этому серьезнее ладно?"
        hide sv
        menu:
            "{image=icon_say}Хорошо!{image=icon_say}":
                $ renpy.block_rollback()
                show sv smile
                sv "Отличненько!"
                sv "Тогда как обычно, займись этим сам. Дышать химией опасно для здоровья!"
                sv "Удачи!"
                hide sv
                play sound move
                hide window
                $ renpy.pause(1, hard=True)
                jump ptcare
            "{image=icon_answer}Упс, повтори ещё раз, пожалуйста.{image=icon_answer}":
                $ renpy.block_rollback()
                show sv smile
                sv "Ладно, но в этот раз слушай внимательно"
                jump ptref6
    menu ptcare:
        "{image=icon_plow}Прополоть | [wee]{image=icon_plow}":
            $ renpy.block_rollback()
            hide screen staty
            show potatoplowing
            $ wee +=1
            play sound dig
            $ renpy.pause(3, hard=True)
            hide potatoplowing
            show screen staty
            jump ptcare
        "{image=icon_herbi}Использовать гербециды | [herbi]{image=icon_herbi}":
            $ renpy.block_rollback()
            hide screen staty
            $ herbi +=1
            play sound spray
            show herbi
            $ renpy.pause(5, hard=True)
            hide herbi
            show screen staty
            jump ptcare
        "{image=icon_insec}Использовать инстекциды | [insec]{image=icon_insec}":
            $ renpy.block_rollback()
            hide screen staty
            $ insec +=1
            play sound spray
            show insec
            $ renpy.pause(5, hard=True)
            hide insec
            show screen staty
            jump ptcare
        "{image=icon_fungi}Использовать фунгициды | [fungi]{image=icon_fungi}":
            $ renpy.block_rollback()
            hide screen staty
            $ fungi +=1
            play sound spray
            show fungi
            $ renpy.pause(5, hard=True)
            hide fungi
            show screen staty
            jump ptcare
        "Закончить уход.":
            $ renpy.block_rollback()
            if (insec<1):
                hide screen staty
                show insects
                play sound laugh
                $ renpy.pause(3, hard=True)
                hide insects
            jump ptfinishcare

label ptfinishcare:
    hide screen staty
    with fade2
    if wee ==3 and herbi==2 and insec==2 and fungi==2:
        $ taste +=12
    elif wee <3:
        $ taste -=3
        if herbi<2:
            $ taste -=3
            if insec<2:
                $ taste -=3
                if fungi<2:
                    $ taste -=3
    elif wee ==0 and herbi==0 and insec==0 and fungi==0:
        $ taste -=12
    elif wee >3:
        $ taste -=3
        if herbi>2:
            $ taste -=3
            if insec>2:
                $ taste -=3
                if fungi>2:
                    $ taste -=3
    if insec<1:
        $ Ur/=2
        show potato stage1damaged behind sv
        play sound grow
        $ renpy.pause(1, hard=True)
        play sound picturebuzzer
        show sv smile
        show screen staty
        sv "Чтож, давай посмотрим что у тебя получи..."
        show sv doubt
        sv "Подожди, а это что? Почему картошка дырявая?"
        show sv angry
        sv "[pl_name], только не говори, что ты решил не проводить химическую защиту?"
        sv "Ты понимаешь, как ты серьезно ошибся?"
        sv "Пологаю, теперь ты увоил урок, почему это очень важно."
        show sv sad
        sv "В редких случаях бывает такое, что человек отказывается от обработки пестицидами."
        sv "Видимо это уже совсем недалекий человек."
        sv "Обработку пестицидами нужно проводить неменее чем за 20-30 дней до снятие урожая, а то и вовсе за 45-60 дней."
        sv "Это делается с целью предотравщения отравления человека и животных."
        sv "Сроки очень важны, особенно если это касается сельскохозяйственных преприятий."
        show sv smile
        sv "Хорошо что в данным момент мы можем что-то исправить."
        show sv sad
        sv "Однако, половину урожая потеряно почем зря."
        show sv smile
        sv "Ладно, за дело!"
        hide sv
        hide screen staty
        $ insec +=1
        play sound spray
        show poison
        $ renpy.pause(5, hard=True)
        hide insec
        $ renpy.block_rollback()
        hide poison
        with fade2
        show potato stage2damaged behind sv
        play sound grow
        $ renpy.pause(1, hard=True)
        $ taste -=6
        show screen staty
        play sound picturebuzzer
        show sv smile
        sv "Фух, спасли!"
    else:
        show  potato stage2
        play sound grow
        $ renpy.pause(1, hard=True)
        show sv smile
        play sound picturebuzzer
        show screen staty
        sv "Чтож, давай посмотрим что у тебя получилось!"
        sv "Вау, отличная работа."
    $ stage_name = "Сбор"
    show sv smile
    sv "Чтож, теперь нужно немного подождать, когда картошка выростет полностью."
    sv "Ты подумал над датой уборки?"
    menu:
        "{image=icon_answer}А когда нужно убирать картофель?{image=icon_answer}":
            sv "Картофель нужно убирать желательно в сентябре в 10-тых числах."
            sv "К тому времени она точно выростет полностью и будет самой лучшей."
            sv "Можно конечно и раньше, но будет меньше урожая и сократиться срок хранения картофеля."
            sv "Не хотелось бы посреди зимы что бы картофель вышел из срока годности."
    sv "Ну чтож, когда будешь собирать картофель?"
    hide sv
    show calendar2 at left2
    menu:
        "10 июля.":
            hide calendar2
            $ Ur/=1.5
            $ Ur=int(Ur)
            show sv angry
            sv "Ты меня вообще слушал?"
            sv "Ладно. Твое право."
            hide sv
            jump finishpotatoroute
        "10 августа":
            hide calendar2
            $ Ur/=1.2
            $ Ur=int(Ur)
            show sv sad
            sv "Ну... собрать на месяц раньше вприципе не критично."
            sv "Твое право."
            hide sv
            jump finishpotatoroute
        "10 сентября":
            play sound wow
            hide calendar2
            $ svFrendship +=20
            show sv smile
            sv "Отлично! Я рада, что ты послушал меня!"
            hide sv
            jump finishpotatoroute

label finishpotatoroute:
    $ renpy.block_rollback()
    hide screen staty
    with fade2
    hide sv
    if it==1:
        show farm autumn behind soil with dissolve
    elif it==2 or it==3:
        show farm spring behind soil
    if Ur>10:
        if Ur>199:
            show potato stage3good with dissolve
            play sound grow
            $ renpy.pause(1.5, hard=True)
            play sound picturebuzzer
            show sv smile at centre with easeinbottom
            sv "Ура, ты вырастил [Ur] ценнера картофеля!"
            if taste<25:
                show sv sad
                sv "Но кажется она не самого лучшего качества."
                if soil=="Суглинистая" or soil=="Легкосуглинистая":
                    sv "А ещё вдобавок не вкусная!"
                sv "Не сказала бы, что работа проделана отлично."
                show sv calm
                sv "Но ты всегда можешь перееиграть и выйти на более лучший результат!"
                sv "Надеюсь, ты запомнил свои ошибки и в следующий раз качество картошки будет лучше!"
            else:
                if soil=="Суглинистая" or soil=="Легкосуглинистая":
                    show sv sad
                    sv "Но она не вкусная!"
                    sv "Значит мы где-то ошиблись."
                    show sv calm
                    sv "Но ты всегда можешь перееиграть и выйти на более лучший результат!"
                    sv "Надеюсь, ты помнишь свои ошибки и в следующий раз картошка будет вкусной!"
                else:
                    show sv smile
                    sv "Она вдобавок ещё и отличного качества!"
                    sv "По-моему это успех!"
                    show sv calm2
                    sv "Я так рада, что ты предерживался моих рекомендаций!"
                    sv "Думаю с остальными овощами тебе будет ещё легче!"
        elif 200>Ur>49:
            show potato stage3medium with dissolve
            play sound grow
            $ renpy.pause(1.5, hard=True)
            play sound picturebuzzer
            show sv smile at centre with easeinbottom
            sv "Ура, ты вырастил аж [Ur] ценнера картофеля!"
            if taste<25:
                sv "Довольно неплохо я бы сказала."
                show sv sad
                sv "Но кажется она не самого лучшего качества."
                if soil=="Суглинистая" or soil=="Легкосуглинистая":
                    sv "А ещё вдобавок не вкусная!"
                sv "Не сказала бы, что работа проделана отлично."
                show sv smile
                sv "Но ты всегда можешь перееиграть и выйти на более лучший результат!"
                sv "Надеюсь, ты запомнил свои ошибки и в следующий раз качество картошки будет лучше!"
            else:
                if soil=="Суглинистая" or soil=="Легкосуглинистая":
                    show sv sad
                    sv "Но она не вкусная!"
                    sv "Кажется, мы где-то ошиблись."
                    show sv smile
                    sv "Но ты всегда можешь перееиграть и выйти на более лучший результат!"
                    sv "Надеюсь, ты помнишь свои ошибки и в следующий раз картошка будет вкусной!"
                else:
                    sv "Она вдобавок ещё и отличного качества!"
                    sv "Не смотря на то, что мы не достигли предела, это уже хороший результат."
                    sv "Но ты всегда можешь перееиграть и выйти на более лучший результат!"
                    show sv calm2
                    sv "Надеюсь, ты помнишь свои ошибки и в следующий раз картошки будет больше!"
        elif 50>Ur>9:
            show potato stage3low with dissolve
            play sound grow
            $ renpy.pause(1.5, hard=True)
            play sound picturebuzzer
            show sv sad at centre with easeinbottom
            sv "Ты вырастил [Ur] ценнера картофеля. Это очень мало."
            if taste<25:
                show sv sad
                sv "Так ещё она не самого лучшего качества."
                if soil=="Суглинистая" or soil=="Легкосуглинистая":
                    sv "А ещё вдобавок не вкусная!"
                show sv smile
                sv "Не расстраивайся, ладно? Ты всегда можешь переиграть и выйти на более лучший результат!"
                sv "Надеюсь, ты запомнил свои ошибки и в следующий раз качество картошки будет лучше!"
            else:
                if soil=="Суглинистая" or soil=="Легкосуглинистая":
                    sv "Вдобавок она ещё и не вкусная."
                    sv "Такой убыток."
                    sv "Мы где-то очень серьезно ошиблись. Ты же помнишь где именно?"
                    show sv smile
                    sv "Ты всегда можешь перееиграть и выйти на более лучший результат!"
                else:
                    show sv smile
                    sv "Однако она отличного качества!"
                    sv "Хоть и маленький, но уже успех."
                    sv "Однако ты всегда можешь перееиграть и выйти на более лучший результат!"
                    show sv calm2
                    sv "Надеюсь, ты помнишь свои ошибки и в следующий раз картошки будет больше!"
    else:
        hide potato
        play sound badend
        show sv sad at centre with easeinbottom
        sv "Упс, кажется ты настолько плохо слушал мои указания, что в итоге у нас не выросла картошка!"
        show sv smile
        sv "Не расстраивайся, ладно? Ты всегда можешь переиграть и выйти на более лучший результат!"
        sv "Надеюсь, ты помнишь где ошибся и в следующий раз у тебя будет какая-никакая картошка."
    hide sv
    $ renpy.block_rollback()
    if  Ur>199:
        show potato baggood at right4 with dissolve
    elif 200>Ur>49:
        show potato bagmedium at right4 with dissolve
    elif 50>Ur>9:
        show potato baglow at right4 with dissolve
    avtor "{color=#ffd040}{size=50}ИТОГИ{/size}{/color}"
    avtor "{color=#ffd040}Урожайность{/color} [Ur]/500"
    avtor "{color=#ffd040}Качество{/color} [taste]/48"
    if Ur>100:
        $point +=50
        if 49>taste>24:
            $point+=50
        else:
            $point-=20
    if 1001>Ur>50:
        $point +=25
        if 49>taste>24:
            $point+=50
        else:
            $point-=20
    if 51<Ur>10:
        $point+=5
        if 49>taste>24:
            $point+=50
        else:
            $point-=20
    if Ur<10:
        $point=0
    if insec<1:
        avtor "-3 - отказ от инсектицидов"
    elif insec==1:
        avtor "-3 - недостаток инсектицидов"
    elif insec>2:
        avtor "-3 - переизбыток инсектицидов"
    if fungi<1:
        avtor "-3 - отказ от фунгицидов"
    elif fungi>2:
        avtor "-3 - переизбыток фунгицидов"
    elif fungi==1:
        avtor "-3 - недостаток фунгицидов"
    if herbi<2:
        avtor "-3 - отказ от гербецидов"
    elif herbi>2:
        avtor "-3 - переизбыток гербицидов"
    elif fungi==1:
        avtor "-3 - недостаток гербицидов"
    if wee<1:
        avtor "-3 - отказ от прополки"
    elif wee>3:
        avtor "-3 - лишняя прополка"
    elif 3>wee>1:
        avtor "-3 - недостаток прополки"
    if 300>Nu>119:
        avtor "-12 - переизбыток азотного удобрения"
    if kpotato >0:
        avtor "Прошлый балл за прохождение: [potato]"
    avtor "{color=#ffd040}{size=40}Заработано очков{/color}: [point]{/color}"
    $ kpotato+=1
    $ potato=point
    $ money+=point
    show sv smile
    sv "Какой овощ ты хочешь посадить следующим?"
    hide potato
    show sv at right with ease
    show soil peaty behind sv with dissolve
    show farm spring behind soil with dissolve
    $ renpy.block_rollback()
    jump route
