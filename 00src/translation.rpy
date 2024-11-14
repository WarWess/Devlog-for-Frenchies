init offset = -1

screen OkPrompt(message, go_menu):

    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("OK") activate_sound "audio/ui/tick_001.ogg" action If(go_menu, true=MainMenu(False,False), false=[Hide(),Return()])

screen hiddenOkPrompt(message, go_menu):

    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("OK") activate_sound "audio/ui/tick_001.ogg" action If(go_menu, true=MainMenu(False,False), false=Hide())

default persistent.seenWarning = []
default persistent.languaged_up = None

init python:

    from math import ceil

    notice = _("NOTICE: Please keep in mind this is a fan translation, and as such it may not be completely accurate to the original intent of any written lines.")

    languages = [
        {'image': 'gui/flag/USA.png', 'name': 'English', 'value': 'English' },
        {'image': 'gui/flag/Mexico.png', 'name': 'Español', 'value': 'Spanish'},
        {'image': 'gui/flag/Russia.png', 'name': 'Русский', 'value': 'Russia'},
        {'image': 'gui/flag/France.png', 'name': 'Français', 'value': 'French'}
    ]


    maxItems = len(languages)
    maxRows = ceil(maxItems/4)
    if maxItems > 4:
        maxItems = 4*maxRows

init:
    transform renpysdumb: # Needed to scale down the imagebuttons.
        zoom 0.5
    transform icon: #For the preferences screen
        truecenter
        zoom 0.1

    transform glowie(img):
        img
        easein_cubic 0.30 matrixcolor TintMatrix(Color((255, 255, 255)))

    transform darkie(img):
        img
        easeout_cubic 0.30 matrixcolor TintMatrix(Color((255/2, 255/2, 255/2)))

screen lang_sel():

    tag menu

    frame:

        background Transform(gui.main_menu_background, matrixcolor=TintMatrix('#222'))

        padding (120, 40)

        vbox:
            style_prefix "navigation"
            vbox:
                label _("Choose Your Language") text_size 80
                add Null(0, 40)

            vpgrid:
                if maxItems <= 4:
                    cols maxItems
                    rows 1
                else:
                    cols 4
                    rows maxRows
                #spacing 30
                draggable True
                mousewheel True

                if maxRows > 3:
                    scrollbars "vertical"

                for i in range(maxItems):
                    fixed:
                        xsize 400
                        ysize 300
                        vbox:
                            if i<len(languages):
                                text languages[i]["name"] at top
                                add Null(0,10)
                                imagebutton:
                                    idle darkie(languages[i]["image"])
                                    hover glowie(languages[i]["image"])
                                    action If(languages[i]["value"] in persistent.seenWarning or languages[i]["value"] == 'English', 
                                        true = [Language(languages[i]["value"]), Return()],
                                        # Important to change the language before calling notice. Otherwise it will be in english.
                                        false = [Language(languages[i]["value"]), AddToSet(set=persistent.seenWarning, value=languages[i]["value"]), Show(screen="OkPrompt", message=notice, go_menu=False)]
                                        )
                                    at renpysdumb # Scales the imagebutton down. No, you can't just specify the zoom here. It has to be a defined transform.
                            else:
                                # Renpy seethes if a vpgrid doesn't have the exact maximum amount of items for some reason.
                                add Null(0,0)
                            at truecenter

screen lang_button(lang):
    hbox:
        spacing 15
        textbutton lang["name"]:
            activate_sound "audio/ui/tick_001.ogg"
            action If(lang["value"] in persistent.seenWarning or lang["value"] == 'English', 
            true = [Language(lang["value"])],
            false = [Language(lang["value"]), AddToSet(set=persistent.seenWarning, value=lang["value"]), Show(screen="hiddenOkPrompt", message=notice, go_menu=False)]
            )
        if _preferences.language == lang["value"]:
            add glowie(lang["image"]) at icon
        else:
            add darkie(lang["image"]) at icon
