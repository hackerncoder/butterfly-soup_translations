################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language
    font "YunusH.ttf"
translate tamil style default:
    font "tamil.ttf"

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")
    font "YunusH.ttf"
translate tamil style gui_text:
    font "tamil.ttf"
    size 24

style button:
    properties gui.button_properties("button") #This is the menu side and selection text. For example, the "Fullscreen" option text
    hover_sound "sound/peep.ogg"
    activate_sound "sound/select2.ogg"
style button_text is gui_text:
    properties gui.text_properties("button")
    font "YunusH.ttf"
    yalign 0.5
translate tamil style button_text:
    font "tamil.ttf"
    size 20

#alternate buttons
style textbutton1 is default: #settings menu buttons
    properties gui.button_properties("main_menu_button")
    hover_sound "sound/peep.ogg"
style textbutton1_text is gui_button_text
style textbutton1_text:
    font "YunusH.ttf"
    size 32
translate tamil style textbutton1_text:
    font "tamil.ttf"
    size 20


style textbutton2 is default: #settings menu buttons
    properties gui.button_properties("main_menu_button")
    hover_sound "sound/pop.ogg"

style textbutton2_text is gui_button_text
style textbutton2_text:
    font "YunusH.ttf"
    size 32
translate tamil style textbutton2_text:
    font "tamil.ttf"
    size 20

style choice1_button:
    hover_sound "sound/peep.ogg"

style choice2_button:
    hover_sound "sound/pop.ogg"

style label_text is gui_text:
    properties gui.text_properties("label", accent=True)
    font "YunusH.ttf"
translate tamil style label_text:
    font "tamil.ttf"
    #size 20

style prompt_text is gui_text:
    properties gui.text_properties("prompt")
    font "YunusH.ttf"
translate tamil style prompt_text:
    font "tamil.ttf"
    size 20

style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)



style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Solid('#f69fe3')
   # base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
   # thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Solid("#949EF5")
    hover_thumb ("#c1c8fb")
    ypos 0
    xpos -100
    ysize 400


style vscrollbar2 is default:
   # properties gui.bar_properties("vscrollbar")
#    define gui.vbar_borders = Borders(4, 4, 4, 4)
#    define gui.vscrollbar_borders = Borders(4, 4, 4, 4)
#    define gui.vslider_borders = Borders(4, 4, 4, 4)
    base_bar None
    #    style.vscrollbar.hover_background = "#919191" does nothing
    thumb Solid("#949EF5")
    hover_thumb ("#c1c8fb")
    xsize gui.scrollbar_size
   #xsize 15
    xpos 0.51
    bar_vertical True
    ypos 8
style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

style image_button:
    hover_sound "sound/peep.ogg"
    activate_sound "sound/select2.ogg"

style imagebutton1 is default:
    properties gui.button_properties("image_button")
    hover_sound "sound/peep.ogg"

style imagebutton2 is default:
    properties gui.button_properties("image_button")
    hover_sound "sound/pop.ogg"

################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"
    if newSpeaker:
        window:
            id "window"
            #at winFade
            if who is not None:

                window:
                    style "namebox"
                    text who id "who"

            text what id "what"

    else:

        window:
            id "window"
            if who is not None:

                window:
                    style "namebox"
                    text who id "who"

            text what id "what"


                ## If there's a side image, display it above the text. Do not display on the
                ## phone variant - there's no room.
    if not renpy.variant("small"):
            add SideImage() xalign 0.0 yalign 1.0
style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign 1.0
    ysize 250
    right_padding 35
    top_padding 78
    left_padding 105
    ypos 753
    left_margin 15
    right_margin 0
    yminimum  250
    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox: #literally the pink/blue namebox
    xpos -78
    xanchor 0
    xsize 430
    ypos -95
    ysize gui.namebox_height

    background "gui/namebox2.png"
    left_padding 36
    top_padding 16
   # background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
   # padding gui.namebox_borders.padding
translate tamil style namebox:
    top_padding 14 #adjust height of name text inside namebox

