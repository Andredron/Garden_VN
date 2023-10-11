label tomato_route:
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
    $ cult = "Помидор"
    $ Ur = 0
    show sv at centre with ease
##Блок для объяснений
##Что такое помидор?
##Рассказ о том какой месяц
##При какой температуре лучше садить помидор
    show sv smile
    sv "О, значит помидор. Хороший выбор!"
    show sv at right2 with ease
    play sound picturebuzzer
    show tmattach2 behind sv at attach with easeinright
    sv "Помидор или же томат — травянистое растение рода пасленовые, выращивается как овощная культура."
    sv "Является одной из востребованных культур в мире, широко используемой в пищевой промышленности."
    sv "В наше время так много блюд, содержащие помидор: салаты, соления, различные маринады, пицца, сок - это только малая часть того где он используется."
    sv "Так же его используют в восточной и народной медецине."
    hide tmattach2
    show sv at centre with ease
    sv "Хочешь послушать историю данной кульуры?"
    hide sv
    menu:
        "{image=icon_say}Да{image=icon_say}":
            $ stage_name = "История"
            show sv smile
            $ svFrendship +=10
            sv "Неужели тебе и вправду интересно? Тогда слушай!"
            sv "Помидор родом из Южной Америки."
            sv "В Европе помидор оказался благодаря испанским канкистадорам, которые завезли его в XVI веке."
            sv "Жителям испании помидор пришелся по душе, а в Италии называли его “золотым яблоком”."
            sv "На руси же, данный овощ оказался в конце XVIII века."
            show sv at right2 with ease
            play sound picturebuzzer
            show tmattach3 behind sv at attach4 with easeinright
            sv "Императрица Екатерина велела доставлять помидоры ко двору ежедневно."
            hide tmattach3
            show sv at centre with ease
            sv "Томаты быстро культивировались на руси, сначала как декоративная культура, а затем их приравняли к обычным овощам."
        "{image=icon_no}Нет{image=icon_no}":
            show sv calm
            sv "Ну как хочешь."
    $ stage_name = "Месяц"
    sv "Тогда время начинать!"
    sv "Первым этапом является {u}выбор месяца для посадки{/u}."
    label tmref1:
        show sv smile
        sv "Из-за того, что мы садим помидор в открытом грунте, то идеальной температурой воздуха для посадки яляется от +20 до +25."
        sv "Лучшим временем для посадки помидоров является {color=#ffd040}третья декада мая{/color} и {color=#ffd040}первая декада июня{/color}."
        sv "В это время минует опасность в виде заморозков."
        show sv sad
        sv "Для помидора холода - это верная смерть!"
        show sv angry
        sv "Поэтому даже не пытайся посадить помидоры в {color=#ffd040}марте{/color} или {color=#ffd040}апреле{/color} в открытом грунте, ведь это пустая трата семян!"
        show sv smile
        sv "Надеюсь ты все понял?"
        hide sv
        menu:
            "{image=icon_say}Все понятно!{image=icon_say}":
                show sv calm2
                sv "Я надеюсь, ты сделаешь правильный выбор."
                jump tmmenumount
            "{image=icon_answer}Можешь ещё раз повторить, пожалуйста?{image=icon_answer}":
                show sv smile
                sv "Хорошо, но в этот раз слушай внимательно."
                jump tmref1
label tmmenumount:
    show screen staty
    scene bc
    show sun at sunfarm
    show farm
    show soil peaty
    show calendar1 at left2
    hide sv
    menu:
        "Март":
            hide screen staty
            scene black with fade2
            play sound badend
            show text "Поздравляю, ваш урожай замерз!"
            $ renpy.pause(3, hard=True)
            hide text
            $ renpy.block_rollback()
            jump tmmenumount
        "Апрель":
            hide screen staty
            scene black with fade2
            play sound badend
            show text "Поздравляю, ваш урожай замерз!"
            $ renpy.pause(3, hard=True)
            hide text
            $ renpy.block_rollback()
            jump tmmenumount
        "Май":
            hide calendar1
            play sound wow
            $ month="Май"
            show sv smile
            sv "Отличный выбор!"
        "Июнь":
            hide calendar1
            play sound wow
            $ month="Июнь"
            show sv smile
            sv "Отличный выбор!"
label tmmenut:
            $ stage_name = "Температура"
            show screen staty
            scene bc
            show sun at sunfarm
            show farm
            show soil peaty
            show sv calm2
            show tmthermometer at left2 with easeinright
            $ t=renpy.input(_("{color=#ffd040}Как думаешь какая сейчас температура?{/color}"),length=3, default= 0, allow = "1234567890-+").strip()
            $ t=int(t)
            if t>26:
                hide screen staty
                scene black with fade2
                play sound badend
                show text "Поздравляю, вы сожгли свой урожай!"
                $ renpy.pause(3, hard=True)
                hide text
                $ t=0
                $ renpy.block_rollback()
                jump tmmenut
            if t<26 and t>=19:
                hide tmthermometer
                play sound wow
                show sv smile
                sv "Я тоже так думаю!"
                jump tomato_stage2
            if t<20:
                hide screen staty
                scene black with fade2
                play sound badend
                show text "Поздравляю, ваш урожай замерз!"
                $ renpy.pause(3, hard=True)
                $ t=0
                hide text
                $ renpy.block_rollback()
                jump tmmenut
