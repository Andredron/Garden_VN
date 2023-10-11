############################################################
##ПЕРЕМЕННЫЕ
############################################################
init:
#Персонажи
    $ avtor = Character(None, what_color="#ffffff", kind=nvl)
    $ player = Character('[pl_name]', color="#ffffff")
    $ un = Character('???', color="#ffffff")
    $ sv = Character(_('{color=#e62e24}С{/color}вета'), color="#ffffff")
    $ il = Character(_('{color=#e62e24}И{/color}лья'), color="#ffffff")

##Переменные для игры
    $ pl_name = "" ##Имя
    $ cult = "" ##Культура
    $ t = 0 ##Темература
    $ soil = "Неизвестно" ##Почва
    $ stage_name = "???" ##Почва
    $ month = "???" ##Месяц
    $ taste = 0 ##качество
    $ Ur = 0 ##Урожай
    $ vid = 2
    $ svFrendship = 20 #очки дружбы с Машей
    $ ilFrendship = 0 #очки дружбы с Ильей
    $ point = 0
    $ money = 0
    $ err = 0 ##Переключатель
##Количества удобрений
    $ Pu = 0 ##Фосфорное удобрение
    $ Nu = 0 ##Азотное удобрение
    $ Ku = 0 ##Калийное удобрение
    $ Eu = 0 ##Органическое удобрение
##Доп.переменные
    $ q = 0
    $ mn = 0
    $ wee = 0 #кол-во прополки
    $ herbi = 0 #кол-во гербецидов
    $ insec = 0 #кол-во инсектецидов
    $ fungi = 0 #кол-во фунгицидов
    $ fert = 0 #кол-во фунгицидов
    $ it= 0
##Последние баллы
    $ kpotato = 0
    $ potato = 0
    $ ktomato = 0
    $ tomato = 0
##Счетчик рутов
init python:
    if persistent.ends is None:
        persistent.ends = []
    def end(name):
        if not name in persistent.ends:
            persistent.ends.append(name)
############################################################
##Техническое
############################################################
init:
##Переходы
    $ flash = Fade(0, 0, 0.2, color="#fff")
    $ flash2 = Fade(0, 0, 1, color="#fff")
    $ fade2 = Fade(1, 0, 1, color="#000000")
##Позиции
    transform left:
        xalign 0.80
        yalign 1.0
    transform left2:
        xalign 0.90
        yalign 0.05
    transform left3:
        xalign 0.88
        yalign 0.2
    transform left4:
        xalign 1.0
        yalign 0.2
    transform left5:
        xalign 1.0
        yalign 0.1
    transform right:
        xalign -0.05
        yalign 1.0
    transform right2:
        xalign 0.35
        yalign 1.0
    transform right3:
        xalign 0.26
        yalign 1.0
    transform right4:
        xalign 0.1
        yalign 1.0
    transform centre:
        xalign 0.5
        yalign 1.0
    transform sunfarm:
        xalign 1.2
        yalign -0.7
    transform xz(x=0.75):
        xzoom x
    transform attach:
        xalign 0.99
        yalign 0.3
    transform attach4:
        xalign 0.95
        yalign 0.3
    transform attach2:
        xalign 0.85
        yalign 0.15
    transform attach3:
        xalign 0.96
        yalign 0.7
    transform attach5:
        xalign 0.9
        yalign 0.1
    transform attach6:
        xalign 0.96
        yalign 0.75
    transform xz(x=0.75):
        xzoom x
    transform naklon:
        rotate -5
screen ctc(arg=None):
    if not config.skipping:
        on 'hide' action Play('sound', 'audio/sound/Click.wav')
########################################А####################
##Саунд
############################################################
#BGM
define audio.Village = "audio/BGM/BGM-village.mp3"

#EMOTION
define audio.gloom = "audio/sound/GLOOM.wav"
define audio.shout = "audio/sound/SHOUT.wav"
define audio.wow = "audio/sound/WOW.wav"

#SE
define audio.spray = "audio/sound/SPRAYING.wav"
define audio.dig = "audio/sound/DIG.wav"
define audio.grow = "audio/sound/GROWTH.wav"
define audio.laugh = "audio/sound/LAUGH.wav"
define audio.badend = "audio/sound/badend.wav"
define audio.picturebuzzer = "audio/sound/picturebuzzer.wav"
define audio.cut = "audio/sound/CUT.wav"
define audio.addfert = "audio/sound/addfert.wav"