style say_label:
    properties gui.text_properties("name", accent=True)
  #  xalign gui.name_xalign
    yalign 0.5
translate tamil style say_label:
    font "tamil.ttf"
    size 40

style say_dialogue:
    properties gui.text_properties("dialogue")
    font "myriad.OTF"
    size 36
    xpos 0
    xsize 1000
    ypos 0
    line_spacing 2
translate tamil style say_dialogue:
    font "tamil.ttf"
    size 32

translate farsi python:
    gui.dialogue_text_xalign = 1.0  #right align text

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):



    style_prefix "choice"
    $n=1
     #for language select choice, make special menu that's 2 columns
    if menuStyle == "language":
        vpgrid:
            cols 2
            xalign 0.5
            yalign 0.5

            for i in items:
                if i.action:

                    button:
                        action i.action
                        style "language_choice_button"

                        text i.caption style "language_choice_button"

                else:
                    text i.caption style "language_choice_button_text"
    else:
        vbox:
               for i in items:
                    if (n % 2 == 0): #even


                        if i.action:

                            button:
                                action i.action
                                style "choice2_button"

                                text i.caption style "choice2_button"

                        else:
                            text i.caption style "choice1_button_text"
                    else: #odd



                        if i.action:

                            button:
                                action i.action
                                style "choice1_button"

                                text i.caption style "choice1_button"

                        else:
                            text i.caption style "choice1_button_text"

                    $n+=1
## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style language_choice_button is button: #language choice
    properties gui.button_properties("choice_button")
    top_padding 20
    xpos 0.5
    xanchor 0.5
    hover_color gui.accent_color
    size 42
    idle_background Frame ("gui/button/language_choice_idle_background.png", 0, 0 )
    hover_background  Frame ("gui/button/language_choice_hover_background.png", 0, 0 )
    xminimum int(config.screen_width * 0.25)
    xmaximum int(config.screen_width * 0.25)
translate japanese style language_choice_button:
    size 28
style language_choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    idle_background Frame ("gui/button/language_choice_idle_background.png", 0, 0 )
    hover_background  Frame ("gui/button/language_choice_hover_background.png", 0, 0 )



style choice1_button is default: #in-game choice
    properties gui.button_properties("choice_button")
    top_padding 20
    xpos 0.5
    xanchor 0.5
    hover_color gui.accent_color
    font "YunusH.ttf"
    size 42

style choice1_button_text is default:
    properties gui.button_text_properties("choice_button")
translate tamil style choice1_button:
    font "tamil.ttf"
    size 32

style choice2_button is default:
    properties gui.button_properties("choice_button")
    idle_background Frame ("gui/button/choice2_idle_background.png", 0, 0 )
    hover_background  Frame ("gui/button/choice2_hover_background.png", 0, 0 )
    xpos 0.5
    xanchor 0.5
    top_padding 25
    hover_color gui.accent_color
    font "YunusH.ttf"
    size 42
style choice_vbox is vbox
style choice_button is button
translate tamil style choice2_button:
    font "tamil.ttf"
    size 32

style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

translate japanese style choice_vbox:
    ypos 340

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    color "#fff"

screen quick_menu():

#    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 0.9
        yalign 0.968

        textbutton _("Save") action ShowMenu('save')
#        textbutton _("Skip") action Skip()
        textbutton _("Skip") action Skip(fast=True, confirm=True)
##        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu('preferences')

screen quick_menu3:
    style_group "navigation"
    add "gui/qMenuBar.png" xanchor 1.0 xpos 1366 yanchor 0 ypos -1

    imagebutton:
        style "imagebutton2"
        auto "gui/rollback_%s.png" action renpy.rollback xpos 1096  ypos 18

    imagebutton:
        style "imagebutton1"
        auto "gui/quick_log_%s.png" action ShowMenu('history') xpos 1141 ypos 18

    imagebutton:
        style "imagebutton2"
        auto "gui/quick_skip_%s.png" action Skip(fast=False, confirm=True) xpos 1191 ypos 18
    imagebutton:
        style "imagebutton1"
        auto "gui/quick_save_%s.png" action ShowMenu('save') xpos 1251 ypos 18
    imagebutton:
        style "imagebutton2"
        auto "gui/quick_config_%s.png" action ShowMenu('preferences') xpos 1296 ypos 18