label tomato_stage2:
##Блок для объяснений
##Индетерминатные и детерминатные томаты
    $ stage_name = "Вид"
    sv "Вторым этапом является {u}выбор вида помидора{/u}."
    sv "Помидоры бывают {color=#ffd040}индетерминатный{/color} и {color=#ffd040}детерменантный{/color}."
    hide sv
label tmref2:
    menu:
        "{image=icon_answer}Что такое «индетерминатный помидор»?{image=icon_answer}":
            $ it+=1
            show sv smile at right3 with ease
            play sound picturebuzzer
            show tmattach4 behind sv at attach with easeinright
            sv "{color=#ffd040}Индетерминатный помидор{/color} - это растение с неограниченным ростом."
            sv "Они могут быть высотой от 2-х до 10-ти метров!"
            sv "Поэтому нужно устаналивать опору для таких помидоров."
            sv "Так же данный вид является позднеспелым."
            hide tmattach4
            if it!=2:
                hide sv
                jump tmref2
        "{image=icon_answer}Что такое «детерменантный помидор»?{image=icon_answer}":
            $ it+=1
            show sv smile at right3 with ease
            play sound picturebuzzer
            show tmattach5 behind sv at attach with easeinright
            sv "{color=#ffd040}Детерминантные помидор{/color} - это низкорослые растения, которые хорошо кустятся."
            sv "Данный вид самый распространенный из всех, так как растет почти везде."
            sv "Так же их особенностью является - рост ограничен, и как только он достигает предела, то больше не растет."
            sv "У него есть ранний срок созревания."
            hide tmattach5
            if it!=2:
                hide sv
                jump tmref2
    show sv smile at centre with ease
    sv "Поэтому взависимости от вида нужно будет решать как выращивать помидоры дальше."
    sv "Надеюсь, ты все понял?"
    $ it=0
    hide sv
    menu:
        "{image=icon_say}Да, все понятно{image=icon_say}":
            show sv calm2
            sv "Вот и славно!"
        "{image=icon_answer}Можешь повторить ещё раз?{image=icon_answer}":
            show sv smile
            sv "Хорошо, но в этот раз слушай внимательнее."
            jump tmref2
    sv "Какой вид ты выберешь?"
    hide sv
    menu:
        "Индетерминатный помидор":
            $ cult = "Помидор(Ин.)"
            play sound wow
            show sv smile
            sv "Отличный выбор!"
            sv "Тогда необходимо тогда поставить стойку для подвязывания."
            hide sv
            with fade2
            show tomato idtstage0 behind sv
            $ renpy.pause(1, hard=True)
            show sv smile
        "Детерминатный помидор":
            $ cult = "Помидор(Дт.)"
            play sound wow
            show sv smile
            sv "Отличный выбор!"
label tomato_stage3:
##Блок для объяснений
##Пояснение за почвы
    $ stage_name = "Почва"
    sv "Следующим этапом является {u}почва{/u}."
    label tmref3:
        sv "Помидоры любят рыхлую, воздухопроницаемую, богатую органическими и минеральными веществами почву, как чернозем."
        sv "Но, чернозема у нас нет."
        sv "Но не волнуйся! Остальные виды почв тоже подходят, но их необходимо улучшать."
        sv "{color=#ffd040}Супесчаные{/color}, {color=#ffd040}глинистые грунты{/color} и {color=#ffd040}суглинки{/color} улучшают, добавляя в них перегной, компост, торф, речной или озерный ил."
        sv "Так же в почву можно добавить немного песка, опилок, соломы."
        show sv angry
        sv "Ни в коем случае нельзя добавлять в почву свежий навоз!"
        sv "Добавление навоза в качестве удобрения приведет к бурному образованию листьев, а плоды завязываться не буду."
        show sv smile
        sv "Моим советом будет выбрать легкие почвы, а так же торфянник и дерновая."
        sv "Надеюсь, ты все понял?"
        hide sv
        $ it=0
        menu:
            "{image=icon_say}Да, все понятно{image=icon_say}":
                show sv smile
                sv "Вот и хорошо!"
            "{image=icon_answer}Можешь повторить ещё раз?{image=icon_answer}":
                show sv smile
                sv "Хорошо, но в этот раз слушай внимательнее."
                jump tmref3
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
            jump tomato_stage4
        "{image=icon_sandyloam}Супесчанная почва{image=icon_sandyloam}":
            $ renpy.block_rollback()
            show soil sandyloam behind sv with dissolve
            play sound wow
            $ soil = "Супесчанная"
            $ taste += 12
            show sv calm2
            sv "Отличный выбор!"
            jump tomato_stage4
        "{image=icon_sandy}Песчаная почва{image=icon_sandy}":
            $ renpy.block_rollback()
            show soil sandy behind sv with dissolve
            play sound wow
            $ soil = "Песчаная"
            $ taste += 12
            show sv calm2
            sv "Отличный выбор!"
            jump tomato_stage4
        "{image=icon_peaty}Торфянная почва{image=icon_peaty}":
            $ renpy.block_rollback()
            show soil peaty behind sv with dissolve
            play sound wow
            $ soil = "Торфянник"
            $ taste += 12
            show sv calm2
            sv "Отличный выбор!"
            jump tomato_stage4
        "{image=icon_humus}Дерновая почва{image=icon_humus}":
            $ renpy.block_rollback()
            show soil humus behind sv with dissolve
            play sound wow
            $ soil = "Дерновая"
            $ taste += 12
            show sv calm2
            sv "Отличный выбор!"
            jump tomato_stage4

