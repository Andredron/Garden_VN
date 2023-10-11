label splashscreen:
    scene black

    menu:
        "English":
            $ renpy.change_language("english")
        "Русский":
            $ renpy.change_language("russian")

    show logo2 with dissolve
    $ renpy.pause(1.5, hard=True)
    hide logo2 with dissolve      
    show logo with dissolve
    $ renpy.pause(1.5, hard=True)
    hide logo with dissolve
    return

screen name_input:
    modal True
    frame:
        background Frame("#7fb000")
        align (0.5, 0.5)
        xsize 400 ysize 200
        vbox:
            xfill True
            yfill True
            text _("{color=#ffd040}Ваше имя?{/color}")  xalign 0.5
            input id "input" xalign 0.5 length 14 allow "йцукенгшщззхъёфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮQWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
################################################################
label start:
    with fade2
    call screen name_input
    $ pl_name =_return
    if len(pl_name)==0:
        $ pl_name = "Аноним"
label game:
    with fade2
    play music Village fadein 3
    scene bc
    show sun at sunfarm
    show farm spring
    show soil peaty
    $ renpy.block_rollback()
    avtor "Вы, [pl_name], начинающий огородник."
    avtor "Вы пару дней назад переехали из большого города, чтобы начать новую жизнь и посвятить её выращиванию сельскохозяйственных культур."
    avtor "Теперь вашей целью является обучиться и понять технологию выращивания сельскохозяйственных культур."
    nvl clear
    avtor "Сейчас на фоне, ты видишь свой огород."
    avtor "Плодородное и живописное место. Самое то для того чтобы выращивать овоши."
    avtor "Однако выращивать овощи с кем-то гораздо легче, чем одному."
    avtor "У тебя будет помощница, которая объяснит как нужно правильно вырастить культуру."
    avtor "Желаю удачи!"
    nvl hide
    play sound picturebuzzer
    show sv smile at centre with easeinbottom
    sv "Приветствую тебя на огороде, [pl_name]! Меня зовут {color=#ffd040}Гончарова Светлана{/color}, но называй меня просто {color=#ffd040}Света{/color}."
    sv "Я так понимаю, ты именно тот, кого мне нужно будет обучать."
    sv "Можешь не волноваться! Ты в надежных руках!"
    sv "Для начала ты можешь ознакомиться с основными моментами выращивания овощей."
    sv "Но если ты уже и так все знаешь, ты можешь пропустить этот момент."
    nvl clear
    show sv at right with ease
    play sound picturebuzzer
    show plant0 at left5 with easeinright
    ##Теоритически сводки
    menu teory:
        "Игровой процесс":
            hide plant0
            $ renpy.block_rollback()
            show manual slide1
            $ renpy.pause(delay=None)
            play sound click
            show manual slide2
            $ renpy.pause(delay=None)
            play sound click
            show manual slide3
            $ renpy.pause(delay=None)
            play sound click
            show manual slide4
            $ renpy.pause(delay=None)
            play sound click
            show manual slide5
            $ renpy.pause(delay=None)
            play sound click
            show manual slide6
            $ renpy.pause(delay=None)
            play sound click
            show manual slide7
            $ renpy.pause(delay=None)
            play sound click
            show manual slide8
            $ renpy.pause(delay=None)
            play sound click
            show manual slide10
            $ renpy.pause(delay=None)
            play sound click
            show manual slide11
            $ renpy.pause(delay=None)
            play sound click
            show manual slide12
            $ renpy.pause(delay=None)
            play sound click
            show manual slide13
            $ renpy.pause(delay=None)
            play sound click
            hide manual
            $ renpy.block_rollback()
            play sound picturebuzzer
            show plant0 at left5 with easeinright
            jump teory
        "{image=icon_fert}Удобрение{image=icon_fert}":
            hide plant0
            $ renpy.block_rollback()
            avtor "{color=#ffd040}Удобения{/color} — вещества для питания растений и повышения плодородия почв. Их эффект обусловлен тем, что они предоставляют растениями один или несколько дефецитных компонентов, необходимых для нормального роста и развития."
            avtor "Удобения бывают {color=#ffd040}минеральные{/color} и {color=#ffd040}органические{/color}."
            avtor "{color=#ffd040}Органические удобрения{/color} - это удобрения содержащие элементы питания в виде органических соеденений."
            nvl clear
            avtor "Они содержат основные элементы для питания растений такие как азот, фосфор, калий, кальций и т.д"
            avtor "К органическому удобрению относят навоз, компост, торф, солома, зеленое удобрение, ил, промышленные и хозяйственные отходы."
            avtor "{color=#ffd040}Минеральное удобрение{/color} - неорганическое соеденение содержащие необходимые для растений элементы питания."
            avtor "Минеральные удобрения бывают {color=#ffd040}простые{/color} и {color=#ffd040}комплексные{/color}."
            window hide
            nvl clear
            avtor "{color=#ffd040}Простые удобрения{/color} содержат один конкретный элемент питания."
            avtor "{color=#ffd040}Комплесные удобрения{/color} содержат в себе одновременное два и более основных питательных элементов."
            nvl clear
            $ renpy.block_rollback()
            show plant0 at left5 with easeinright
            play sound picturebuzzer
            jump teory
        "{image=icon_poison}Химическая защита{image=icon_poison}":
            hide plant0
            $ renpy.block_rollback()
            avtor "{color=#ffd040}Химическая защита растений{/color} — система мероприятий по защите растений и продукции растительного происхождения от вредных организмов с помощью химических средств."
            avtor "{color=#ffd040}Пестициды{/color} — ядовитые вещества, используемые для уничтожения вредителей и возбудителей болезней растений, а также различных паразитов, сорняков, вредителей зерна и зернопродуктов, древесины, изделий из хлопка, шерсти, кожи, эктопаразитов домашних животных, переносчиков опасных заболеваний человека и животных. Является объеденяющим понятием {color=#ffd040}гербицидов{/color}, {color=#ffd040}инсектицидов{/color} и {color=#ffd040}фунгицидов{/color}."
            nvl clear
            avtor "{color=#ffd040}Фунгициды{/color} — химические препараты предназначенные для борьбы с грибковыми болезнями растений."
            avtor "{color=#ffd040}Гербициды{/color} — химические препараты предназначенные для уничтожения нежелательной растительности."
            avtor "{color=#ffd040}Инсектициды{/color} — химические препараты предназначенные для унижения вредных насекомых."
            window hide
            nvl clear
            $ renpy.block_rollback()
            play sound picturebuzzer
            show plant0 at left5 with easeinright
            jump teory
        "{image=icon_peaty}Почва. Виды почв{image=icon_peaty}":
            hide plant0
            $ renpy.block_rollback()
            avtor "{color=#ffd040}Почва{/color} — это поверхностных слой земной коры, вохникающий в результате влияние организмов, воздуха, влаги и солнечного света на литосферу и имеет свойство плодородия."
            avtor "{color=#ffd040}Плодородие почвы{/color} — способность почвы удолетворять потребность растений в элементах питания, влаге и воздухе, а также обеспечивать условия для их нормальной работы."
            avtor "Используемые в данном приложении почвы являются {color=#ffd040}глинистая{/color}, {color=#ffd040}песчаная{/color}, {color=#ffd040}супесчаная{/color}, {color=#ffd040}суглинистая{/color}, {color=#ffd040}торфяная{/color}, {color=#ffd040}дерновая{/color}."
            nvl clear
            avtor """{color=#ffd040}Глинистая почва(Глинозем){/color}\n
            {size=25}Относятся к тяжелым почвам с преобладанием в составе глинистых и лессовых (илистых) осадочных пород. Их трудно обрабатывать, в них мало воздуха и они холоднее песчаных почв. Развитие растений на них несколько запаздывает. На поверхности очень тяжелых почв может застаиваться вода из-за низкого коэффициента водопоглощения. Поэтому выращивать на ней культуры достаточно проблематично. Однако, если глинистую почву грамотно окультурить, она способна стать достаточно плодородной.
            Глинистую почву можно определить по крупнокомковатой плотной структуре, увлажненная липнет к ногам, плохо впитывает воду, легко слипается.{/size}"""
            nvl clear
            avtor """{color=#ffd040}Песчаная почва(Песчаниики){/color}\n
            {size=25}Относятся к легким видам почв. Они рыхлые, сыпучие, легко пропускают воду. Если горсть такой земли взять в руки и попробовать сформировать комок, то он будет рассыпаться.
            Достоинство таких почв — они быстро прогреваются, хорошо аэрируются, легко обрабатываются. Но вместе с тем, быстро охлаждаются, пересыхают, слабо удерживают в зоне корней минеральные вещества — и это недостаток. Питательные элементы вымываются водой в глубинные слои грунта, что приводит к снижению наличия полезной микрофлоры и пригодности для выращивания культур.{/size}"""
            nvl clear
            avtor """{color=#ffd040}Супесчаная почва(Супеси){/color}\n
            {size=25}Ещё один вариант легких по механическому составу грунтов. По своим качествам они схожи с песчаником, но содержат немного больший процент глинистых включений.
            Основные достоинства супесей —  они обладают лучшей удерживающей способностью к минеральным и органическим веществам, быстро прогреваются и относительно долго его удерживают, меньше пропускает влагу и медленнее пересыхает, хорошо аэрируется и легко поддается обработке.
            При обычных методах и выборе районированных сортов на супесчаной почве может расти все. Это один из неплохих вариантов для садов и огородов. Однако приемы повышения и поддержания плодородия для данных почв так же приемлемы. Это предполагает внесение органики (в обычных дозах), высев сидеральных культур, проведение мульчирования.{/size}"""
            nvl clear
            avtor """{color=#ffd040}Суглинистая почва(Суглинки){/color}\n
            {size=25}Самый подходящий вид для выращивания садово-огородных культур. Она легко поддается обработке, содержит большой процент питательных элементов, имеет высокие показатели воздухо- и водопроводимости, способна не только сохранять влагу, но и равномерно распределять ее по толще горизонта, хорошо удерживает тепло.
            Определить суглиник можно, взяв пригоршню данного грунта в ладони и скатать его.
            Благодаря совокупности имеющихся свойств, суглинистую почву не нужно улучшать, а необходимо только поддерживать ее плодородие: мульчировать, периодически вносить органические и минеральными удобрениями.{/size}"""
            nvl clear
            avtor """{color=#ffd040}Болотистая почва(Торфянник){/color}\n
            {size=25}Данные почвы не редкость на садовых участках. К сожалению, назвать их хорошими для выращивания культур сложно. Это обусловлено минимальным содержании в них элементов питания для растений. Такие почвы быстро впитывают воду, так же быстро ее и отдают, плохо прогреваются, часто имеют высокий показатель кислотности.
            Используя в качестве огорода, торфяник нужно тщательно окультуривать или, как в варианте с песчаными почвами, закладывать глиняную прослойку и уже на нее засыпать перемешанный с торфом суглинок, органические удобрения и известь. Для выращивания крыжовника, смородины, черноплодной рябины и садовой земляники можно ничего не делать, только поливать и выпалывать сорняки, так как данные культуры на таких почвах произрастают и без окультуривания.{/size}"""
            nvl clear
            avtor """{color=#ffd040}Дерновая почва{/color}\n
            {size=25}Являются интразональными, обладают высоким плодородием. Гумусовый горизонт ярко выражен и имеет комковато-зернистую структуру. В нем преобладают гуминовые кислоты, а содержание гумуса достигает 15%%. Оподзоленность отсутствует или выражена слабо.
            В грунтах заметно повышенное содержание азота и зольных элементов, которые питают растения. В их профиле присутствуют карбонаты. Слабокислая, нейтральная или слабощелочная реакция. Емкость поглощения высокая.{/size}"""
            window hide
            $ renpy.block_rollback()
            nvl clear
            play sound picturebuzzer
            show plant0 at left5 with easeinright
            jump teory
        "Закончить обучение":
            hide plant0
            $ renpy.block_rollback()
    if mn<1:
        show sv at centre with ease
        sv "Теперь самое время решить какую культуру ты хочешь посадить."
        sv "У меня есть несколько семян с собой. Выбирай, что хочешь."
        window hide
        $mn=1
        show sv at right with ease
        play sound picturebuzzer
        show plant4 at left5 with easeinright
    else:
        show sv at centre with ease
        sv "Какую культуру ты хочешь посадить?"
        window hide
        show sv at right with ease
        play sound picturebuzzer
        show plant4 at left5 with easeinright

    menu route:
        "{image=icon_potato}Картошка{image=icon_potato}":
            hide plant4
            jump potato_route
        "{image=icon_tomato}Помидор{image=icon_tomato}":
            hide plant4
            jump tomato_route
        "{image=icon_corn}Кукуруза{image=icon_corn}":
            hide plant4
            jump corn_route
        "{image=icon_teory}Теоритическое обучение.{image=icon_teory}":
            hide plant4
            play sound picturebuzzer
            show plant0 at left5 with easeinright
            jump teory