init -2:
    style quick_button:
        is default
        background None
        xpadding 10

    style quick_button_text:
        is default
        size 2
        outlines [(2, "#fff", 0, 0)]
        idle_color "#000"
        hover_color "#545454"
        selected_idle_color "#000"
        selected_hover_color "#545454"
        insensitive_color "#4448"


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():
    modal True
    zorder 1000
    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        #yalign 0.5
        yanchor 0
        ypos gui.navigation_ypos

        spacing gui.navigation_spacing

        if main_menu:

       #     textbutton _("Start") action Start()
            textbutton _("New Game"):
                style "textbutton1"
                action Show ("whiteScreen", transition=Dissolve(1.4))# hovered [ Play ("test_one", "sound/menuClick.ogg") ]
        else:

            textbutton _("History"):
                style "textbutton2"
                action ShowMenu("history") #hovered [ Play ("test_one", "sound/menuClick.ogg") ]

            textbutton _("Save"):
                style "textbutton1"
                action ShowMenu("save")# hovered [ Play ("test_one", "sound/menuClick.ogg") ]

        textbutton _("Load Game"):
            style "textbutton2"
            action ShowMenu("load")# hovered [ Play ("test_one", "sound/menuClick.ogg") ]

        textbutton _("Settings"):
            style "textbutton1"
            action ShowMenu("preferences") #hovered [ Play ("test_one", "sound/menuClick.ogg") ]

        textbutton _("About"):
            style "textbutton2"
            action ShowMenu("about")# hovered [ Play ("test_one", "sound/menuClick.ogg") ]
        if _in_replay:

            textbutton _("End Replay"):
                style "textbutton2"
                action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu"):
                style "textbutton1"
                action MainMenu() #hovered [ Play ("test_one", "sound/menuClick.ogg") ]
           # textbutton _("Main Menu") action Show ("qte_titleScreen2")
        if renpy.variant("pc"):

            ## Help isn't necessary or relevant to mobile devices.
            #textbutton _("Help") action ShowMenu("help")

            ## The quit button is banned on iOS and unnecessary on Android.
            textbutton _("Quit"):
                style "textbutton1"
                action Quit(confirm=not main_menu)# hovered [ Play ("test_one", "sound/menuClick.ogg") ]


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

   # hover_background Frame ("gui/underButton.png", 0,0)
style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


##############################################################################
# new Main Menu

# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu
## ■██▓▒░ MAIN MENU ░▒▓█████████████████████████████████████■
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu
screen main_menu:
    style_prefix "main_menu"
    tag menu # This ensures that any other menu screen is replaced.

  #  add gui.main_menu_background
 #   add "gui/main_menu.png"# Add a background image for the main menu.
 #   add "gui/logo.png" at titleFade
    if persistent.ending1:

        add "titleScantron2" at Pan((0, 0), (0, 3417), 95, repeat=True)
    else:
        add "titleScantron1" at Pan((0, 0), (0, 3417), 95, repeat=True)
    add "gui/title.png" at titleFade3
   # add "gui/titleLine.png" at titleFade2

    $ y=180 # To make things easier, we define a variable y and use it to set positions for our imagebuttons

    hbox:
            at titleFade4
            textbutton _("New Game") action Show ("whiteScreen", transition=Dissolve(1.4))
            textbutton _("Load Game") action ShowMenu("load")
            textbutton _("Settings") action ShowMenu("preferences")
     #   if persistent.extra_unlocked: # We only show the extras, if they have been unlocked. Because we are using a variable (y) for ypos, we don't need to worry about positioning the rest of the button(s).
     #       imagebutton auto "gui/main_extras_%s.png" xpos 773 ypos y focus_mask True action Start('extras') hovered [ Play ("sound", "sound/menuClick.ogg") ] at main_eff4
            textbutton _("About") action ShowMenu("about")
            textbutton _("Quit") action Quit(confirm=not main_menu)

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_hbox:
    font "YunusH.ttf"
    spacing 21
    xpos 411
    ypos 513