label tomato_stage4:
    $ stage_name = "Удобрение"
    show sv smile
    sv "Теперь давай займемся {u}удобрением{/u}."
    label tmref4:
        sv "Помидоры удобряют для хорошего роста и лучшего урожая."
        sv "Почва может не всегда содержать достаточное количество пиательных веществ, чтобы вырос хороший урожай помидоров."
        sv "Самыми {u}основными пительными элементами{/u} для помидор являются: {color=#ffd040}азот{/color}, {color=#ffd040}фосфор{/color} и {color=#ffd040}калий{/color}."
        sv "Помидоры поглащают больше калия и фосфора, ведь недостаток калия и фосфора сказываются на росте плодов."
        sv "Фосфор нужен помидорам для укрепления корневой системы, а так же благодаря фосфору у плодов повышается уровень сахаристости и сухого вещества."
        sv "Но азот не нужно списывать со счетов. Помидоры требовательны к азотному питанию."
        sv "Но всего должно быть в меру."
        sv "При переизбытке азота приводит к задержке плодоношения, растение становиться уязвимым к болезням."
        sv "А ещё может урожай может стать загрязненным нитратами и непригодным для пищи."
        show sv at right3 with ease
        play sound picturebuzzer
        show tmattach1 behind sv at attach with easeinright
        sv "Вот таблица которая тебе поможет."
        sv "Будешь следовать ей, то получишь примерно такие результаты."
        sv "Надеюсь все понятно?"
        hide tmattach1
        hide sv
        menu:
            "{image=icon_say}Все понятно!{image=icon_say}":
                show sv smile
                jump tmfert
            "{image=icon_answer}Можешь ещё раз повторить, пожалуйста?{image=icon_answer}":
                show sv smile
                sv "Хорошо, но в этот раз слушай внимательно."
                jump tmref4
##Блок для объяснений
##Объяснение про удобрения, их соотношение и т.д
label tmfert:
    $ Nu = renpy.input(_("{color=#ffd040}Введите количество азотного удобрения(кг/га).{/color}"),length=3, default= 0, allow = "1234567890").strip()
    $ Nu = int(Nu)
    if Nu==0:
        $ Nu=0
    elif Nu>=120:
        show sv angry
        play sound shout
        sv "Ты совсем?! Ты хочешь уничтожить урожай?" with hpunch
        jump tmfert
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
        if 91>Nu>70:
            $Ur+=300
        elif 31>Nu>19:
            $Ur+=66
        elif 71>Nu>49:
            $Ur+=167
        elif Nu<20:
            $Ur+=20
        elif 121>Nu>99:
            $Ur+=45
            $ taste-=12
        elif 50>Nu>30:
            $Ur+=132
    ##Подсчет урожайности по азотному удобрению
        $ Ku = renpy.input(_("{color=#ffd040}Введите количество калийного удобрения(кг/га).{/color}"),length=3, default= 0, allow = "1234567890").strip()
        $ Ku = int(Ku)
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
        if Ku>89:
            $Ur+=300
        elif 31>Ku>19:
            $Ur+=66
        elif 51>Ku>39:
            $Ur+=167
        elif Ku<20:
            $Ur+=20
        elif 40>Ku>30:
            $Ur+=132
        elif 90>Ku>49:
            $Ur+=232
        $ Pu = renpy.input(_("{color=#ffd040}Введите количество фосфорного удобрения(кг/га).{/color}"),length=3, default= 0, allow = "1234567890").strip()
        $ Pu = int(Ku)
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
        if Pu>119:
            $Ur+=300
        elif 31>Pu>19:
            $Ur+=66
        elif 101>Pu>89:
            $Ur+=167
        elif Pu<20:
            $Ur+=20
        elif 90>Pu>30:
            $Ur+=132
        elif 120>Ku>99:
            $Ur+=232
    jump tomato_stage6

label tomato_stage6:
    $ stage_name = "Посадка"
    with fade2
    play sound move
    show sv smile
    sv "Отличненько!"
    sv "Самое время поговорить о тонкостях посадки помидоров."
    ##Блок для объяснений
    ##Расстояние для посадки картошки между рядами и друг другом
label tmref6:
    sv "У помидора есть схемы посадки, которую стоит придерживаться независимо от вида почвы."
    sv "Для индетерминантных помидоров нужно использовать 70х50. 70 см - это расстояние междурядами, а 50 см это растояние между самими посадками."
    sv "Детерминантные же садяться по схеме 70х30."
    sv "Однако если ты посадишь больше или же меньше нужного, то пиши пропало."
    sv "Детерминантные помидоры садят либо в 2 ряда, либо в шахматном порядке. Во втором случае между растениями должно быть 50-60 сантиметров."
    sv "Но это так, мелочи."
    sv "Главное запомни 2 схемы. Это же не составит особого труда."
