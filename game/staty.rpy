screen staty():
    style_prefix "staty"

    add "gui/staty/staty.png"
    if vid in [1,2,3,4]:
        add "gui/staty/cv[vid].png"
    label month + ", [t]°C" pos (180, 20) at xz(x=0.7)

    vbox at naklon:
        pos (28, 52)
        text _("Культура:")
        text _("Урожайность(ц/га):")
        text _("Качество(баллы):")
        text _("Этап:")
    vbox at naklon:
        xminimum 200
        pos (60, 88)
        text "[cult]"
        text "[Ur]"
        text "[taste]"
        text "[stage_name]"

style staty_label_text:
    size 50
style staty_text:
    font "MarckScript.ttf"
    color "#3A247B"
    size 28
style staty_vbox:
    xminimum 100
    spacing 30