translate tamil style main_menu_hbox:
    font "tamil.ttf"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")

style main_menu_button:
    left_padding 9
    right_padding 9
translate tamil style main_menu_button: #optional, only japanese and korean have it in the official
    left_padding 24
    right_padding 24

style main_menu_button_text: #main title screen buttons
    xanchor 0.5
    xalign 0.5
    text_align 0.5
    font "YunusH.ttf"
    size 45
    color "#c1adff"
    hover_color "#ffcef2"
translate tamil style main_menu_button_text:
    font "tamil.ttf"
    size 36


init -2:
    transform main_eff1:
        zoom 0.5
        easein 0.8 zoom 1.0
    transform main_eff2:
        zoom 0.5
        easein 1.2 zoom 1.0
    transform main_eff3:
        zoom 0.5
        easein 1.6 zoom 1.0
    transform main_eff4:
        zoom 0.5
        easein 1.8 zoom 1.0
    transform main_eff5:
        zoom 0.5
        easein 2.0 zoom 1.0


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None):

    style_prefix "game_menu"
    modal True
    zorder 1000
    if persistent.ending1:

        add "titleScantron2" at Pan((0, 0), (0, 3417), 95, repeat=True)
    else:
        add "titleScantron1" at Pan((0, 0), (0, 3417), 95, repeat=True)
#    if main_menu:
#        add "titleScantron" at Pan((0, 0), (0, 768), 65, repeat=True)
#       # add gui.main_menu_background
#    else:
#        add "titleScantron" at Pan((0, 0), (0, 768), 65, repeat=True)
       # add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial 1.0

                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 160

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    ysize 500
    #yfill True

style game_menu_content_frame:
    left_margin 130
    right_margin 120
    top_margin 10
translate tamil style game_menu_content_frame: #(official comment) doesn't seem to do anything?
    left_margin 130 #optional, only chinese and pt-BR has it official

style game_menu_viewport:
    xsize 920
    ysize 400

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 480
    ypos 40
    ysize 120

style game_menu_vpgrid:
    ysize 400

style game_menu_label_text: #the settings title in the white rectangle
    font "YunusH.ttf"
    size gui.title_text_size
    color gui.accent_color
    yalign 0.54