label tmwd1:
    show sv smile at centre
    sv "Расстояние междурядий помидора?"
    hide sv
    show plant1 at left4 with easeinright
    play sound picturebuzzer
    menu:
        "50 см":
            hide plant1
            $ taste=0
        "70 см":
            hide plant1
            $ taste+=12
        "75 см":
            hide plant1
            $ taste=0
    show sv smile at centre
    sv "На каком расстоянии друг от друга ты посадишь помидор?"
    hide sv
    show plant2 at left4 with easeinright
    play sound picturebuzzer
    menu:
        "20 см":
            hide plant2
            $ taste=0
        "30 см":
            hide plant2
            if cult == "Помидор(Дт.)":
                $ taste+=12
            else:
                $ taste+=6
        "40 см":
            hide plant2
            if cult == "Помидор(Ин.)":
                $ taste+=12
            else:
                $ taste+=6
label tomato_stage7:
    hide screen staty
    with fade2
    if cult=="Помидор(Ин.)":
        show tomato idtstage1 behind sv
    elif cult=="Помидор(Дт.)":
        show tomato stage1 behind sv
    play sound grow
    $ renpy.pause(1, hard=True)
    show sv smile
    sv"Вооот, смотри! Как выросли наши помидорчики!"
    show screen staty
    $ stage_name = "Уход"
    sv "И так следующий этап, это уход за посадками."
    label tmref5:
        sv "В уход за ними входит прополка от сорняков и защита от насекомых и болезней."
        show sv sad
        sv "Перечень вредители помидоров в открытом грунте достаточно большой."
        show sv angry
        sv "Однако нужно знать врага в лицо!"
        show sv at right2 with ease
        play sound picturebuzzer
        show tmattach6 at attach2 with easeinright
        sv "Например {color=#ffd040}белокрылка{/color}."
        sv "Поселяются белые мушки на нижней стороне листьев, высасывают из растений сок."
        play sound picturebuzzer
        show tmattach7 at attach3 with easeinright
        sv "Продукты жизнедеятельности этих вредителей – питание для сажистого грибка."
        sv "Совместными усилиями эти два врага огородников способны быстро погубить весь помидорный куст!"
        show sv sad
        sv "Ты понимаешь какие это потери?"
        show sv angry
        sv "К тому же белокрылки – разносчицы вирусных заболеваний растений."
        hide tmattach7
        hide tmattach6
        play sound picturebuzzer
        show tmattach8 at attach2 with easeinright
        sv "Так же есть такой вредитель, как {color=#ffd040}совка{/color}."
        sv "Появляется оно уже в середине мая."
        sv "Чаще всего совки откладывают яйца на нижней стороне листьев, реже на стеблях томатов."
        play sound picturebuzzer
        show tmattach9 at attach3 with easeinright
        sv "При благоприятных условиях из яиц уже через несколько дней появляются гусеницы, которые наносят колоссальный вред!"
        sv "Совки поражают не только плоды, но и цветы, завязи, листья помидоров."
        sv "В образовавшихся пустотах возникают очаги гниения."
        hide tmattach9
        hide tmattach8
        play sound picturebuzzer
        show tmattach10 at attach2 with easeinright
        sv "А ещё не стоит забывать про {color=#ffd040}паутинного клеща{/color}."
        sv "Массовое размножение клеща наблюдается в период жаркой и сухой погоды."
        sv "Cелятся они на нижней поверхности листа и питаются клеточным соком."
        sv "Окраска листа становится мраморной, затем пластины засыхают."
        play sound picturebuzzer
        show tmattach11 at attach3 with easeinright
        sv "Обнаружить вредителя можно благодаря тонкой паутине на ростках."
        hide tmattach10
        hide tmattach11
        show sv at centre with ease
        sv "Так же таких вредителей как кораладский жук и проволочнник можно встретить и на помидорах."
        sv "Не стоит забывать о болезнях помидора. Начнем с самой распространненой болезни - {color=#ffd040}фитофтороза{/color}."
        if kpotato>0:
            sv "Ты уже знаком с ней по картофелю."
            sv "Однако, не смотря на это мне есть что сказать."
        sv "Из-за того первичная инфекция скрытая и труднодиагностируемая, фитофтороз диагнастируют на поздней стадии."
        sv "Только тогда его можно будет увидеть глядя на внешний вид."
        show sv at right2 with ease
        play sound picturebuzzer
        show tmattach14 at attach5 with easeinright
        play sound picturebuzzer
        show tmattach15 at attach6 with easeinright
        sv "Фитофтороз томата проявляется чаще всего в период с конца мая по август. Чаще всего поражаются позднеспелые сорта томатов."
        sv "Споры грибка не любят высокие температуры, поэтому в первой половине лета им не очень комфортно размножаться."
        show sv sad
        sv "Фитофтороз поражает стебли, плоды и листья помидоров."
        sv "На листьях можно будет увидеть бурые темные пятна, которые с каждым разом увеличиваются в размере. Вскоре лист чернеет и усыхает."
        sv "Стебель так же будет в пятнах. Из-за влаги и дождя инфекция быстро распространиться по стеблю."
        sv "А на плодах невооруженным взглядом можно будет заметить твердую бурую гниль. Цвет пятен варьриуется от лилового-бурого до почти черного."
        sv "Лечением данной заразы является сокращение поливов и удаление зараженных бутонов и листьев."
        hide tmattach15
        hide tmattach14
        show sv angry
        sv "Есть ещё такая болезнь как {color=#ffd040}бактериоз{/color} или же бактериальный рак."
        show tmattach16 at attach5 with easeinright
        sv "Имеет более простое название «птичий глаз» из-за характерного строения пятен."
        show sv sad
        sv "Распространяется он слишком быстро, поражая томаты от корней до кончиков листьев."
        sv "Существует две формы бактериального рака – диффузная и локальная."
        sv "При диффузной разрастание колонии бактерий начинается при рассаде зараженных семян или поражении стебля."
        sv "Локальная форма менее опасна для томатов, не сопровождается гнилью стебля и позволяет сохранить часть урожая при правильном уходе."
        sv "Жаль, что симптомы проявляются зачастую уже при плодоношении, а зараженные семена сохраняют инфекцию до 3х лет."
        sv "Спасти помидор от данной напасти можно при помощи химических и биологических препаратов или же выбрать устойчивый к данной заразе сорт."
        hide tmattach16
        show sv sad at centre with ease
        sv "И это только малая часть того, кто может навредить помидорам."
        sv "Но даже один из этих вредителей способен погубить урожай на раз-два."
        show sv calm
        sv "Поэтому небходима обработка химическими препаратами, чтобы избежать их возможное появление."
        sv "Для идеала необходимо 3 раза прополоть и по 2 раза использовать пестициды."
        sv "Отнесись к этому серьезнее ладно?"
        hide sv
        menu:
            "{image=icon_say}Хорошо!{image=icon_say}":
                $ renpy.block_rollback()
                show sv smile
                sv "Ах да, чуть не забыла!"
                sv "Помидоры необходимо подкармливать в течении роста, около двух раз."
                sv "Это делается для повышения урожайности и вкуса, а так же для усточивости к болезням."
                show sv at right3 with ease
                play sound picturebuzzer
                show tmattach12 behind sv at attach with easeinright
                sv "Вот таблица которая тебе поможет при первой подкормке удобрениями."
                hide tmattach12
                show sv at right3 with ease
                play sound picturebuzzer
                show tmattach13 behind sv at attach with easeinright
                sv "А вот это таблица для второй подкормки."
                hide tmattach13
                show sv at centre with ease
                sv "Надеюсь это будет не сложно запомнить."
            "{image=icon_answer}Упс, я все прослушал. Можешь повторить, пожалуйста?.{image=icon_answer}":
                $ renpy.block_rollback()
                show sv smile
                sv "Хорошо, но в этот раз слушай внимательно."
                jump tmref5
        sv "Чтож, пологаюсь на тебя! А я отойду на свой огород."
        sv "Дышать химией не имея средств защиты опасно для здоровья!"
        sv "Удачи!"
        hide sv
        play sound move
        hide window
        $ renpy.pause(1, hard=True)
label tmcare:
    menu:
        "{image=icon_plow}Прополоть | [wee]{image=icon_plow}":
            hide screen staty
            show tomatoplowing
            $ wee +=1
            play sound dig
            $ renpy.pause(3, hard=True)
            hide tomatoplowing
            show screen staty
            jump tmcare
        "{image=icon_herbi}Использовать гербециды | [herbi]{image=icon_herbi}":
            hide screen staty
            $ herbi +=1
            play sound spray
            show herbi
            $ renpy.pause(5, hard=True)
            hide herbi
            show screen staty
            jump tmcare
        "{image=icon_insec}Использовать инстекциды | [insec]{image=icon_insec}":
            hide screen staty
            $ insec +=1
            play sound spray
            show insec
            $ renpy.pause(5, hard=True)
            hide insec
            show screen staty
            jump tmcare
        "{image=icon_fungi}Использовать фунгициды | [fungi]{image=icon_fungi}":
            hide screen staty
            $ fungi +=1
            play sound spray
            show fungi
            $ renpy.pause(5, hard=True)
            hide fungi
            show screen staty
            jump tmcare
        "{image=icon_fert}Подкормить | [fert]{image=icon_fert}":
            $ fert +=1
            if fert ==1:
                $ Nu = renpy.input(_("{color=#ffd040}Введите количество азотного удобрения(кг/га).{/color}"),length=3, default= 0, allow = "1234567890").strip()
                $ Nu = int(Nu)
                if Nu==0:
                    $ Nu=0
                elif Nu>=20:
                    play sound shout
                    player "По моему это перебор!" with hpunch
                    jump tmfert
                else:
                    window hide
                    hide screen staty
                    play sound addfert
                    show addN
                    $ renpy.pause(1.5, hard=True)
                    hide addN
                    show screen staty
                ##Подсчет урожайности по азотному удобрению
                    $ Ku = renpy.input(_("{color=#ffd040}Введите количество калийного удобрения(кг/га).{/color}"),length=3, default= 0, allow = "1234567890").strip()
                    $ Ku = int(Ku)
                    if Ku>0:
                        window hide
                        hide screen staty
                        play sound addfert
                        show addK
                        $ renpy.pause(1.5, hard=True)
                        hide addK
                        show screen staty
                    $ Pu = renpy.input(_("{color=#ffd040}Введите количество фосфорного удобрения(кг/га).{/color}"),length=3, default= 0, allow = "1234567890").strip()
                    $ Pu = int(Ku)
                    if Pu>0:
                        window hide
                        hide screen staty
                        play sound addfert
                        show addP
                        $ renpy.pause(1.5, hard=True)
                        hide addP
                        show screen staty
                ##Подсчет урожайности по калийному удобрению
                    if Ku>9:
                        $Ur+=0
                    elif 10>Ku>4:
                        $Ur/=1.2
                        $ Ur=int(Ur)
                    elif 5>Ku>0:
                        $Ur/=1.5
                        $ Ur=int(Ur)
                ##Подсчет урожайности по фосфорному удобрению
                    if Pu>20:
                        $Ur+=0
                    elif 21>Pu>9:
                        $Ur/=1.2
                        $ Ur=int(Ur)
                    elif 10>Pu>0:
                        $Ur/=1.5
                        $ Ur=int(Ur)
                ##Подсчет урожайности по азотному удобрению
                    if 16>Nu>10:
                        $Ur+=0
                    elif 10>Nu>4:
                        $Ur/=1.2
                        $ Ur=int(Ur)
                    elif 5>Nu>0:
                        $Ur/=1.5
                        $ Ur=int(Ur)
                    elif 21>Nu>15:
                        $ taste-=10
            elif fert==2:
                $ Nu = renpy.input(_("{color=#ffd040}Введите количество азотного удобрения(кг/га).{/color}"),length=3, default= 0, allow = "1234567890").strip()
                $ Nu = int(Nu)
                if Nu==0:
                    $ Nu=0
                elif Nu>=20:
                    show sv angry
                    play sound shout
                    player "Подожди! Это уже слишком!" with hpunch
                    jump tmfert
                else:
                    window hide
                    hide screen staty
                    play sound addfert
                    show addN
                    $ renpy.pause(1.5, hard=True)
                    hide addN
                    show screen staty
                ##Подсчет урожайности по азотному удобрению
                    $ Ku = renpy.input(_("{color=#ffd040}Введите количество калийного удобрения(кг/га).{/color}"),length=3, default= 0, allow = "1234567890").strip()
                    $ Ku = int(Ku)
                    if Ku>0:
                        window hide
                        hide screen staty
                        play sound addfert
                        show addK
                        $ renpy.pause(1.5, hard=True)
                        hide addK
                        show screen staty
                    $ Pu = renpy.input(_("{color=#ffd040}Введите количество фосфорного удобрения(кг/га).{/color}"),length=3, default= 0, allow = "1234567890").strip()
                    $ Pu = int(Ku)
                    if Pu>0:
                        window hide
                        hide screen staty
                        play sound addfert
                        show addP
                        $ renpy.pause(1.5, hard=True)
                        hide addP
                        show screen staty
                ##Подсчет урожайности по калийному удобрению
                    if Ku>29:
                        $Ur+=0
                    elif 30>Ku>14:
                        $Ur/=1.2
                        $ Ur=int(Ur)
                    elif 15>Ku>0:
                        $Ur/=1.5
                        $ Ur=int(Ur)
                ##Подсчет урожайности по фосфорному удобрению
                    if Pu>29:
                        $Ur+=0
                    elif 30>Pu>14:
                        $Ur/=1.2
                        $ Ur=int(Ur)
                    elif 15>Pu>0:
                        $Ur/=1.5
                        $ Ur=int(Ur)

            elif fert>=3:
                $ fert =2
                play sound shout
                player "Мы уже достаточно подкормили!" with hpunch
            jump tmcare
        "Закончить уход.":
            if (insec<1):
                hide screen staty
                show insects
                play sound laugh
                $ renpy.pause(3, hard=True)
                hide insects
                $ err+=1
            jump tomato_stage8