translate tamil style game_menu_label_text:
    font "tamil.ttf"
    size 36

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -180


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

           # label ""
            text _("[config.name!t] Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

           # text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")
            text _("Game by {a=http://me-patra.tumblr.com/}Brianna Lei{/a}\n\nMade with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n")

            text _("\n\nMusic:")
            text _("Thought Projection, Holding Your Breath, and Thoughts of You by {a=http://ketsamusic.com/}Ketsa{/a}\nare licensed under CC BY-NC-ND 4.0\n")
            text _("Romaras, Blooming, and Side by Side by Miltata are licensed\nunder CC BY-NC 3.0")
            text _("{a=https://miltata.bandcamp.com/}This artist has songs available for purchase! Please support him here!{/a}\n")
            text _("{a=http://freemusicarchive.org/music/Bloodgod/Catharsis/}Valar Morghulis{/a}  by {b}Bloodgod{/b} is licensed under\nCC BY-NC-ND 4.0\n")
            text _("{a=http://www.hurtrecord.com/bgm/24/the-flame-of-love.html}Flame of Love{/a} by {b}YOSHI{/b} is licensed under CC\n")
            text _("Overflowing by {b}Tatsuya Kato{/b}\n")
            text _("My Heart Will Go On - Recorder By Candlelight by {b}Matt Mulholland{/b}")
            text _("{a=https://mattmulholland.bandcamp.com/album/matt-mulholland-sings-covers}This song is available for purchase! Please support the artist!{/a}\n")

            text _("Title song: Miyauchi Yuri/110515 (miltata remix) by {b}Miltata{/b}")
            text _("Credits song: Calling Project 2 by {b}{a=http://que-music.net/}.que{/a}{/b}\n")


            text _("\n\nSound:")
            text _("{a=https://github.com/NormalVR/CutieKeys}Cutie Keys{/a}")
            text _("{a=http://freesound.org/people/LittleRobotSoundFactory/packs/16881/}Electric Sound Effects Library{/a} by LittleRobotSoundFactory is licensed\nunder CC BY 3.0")
            text _("{a=http://freesound.org/people/CGEffex/sounds/92634/}Clipping with Scissors{/a} by CGEffex is licensed\nunder CC BY 3.0")
            text _("{a=http://freesound.org/people/Peacewaves/sounds/317334/}Metal Locker{/a} by Peacewaves is licensed under CC BY 3.0")

            text _("\n\nAdditional scripting help:")
            text _("{a=https://twitter.com/ArazatiTea}Arazati{/a}")

            text _("\n\ntamil locilization by:")
            text _("YOUR NAME")
            #Insert soemthing like this to link to a page: {a=YOURLINK}{font=tamil.ttf}CLICKABLE_TEXT{/font}{/a}



## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


translate tamil style about_text: #about page text
    font "tamil.ttf"
    size 20

style hyperlink_text: #hyperlinks in about page
    size 32
    color "#fff"
translate tamil style hyperlink_text:
    size 20

## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load Game"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.




            grid 2 2:
                style_prefix "slot"

                xalign 0.2
                yalign 0.18

                spacing gui.slot_spacing

                for i in range(2 * 2):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("%B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                           style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 0.97

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:

    xpadding 50
    ypadding 3

style page_label_text: #save/load page's large "Page 1" title on the right side
    font "YunusH.ttf"
    size gui.title_text_size
    color gui.selected_color
    text_align 0.5
    ypos -40
    layout "subtitle"
   # hover_color gui.hover_color
translate tamil style page_label_text:
    font "tamil.ttf"
    size 38

style page_button:
    properties gui.button_properties("page_button")
    activate_sound "sound/pageTurn.ogg"
style page_button_text:
    properties gui.button_text_properties("page_button")
    selected_color gui.accent_color
    color "#c1adff"
    hover_color "#ffcef2"

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text: #size of save file descriptions on the save/load page
    properties gui.button_text_properties("slot_button")
    font "YunusH.ttf"
    ypos 24
    size 28
translate tamil style slot_button_text:
    font "tamil.ttf"
    size 20


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    if renpy.mobile:
        $ cols = 2
    else:
        $ cols = 4

    use game_menu(_("Settings"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")


                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")


                vbox:
                    style_prefix "check"
                    label _("Screen Motion")
                    textbutton _("Background Pan") action ToggleField(persistent, "bgPan")
                    textbutton _("Screenshake") action ToggleField(persistent, "screenshake")

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)
            hbox:
                box_wrap True

                vbox:
                    style_prefix "slider"
                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

                    label _("Text Speed")
                    hbox:
                        bar value Preference("text speed")


                vbox:
                    style_prefix "radio"
                    xsize 400

                    label _("Language")
                    textbutton _("English") action Language(None)
                    textbutton _("{font=tamil.ttf}{size=30}tamil{/size}{/font}") action Language("tamil")







style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text: #size of Settings menu submenu text (like Volume)
    yalign 1.0
    font "YunusH.ttf"
    color gui.selected_color
    bold False
    size 45
translate tamil style pref_label_text:
    font "tamil.ttf"
    size 28


style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing


style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 300

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 400


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport")):

        style_prefix "history"

        for h in _history_list:

            window:
                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                text h.what

        if not _history_list:
            label _("The dialogue history is empty.")


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height
    bottom_padding 8

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width


style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign
    color gui.selected_color
    font "myriad.OTF"
    size 24
    bold True

translate tamil style history_name_text:
    font "tamil.ttf"
    size 18


style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    color "fff"
    layout ("subtitle" if gui.history_text_xalign else "tex")
    font "myriad.OTF"
    size 24
   # outlines [ (1, "#00000080", 1, 1) ]
translate tamil style history_text:
    font "tamil.ttf"
    size 18

style history_label:
    xfill True
    bottom_padding 100

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

 #   hbox:
  #      label "H"
  #      text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## http://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5


            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Skipping. To stop skipping, press the CTRL key on your keyboard!")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text message

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")
    font "myriad.OTF"

translate tamil style notify_text:
    font "tamil.ttf"

## NVL screen ##################################################################
##
### This screen is used for NVL-mode dialogue and menus.
###
#### http://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

        frame:
            xpos 0 ypos 0
            background "gui/nvl.png"
            has side "c":
                area (300, 0, 820, 680)
                viewport id "vp":

                    draggable True
                    yadjustment ui.adjustment (value=99999, range=99999)   # err... works, but...

                    vbox:
                        style "nvl_vbox"
                        spacing 7 #controls spacing between each entry
                        # Display dialogue.
                        for who, what, who_id, what_id, window_id in dialogue:
                            if who==diyaChatName or who=="DIYACHATNAME-i18n":
                                window:
                                    id window_id
                                    has hbox:
                                        spacing 0
                                    add "images/chat_diya.png"

                                    if who is not None:
                                        text who id who_id xpos 20 ypos 5
                            elif who==akarshaChatName or who==akarshaChatName2 or who==akarshaChatName3 or who=="YAOISEME-i18n" or who=="NOELLEFUCKER69-i18n" or who=="ALBRETEINSTONG-i18n":

                                window:
                                    id window_id
                                    has hbox:
                                        spacing 0
                                    add "images/chat_akarsha.png"
                                    if who is not None:
                                        text who id who_id xpos 20 ypos 5

                            elif who==noelleChatName or who=="NOELLECHATNAME-i18n":
                                window:
                                    id window_id
                                    has hbox:

                                        #this is the space between the name and dialogue
                                        spacing 0
                                    add "images/chat_noelle.png" #at avatar
                                    if who is not None:

                                        text who id who_id xpos 20 ypos 5
                            elif who==minChatName or who=="MINCHATNAME-i18n":
                                window:
                                    id window_id
                                    has hbox:

                                        #this is the space between the name and dialogue
                                        spacing 0
                                    add "images/chat_min.png" #at avatar
                                    if who is not None:

                                        text who id who_id xpos 20 ypos 5
                            elif who==chryssaChatName or who=="CHRYSSACHATNAME-i18n":
                                window:
                                    id window_id
                                    has hbox:

                                        #this is the space between the name and dialogue
                                        spacing 0
                                    add "images/chat_chryssa.png" #at avatar
                                    if who is not None:

                                        text who id who_id xpos 20 ypos 5
                            elif who==lizChatName or who=="LIZCHATNAME-i18n":
                                window:
                                    id window_id
                                    has hbox:

                                        #this is the space between the name and dialogue
                                        spacing 0
                                    add "images/chat_liz.png" #at avatar
                                    if who is not None:

                                        text who id who_id xpos 20 ypos 5
                            elif who==graceChatName or who=="GRACECHATNAME-i18n":
                                window:
                                    id window_id
                                    has hbox:

                                        #this is the space between the name and dialogue
                                        spacing 0
                                    add "images/chat_grace.png" #at avatar
                                    if who is not None:

                                        text who id who_id xpos 20 ypos 5

                            elif who==sumiChatName or who=="SUMICHATNAME-i18n":
                                window:
                                    id window_id
                                    has hbox:

                                        #this is the space between the name and dialogue
                                        spacing 0
                                    add "images/chat_sumi.png" #at avatar
                                    if who is not None:

                                        text who id who_id xpos 20 ypos 5

                            if who=="":
                                window:
                                    id window_id

                                    top_padding 0
                                    left_padding 15
                                    bottom_padding 50

                                    background None
                                    has vbox:

                                        spacing 0
                                    text what id what_id

                            else:
                                window:

                                    id window_id
                                    top_padding 15
                                    left_padding 15
                                   # right_margin 160
                                    right_padding 15
                                    bottom_padding 15
                                    ypos -55
                                    left_margin 130
                                    background Frame("gui/frameNvl.png", 30, 30)
                                    has vbox:

                                        #this is the space between the name and dialogue
                                        spacing 0
                                    text what id what_id
                        if items:
                            if not textChoice:
                                vbox:
                                    id "menu"

                                    for caption, action, chosen in items:

                                        if action:


                                            button:

                                                style "nvl_menu_choice_button"
                                                action action
                                                text caption style "nvl_menu_choice"


                                        else:

                                            text caption style "nvl_dialogue"


        if items:
                     if textChoice:
                        window:

                            id window_id
                            xpos 435 ypos 636
                            top_padding 15
                            left_padding 15
                            right_padding 15
                            bottom_padding 15
                            background Frame("gui/frameNvlChoice.png", 30, 30)
                            has vbox:
                                        id "menu"

                                        for caption, action, chosen in items:

                                            if action:

                                                button:
                                                    style "nvl_menu_choice_button"
                                                    at nvlChoiceFade

                                                    action action

                                                    text caption style "nvl_menu_choice"


                                            else:

                                                text caption style "nvl_dialogue"
        if not items:
            button: # the button should be AFTER the frame containing the viewport but on the same level
                        hover_sound None
                        activate_sound None
                       # background None # if you comment out this line you'll see the button and the area it takes up

                        xsize 1368 # slightly smaller than the viewport area to make sure you don't click it by accident when fiddling with the scrollbar
                        ysize 768
                        ypos 0
                        action Return()

        use quick_menu3


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = 25

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
translate tamil style nvl_label:
    font "tamil.ttf"

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_menu_choice_button:
    left_margin 0
    xfill False
    hover_background None
    font "myriad.OTF"
    hover_sound "sound/menuClick.ogg"
translate tamil style nvl_menu_choice_button:
    font "tamil.ttf"

style nvl_menu_choice:
    underline False
    color "#fff"
    size 24
    hover_color "#2B1C63"
    font "myriad.OTF"
   # hover_sound "sound/peep.ogg
translate tamil style nvl_menu_choice:
    font "tamil.ttf"

################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 450

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    hbox:
        style_prefix "quick"

        xalign 0.5
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 340

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 400

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 600

    ######################################
## ■██▓▒░ WHITE SCREEN BEFORE START ░▒▓████████████████████████████████████■
## This is where it goes when you click Start in the main menu.

screen whiteScreen:
    modal True
    add "white"

    timer 0.1 action Stop(channel='music', fadeout=2.2)
    timer 3.0 action Start()
   # timer 3.0 action Jump("start2")

## ■██▓▒░ CUSTOM SOUND CHANNEL ░▒▓██████████████████████████■
# This is the block where we declare the individual sound channels. This enables us to play several sound FX's without overlapping
init python:
    renpy.music.register_channel("ctc", "sfx", False)
    renpy.music.register_channel("test_one",  "sfx", False)
    renpy.music.register_channel("test_two", "sfx", False)
    renpy.music.register_channel("test_three", "sfx", False)
    renpy.music.register_channel("test_four","sfx", False)
    renpy.music.register_channel("test_five", "sfx", False)
    renpy.music.register_channel("test_six",  "sfx", False)
    renpy.music.register_channel("sound2",  "sfx", False)

## ■██▓▒░ TOOLTIP ░▒▓███████████████████████████████████████■
screen gui_tooltip:
    add "gui/tooltipLine.png" at alpha_SPEED2
    text tt style "tooltip" at alpha_SPEED
  #  text tt style "chTitle" size 40 text_align 0.5 color "#ffff" at alpha_SPEED

screen qte_tooltip:
 #   add my_picture xpos tt_xpos ypos tt_ypos
    text tt font "YunusH.ttf" size 60 text_align 0.7 color "#fff"  at alpha_SPEEDQTE