label tomato_stage8:
    with fade2
    if wee ==3 and herbi==2 and insec==2 and fungi==2 and fert==2:
        $ taste +=18
    elif wee <3:
        $ taste -=3
        if herbi<2:
            $ taste -=3
            if insec<2:
                $ taste -=3
                if fungi<2:
                    $ taste -=3
                if fert<2:
                    $taste-=3
    elif wee ==0 and herbi==0 and insec==0 and fungi==0 and fert==0:
        $ taste -=12
    elif wee >3:
        $ taste -=3
        if herbi>2:
            $ taste -=3
            if insec>2:
                $ taste -=3
                if fungi>2:
                    $ taste -=3
    if err==1:
        if cult=="Помидор(Ин.)":
            show tomato idtstage1damaged behind sv
        elif cult=="Помидор(Дт.)":
            show tomato stage1damaged behind sv
        $ Ur/=2
        play sound grow
        $ renpy.pause(1, hard=True)
        play sound picturebuzzer
        show sv smile
        show screen staty
        sv "Чтож, давай посмотрим что у тебя получи..."
        show sv doubt
        sv "Подожди, а это что? Почему помидор весь поврежден?"
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
        if cult=="Помидор(Ин.)":
            show tomato idtstage2damaged behind sv
        elif cult=="Помидор(Дт.)":
            show tomato stage2damaged behind sv
        play sound grow
        $ renpy.pause(1, hard=True)
        $ taste -=6
        show screen staty
        play sound picturebuzzer
        show sv smile
        sv "Фух, спасли!"
    else:
        if cult=="Помидор(Ин.)":
            show tomato idtstage2 behind sv
        elif cult=="Помидор(Дт.)":
            show tomato stage2 behind sv
        play sound grow
        $ renpy.pause(1, hard=True)
        show sv smile
        play sound picturebuzzer
        show screen staty
        sv "Чтож, давай посмотрим что у тебя получилось!"
        sv "Вау, отличная работа."

##Блок для объяснений
##Пояснение за подрезание и подвязывание
##Зачем подвязыывать детерменантный помидор
    if cult=="Помидор(Дт.)":
        sv "Как насчет того что бы подвязать помидоры?"
        menu:
            "Зачем подвязывать помидоры?":
                sv "Подвязка – незаменимая поддержка многих культур, выращиваемых на огороде, особенно для помидоров."
                sv "Подвязывание помидоров делается для повышения урожайности и вкуса плодов."
                sv "Так же это делается для устойчивости к болезням и не дает плодам своим весом сломать ветки."
                sv "Ну чтож, что будешь делать?"
        menu:
            "Подвязать помидор.":
                sv "Отлично! Я тебе помогу!"
                $ q = 1
                show tomato stage2belt
                $ renpy.pause(1.5, hard=True)
            "Не подвязывать помидор.":
                $ q = 0
                $ taste -=12
                sv "Как хочешь"
    else:
        sv "Хорошая работа."
    sv "Чтож, теперь нужно немного подождать, когда помидор выростет полностью."
    sv "Ты подумал над датой уборки?"
    menu:
        "{image=icon_answer}А когда нужно убирать помидор?{image=icon_answer}":
            sv "Лучшим временем для уборки помидоров является август."
            sv "К тому времени множество помидоров посспеет."
            sv "Поздние и ранние сроки сбора чреваты сокращением урожайности."
    sv "Ну чтож, когда будешь собирать помидор?"
    hide sv
    show calendar2 at left2
    menu:
        "Июль":
            hide calendar2
            $ Ur/=1.5
            $ Ur=int(Ur)
            $ svFrendship -=12
            show sv angry
            sv "Ты меня вообще слушал?"
            sv "Ладно. Твое право."
            hide sv
            jump finishtomatoroute
        "Август":
            play sound wow
            hide calendar2
            $ svFrendship +=12
            show sv smile
            sv "Отлично! Я рада, что ты послушал меня!"
            hide sv
            jump finishtomatoroute
        "Сентябрь":
            hide calendar2
            $ Ur/=1.5
            $ Ur=int(Ur)
            $ svFrendship -=12
            show sv angry
            sv "Ты меня вообще слушал?"
            sv "Ладно. Твое право."
            hide sv
            jump finishtomatoroute

label finishtomatoroute:
    $ renpy.block_rollback()
    hide screen staty
    with fade2
    hide sv
    if Ur>100:
        if Ur>899:
            if cult=="Помидор(Ин.)":
                show tomato idtstage3good behind sv
            elif cult=="Помидор(Дт.)":
                if q == 0:
                    show tomato stage3good behind sv
                else:
                    show tomato stage3beltgood behind sv
            play sound grow
            $ renpy.pause(1.5, hard=True)
            play sound picturebuzzer
            show sv smile at centre with easeinbottom
            sv "Ура, ты вырастил [Ur] ценнера помидоров!"
            if taste<24:
                show sv sad
                sv "Но кажется они не самого лучшего качества."
                if soil=="Суглинистая" or soil=="Легкосуглинистая":
                    sv "А ещё вдобавок не вкусные!"
                sv "Не сказала бы, что работа проделана отлично."
                show sv calm
                sv "Но ты всегда можешь перееиграть и выйти на более лучший результат!"
                sv "Надеюсь, ты запомнил свои ошибки и в следующий раз качество помидоров будет лучше!"
            else:
                if soil=="Суглинистая" or soil=="Легкосуглинистая":
                    show sv sad
                    sv "Но они не вкусные!"
                    sv "Значит мы где-то ошиблись."
                    show sv calm
                    sv "Но ты всегда можешь перееиграть и выйти на более лучший результат!"
                    sv "Надеюсь, ты помнишь свои ошибки и в следующий раз помидоры будут вкусными!"
                else:
                    show sv smile
                    sv "Они вдобавок ещё и отличного качества!"
                    sv "По-моему это успех!"
                    show sv calm2
                    sv "Я так рада, что ты предерживался моих рекомендаций!"
                    sv "Думаю с остальными овощами тебе будет ещё легче!"
        elif 900>Ur>499:
            if cult=="Помидор(Ин.)":
                show tomato idtstage3medium behind sv
            elif cult=="Помидор(Дт.)":
                if q == 0:
                    show tomato stage3medium behind sv
                else :
                    show tomato stage3beltmedium behind sv
            play sound grow
            $ renpy.pause(1.5, hard=True)
            play sound picturebuzzer
            show sv smile at centre with easeinbottom
            sv "Ура, ты вырастил аж [Ur] ценнера помидоров!"
            if taste<24:
                sv "Довольно неплохо я бы сказала."
                show sv sad
                sv "Но кажется они не самого лучшего качества."
                if soil=="Суглинистая" or soil=="Легкосуглинистая":
                    sv "А ещё вдобавок не вкусные!"
                sv "Не сказала бы, что работа проделана отлично."
                show sv smile
                sv "Но ты всегда можешь перееиграть и выйти на более лучший результат!"
                sv "Надеюсь, ты запомнил свои ошибки и в следующий раз качество помидоров будет лучше!"
            else:
                if soil=="Суглинистая" or soil=="Легкосуглинистая":
                    show sv sad
                    sv "Но они не вкусные!"
                    sv "Кажется, мы где-то ошиблись."
                    show sv smile
                    sv "Но ты всегда можешь перееиграть и выйти на более лучший результат!"
                    sv "Надеюсь, ты помнишь свои ошибки и в следующий раз помидоры будут вкусными!"
                else:
                    sv "Они вдобавок ещё и отличного качества!"
                    sv "Не смотря на то, что мы не достигли предела, это уже хороший результат."
                    sv "Но ты всегда можешь перееиграть и выйти на более лучший результат!"
                    show sv calm2
                    sv "Надеюсь, ты помнишь свои ошибки и в следующий раз картошки будет больше!"
        elif 500>Ur>200:
            if cult=="Помидор(Ин.)":
                show tomato idtstage3low with dissolve
            elif cult=="Помидор(Дт.)":
                if q==0:
                    show tomato stage3low behind sv
                else:
                    show tomato stage3beltlow behind sv
            play sound grow
            $ renpy.pause(1.5, hard=True)
            play sound picturebuzzer
            show sv sad at centre with easeinbottom
            sv "Ты вырастил [Ur] ценнера помидоров. Это очень мало."
            if taste<24:
                show sv sad
                sv "Так ещё они не самого лучшего качества."
                if soil=="Суглинистая" or soil=="Легкосуглинистая":
                    sv "А ещё вдобавок не вкусные!"
                show sv smile
                sv "Не расстраивайся, ладно? Ты всегда можешь переиграть и выйти на более лучший результат!"
                sv "Надеюсь, ты запомнил свои ошибки и в следующий раз качество помидоров будет лучше!"
            else:
                if soil=="Суглинистая" or soil=="Легкосуглинистая":
                    sv "Вдобавок они ещё и не вкусные."
                    sv "Такой убыток."
                    sv "Мы где-то очень серьезно ошиблись. Ты же помнишь где именно?"
                    show sv smile
                    sv "Ты всегда можешь перееиграть и выйти на более лучший результат!"
                else:
                    show sv smile
                    sv "Однако они отличного качества!"
                    sv "Хоть и маленький, но уже успех."
                    sv "Однако ты всегда можешь перееиграть и выйти на более лучший результат!"
                    show sv calm2
                    sv "Надеюсь, ты помнишь свои ошибки и в следующий раз картошки будет больше!"
    else:
        hide tomato
        play sound badend
        show sv sad at centre with easeinbottom
        sv "Упс, кажется ты настолько плохо слушал мои указания, что в итоге у нас не выросли помидоры!"
        show sv smile
        sv "Не расстраивайся, ладно? Ты всегда можешь переиграть и выйти на более лучший результат!"
        sv "Надеюсь, ты помнишь где ошибся и в следующий раз у тебя будет какая-никакие помидоры."

    avtor "{color=#ffd040}{size=50}ИТОГИ{/size}{/color}"
    avtor "Урожайность [Ur]/900"
    avtor "Качество [taste]/48"
    if Ur>500:
        $point +=50
        if 49>taste>24:
            $point+=50
        else:
            $point-=20
    if 501>Ur>200:
        $point +=25
        if 49>taste>24:
            $point+=50
        else:
            $point-=20
    if 201<Ur>50:
        $point+=5
        if 49>taste>24:
            $point+=50
        else:
            $point-=20
    if Ur<50:
        $point+=0
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
    if fert<1:
        avtor "-3 - отказ от подкормки"
    elif wee<2:
        avtor "-3 - недостаток подкормки"
    if 300>Nu>119:
        avtor "-12 - переизбыток азотного удобрения"
    if ktomato >0:
        avtor "Прошлый балл за прохождение: [tomato]"
    avtor "{size=40}Заработано очков [point]{/color}"
    $ ktomato+=1
    $ tomato=point
    $ money+=point
    show sv smile
    sv "Какой овощ ты хочешь посадить следующим?"
    hide tomato
    show sv at right with ease
    show soil peaty behind sv with dissolve
    show farm spring behind soil with dissolve
    $ renpy.block_rollback()
    jump route
