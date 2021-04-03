# The script of the game goes in this file.
init -2:
    $renpy.not_infinite_loop(3)

    define slideright = CropMove(0.6, "slideright")
    define slideleft = CropMove(0.6, "slideleft")
    define clockWipe = ImageDissolve("circlewipe.png", 1.2, ramplen=8, reverse=False, alpha=True, time_warp=None)
    define irisOut = ImageDissolve("iris.png", 0.5, 2)
    define irisIn = ImageDissolve("iris.png", 0.5, 2, reverse=True)
    define iOut = ImageDissolve("iris.png", 0.35, 2)
    define iIn = ImageDissolve("iris.png", 0.35, 2, reverse=True)
#    define circleInOut= MultipleTransition(False, circirisout, "#000", circirisin, True)
    define eyeOpen = ImageDissolve("eyeopen.png", 1.0, 40)
    define eyeClose = ImageDissolve("eyeopen.png", 1.0, 40, reverse=True)
    define dissolve1 = Dissolve(0.2, alpha=False, time_warp=None)
    define dissolve2 = Dissolve(1.5, alpha=False, time_warp=None)
    define dissolveTop = ComposeTransition(dissolve, before=easeoutbottom, after=easeintop)
    define pause1 = Pause(0.3, hard=True)

    define pix1 = ImageDissolve("wipes/pix1.jpg", 0.8, 8)
    define pix2 = ImageDissolve("wipes/pix2.jpg", 0.8, 8)
    define pix3 = ImageDissolve("wipes/pix3.jpg", 0.8, 8)
    define bites = ImageDissolve("wipes/bites.jpg", 1.0, 8)
    define bowtie = ImageDissolve("wipes/bowtie.png", 1.0, 8)
    define dots = ImageDissolve("wipes/dots2.png", 0.8, 8)
    define edges = ImageDissolve("wipes/edges.png", 1.0, 8)
    define letter = ImageDissolve("wipes/letter.png", 1.0, 8)
    define radio = ImageDissolve("wipes/radio.jpg", 1.0, 8)
    define wet = ImageDissolve("wipes/wet.jpg", 1.0, 8)

    define curtains = ImageDissolve("wipes/curtains.png", 0.6, 8)

    define rain2 = ImageDissolve("wipes/rain2.jpg", 1.0, 8)

    define diamond = ImageDissolve("wipes/2.png", 0.8, 8)
    define hearts = ImageDissolve("wipes/11.jpg", 1.0, 8)
    define w20 = ImageDissolve("wipes/20.jpg", 1.0, 8)
    define w28 = ImageDissolve("wipes/28.png", 1.0, 8)
    define w34 = ImageDissolve("wipes/34.png", 1.0, 8)





init -1 python:
    sideImageWidth=580 #this is the width of side images
    sideImageHeight=205 #this is the height of side images
    sideImageHeight2=305

    farthestBackValue=-20
    farBackValue=-50
    backValue=-80
#########TOOLTIP POSITION##########
    tt_xpos=0.5
  #  tt_ypos=0.8
    cur_new = "default"

###########CUSTOM TAGS###############
    def incoherent_tag(tag, argument, contents):
        redColor = "#ff0000"
        return [
                (renpy.TEXT_TAG, u"color={}".format(redColor)),
            ] + [(renpy.TEXT_TAG, u"font=YunusH.ttf"),
            ]+ [(renpy.TEXT_TAG, u"b"),
            ] + contents + [
                (renpy.TEXT_TAG, u"/b"),
            ] +[
                (renpy.TEXT_TAG, u"/font"),
            ] + [
                (renpy.TEXT_TAG, u"/color"),
            ]
    config.custom_text_tags["incoherent"] = incoherent_tag


    def white_tag(tag, argument, contents):
        whiteColor = "#fff"
        #whiteColor = "#0099ff"
        return [
                (renpy.TEXT_TAG, u"color={}".format(whiteColor)),
            ] + contents + [
                (renpy.TEXT_TAG, u"/color"),
            ]
    config.custom_text_tags["white"] = white_tag

    def yellow_tag(tag, argument, contents):

        yellowColor = "#ffff00"
        return [
                (renpy.TEXT_TAG, u"color={}".format(yellowColor)),
            ] + contents + [
                (renpy.TEXT_TAG, u"/color"),
            ]

    config.custom_text_tags["yellow"] = yellow_tag

    def blue_tag(tag, argument, contents):
        blueColor = "#949EF5"
        #blueColor = "#0099ff"
        return [
                (renpy.TEXT_TAG, u"color={}".format(blueColor)),
            ] + contents + [
                (renpy.TEXT_TAG, u"/color"),
            ]
    config.custom_text_tags["blue"] = blue_tag


    def pink_tag(tag, argument, contents):
        pinkColor = "#f89fe2"
        #pinkColor = "#0099ff"
        return [
                (renpy.TEXT_TAG, u"color={}".format(pinkColor)),
            ] + contents + [
                (renpy.TEXT_TAG, u"/color"),
            ]
    config.custom_text_tags["pink"] = pink_tag



    def red_tag(tag, argument, contents):
        redColor = "#ff0000"
        return [
                (renpy.TEXT_TAG, u"color={}".format(redColor)),
            ] + contents + [
                (renpy.TEXT_TAG, u"/color"),
            ]
    config.custom_text_tags["red"] = red_tag

    def slow_tag(tag, argument, contents):
        slowSpeed = 20
        return [
                (renpy.TEXT_TAG, u"cps={}".format(slowSpeed)),
            ] + contents + [
                (renpy.TEXT_TAG, u"/cps"),
            ]
    config.custom_text_tags["slow"] = slow_tag

    def slower_tag(tag, argument, contents):
        slowerSpeed = 15
        return [
                (renpy.TEXT_TAG, u"cps={}".format(slowerSpeed)),
            ] + contents + [
                (renpy.TEXT_TAG, u"/cps"),
            ]
    config.custom_text_tags["slower"] = slower_tag

    def big_tag(tag, argument, contents):
        bigSize = int(argument) + 32

        return [
                (renpy.TEXT_TAG, u"size={}".format(bigSize))
            ]+ contents + [(renpy.TEXT_TAG, u"/size"),]

    config.custom_text_tags["big"] = big_tag

###########FILE NAME CLEANUP###########
    for file in renpy.list_files():
        if file.startswith('images/'):
            if file.endswith('.png'):
                name = file.replace('images/','').replace('/', ' ').replace('.png','')
                renpy.image(name, Image(file))
                continue
            elif file.endswith('.jpg'):
                name = file.replace('images/','').replace('/', ' ').replace('.jpg','')
                renpy.image(name, Image(file))
                continue
            continue

#############CALLBACK###################
    def bgm_play (on=False):
        if on:
            renpy.music.play(channel="music", fadeout=0.1)
        else:
            renpy.music.stop(channel="music", fadeout=0.1)

     #   Talk sounds
    def clack_play(on=False, char=1):
        if on:
            if char==0:
                renpy.music.play("sound/typewriter.wav", channel="ctc", loop="True")
            elif char==1:
                renpy.music.play("sound/talk1.ogg", channel="ctc",loop="True")
            elif char==2:
                renpy.music.play("sound/talk2.wav", channel="ctc", loop="True")
            elif char==3:
                renpy.music.play("sound/talk3.ogg", channel="ctc", loop="True")
            elif char==4:
                renpy.music.play("sound/talk4.ogg", channel="ctc", loop="True")
            elif char==5:
                renpy.music.play("sound/talk5.wav", channel="ctc", loop="True")
            elif char==6:
                renpy.music.play("sound/talkJaehee.ogg", channel="ctc", loop="True")
            elif char==7:
                renpy.music.play("sound/talk3.wav", channel="ctc", loop="True")
        else:
            renpy.music.stop(channel="ctc", fadeout=0.1)
    #Callback
    def clicks(event, char=1,**kwargs):
        if event == "show" or event == "begin":
            clack_play(True, char)
        if event == "slow_done" or event == "end":
            clack_play(False, char)
#        Below was the Ghost Trick click-to-continue sound, which I'm no longer using
#        if event == "end":
#            renpy.music.play("sound/click.wav",channel="ctc")
    def gChat(event, **kwargs):
        if event == "begin":
            renpy.music.play("sound/peep.ogg",channel="ctc")
            #renpy.show("gChatBlink")

init -1 python hide:
    config.empty_window = nvl_show_core #still useless

    ## Used when showing NVL-mode text directly after ADV-mode text.
    config.adv_nvl_transition = Dissolve(0.4)

    ## Used when showing ADV-mode text directly after NVL-mode text.
    config.nvl_adv_transition = Dissolve(0.4)

init 1 python:
    config.keymap['hide_windows'].remove('mouseup_2')
    config.keymap['hide_windows'].remove('h')

    def nvlHide():
        nvl_hide(config.nvl_adv_transition)
        #Hide(nvl, transition=Dissolve(3)) #Dissolve(3))
        renpy.pause(0.1)
        return

    def nvlShow():
        renpy.pause(0.1)
        nvl_show(config.adv_nvl_transition)
        #Show(nvl, transition=downLong) #Dissolve(3))
        return

################Parallax###############
init 800 python:
    class MouseParallax(renpy.Displayable):
        def __init__(self,layer_info):
            super(renpy.Displayable,self).__init__()
            self.xoffset,self.yoffset=0.0,0.0

            self.sort_layer=sorted(layer_info,reverse=True)
            cflayer=[]
            masteryet=False
            for m,n in self.sort_layer:
                if(not masteryet)and(m<0):
                    cflayer.append("master")
                    masteryet=True
                cflayer.append(n)
            if not masteryet:
                cflayer.append("master")
            cflayer.extend(["transient","screens","overlay"])
            config.layers=cflayer
            config.overlay_functions.append(self.overlay)
            return
        def render(self,width,height,st,at):
            return renpy.Render(width,height)
        def parallax(self,m):
            func = renpy.curry(trans)(disp=self, m=m)
            return Transform(function=func)
        def overlay(self):
            ui.add(self)
            for m,n in self.sort_layer:
                renpy.layer_at_list([self.parallax(m)],n)
            return
        def event(self,ev,x,y,st):
            import pygame
            if ev.type==pygame.MOUSEMOTION:
                self.xoffset,self.yoffset=((float)(x)/(config.screen_width))-0.5,((float)(y)/(config.screen_height))-0.5
            return
    #MouseParallax([(-20,"farthestBack"),(-50,"farBack"),(-80,"back"),(-30,"front"),(50,"inyourface")])

    MouseParallax([(farthestBackValue,"farthestBack"),(farBackValue,"farBack"),(backValue,"back"),(-30,"front"),(50,"inyourface")])

    def trans(d, st, at, disp=None, m=None):
        d.xoffset, d.yoffset = int(round(m*disp.xoffset)), int(round(m*disp.yoffset))
        if persistent.bgPan is False:
            d.xoffset, d.yoffset=0,0
        return 0

#############SPECIAL TEXT STYLES###############
style chTitle is text:
    font "YunusH.ttf"
    size 130
translate traditional_chinese style chTitle:
    font "traditional_chinese.ttf"
    size 90
translate brazilian_portuguese style chTitle:
    font "myriad.OTF"
    size 80
translate czech style chTitle:
    font "myriad.OTF"
    size 80
translate japanese style chTitle:
    font "japanese.ttc"
    size 80
translate korean style chTitle:
    font "Binggrae.otf"
    size 80
translate polish style chTitle:
    font "myriad.OTF"
    size 80
translate farsi style chTitle:
    font "times.ttf"
    size 80


style tooltip is text:
    font "YunusH.ttf"
    size 40
    text_align 0.5
    yalign -0.2
    color "#ffff"
translate traditional_chinese style tooltip:
    font "traditional_chinese.ttf"
    yalign 0.0
translate brazilian_portuguese style tooltip:
    font "myriad.OTF"
    yalign -0.1
translate czech style tooltip:
    font "myriad.OTF"
    yalign -0.1
translate japanese style tooltip:
    font "japanese.ttc"
    yalign 0.0
translate korean style tooltip:
    font "Binggrae.otf"
    yalign 0.1
translate polish style tooltip:
    font "myriad.OTF"
    yalign -0.1
translate farsi style tooltip:
    font "times.ttf"
    yalign 0.0

style creditSmall is text:
    font "YunusH.ttf"
    size 50
translate traditional_chinese style creditSmall:
    font "traditional_chinese.ttf"
    size 40
translate brazilian_portuguese style creditSmall:
    font "myriad.OTF"
    size 40
translate czech style creditSmall:
    font "myriad.OTF"
    size 40
translate japanese style creditSmall:
    font "japanese.ttc"
    size 40
translate korean style creditSmall:
    font "Binggrae.otf"
    size 30
translate polish style creditSmall:
    font "myriad.OTF"
    size 40
translate farsi style creditSmall:
    font "times.ttf"
    size 40

style subtitle is text:
    font "myriad.OTF"
translate traditional_chinese style subtitle:
    font "traditional_chinese.ttf"
translate brazilian_portuguese style subtitle:
    font "myriad.OTF"
translate czech style subtitle:
    font "myriad.OTF"
translate japanese style subtitle:
    font "japanese.ttc"
translate korean style subtitle:
    font "Binggrae.otf"
translate polish style subtitle:
    font "myriad.OTF"
translate farsi style subtitle:
    font "times.ttf"

style gChatGrey is text:
   # color "#8080DD"
    color "#2B1C63"
 #   size 45
    size 24
    font "myriad.OTF"
translate traditional_chinese style gChatGrey:
    font "traditional_chinese.ttf"
translate japanese style gChatGrey:
    font "japanese.ttc"
translate korean style gChatGrey:
    font "Binggrae.otf"
translate farsi style gChatGrey:
    font "times.ttf"

style firstLine is text:
    color "#8D8D8D"
    size 10
  #  font "arial.ttf"
style gChatHeader is text:
    color "#ffffff"
    font "YunusH.ttf"

  #  font "MoonFlowerBold.ttf"
    size 34
    #bold True
    text_align 0.0
translate traditional_chinese style gChatHeader:
    font "traditional_chinese.ttf"

style gChatBlack is text:
    color "#000"
    font "myriad.OTF"
  #  size 45
    size 24
translate traditional_chinese style gChatBlack:
    font "traditional_chinese.ttf"
translate japanese style gChatBlack:
    font "japanese.ttc"
translate korean style gChatBlack:
    font "Binggrae.otf"
translate farsi style gChatBlack:
    font "times.ttf"

style gChatName is text:
    font "myriad.OTF"
    size 24
    bold True
    color "#2B1C63"
    ypos 0
translate traditional_chinese style gChatName:
    font "traditional_chinese.ttf"
translate japanese style gChatName:
    font "japanese.ttc"
translate korean style gChatName:
    font "Binggrae.otf"
translate farsi style gChatName:
    font "times.ttf"

image gChatBlink:
    "gui/nvl2.png"
    0.2
    "gui/nvl1.png"

style centeredText is text:
    xpos 0.5
    ypos 0.5
    size 80
    color "ffffff"
#############TRANSFORMS#################
transform winFade:
    on show:
        xanchor 0.5 xalign .5 ypos 860
        alpha 0.0
        easein 0.4 alpha 1.0 ypos 753

#    on replace:
#        xalign .5 ypos 860
#        alpha 0.0
#        easein 0.3 alpha 1.0 ypos 768
    on hide:
        xanchor 0.5 xalign .5 ypos 753
        easein 0.4 alpha 0.0 ypos 860

transform spriteTransform:
    yalign 1.0 xpos 0.5 xalign 0.5 ypos 808
transform bgTransform:
    xanchor 0.5 yanchor 0.5 xalign 0.5 yalign 0.5

    #############TOOLTIP TRANSFORM##############
transform alpha_SPEED: #this is for the text inside the tooltip
#    zoom 1.4
    xalign 0.5
    ypos 1.0
    alpha 0.0
    easein 0.2 alpha 1.0 ypos 0.895
    on hide:
        easein 0.2 alpha 0

transform alpha_SPEED2:
#    zoom 1.4
    xalign 0.5
    ypos 1.0
    alpha 0.0
    easein 0.2 alpha 1.0 ypos 0.88
    on hide:
        easein 0.2 alpha 0

transform alpha_SPEEDQTE:
#    zoom 1.4
    xalign 0.5
    ypos 0.84
    alpha 0.0
    easein 0.2 alpha 1.0
    on hide:
        easein 0.2 alpha 0

transform sideSprite1:
    yanchor 0.5 ypos 270
    on show:
        xpos -20 alpha 0.0
        easein 0.2 xpos 40 alpha 1.0
    on hide:
        xpos 40 alpha 1.0
        easein 0.2 xpos -20 alpha 0.0
transform sideSprite2:
    yanchor 0.5 ypos 270
    on show:
        xpos 920 alpha 0.0
        easein 0.2 xpos 860 alpha 1.0
    on hide:
        xpos 860 alpha 1.0
        easein 0.2 xpos 920 alpha 0.0

image ctc_fixed:
        xanchor 0.5 yanchor 0.5 xalign 0.5 ypos 729 xpos 0.885
        "ctc.png"
        easein 0.5 ypos 715 rotate 120
        easein 0.5 ypos 729
        repeat

transform qte_move:
    xanchor 0.5 yanchor 0.5
    xalign 0.5 yalign 0.5
    alpha 0.8  zoom 0.9
    on hide:
        linear 1.5 alpha 0
    on idle:
        easein 0.1 zoom 0.9 alpha 0.8
    on hover:
        easein 0.2 zoom 1.0 alpha 1.0

transform titleFade:
    alpha 0.0
    easein 2.0 alpha 1.0


transform titleFade2:
    xanchor 0.5 yanchor 0.5 xalign 0.49 yalign 0.7
    alpha 0.0
    easein 1.5 alpha 1.0

transform titleFade3:
    xanchor 0.5 yanchor 0.5 xalign 0.5 yalign 0.24
    alpha 0.0
    easein 1.8 alpha 1.0

transform titleFade4:
    xanchor 0.5 yanchor 0.0 xalign 0.5 yalign 0.83
    alpha 0.0
    easein 2.5 alpha 1.0

transform centered3D:
    xanchor 0.5 yanchor 0.5 xalign 0.5 yalign 0.5

transform nvlChoiceFade:
    alpha 0.0
    easein 0.5 alpha 1.0

image titleScantron1 = im.Composite(
        (1366, 6834),
        (0, 0), "gui/titleScreen.png",
        (0, 3417), "gui/titleScreen.png")


image titleScantron2 = im.Composite(
        (1366, 6834),
        (0, 0), "gui/titleScreen2.png",
        (0, 3417), "gui/titleScreen2.png")
image bg main_menu:
    "gui/main_menu.png"

image film strip1 = im.Composite(
        (1366, 1302),
        (0, 0), "card/film.png",
        (0, 434), "card/film.png",
        (0, 868), "card/film.png")


image film2 strip = im.Composite(
        (169, 1796),
        (500, 0), "card/film.png",
        (500, 898), "card/film.png")
image film2 strip1:
    "film2 strip"
    xanchor 1.0 xalign 1.0

image special camera:
    "camera1"
    1.0
    "camera2"
    1.0
    repeat

image bg main_menu:
    "gui/main_menu.png"

image bg logo:
    "gui/logo.png"

image card roll:
    "card cardDiya"
#    choice:
#        4.0
#        "sprite akarshaBigSmile2"
#        0.08
#        "sprite akarshaBigSmile1"
#        0.15
#    choice:
#        3.0
#    choice:
#        1.5
#    # This randomizes the time between blinking.
#    "sprite akarshaBigSmile2"
    0.1
    choice:
        "card cardNoelle"
        0.1
        "card cardAkarsha"
        0.1
        "card cardMin"
    choice:
        "card cardNoelle"
        0.1
        "card cardMin"
        0.1
        "card cardAkarsha"

    0.1
    repeat

image circle circle1:
    "card circle1"
image circle circleFlash:
   # "card circle1"
   # 0.2
    "card circle2"
    0.2
    "card circle1"
    0.2
    "card circle2"
    0.2
    "card circle1"
    0.2
    "card circle2"
    0.2
    "card circle1"
    0.2
    "card circle2"
    0.2
    "card circle1"
    0.2

image prop peopleBlocking:
    "bg/peopleBlocking.png"
image prop actionLines:
    "bg/action lines1.png"
    0.1
    "bg/action lines2.png"
    0.1
    repeat

image bg cabinet:
    "bg/cabinet1.png"
    0.1
    "bg/cabinet2.png"
    0.1
    repeat
image bg basket:
    "bg/laundry basket1.png"
    0.1
    "bg/laundry basket2.png"
    0.1
    repeat
image bg AMfight3:
    "bg/AM fight31.png"
    0.1
    "bg/AM fight32.png"
    0.1
    repeat
#################SPRITES START HERE############
image sprite diyaNeutral:
    LiveComposite((883, 818),(0,0), "sprite diyaDefault",(0,0), "sprite diyaNeutral1", (0,0), "sprite diyaHat")
image sideSprite1 diyaNeutral:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((200, 0, sideImageWidth, sideImageHeight2), "sprite diyaNeutral"))
image sideSprite2 diyaNeutral:
    "sideSprite1 diyaNeutral"

image sprite diyaBlush:
    LiveComposite((883, 818),(0,0), "sprite diyaDefault",(0,0), "sprite diyaBlush1", (0,0), "sprite diyaHat")
image sideSprite1 diyaBlush:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((200, 0, sideImageWidth, sideImageHeight2), "sprite diyaBlush"))
image sideSprite2 diyaBlush:
    "sideSprite1 diyaBlush"

image sprite diyaHappy:
    LiveComposite((883, 818),(0,0), "sprite diyaDefault",(0,0), "sprite diyaHappy1", (0,0), "sprite diyaHat")
image sideSprite1 diyaHappy:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((200, 0, sideImageWidth, sideImageHeight2), "sprite diyaHappy"))
image sideSprite2 diyaHappy:
    "sideSprite1 diyaHappy"


image sprite diyaDelighted:
    LiveComposite((883, 818),(0,0), "sprite diyaDefault",(0,0), "sprite diyaDelighted1", (0,0), "sprite diyaHat")
image sideSprite1 diyaDelighted:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((200, 0, sideImageWidth, sideImageHeight2), "sprite diyaDelighted"))
image sideSprite2 diyaDelighted:
    "sideSprite1 diyaDelighted"

image sprite diyaAnnoyed:
    LiveComposite((883, 818),(0,0), "sprite diyaDefault",(0,0), "sprite diyaAnnoyed1", (0,0), "sprite diyaHat")
image sideSprite1 diyaAnnoyed:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((200, 0, sideImageWidth, sideImageHeight2), "sprite diyaAnnoyed"))
image sideSprite2 diyaAnnoyed:
    "sideSprite1 diyaAnnoyed"


image sprite diyaSurprised:
    LiveComposite((883, 818),(0,0), "sprite diyaDefault",(0,0), "sprite diyaSurprised1", (0,0), "sprite diyaHat")
image sideSprite1 diyaSurprised:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((200, 0, sideImageWidth, sideImageHeight2), "sprite diyaSurprised"))
image sideSprite2 diyaSurprised:
    "sideSprite1 diyaSurprised"


image sprite diyaAway:
    LiveComposite((883, 818),(0,0), "sprite diyaDefault",(0,0), "sprite diyaAway1", (0,0), "sprite diyaHat")
image sideSprite1 diyaAway:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((200, 0, sideImageWidth, sideImageHeight2), "sprite diyaAway"))
image sideSprite2 diyaAway:
    "sideSprite1 diyaAway"

image sprite diyaWorried:
    LiveComposite((883, 818),(0,0), "sprite diyaDefault",(0,0), "sprite diyaWorried1", (0,0), "sprite diyaHat")
image sideSprite1 diyaWorried:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((200, 0, sideImageWidth, sideImageHeight2), "sprite diyaWorried"))
image sideSprite2 diyaWorried:
    "sideSprite1 diyaWorried"


image sprite diyaWorriedAway:
    LiveComposite((883, 818),(0,0), "sprite diyaDefault",(0,0), "sprite diyaWorriedAway1", (0,0), "sprite diyaHat")
image sideSprite1 diyaWorriedAway:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((200, 0, sideImageWidth, sideImageHeight2), "sprite diyaWorriedAway"))
image sideSprite2 diyaWorriedAway:
    "sideSprite1 diyaWorriedAway"

image sprite diyaScared:
    LiveComposite((883, 818),(0,0), "sprite diyaDefault",(0,0), "sprite diyaScared1", (0,0), "sprite diyaHat")
image sideSprite1 diyaScared:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((200, 0, sideImageWidth, sideImageHeight2), "sprite diyaScared"))
image sideSprite2 diyaScared:
    "sideSprite1 diyaScared"

image sprite diyaShocked:
    LiveComposite((883, 818),(0,0), "sprite diyaDefault",(0,0), "sprite diyaShocked1", (0,0), "sprite diyaHat")
image sideSprite1 diyaShocked:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((200, 0, sideImageWidth, sideImageHeight2), "sprite diyaShocked"))
image sideSprite2 diyaShocked:
    "sideSprite1 diyaShocked"

image sprite diyaAwayHappy:
    LiveComposite((883, 818),(0,0), "sprite diyaDefault",(0,0), "sprite diyaAwayHappy1", (0,0), "sprite diyaHat")
image sideSprite1 diyaAwayHappy:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((200, 0, sideImageWidth, sideImageHeight2), "sprite diyaAwayHappy"))
image sideSprite2 diyaAwayHappy:
    "sideSprite1 diyaAwayHappy"

image sprite diyaNeutralB:
    LiveComposite((883, 818),(0,0), "sprite diyaBaseball",(0,0), "sprite diyaNeutral1", (0,0), "sprite diyaHair")
image sideSprite1 diyaNeutralB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((200, 0, sideImageWidth, sideImageHeight2), "sprite diyaNeutralB"))
image sideSprite2 diyaNeutralB:
    "sideSprite1 diyaNeutralB"

image sprite diyaBlushB:
    LiveComposite((883, 818),(0,0), "sprite diyaBaseball",(0,0), "sprite diyaBlush1", (0,0), "sprite diyaHair")
image sideSprite1 diyaBlushB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((200, 0, sideImageWidth, sideImageHeight2), "sprite diyaBlushB"))
image sideSprite2 diyaBlushB:
    "sideSprite1 diyaBlushB"

image sprite diyaHappyB:
    LiveComposite((883, 818),(0,0), "sprite diyaBaseball",(0,0), "sprite diyaHappy1", (0,0), "sprite diyaHair")
image sideSprite1 diyaHappyB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((200, 0, sideImageWidth, sideImageHeight2), "sprite diyaHappyB"))
image sideSprite2 diyaHappyB:
    "sideSprite1 diyaHappyB"


image sprite diyaDelightedB:
    LiveComposite((883, 818),(0,0), "sprite diyaBaseball",(0,0), "sprite diyaDelighted1", (0,0), "sprite diyaHair")
image sideSprite1 diyaDelightedB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((200, 0, sideImageWidth, sideImageHeight2), "sprite diyaDelightedB"))
image sideSprite2 diyaDelightedB:
    "sideSprite1 diyaDelightedB"

image sprite diyaAnnoyedB:
    LiveComposite((883, 818),(0,0), "sprite diyaBaseball",(0,0), "sprite diyaAnnoyed1", (0,0), "sprite diyaHair")
image sideSprite1 diyaAnnoyedB:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((200, 0, sideImageWidth, sideImageHeight2), "sprite diyaAnnoyedB"))
image sideSprite2 diyaAnnoyedB:
    "sideSprite1 diyaAnnoyedB"


image sprite diyaSurprisedB:
    LiveComposite((883, 818),(0,0), "sprite diyaBaseball",(0,0), "sprite diyaSurprised1", (0,0), "sprite diyaHair")
image sideSprite1 diyaSurprisedB:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((200, 0, sideImageWidth, sideImageHeight2), "sprite diyaSurprisedB"))
image sideSprite2 diyaSurprisedB:
    "sideSprite1 diyaSurprisedB"


image sprite diyaAwayB:
    LiveComposite((883, 818),(0,0), "sprite diyaBaseball",(0,0), "sprite diyaAway1", (0,0), "sprite diyaHair")
image sideSprite1 diyaAwayB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((200, 0, sideImageWidth, sideImageHeight2), "sprite diyaAwayB"))
image sideSprite2 diyaAwayB:
    "sideSprite1 diyaAwayB"

image sprite diyaWorriedB:
    LiveComposite((883, 818),(0,0), "sprite diyaBaseball",(0,0), "sprite diyaWorried1", (0,0), "sprite diyaHair")
image sideSprite1 diyaWorriedB:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((200, 0, sideImageWidth, sideImageHeight2), "sprite diyaWorriedB"))
image sideSprite2 diyaWorriedB:
    "sideSprite1 diyaWorriedB"


image sprite diyaWorriedAwayB:
    LiveComposite((883, 818),(0,0), "sprite diyaBaseball",(0,0), "sprite diyaWorriedAway1", (0,0), "sprite diyaHair")
image sideSprite1 diyaWorriedAwayB:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((200, 0, sideImageWidth, sideImageHeight2), "sprite diyaWorriedAwayB"))
image sideSprite2 diyaWorriedAwayB:
    "sideSprite1 diyaWorriedAwayB"

image sprite diyaScaredB:
    LiveComposite((883, 818),(0,0), "sprite diyaBaseball",(0,0), "sprite diyaScared1", (0,0), "sprite diyaHair")
image sideSprite1 diyaScaredB:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((200, 0, sideImageWidth, sideImageHeight2), "sprite diyaScaredB"))
image sideSprite2 diyaScaredB:
    "sideSprite1 diyaScaredB"

image sprite diyaShockedB:
    LiveComposite((883, 818),(0,0), "sprite diyaBaseball",(0,0), "sprite diyaShocked1", (0,0), "sprite diyaHair")
image sideSprite1 diyaShockedB:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((200, 0, sideImageWidth, sideImageHeight2), "sprite diyaShockedB"))
image sideSprite2 diyaShockedB:
    "sideSprite1 diyaShockedB"

image sprite diyaAwayHappyB:
    LiveComposite((883, 818),(0,0), "sprite diyaBaseball",(0,0), "sprite diyaAwayHappy1", (0,0), "sprite diyaHair")
image sideSprite1 diyaAwayHappyB:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((200, 0, sideImageWidth, sideImageHeight2), "sprite diyaAwayHappyB"))
image sideSprite2 diyaAwayHappyB:
    "sideSprite1 diyaAwayHappyB"

image sprite yDiyaNeutral:
    LiveComposite((883, 818),(0,0), "sprite yDiyaDefault",(0,0), "sprite yDiyaNeutral1", (0,0), "sprite yDiyaHat1")
    zoom 1.05
image sideSprite1 yDiyaNeutral:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((235, 80, sideImageWidth, sideImageHeight2), "sprite yDiyaNeutral"))
image sideSprite2 yDiyaNeutral:
    "sideSprite1 yDiyaNeutral"

image sprite yDiyaBlush:
    LiveComposite((883, 818),(0,0), "sprite yDiyaDefault",(0,0), "sprite yDiyaBlush1", (0,0), "sprite yDiyaHat1")
    zoom 1.05
image sideSprite1 yDiyaBlush:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((235, 80, sideImageWidth, sideImageHeight2), "sprite yDiyaBlush"))
image sideSprite2 yDiyaBlush:
    "sideSprite1 yDiyaBlush"

image sprite yDiyaHappy:
    LiveComposite((883, 818),(0,0), "sprite yDiyaDefault",(0,0), "sprite yDiyaHappy1", (0,0), "sprite yDiyaHat1")
    zoom 1.05
image sideSprite1 yDiyaHappy:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((235, 80, sideImageWidth, sideImageHeight2), "sprite yDiyaHappy"))
image sideSprite2 yDiyaHappy:
    "sideSprite1 yDiyaHappy"


image sprite yDiyaDelighted:
    LiveComposite((883, 818),(0,0), "sprite yDiyaDefault",(0,0), "sprite yDiyaDelighted1", (0,0), "sprite yDiyaHat1")
    zoom 1.05
image sideSprite1 yDiyaDelighted:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((235, 80, sideImageWidth, sideImageHeight2), "sprite yDiyaDelighted"))
image sideSprite2 yDiyaDelighted:
    "sideSprite1 yDiyaDelighted"

image sprite yDiyaAnnoyed:
    LiveComposite((883, 818),(0,0), "sprite yDiyaDefault",(0,0), "sprite yDiyaAnnoyed1", (0,0), "sprite yDiyaHat1")
    zoom 1.05
image sideSprite1 yDiyaAnnoyed:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((235, 80, sideImageWidth, sideImageHeight2), "sprite yDiyaAnnoyed"))
image sideSprite2 yDiyaAnnoyed:
    "sideSprite1 yDiyaAnnoyed"


image sprite yDiyaSurprised:
    LiveComposite((883, 818),(0,0), "sprite yDiyaDefault",(0,0), "sprite yDiyaSurprised1", (0,0), "sprite yDiyaHat1")
    zoom 1.05
image sideSprite1 yDiyaSurprised:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((235, 80, sideImageWidth, sideImageHeight2), "sprite yDiyaSurprised"))
image sideSprite2 yDiyaSurprised:
    "sideSprite1 yDiyaSurprised"


image sprite yDiyaAway:
    LiveComposite((883, 818),(0,0), "sprite yDiyaDefault",(0,0), "sprite yDiyaAway1", (0,0), "sprite yDiyaHat1")
    zoom 1.05
image sideSprite1 yDiyaAway:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((235, 80, sideImageWidth, sideImageHeight2), "sprite yDiyaAway"))
image sideSprite2 yDiyaAway:
    "sideSprite1 yDiyaAway"

image sprite yDiyaWorried:
    LiveComposite((883, 818),(0,0), "sprite yDiyaDefault",(0,0), "sprite yDiyaWorried1", (0,0), "sprite yDiyaHat1")
    zoom 1.05
image sideSprite1 yDiyaWorried:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((235, 80, sideImageWidth, sideImageHeight2), "sprite yDiyaWorried"))
image sideSprite2 yDiyaWorried:
    "sideSprite1 yDiyaWorried"


image sprite yDiyaAwayHappy:
    LiveComposite((883, 818),(0,0), "sprite yDiyaBaseball",(0,0), "sprite yDiyaAwayHappy1", (0,0), "sprite yDiyaHat2")
    zoom 1.05
image sideSprite1 yDiyaAwayHappy:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((235, 80, sideImageWidth, sideImageHeight2), "sprite yDiyaAwayHappy"))
image sideSprite2 yDiyaAwayHappy:
    "sideSprite1 yDiyaAwayHappy"

image sprite yDiyaWorriedAway:
    LiveComposite((883, 818),(0,0), "sprite yDiyaDefault",(0,0), "sprite yDiyaWorriedAway1", (0,0), "sprite yDiyaHat1")
    zoom 1.05
image sideSprite1 yDiyaWorriedAway:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((235, 80, sideImageWidth, sideImageHeight2), "sprite yDiyaWorriedAway"))
image sideSprite2 yDiyaWorriedAway:
    "sideSprite1 yDiyaWorriedAway"

image sprite yDiyaScared:
    LiveComposite((883, 818),(0,0), "sprite yDiyaDefault",(0,0), "sprite yDiyaScared1", (0,0), "sprite yDiyaHat1")
    zoom 1.05
image sideSprite1 yDiyaScared:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((235, 80, sideImageWidth, sideImageHeight2), "sprite yDiyaScared"))
image sideSprite2 yDiyaScared:
    "sideSprite1 yDiyaScared"

image sprite yDiyaShocked:
    LiveComposite((883, 818),(0,0), "sprite yDiyaDefault",(0,0), "sprite yDiyaShocked1", (0,0), "sprite yDiyaHat1")
    zoom 1.05
image sideSprite1 yDiyaShocked:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((235, 80, sideImageWidth, sideImageHeight2), "sprite yDiyaShocked"))
image sideSprite2 yDiyaShocked:
    "sideSprite1 yDiyaShocked"

image sprite yDiyaAwayHappy:
    LiveComposite((883, 818),(0,0), "sprite yDiyaDefault",(0,0), "sprite yDiyaAwayHappy1", (0,0), "sprite yDiyaHat1")
    zoom 1.05
image sideSprite1 yDiyaAwayHappy:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((235, 80, sideImageWidth, sideImageHeight2), "sprite yDiyaAwayHappy"))
image sideSprite2 yDiyaAwayHappy:
    "sideSprite1 yDiyaAwayHappy"

image sprite yDiyaNeutralB:
    LiveComposite((883, 818),(0,0), "sprite yDiyaBaseball",(0,0), "sprite yDiyaNeutral1", (0,0), "sprite yDiyaHat2")
    zoom 1.05
image sideSprite1 yDiyaNeutralB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((235, 80, sideImageWidth, sideImageHeight2), "sprite yDiyaNeutralB"))
image sideSprite2 yDiyaNeutralB:
    "sideSprite1 yDiyaNeutralB"

image sprite yDiyaBlushB:
    LiveComposite((883, 818),(0,0), "sprite yDiyaBaseball",(0,0), "sprite yDiyaBlush1", (0,0), "sprite yDiyaHat2")
    zoom 1.05
image sideSprite1 yDiyaBlushB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((235, 80, sideImageWidth, sideImageHeight2), "sprite yDiyaBlushB"))
image sideSprite2 yDiyaBlushB:
    "sideSprite1 yDiyaBlushB"

image sprite yDiyaHappyB:
    LiveComposite((883, 818),(0,0), "sprite yDiyaBaseball",(0,0), "sprite yDiyaHappy1", (0,0), "sprite yDiyaHat2")
    zoom 1.05
image sideSprite1 yDiyaHappyB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((235, 80, sideImageWidth, sideImageHeight2), "sprite yDiyaHappyB"))
image sideSprite2 yDiyaHappyB:
    "sideSprite1 yDiyaHappyB"


image sprite yDiyaDelightedB:
    LiveComposite((883, 818),(0,0), "sprite yDiyaBaseball",(0,0), "sprite yDiyaDelighted1", (0,0), "sprite yDiyaHat2")
    zoom 1.05
image sideSprite1 yDiyaDelightedB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((235, 80, sideImageWidth, sideImageHeight2), "sprite yDiyaDelightedB"))
image sideSprite2 yDiyaDelightedB:
    "sideSprite1 yDiyaDelightedB"

image sprite yDiyaAnnoyedB:
    LiveComposite((883, 818),(0,0), "sprite yDiyaBaseball",(0,0), "sprite yDiyaAnnoyed1", (0,0), "sprite yDiyaHat2")
    zoom 1.05
image sideSprite1 yDiyaAnnoyedB:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((235, 80, sideImageWidth, sideImageHeight2), "sprite yDiyaAnnoyedB"))
image sideSprite2 yDiyaAnnoyedB:
    "sideSprite1 yDiyaAnnoyedB"


image sprite yDiyaSurprisedB:
    LiveComposite((883, 818),(0,0), "sprite yDiyaBaseball",(0,0), "sprite yDiyaSurprised1", (0,0), "sprite yDiyaHat2")
    zoom 1.05
image sideSprite1 yDiyaSurprisedB:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((235, 80, sideImageWidth, sideImageHeight2), "sprite yDiyaSurprisedB"))
image sideSprite2 yDiyaSurprisedB:
    "sideSprite1 yDiyaSurprisedB"

image sprite yDiyaAwayHappyB:
    LiveComposite((883, 818),(0,0), "sprite yDiyaBaseball",(0,0), "sprite yDiyaAwayHappy1", (0,0), "sprite yDiyaHat2")
    zoom 1.05
image sideSprite1 yDiyaAwayHappyB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((235, 80, sideImageWidth, sideImageHeight2), "sprite yDiyaAwayHappyB"))
image sideSprite2 yDiyaAwayHappyB:
    "sideSprite1 yDiyaAwayHappyB"

image sprite yDiyaAwayB:
    LiveComposite((883, 818),(0,0), "sprite yDiyaBaseball",(0,0), "sprite yDiyaAway1", (0,0), "sprite yDiyaHat2")
    zoom 1.05
image sideSprite1 yDiyaAwayB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((235, 80, sideImageWidth, sideImageHeight2), "sprite yDiyaAwayB"))
image sideSprite2 yDiyaAwayB:
    "sideSprite1 yDiyaAwayB"

image sprite yDiyaWorriedB:
    LiveComposite((883, 818),(0,0), "sprite yDiyaBaseball",(0,0), "sprite yDiyaWorried1", (0,0), "sprite yDiyaHat2")
    zoom 1.05
image sideSprite1 yDiyaWorriedB:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((235, 80, sideImageWidth, sideImageHeight2), "sprite yDiyaWorriedB"))
image sideSprite2 yDiyaWorriedB:
    "sideSprite1 yDiyaWorriedB"


image sprite yDiyaWorriedAwayB:
    LiveComposite((883, 818),(0,0), "sprite yDiyaBaseball",(0,0), "sprite yDiyaWorriedAway1", (0,0), "sprite yDiyaHat2")
    zoom 1.05
image sideSprite1 yDiyaWorriedAwayB:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((235, 80, sideImageWidth, sideImageHeight2), "sprite yDiyaWorriedAwayB"))
image sideSprite2 yDiyaWorriedAwayB:
    "sideSprite1 yDiyaWorriedAwayB"

image sprite yDiyaScaredB:
    LiveComposite((883, 818),(0,0), "sprite yDiyaBaseball",(0,0), "sprite yDiyaScared1", (0,0), "sprite yDiyaHat2")
    zoom 1.05
image sideSprite1 yDiyaScaredB:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((235, 80, sideImageWidth, sideImageHeight2), "sprite yDiyaScaredB"))
image sideSprite2 yDiyaScaredB:
    "sideSprite1 yDiyaScaredB"

image sprite yDiyaShockedB:
    LiveComposite((883, 818),(0,0), "sprite yDiyaBaseball",(0,0), "sprite yDiyaShocked1", (0,0), "sprite yDiyaHat2")
    zoom 1.05
image sideSprite1 yDiyaShockedB:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((235, 80, sideImageWidth, sideImageHeight2), "sprite yDiyaShockedB"))
image sideSprite2 yDiyaShockedB:
    "sideSprite1 yDiyaShockedB"

image sprite yDiyaAwayHappyB:
    LiveComposite((883, 818),(0,0), "sprite yDiyaBaseball",(0,0), "sprite yDiyaAwayHappy1", (0,0), "sprite yDiyaHat2")
    zoom 1.05
image sideSprite1 yDiyaAwayHappyB:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((235, 80, sideImageWidth, sideImageHeight2), "sprite yDiyaAwayHappyB"))
image sideSprite2 yDiyaAwayHappyB:
    "sideSprite1 yDiyaAwayHappyB"

image sprite yMinNeutral:
     LiveComposite((1038, 818),(0,0), "sprite yMinDefault",(0,0), "sprite yMinNeutral1", (0,0), "sprite yMinHair1")
     zoom 1.05
image sideSprite1 yMinNeutral:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((350, 110, sideImageWidth, sideImageHeight2), "sprite yMinNeutral"))
image sideSprite2 yMinNeutral:
    "sideSprite1 yMinNeutral"

image sprite yMinShocked:
    LiveComposite((1038, 818),(0,0), "sprite yMinDefault",(0,0), "sprite yMinShocked1", (0,0), "sprite yMinHair1")
    zoom 1.05
image sideSprite1 yMinShocked:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((350, 110, sideImageWidth, sideImageHeight2), "sprite yMinShocked"))
image sideSprite2 yMinShocked:
    "sideSprite1 yMinShocked"



image sprite yMinHm:
    LiveComposite((1038, 818),(0,0), "sprite yMinDefault",(0,0), "sprite yMinHm1", (0,0), "sprite yMinHair1")
    zoom 1.05
image sideSprite1 yMinHm:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((350, 110, sideImageWidth, sideImageHeight2), "sprite yMinHm"))
image sideSprite2 yMinHm:
    "sideSprite1 yMinHm"


image sprite yMinAway:
    LiveComposite((1038, 818),(0,0), "sprite yMinDefault",(0,0), "sprite yMinAway1", (0,0), "sprite yMinHair1")
    zoom 1.05
image sideSprite1 yMinAway:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((350, 110, sideImageWidth, sideImageHeight2), "sprite yMinAway"))
image sideSprite2 yMinAway:
    "sideSprite1 yMinAway"

image sprite yMinHappy:
   LiveComposite((1038, 818),(0,0), "sprite yMinDefault",(0,0), "sprite yMinHappy1", (0,0), "sprite yMinHair1")
   zoom 1.05
image sideSprite1 yMinHappy:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((350, 110, sideImageWidth, sideImageHeight2), "sprite yMinHappy"))
image sideSprite2 yMinHappy:
    "sideSprite1 yMinHappy"


image sprite yMinStupidHappy:
    LiveComposite((1038, 818),(0,0), "sprite yMinDefault",(0,0), "sprite yMinStupidHappy1", (0,0), "sprite yMinHair1")
    zoom 1.05
image sideSprite1 yMinStupidHappy:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((350, 110, sideImageWidth, sideImageHeight2), "sprite yMinStupidHappy"))
image sideSprite2 yMinStupidHappy:
    "sideSprite1 yMinStupidHappy"

image sprite yMinSmug:
    LiveComposite((1038, 818),(0,0), "sprite yMinDefault",(0,0), "sprite yMinHappy2", (0,0), "sprite yMinHair1")
    zoom 1.05
image sideSprite1 yMinSmug:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((350, 110, sideImageWidth, sideImageHeight2), "sprite yMinSmug"))
image sideSprite2 yMinSmug:
    "sideSprite1 yMinSmug"

image sprite yMinCough:
    LiveComposite((1038, 818),(0,0), "sprite yMinDefault",(0,0), "sprite yMinShocked2", (0,0), "sprite yMinHair1")
    zoom 1.05
image sideSprite1 yMinCough:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((350, 110, sideImageWidth, sideImageHeight2), "sprite yMinCough"))
image sideSprite2 yMinCough:
    "sideSprite1 yMinCough"

image sprite yMinAnnoyed:
    LiveComposite((1038, 818),(0,0), "sprite yMinDefault",(0,0), "sprite yMinAnnoyed1", (0,0), "sprite yMinHair1")
    zoom 1.05
image sideSprite1 yMinAnnoyed:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((350, 110, sideImageWidth, sideImageHeight2), "sprite yMinAnnoyed"))
image sideSprite2 yMinAnnoyed:
    "sideSprite1 yMinAnnoyed"

image sprite yMinAnnoyedAway:
    LiveComposite((1038, 818),(0,0), "sprite yMinDefault",(0,0), "sprite yMinAnnoyedAway1", (0,0), "sprite yMinHair1")
    zoom 1.05
image sideSprite1 yMinAnnoyedAway:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((350, 110, sideImageWidth, sideImageHeight2), "sprite yMinAnnoyedAway"))
image sideSprite2 yMinAnnoyedAway:
    "sideSprite1 yMinAnnoyedAway"

image sprite yMinAway:
    LiveComposite((1038, 818),(0,0), "sprite yMinDefault",(0,0), "sprite yMinAway1", (0,0), "sprite yMinHair1")
    zoom 1.05
image sideSprite1 yMinAway:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((350, 110, sideImageWidth, sideImageHeight2), "sprite yMinAway"))
image sideSprite2 yMinAway:
    "sideSprite1 yMinAway"

image sprite yMinFlustered:
   LiveComposite((1038, 818),(0,0), "sprite yMinDefault",(0,0), "sprite yMinFlustered1", (0,0), "sprite yMinHair1")
   zoom 1.05
image sideSprite1 yMinFlustered:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((350, 110, sideImageWidth, sideImageHeight2), "sprite yMinFlustered"))
image sideSprite2 yMinFlustered:
    "sideSprite1 yMinFlustered"

image sprite yMinSurprised:
  LiveComposite((1038, 818),(0,0), "sprite yMinDefault",(0,0), "sprite yMinSurprised1", (0,0), "sprite yMinHair1")
  zoom 1.05
image sideSprite1 yMinSurprised:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((350, 110, sideImageWidth, sideImageHeight2), "sprite yMinSurprised"))
image sideSprite2 yMinSurprised:
    "sideSprite1 yMinSurprised"

image sprite yMinEvasive:
    LiveComposite((1038, 818),(0,0), "sprite yMinDefault",(0,0), "sprite yMinEvasive1", (0,0), "sprite yMinHair1")
    zoom 1.05
image sideSprite1 yMinEvasive:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((350, 110, sideImageWidth, sideImageHeight2), "sprite yMinEvasive"))
image sideSprite2 yMinEvasive:
    "sideSprite1 yMinEvasive"

image sprite yMinBlush:
    LiveComposite((1038, 818),(0,0), "sprite yMinDefault",(0,0), "sprite yMinBlush1", (0,0), "sprite yMinHair1")
    zoom 1.05
image sideSprite1 yMinBlush:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((350, 110, sideImageWidth, sideImageHeight2), "sprite yMinBlush"))
image sideSprite2 yMinBlush:
    "sideSprite1 yMinBlush"

image sprite yMinBlushAway:
    LiveComposite((1038, 818),(0,0), "sprite yMinDefault",(0,0), "sprite yMinBlushAway1", (0,0), "sprite yMinHair1")
    zoom 1.05
image sideSprite1 yMinBlushAway:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((350, 110, sideImageWidth, sideImageHeight2), "sprite yMinBlushAway"))
image sideSprite2 yMinBlushAway:
    "sideSprite1 yMinBlushAway"

image sprite yMinWorried:
    LiveComposite((1038, 818),(0,0), "sprite yMinDefault",(0,0), "sprite yMinWorried1", (0,0), "sprite yMinHair1")
    zoom 1.05
image sideSprite1 yMinWorried:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((350, 110, sideImageWidth, sideImageHeight2), "sprite yMinWorried"))
image sideSprite2 yMinWorried:
    "sideSprite1 yMinWorried"

image sprite gMinNeutral:
     LiveComposite((1038, 818),(0,0), "sprite yMinGirl",(0,0), "sprite yMinNeutral1", (0,0), "sprite yMinHair2")
     zoom 1.05
image sideSprite1 gMinNeutral:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((350, 110, sideImageWidth, sideImageHeight2), "sprite gMinNeutral"))
image sideSprite2 gMinNeutral:
    "sideSprite1 gMinNeutral"

image sprite gMinShocked:
    LiveComposite((1038, 818),(0,0), "sprite yMinGirl",(0,0), "sprite yMinShocked1", (0,0), "sprite yMinHair2")
    zoom 1.05
image sideSprite1 gMinShocked:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((350, 110, sideImageWidth, sideImageHeight2), "sprite gMinShocked"))
image sideSprite2 gMinShocked:
    "sideSprite1 gMinShocked"



image sprite gMinHm:
    LiveComposite((1038, 818),(0,0), "sprite yMinGirl",(0,0), "sprite yMinHm1", (0,0), "sprite yMinHair2")
    zoom 1.05
image sideSprite1 gMinHm:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((350, 110, sideImageWidth, sideImageHeight2), "sprite gMinHm"))
image sideSprite2 gMinHm:
    "sideSprite1 gMinHm"


image sprite gMinAway:
    LiveComposite((1038, 818),(0,0), "sprite yMinGirl",(0,0), "sprite yMinAway1", (0,0), "sprite yMinHair2")
    zoom 1.05
image sideSprite1 gMinAway:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((350, 110, sideImageWidth, sideImageHeight2), "sprite gMinAway"))
image sideSprite2 gMinAway:
    "sideSprite1 gMinAway"

image sprite gMinHappy:
   LiveComposite((1038, 818),(0,0), "sprite yMinGirl",(0,0), "sprite yMinHappy1", (0,0), "sprite yMinHair2")
   zoom 1.05
image sideSprite1 gMinHappy:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((350, 110, sideImageWidth, sideImageHeight2), "sprite gMinHappy"))
image sideSprite2 gMinHappy:
    "sideSprite1 gMinHappy"


image sprite gMinStupidHappy:
    LiveComposite((1038, 818),(0,0), "sprite yMinGirl",(0,0), "sprite yMinStupidHappy1", (0,0), "sprite yMinHair2")
    zoom 1.05
image sideSprite1 gMinStupidHappy:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((350, 110, sideImageWidth, sideImageHeight2), "sprite gMinStupidHappy"))
image sideSprite2 gMinStupidHappy:
    "sideSprite1 gMinStupidHappy"

image sprite gMinSmug:
    LiveComposite((1038, 818),(0,0), "sprite yMinGirl",(0,0), "sprite yMinHappy2", (0,0), "sprite yMinHair2")
    zoom 1.05
image sideSprite1 gMinSmug:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((350, 110, sideImageWidth, sideImageHeight2), "sprite gMinSmug"))
image sideSprite2 gMinSmug:
    "sideSprite1 gMinSmug"

image sprite gMinCough:
    LiveComposite((1038, 818),(0,0), "sprite yMinGirl",(0,0), "sprite yMinShocked2", (0,0), "sprite yMinHair2")
    zoom 1.05
image sideSprite1 gMinCough:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((350, 110, sideImageWidth, sideImageHeight2), "sprite gMinCough"))
image sideSprite2 gMinCough:
    "sideSprite1 gMinCough"

image sprite gMinAnnoyed:
    LiveComposite((1038, 818),(0,0), "sprite yMinGirl",(0,0), "sprite yMinAnnoyed1", (0,0), "sprite yMinHair2")
    zoom 1.05
image sideSprite1 gMinAnnoyed:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((350, 110, sideImageWidth, sideImageHeight2), "sprite gMinAnnoyed"))
image sideSprite2 gMinAnnoyed:
    "sideSprite1 gMinAnnoyed"

image sprite gMinAnnoyedAway:
    LiveComposite((1038, 818),(0,0), "sprite yMinGirl",(0,0), "sprite yMinAnnoyedAway1", (0,0), "sprite yMinHair2")
    zoom 1.05
image sideSprite1 gMinAnnoyedAway:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((350, 110, sideImageWidth, sideImageHeight2), "sprite gMinAnnoyedAway"))
image sideSprite2 gMinAnnoyedAway:
    "sideSprite1 gMinAnnoyedAway"

image sprite gMinAway:
    LiveComposite((1038, 818),(0,0), "sprite yMinGirl",(0,0), "sprite yMinAway1", (0,0), "sprite yMinHair2")
    zoom 1.05
image sideSprite1 gMinAway:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((350, 110, sideImageWidth, sideImageHeight2), "sprite gMinAway"))
image sideSprite2 gMinAway:
    "sideSprite1 gMinAway"

image sprite gMinFlustered:
   LiveComposite((1038, 818),(0,0), "sprite yMinGirl",(0,0), "sprite yMinFlustered1", (0,0), "sprite yMinHair2")
   zoom 1.05
image sideSprite1 gMinFlustered:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((350, 110, sideImageWidth, sideImageHeight2), "sprite gMinFlustered"))
image sideSprite2 gMinFlustered:
    "sideSprite1 gMinFlustered"

image sprite gMinSurprised:
  LiveComposite((1038, 818),(0,0), "sprite yMinGirl",(0,0), "sprite yMinSurprised1", (0,0), "sprite yMinHair2")
  zoom 1.05
image sideSprite1 gMinSurprised:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((350, 110, sideImageWidth, sideImageHeight2), "sprite gMinSurprised"))
image sideSprite2 gMinSurprised:
    "sideSprite1 gMinSurprised"

image sprite gMinEvasive:
    LiveComposite((1038, 818),(0,0), "sprite yMinGirl",(0,0), "sprite yMinEvasive1", (0,0), "sprite yMinHair2")
    zoom 1.05
image sideSprite1 gMinEvasive:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((350, 110, sideImageWidth, sideImageHeight2), "sprite gMinEvasive"))
image sideSprite2 gMinEvasive:
    "sideSprite1 gMinEvasive"

image sprite gMinBlush:
    LiveComposite((1038, 818),(0,0), "sprite yMinGirl",(0,0), "sprite yMinBlush1", (0,0), "sprite yMinHair2")
    zoom 1.05
image sideSprite1 gMinBlush:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((350, 110, sideImageWidth, sideImageHeight2), "sprite gMinBlush"))
image sideSprite2 gMinBlush:
    "sideSprite1 gMinBlush"

image sprite gMinBlushAway:
    LiveComposite((1038, 818),(0,0), "sprite yMinGirl",(0,0), "sprite yMinBlushAway1", (0,0), "sprite yMinHair2")
    zoom 1.05
image sideSprite1 gMinBlushAway:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((350, 110, sideImageWidth, sideImageHeight2), "sprite gMinBlushAway"))
image sideSprite2 gMinBlushAway:
    "sideSprite1 gMinBlushAway"

image sprite gMinWorried:
    LiveComposite((1038, 818),(0,0), "sprite yMinGirl",(0,0), "sprite yMinWorried1", (0,0), "sprite yMinHair2")
    zoom 1.05
image sideSprite1 gMinWorried:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((350, 110, sideImageWidth, sideImageHeight2), "sprite gMinWorried"))
image sideSprite2 gMinWorried:
    "sideSprite1 gMinWorried"



image sprite minNeutral:
    LiveComposite((1038, 818),(0,0), "sprite minDefault2",(0,0), "sprite minNeutral1", (0,0), "sprite minHair2")
image sideSprite1 minNeutral:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((280, 90, sideImageWidth, sideImageHeight2), "sprite minNeutral"))
image sideSprite2 minNeutral:
    "sideSprite1 minNeutral"

image sprite minShocked:
     LiveComposite((1038, 818),(0,0), "sprite minDefault1",(0,0), "sprite minShocked1", (0,0), "sprite minHair1")
image sideSprite1 minShocked:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((260, 90, sideImageWidth, sideImageHeight2), "sprite minShocked"))
image sideSprite2 minShocked:
    "sideSprite1 minShocked"

image sprite minUnamused:
    LiveComposite((1038, 818),(0,0), "sprite minDefault2",(0,0), "sprite minUnamused1", (0,0), "sprite minHair2")
image sideSprite1 minUnamused:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((280, 90, sideImageWidth, sideImageHeight2), "sprite minUnamused"))
image sideSprite2 minUnamused:
    "sideSprite1 minUnamused"

image sprite minUh:
    LiveComposite((1038, 818),(0,0), "sprite minDefault2",(0,0), "sprite minUh1", (0,0), "sprite minHair2")
image sideSprite1 minUh:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((280, 90, sideImageWidth, sideImageHeight2), "sprite minUh"))
image sideSprite2 minUh:
    "sideSprite1 minUh"


image sprite minStupidHappy:
    LiveComposite((1038, 818),(0,0), "sprite minDefault1",(0,0), "sprite minStupidHappy1", (0,0), "sprite minHair1")
image sideSprite1 minStupidHappy:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((260, 90, sideImageWidth, sideImageHeight2), "sprite minStupidHappy"))
image sideSprite2 minStupidHappy:
    "sideSprite1 minStupidHappy"

image sprite minAnnoyed:
    LiveComposite((1038, 818),(0,0), "sprite minDefault1",(0,0), "sprite minAnnoyed1", (0,0), "sprite minHair1")
image sideSprite1 minAnnoyed:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((260, 90, sideImageWidth, sideImageHeight2), "sprite minAnnoyed"))
image sideSprite2 minAnnoyed:
    "sideSprite1 minAnnoyed"

image sprite minSurprised:
     LiveComposite((1038, 818),(0,0), "sprite minDefault1",(0,0), "sprite minSurprised1", (0,0), "sprite minHair1")
image sideSprite1 minSurprised:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((260, 90, sideImageWidth, sideImageHeight2), "sprite minSurprised"))
image sideSprite2 minSurprised:
    "sideSprite1 minSurprised"


image sprite minSmug:
    LiveComposite((1038, 818),(0,0), "sprite minDefault2",(0,0), "sprite minSmug1", (0,0), "sprite minHair2")
image sideSprite1 minSmug:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((280, 90, sideImageWidth, sideImageHeight2), "sprite minSmug"))
image sideSprite2 minSmug:
    "sideSprite1 minSmug"

image sprite minBlush:
    LiveComposite((1038, 818),(0,0), "sprite minDefault1",(0,0), "sprite minBlush1", (0,0), "sprite minHair1")
image sideSprite1 minBlush:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((260, 90, sideImageWidth, sideImageHeight2), "sprite minBlush"))
image sideSprite2 minBlush:
    "sideSprite1 minBlush"

image sprite minFlustered:
   LiveComposite((1038, 818),(0,0), "sprite minDefault2",(0,0), "sprite minFlustered1", (0,0), "sprite minHair2")
image sideSprite1 minFlustered:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((280, 90, sideImageWidth, sideImageHeight2), "sprite minFlustered"))
image sideSprite2 minFlustered:
    "sideSprite1 minFlustered"

image sprite minFlusteredOpen:
    LiveComposite((1038, 818),(0,0), "sprite minDefault2",(0,0), "sprite minFlustered2", (0,0), "sprite minHair2")
image sideSprite1 minFlusteredOpen:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((280, 90, sideImageWidth, sideImageHeight2), "sprite minFlusteredOpen"))
image sideSprite2 minFlusteredOpen:
    "sideSprite1 minFlusteredOpen"

image sprite minCute:
    LiveComposite((1038, 818),(0,0), "sprite minDefault2",(0,0), "sprite minCute1", (0,0), "sprite minHair2")
image sideSprite1 minCute:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((280, 90, sideImageWidth, sideImageHeight2), "sprite minCute"))
image sideSprite2 minCute:
    "sideSprite1 minCute"

image sprite minAway:
   LiveComposite((1038, 818),(0,0), "sprite minDefault2",(0,0), "sprite minAway1", (0,0), "sprite minHair2")
image sideSprite1 minAway:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((280, 90, sideImageWidth, sideImageHeight2), "sprite minAway"))
image sideSprite2 minAway:
    "sideSprite1 minAway"

image sprite minHm:
    LiveComposite((1038, 818),(0,0), "sprite minDefault2",(0,0), "sprite minHm1", (0,0), "sprite minHair2")
image sideSprite1 minHm:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((280, 90, sideImageWidth, sideImageHeight2), "sprite minHm"))
image sideSprite2 minHm:
    "sideSprite1 minHm"

image sprite minHappy:
    LiveComposite((1038, 818),(0,0), "sprite minDefault1",(0,0), "sprite minHappy1", (0,0), "sprite minHair1")
image sideSprite1 minHappy:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((280, 90, sideImageWidth, sideImageHeight2), "sprite minHappy"))
image sideSprite2 minHappy:
    "sideSprite1 minHappy"


image sprite minNeutralOpen:
    LiveComposite((1038, 818),(0,0), "sprite minDefault1",(0,0), "sprite minNeutralOpen1", (0,0), "sprite minHair1")
image sideSprite1 minNeutralOpen:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((260, 90, sideImageWidth, sideImageHeight2), "sprite minNeutralOpen"))
image sideSprite2 minNeutralOpen:
    "sideSprite1 minNeutralOpen"


image sprite minNeutralB:
    LiveComposite((1038, 818),(0,0), "sprite minBaseball2",(0,0), "sprite minNeutral1", (0,0), "sprite minHat2")
image sideSprite1 minNeutralB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((280, 90, sideImageWidth, sideImageHeight2), "sprite minNeutralB"))
image sideSprite2 minNeutralB:
    "sideSprite1 minNeutralB"

image sprite minShockedB:
     LiveComposite((1038, 818),(0,0), "sprite minBaseball1",(0,0), "sprite minShocked1", (0,0), "sprite minHat1")
image sideSprite1 minShockedB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((260, 90, sideImageWidth, sideImageHeight2), "sprite minShockedB"))
image sideSprite2 minShockedB:
    "sideSprite1 minShockedB"

image sprite minUnamusedB:
     LiveComposite((1038, 818),(0,0), "sprite minBaseball2",(0,0), "sprite minUnamused1", (0,0), "sprite minHat2")
image sideSprite1 minUnamusedB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((260, 90, sideImageWidth, sideImageHeight2), "sprite minUnamusedB"))
image sideSprite2 minUnamusedB:
    "sideSprite1 minUnamusedB"

image sprite minUhB:
    LiveComposite((1038, 818),(0,0), "sprite minBaseball2",(0,0), "sprite minUh1", (0,0), "sprite minHat2")
image sideSprite1 minUhB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((260, 90, sideImageWidth, sideImageHeight2), "sprite minUhB"))
image sideSprite2 minUhB:
    "sideSprite1 minUhB"


image sprite minStupidHappyB:
    LiveComposite((1038, 818),(0,0), "sprite minBaseball1",(0,0), "sprite minStupidHappy1", (0,0), "sprite minHat1")
image sideSprite1 minStupidHappyB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((260, 90, sideImageWidth, sideImageHeight2), "sprite minStupidHappyB"))
image sideSprite2 minStupidHappyB:
    "sideSprite1 minStupidHappyB"

image sprite minAnnoyedB:
    LiveComposite((1038, 818),(0,0), "sprite minBaseball1",(0,0), "sprite minAnnoyed1", (0,0), "sprite minHat1")
image sideSprite1 minAnnoyedB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((260, 90, sideImageWidth, sideImageHeight2), "sprite minAnnoyedB"))
image sideSprite2 minAnnoyedB:
    "sideSprite1 minAnnoyedB"

image sprite minSurprisedB:
     LiveComposite((1038, 818),(0,0), "sprite minBaseball1",(0,0), "sprite minSurprised1", (0,0), "sprite minHat1")
image sideSprite1 minSurprisedB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((260, 90, sideImageWidth, sideImageHeight2), "sprite minSurprisedB"))
image sideSprite2 minSurprisedB:
    "sideSprite1 minSurprisedB"


image sprite minSmugB:
    LiveComposite((1038, 818),(0,0), "sprite minBaseball2",(0,0), "sprite minSmug1", (0,0), "sprite minHat2")
image sideSprite1 minSmugB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((280, 90, sideImageWidth, sideImageHeight2), "sprite minSmugB"))
image sideSprite2 minSmugB:
    "sideSprite1 minSmugB"

image sprite minBlushB:
    LiveComposite((1038, 818),(0,0), "sprite minBaseball1",(0,0), "sprite minBlush1", (0,0), "sprite minHat1")
image sideSprite1 minBlushB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((260, 90, sideImageWidth, sideImageHeight2), "sprite minBlushB"))
image sideSprite2 minBlushB:
    "sideSprite1 minBlushB"

image sprite minFlusteredB:
   LiveComposite((1038, 818),(0,0), "sprite minBaseball2",(0,0), "sprite minFlustered1", (0,0), "sprite minHat2")
image sideSprite1 minFlusteredB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((280, 90, sideImageWidth, sideImageHeight2), "sprite minFlusteredB"))
image sideSprite2 minFlusteredB:
    "sideSprite1 minFlusteredB"

image sprite minFlusteredOpenB:
    LiveComposite((1038, 818),(0,0), "sprite minBaseball2",(0,0), "sprite minFlustered2", (0,0), "sprite minHat2")
image sideSprite1 minFlusteredOpenB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((280, 90, sideImageWidth, sideImageHeight2), "sprite minFlusteredOpenB"))
image sideSprite2 minFlusteredOpenB:
    "sideSprite1 minFlusteredOpenB"

image sprite minCuteB:
    LiveComposite((1038, 818),(0,0), "sprite minBaseball2",(0,0), "sprite minCute1", (0,0), "sprite minHat2")
image sideSprite1 minCuteB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((280, 90, sideImageWidth, sideImageHeight2), "sprite minCuteB"))
image sideSprite2 minCuteB:
    "sideSprite1 minCuteB"

image sprite minAwayB:
   LiveComposite((1038, 818),(0,0), "sprite minBaseball2",(0,0), "sprite minAway1", (0,0), "sprite minHat2")
image sideSprite1 minAwayB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((280, 90, sideImageWidth, sideImageHeight2), "sprite minAwayB"))
image sideSprite2 minAwayB:
    "sideSprite1 minAwayB"

image sprite minHmB:
    LiveComposite((1038, 818),(0,0), "sprite minBaseball2",(0,0), "sprite minHm1", (0,0), "sprite minHat2")
image sideSprite1 minHmB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((280, 90, sideImageWidth, sideImageHeight2), "sprite minHmB"))
image sideSprite2 minHmB:
    "sideSprite1 minHmB"

image sprite minHappyB:
    LiveComposite((1038, 818),(0,0), "sprite minBaseball1",(0,0), "sprite minHappy1", (0,0), "sprite minHat1")
image sideSprite1 minHappyB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((280, 90, sideImageWidth, sideImageHeight2), "sprite minHappyB"))
image sideSprite2 minHappyB:
    "sideSprite1 minHappyB"


image sprite minNeutralOpenB:
    LiveComposite((1038, 818),(0,0), "sprite minBaseball1",(0,0), "sprite minNeutralOpen1", (0,0), "sprite minHat1")
image sideSprite1 minNeutralOpenB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((260, 90, sideImageWidth, sideImageHeight2), "sprite minNeutralOpenB"))
image sideSprite2 minNeutralOpenB:
    "sideSprite1 minNeutralOpenB"


image sprite junNeutral:
    "sprite junNeutral1"
#    choice:
#        4.0
#        "sprite junNeutral2"
#        0.08
#        "sprite junNeutral1"
#        0.15
#    choice:
#        3.0
#    choice:
#        1.5
#    # This randomizes the time between blinking.
#    "sprite junNeutral2"
#    .10
#    repeat
image sideSprite1 junNeutral:
  #  "sprite junNeutral"

    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((260, 50, sideImageWidth, sideImageHeight2), "sprite junNeutral"))
image sideSprite2 junNeutral:
    "sideSprite1 junNeutral"

image sprite junWorried:
    "sprite junWorried1"
#    choice:
#        4.0
#        "sprite junWorried2"
#        0.08
#        "sprite junWorried1"
#        0.15
#    choice:
#        3.0
#    choice:
#        1.5
#    # This randomizes the time between blinking.
#    "sprite junWorried2"
#    .10
#    repeat
image sideSprite1 junWorried:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((260, 50, sideImageWidth, sideImageHeight2), "sprite junWorried"))
image sideSprite2 junWorried:
    "sideSprite1 junWorried"

image sprite junSigh:
    "sprite junUh1"
image sideSprite1 junSigh:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((260, 50, sideImageWidth, sideImageHeight2), "sprite junSigh"))
image sideSprite2 junSigh:
    "sideSprite1 junSigh"

image sprite junHappy:
    "sprite junHappy1"
#    choice:
#        4.0
#        "sprite junHappy2"
#        0.08
#        "sprite junHappy1"
#        0.15
#    choice:
#        3.0
#    choice:
#        1.5
#    # This randomizes the time between blinking.
#    "sprite junHappy2"
#    .10
#    repeat
image sideSprite1 junHappy:
  #  "sprite junHappy"

    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((260, 50, sideImageWidth, sideImageHeight2), "sprite junHappy"))
image sideSprite2 junHappy:
    "sideSprite1 junHappy"

image sprite junNervous:
    "sprite junNervous1"
#    choice:
#        4.0
#        "sprite junNervous2"
#        0.08
#        "sprite junNervous1"
#        0.15
#    choice:
#        3.0
#    choice:
#        1.5
#    # This randomizes the time between blinking.
#    "sprite junNervous2"
#    .10
#    repeat
image sideSprite1 junNervous:
  #  "sprite junNervous"

    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((260, 50, sideImageWidth, sideImageHeight2), "sprite junNervous"))
image sideSprite2 junNervous:
    "sideSprite1 junNervous"


image sprite junAway:
    "sprite junAway1"
#    choice:
#        4.0
#        "sprite junAway2"
#        0.08
#        "sprite junAway1"
#        0.15
#    choice:
#        3.0
#    choice:
#        1.5
#    # This randomizes the time between blinking.
#    "sprite junAway2"
#    .10
#    repeat
image sideSprite1 junAway:
  #  "sprite junAway"

    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((260, 50, sideImageWidth, sideImageHeight2), "sprite junAway"))
image sideSprite2 junAway:
    "sideSprite1 junAway"


image sprite tJunNeutral:
    "sprite tJunNeutral1"
#    choice:
#        4.0
#        "sprite tJunNeutral2"
#        0.08
#        "sprite tJunNeutral1"
#        0.15
#    choice:
#        3.0
#    choice:
#        1.5
#    # This randomizes the time between blinking.
#    "sprite tJunNeutral2"
#    .10
#    repeat
image sideSprite1 tJunNeutral:
  #  "sprite tJunNeutral"

    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((230, 45, sideImageWidth, sideImageHeight2), "sprite tJunNeutral"))
image sideSprite2 tJunNeutral:
    "sideSprite1 tJunNeutral"


image sprite tJunHappy:
    "sprite tJunHappy1"
#    choice:
#        4.0
#        "sprite tJunHappy2"
#        0.08
#        "sprite tJunHappy1"
#        0.15
#    choice:
#        3.0
#    choice:
#        1.5
#    # This randomizes the time between blinking.
#    "sprite tJunHappy2"
#    .10
#    repeat
image sideSprite1 tJunHappy:
  #  "sprite tJunHappy"

    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((230, 45, sideImageWidth, sideImageHeight2), "sprite tJunHappy"))
image sideSprite2 tJunHappy:
    "sideSprite1 tJunHappy"

image sprite tJunAnnoyed:
    "sprite tJunAnnoyed1"
#    choice:
#        4.0
#        "sprite tJunAnnoyed2"
#        0.08
#        "sprite tJunAnnoyed1"
#        0.15
#    choice:
#        3.0
#    choice:
#        1.5
#    # This randomizes the time between blinking.
#    "sprite tJunAnnoyed2"
#    .10
#    repeat
image sideSprite1 tJunAnnoyed:
  #  "sprite tJunAnnoyed"

    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((230, 45, sideImageWidth, sideImageHeight2), "sprite tJunAnnoyed"))
image sideSprite2 tJunAnnoyed:
    "sideSprite1 tJunAnnoyed"

image sprite tJunShocked:
    "sprite tJunShocked1"
#    choice:
#        4.0
#        "sprite tJunShocked2"
#        0.08
#        "sprite tJunShocked1"
#        0.15
#    choice:
#        3.0
#    choice:
#        1.5
#    # This randomizes the time between blinking.
#    "sprite tJunShocked2"
#    .10
#    repeat
image sideSprite1 tJunShocked:
  #  "sprite tJunShocked"

    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((230, 45, sideImageWidth, sideImageHeight2), "sprite tJunShocked"))
image sideSprite2 tJunShocked:
    "sideSprite1 tJunShocked"

image sprite tCamNeutral:
    "sprite tCamNeutral1"
#    choice:
#        4.0
#        "sprite tCamNeutral2"
#        0.08
#        "sprite tCamNeutral1"
#        0.15
#    choice:
#        3.0
#    choice:
#        1.5
#    # This randomizes the time between blinking.
#    "sprite tCamNeutral2"
#    .10
#    repeat
image sideSprite1 tCamNeutral:
  #  "sprite tCamNeutral"

    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((210, 0, sideImageWidth, sideImageHeight2), "sprite tCamNeutral"))
image sideSprite2 tCamNeutral:
    "sideSprite1 tCamNeutral"

image sprite tCamShocked:
    "sprite tCamShocked1"
#    choice:
#        4.0
#        "sprite tCamShocked2"
#        0.08
#        "sprite tCamShocked1"
#        0.15
#    choice:
#        3.0
#    choice:
#        1.5
#    # This randomizes the time between blinking.
#    "sprite tCamShocked2"
#    .10
#    repeat
image sideSprite1 tCamShocked:
  #  "sprite tCamShocked"

    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((210, 0, sideImageWidth, sideImageHeight2), "sprite tCamShocked"))
image sideSprite2 tCamShocked:
    "sideSprite1 tCamShocked"


image sprite tCamAnnoyed:
    "sprite tCamAnnoyed1"
#    choice:
#        4.0
#        "sprite tCamAnnoyed2"
#        0.08
#        "sprite tCamAnnoyed1"
#        0.15
#    choice:
#        3.0
#    choice:
#        1.5
#    # This randomizes the time between blinking.
#    "sprite tCamAnnoyed2"
#    .10
#    repeat
image sideSprite1 tCamAnnoyed:
  #  "sprite tCamAnnoyed"

    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((210, 0, sideImageWidth, sideImageHeight2), "sprite tCamAnnoyed"))
image sideSprite2 tCamAnnoyed:
    "sideSprite1 tCamAnnoyed"

image sprite tCamSigh:
    "sprite tCamSigh1"
#    choice:
#        4.0
#        "sprite tCamSigh2"
#        0.08
#        "sprite tCamSigh1"
#        0.15
#    choice:
#        3.0
#    choice:
#        1.5
#    # This randomizes the time between blinking.
#    "sprite tCamSigh2"
#    .10
#    repeat
image sideSprite1 tCamSigh:
  #  "sprite tCamSigh"

    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((210, 0, sideImageWidth, sideImageHeight2), "sprite tCamSigh"))
image sideSprite2 tCamSigh:
    "sideSprite1 tCamSigh"



image sprite tCamHappy:
    "sprite tCamHappy1"
#    choice:
#        4.0
#        "sprite tCamHappy2"
#        0.08
#        "sprite tCamHappy1"
#        0.15
#    choice:
#        3.0
#    choice:
#        1.5
#    # This randomizes the time between blinking.
#    "sprite tCamHappy2"
#    .10
#    repeat
image sideSprite1 tCamHappy:
  #  "sprite tCamHappy"

    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((210, 0, sideImageWidth, sideImageHeight2), "sprite tCamHappy"))
image sideSprite2 tCamHappy:
    "sideSprite1 tCamHappy"


image sprite camNeutral:
    "sprite camNeutral1"
    zoom 1.05
image sideSprite1 camNeutral:
  #  "sprite camNeutral"

    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((240, 70, sideImageWidth, sideImageHeight2), "sprite camNeutral"))
image sideSprite2 camNeutral:
    "sideSprite1 camNeutral"

image sprite camAnnoyed:
    "sprite camAnnoyed1"
    zoom 1.05
image sideSprite1 camAnnoyed:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((240, 80, sideImageWidth, sideImageHeight2), "sprite camAnnoyed"))
image sideSprite2 camAnnoyed:
    "sideSprite1 camAnnoyed"


image sprite camShocked:
    "sprite camShocked1"
    zoom 1.05
image sideSprite1 camShocked:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((240, 80, sideImageWidth, sideImageHeight2), "sprite camShocked"))
image sideSprite2 camShocked:
    "sideSprite1 camShocked"

image sprite camSigh:
    "sprite camAnnoyed2"
    zoom 1.05
image sideSprite1 camSigh:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((240, 80, sideImageWidth, sideImageHeight2), "sprite camSigh"))
image sideSprite2 camSigh:
    "sideSprite1 camSigh"

image sprite camHappy:
    "sprite camHappy1"
    zoom 1.05
image sideSprite1 camHappy:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((240, 80, sideImageWidth, sideImageHeight2), "sprite camHappy"))
image sideSprite2 camHappy:
    "sideSprite1 camHappy"

image sprite camSurprised:
    "sprite camSurprised1"
    zoom 1.05
image sideSprite1 camSurprised:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((240, 80, sideImageWidth, sideImageHeight2), "sprite camSurprised"))
image sideSprite2 camSurprised:
    "sideSprite1 camSurprised"


image sprite lizNeutral:
   # "sprite lizNeutral1"
    LiveComposite((898, 818),(0,0), "sprite lizDefault",(0,0), "sprite lizNeutral1")

#    choice:
#        4.0
#        "sprite lizNeutral2"
#        0.08
#        "sprite lizNeutral1"
#        0.15
#    choice:
#        3.0
#    choice:
#        1.5
#    # This randomizes the time between blinking.
#    "sprite lizNeutral2"
#    .10
#    repeat
image sideSprite1 lizNeutral:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((220, 60, sideImageWidth, sideImageHeight2), "sprite lizNeutral"))
image sideSprite2 lizNeutral:
    "sideSprite1 lizNeutral"

image sprite lizHappy:
    LiveComposite((898, 818),(0,0), "sprite lizDefault",(0,0), "sprite lizHappy1")
 #   "sprite lizHappy1"
#    choice:
#        4.0
#        "sprite lizHappy2"
#        0.08
#        "sprite lizHappy1"
#        0.15
#    choice:
#        3.0
#    choice:
#        1.5
#    # This randomizes the time between blinking.
#    "sprite lizHappy2"
#    .10
#    repeat
image sideSprite1 lizHappy:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((220, 60, sideImageWidth, sideImageHeight2), "sprite lizHappy"))
image sideSprite2 lizHappy:
    "sideSprite1 lizHappy"

image sprite lizSurprised:
    LiveComposite((898, 818),(0,0), "sprite lizDefault",(0,0), "sprite lizSurprised1")
#    choice:
#        4.0
#        "sprite lizSurprised2"
#        0.08
#        "sprite lizSurprised1"
#        0.15
#    choice:
#        3.0
#    choice:
#        1.5
#    # This randomizes the time between blinking.
#    "sprite lizSurprised2"
#    .10
#    repeat
image sideSprite1 lizSurprised:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((220, 60, sideImageWidth, sideImageHeight2), "sprite lizSurprised"))
image sideSprite2 lizSurprised:
    "sideSprite1 lizSurprised"

image sprite lizBigSmile:
    LiveComposite((898, 818),(0,0), "sprite lizDefault",(0,0), "sprite lizBigSmile1")
#    choice:
#        4.0
#        "sprite lizBigSmile2"
#        0.08
#        "sprite lizBigSmile1"
#        0.15
#    choice:
#        3.0
#    choice:
#        1.5
#    # This randomizes the time between blinking.
#    "sprite lizBigSmile2"
#    .10
#    repeat
image sideSprite1 lizBigSmile:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((220, 60, sideImageWidth, sideImageHeight2), "sprite lizBigSmile"))
image sideSprite2 lizBigSmile:
    "sideSprite1 lizBigSmile"

image sprite lizNeutralB:
    LiveComposite((898, 818),(0,0), "sprite lizBaseball",(0,0), "sprite lizNeutral1")


image sideSprite1 lizNeutralB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((220, 60, sideImageWidth, sideImageHeight2), "sprite lizNeutralB"))
image sideSprite2 lizNeutralB:
    "sideSprite1 lizNeutralB"

image sprite lizHappyB:
    LiveComposite((898, 818),(0,0), "sprite lizBaseball",(0,0), "sprite lizHappy1")

image sideSprite1 lizHappyB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((220, 60, sideImageWidth, sideImageHeight2), "sprite lizHappyB"))
image sideSprite2 lizHappyB:
    "sideSprite1 lizHappyB"

image sprite lizSurprisedB:
    LiveComposite((898, 818),(0,0), "sprite lizBaseball",(0,0), "sprite lizSurprised1")

image sideSprite1 lizSurprisedB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((220, 60, sideImageWidth, sideImageHeight2), "sprite lizSurprisedB"))
image sideSprite2 lizSurprisedB:
    "sideSprite1 lizSurprisedB"

image sprite lizBigSmileB:
    LiveComposite((898, 818),(0,0), "sprite lizBaseball",(0,0), "sprite lizBigSmile1")

image sideSprite1 lizBigSmileB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((220, 60, sideImageWidth, sideImageHeight2), "sprite lizBigSmileB"))
image sideSprite2 lizBigSmileB:
    "sideSprite1 lizBigSmileB"


image sprite yLizBigSmile:
    "sprite yLizBigSmile1"
image sideSprite1 yLizBigSmile:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((220, 60, sideImageWidth, sideImageHeight2), "sprite yLizBigSmile"))
image sideSprite2 yLizBigSmile:
    "sideSprite1 yLizBigSmile"


image sprite akarshaNeutral:
    LiveComposite((1035, 818),(0,0), "sprite akarshaDefault",(0,0), "sprite akarshaNeutral1")
image sideSprite1 akarshaNeutral:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((300, 80, sideImageWidth, sideImageHeight2), "sprite akarshaNeutral"))
image sideSprite2 akarshaNeutral:
    "sideSprite1 akarshaNeutral"

image sprite akarshaBigSmile:
    LiveComposite((1035, 818),(0,0), "sprite akarshaDefault",(0,0), "sprite akarshaBigSmile1")
image sideSprite1 akarshaBigSmile:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((300, 80, sideImageWidth, sideImageHeight2), "sprite akarshaBigSmile"))
image sideSprite2 akarshaBigSmile:
    "sideSprite1 akarshaBigSmile"

image sprite akarshaHappy:
     LiveComposite((1035, 818),(0,0), "sprite akarshaDefault",(0,0), "sprite akarshaHappy1")
image sideSprite1 akarshaHappy:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((300, 80, sideImageWidth, sideImageHeight2), "sprite akarshaHappy"))
image sideSprite2 akarshaHappy:
    "sideSprite1 akarshaHappy"


image sprite akarshaShrug:
    LiveComposite((1035, 818),(0,0), "sprite akarshaShrug1",(0,0), "sprite akarshaShrug2")
image sideSprite1 akarshaShrug:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((300, 80, sideImageWidth, sideImageHeight2), "sprite akarshaShrug"))
image sideSprite2 akarshaShrug:
    "sideSprite1 akarshaShrug"

image sprite akarshaAnnoyed:
    LiveComposite((1035, 818),(0,0), "sprite akarshaDefault",(0,0), "sprite akarshaAnnoyed1")
image sideSprite1 akarshaAnnoyed:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((300, 80, sideImageWidth, sideImageHeight2), "sprite akarshaAnnoyed"))
image sideSprite2 akarshaAnnoyed:
    "sideSprite1 akarshaAnnoyed"

image sprite akarshaAnnoyedAway:
    LiveComposite((1035, 818),(0,0), "sprite akarshaDefault",(0,0), "sprite akarshaAnnoyedAway1")
image sideSprite1 akarshaAnnoyedAway:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((300, 80, sideImageWidth, sideImageHeight2), "sprite akarshaAnnoyedAway"))
image sideSprite2 akarshaAnnoyedAway:
    "sideSprite1 akarshaAnnoyedAway"

image sprite akarshaShocker:
    LiveComposite((1035, 818),(0,0), "sprite akarshaShockerDefault",(0,0), "sprite akarshaShocker1")
image sideSprite1 akarshaShocker:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((300, 60, sideImageWidth, sideImageHeight2), "sprite akarshaShocker"))
image sideSprite2 akarshaShocker:
    "sideSprite1 akarshaShocker"


image sprite akarshaAway:
    "sprite akarshaAway1"
    LiveComposite((1035, 818),(0,0), "sprite akarshaThinking",(0,0), "sprite akarshaAway1")
image sideSprite1 akarshaAway:
 #   LiveComposite((354, 205),(0, 0), "sidebox.png",(1,2), LiveCrop((160, 80, sideImageWidth, sideImageHeight), "sprite akarshaAway"))

    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((300, 80, sideImageWidth, sideImageHeight2), "sprite akarshaAway"))
image sideSprite2 akarshaAway:
    "sideSprite1 akarshaAway"


image sprite akarshaHm:
    LiveComposite((1035, 818),(0,0), "sprite akarshaThinking",(0,0), "sprite akarshaHm1")
image sideSprite1 akarshaHm:
 #   LiveComposite((354, 205),(0, 0), "sidebox.png",(1,2), LiveCrop((160, 80, sideImageWidth, sideImageHeight), "sprite akarshaHm"))

    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((300, 80, sideImageWidth, sideImageHeight2), "sprite akarshaHm"))
image sideSprite2 akarshaHm:
    "sideSprite1 akarshaHm"

image sprite akarshaSurprised:
    LiveComposite((1035, 818),(0,0), "sprite akarshaDefault",(0,0), "sprite akarshaSurprised1")
image sideSprite1 akarshaSurprised:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((300, 80, sideImageWidth, sideImageHeight2), "sprite akarshaSurprised"))
image sideSprite2 akarshaSurprised:
    "sideSprite1 akarshaSurprised"


image sprite akarshaNeutralB:
    LiveComposite((1035, 818),(0,0), "sprite akarshaBaseball",(0,0), "sprite akarshaNeutral1")
image sideSprite1 akarshaNeutralB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((300, 80, sideImageWidth, sideImageHeight2), "sprite akarshaNeutralB"))
image sideSprite2 akarshaNeutralB:
    "sideSprite1 akarshaNeutralB"

image sprite akarshaBigSmileB:
    LiveComposite((1035, 818),(0,0), "sprite akarshaBaseball",(0,0), "sprite akarshaBigSmile1")
image sideSprite1 akarshaBigSmileB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((300, 80, sideImageWidth, sideImageHeight2), "sprite akarshaBigSmileB"))
image sideSprite2 akarshaBigSmileB:
    "sideSprite1 akarshaBigSmileB"

image sprite akarshaHappyB:
     LiveComposite((1035, 818),(0,0), "sprite akarshaBaseball",(0,0), "sprite akarshaHappy1")
image sideSprite1 akarshaHappyB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((300, 80, sideImageWidth, sideImageHeight2), "sprite akarshaHappyB"))
image sideSprite2 akarshaHappyB:
    "sideSprite1 akarshaHappyB"


image sprite akarshaShrugB:
    LiveComposite((1035, 818),(0,0), "sprite akarshaBaseball",(0,0), "sprite akarshaShrug2")
image sideSprite1 akarshaShrugB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((300, 80, sideImageWidth, sideImageHeight2), "sprite akarshaShrugB"))
image sideSprite2 akarshaShrugB:
    "sideSprite1 akarshaShrugB"

image sprite akarshaAnnoyedB:
    LiveComposite((1035, 818),(0,0), "sprite akarshaBaseball",(0,0), "sprite akarshaAnnoyed1")
image sideSprite1 akarshaAnnoyedB:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((300, 80, sideImageWidth, sideImageHeight2), "sprite akarshaAnnoyedB"))
image sideSprite2 akarshaAnnoyedB:
    "sideSprite1 akarshaAnnoyedB"

image sprite akarshaAnnoyedAwayB:
    LiveComposite((1035, 818),(0,0), "sprite akarshaBaseball",(0,0), "sprite akarshaAnnoyedAway1")
image sideSprite1 akarshaAnnoyedAwayB:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((300, 80, sideImageWidth, sideImageHeight2), "sprite akarshaAnnoyedAwayB"))
image sideSprite2 akarshaAnnoyedAwayB:
    "sideSprite1 akarshaAnnoyedAwayB"

image sprite akarshaShockerB:
    LiveComposite((1035, 818),(0,0), "sprite akarshaShockerBaseball",(0,0), "sprite akarshaShocker1")
image sideSprite1 akarshaShockerB:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((300, 60, sideImageWidth, sideImageHeight2), "sprite akarshaShockerB"))
image sideSprite2 akarshaShockerB:
    "sideSprite1 akarshaShockerB"


image sprite akarshaAwayB:
    "sprite akarshaAway1"
    LiveComposite((1035, 818),(0,0), "sprite akarshaBaseball",(0,0), "sprite akarshaAway1")
image sideSprite1 akarshaAwayB:
 #   LiveComposite((354, 205),(0, 0), "sidebox.png",(1,2), LiveCrop((160, 80, sideImageWidth, sideImageHeight), "sprite akarshaAwayB"))

    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((300, 80, sideImageWidth, sideImageHeight2), "sprite akarshaAwayB"))
image sideSprite2 akarshaAwayB:
    "sideSprite1 akarshaAwayB"


image sprite akarshaHmB:
    LiveComposite((1035, 818),(0,0), "sprite akarshaBaseball",(0,0), "sprite akarshaHm1")
image sideSprite1 akarshaHmB:
 #   LiveComposite((354, 205),(0, 0), "sidebox.png",(1,2), LiveCrop((160, 80, sideImageWidth, sideImageHeight), "sprite akarshaHmB"))

    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((300, 80, sideImageWidth, sideImageHeight2), "sprite akarshaHmB"))
image sideSprite2 akarshaHmB:
    "sideSprite1 akarshaHmB"

image sprite akarshaSurprisedB:
    LiveComposite((1035, 818),(0,0), "sprite akarshaBaseball",(0,0), "sprite akarshaSurprised1")
image sideSprite1 akarshaSurprisedB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((300, 80, sideImageWidth, sideImageHeight2), "sprite akarshaSurprisedB"))
image sideSprite2 akarshaSurprisedB:
    "sideSprite1 akarshaSurprisedB"

image sprite noelleNeutral:
    LiveComposite((1090, 818),(0,0), "sprite noelleDefault",(0,0), "sprite noelleNeutral1")
image sideSprite1 noelleNeutral:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((320, 50, sideImageWidth, sideImageHeight2), "sprite noelleNeutral"))
image sideSprite2 noelleNeutral:
    "sideSprite1 noelleNeutral"

image sprite noelleUh:
    LiveComposite((1090, 818),(0,0), "sprite noelleDefault",(0,0), "sprite noelleUh1")
image sideSprite1 noelleUh:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((320, 50, sideImageWidth, sideImageHeight2), "sprite noelleUh"))
image sideSprite2 noelleUh:
    "sideSprite1 noelleUh"

image sprite noelleBigSmile:
    LiveComposite((1090, 818),(0,0), "sprite noelleDefault",(0,0), "sprite noelleBigSmile1")
image sideSprite1 noelleBigSmile:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((320, 50, sideImageWidth, sideImageHeight2), "sprite noelleBigSmile"))
image sideSprite2 noelleBigSmile:
    "sideSprite1 noelleBigSmile"

image sprite noelleTsun:

    LiveComposite((1090, 818),(0,0), "sprite noelleDefault",(0,0), "sprite noelleTsun1")
image sideSprite1 noelleTsun:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((320, 50, sideImageWidth, sideImageHeight2), "sprite noelleTsun"))
image sideSprite2 noelleTsun:
    "sideSprite1 noelleTsun"

image sprite noelleFacepalm:
    "sprite noelleFacepalm1"
image sideSprite1 noelleFacepalm:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((300, 50, sideImageWidth, sideImageHeight2), "sprite noelleFacepalm"))
image sideSprite2 noelleFacepalm:
    "sideSprite1 noelleFacepalm"

image sprite noelleAway:
   LiveComposite((1090, 818),(0,0), "sprite noelleDefault",(0,0), "sprite noelleAway1")
image sideSprite1 noelleAway:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((320, 50, sideImageWidth, sideImageHeight2), "sprite noelleAway"))
image sideSprite2 noelleAway:
    "sideSprite1 noelleAway"

image sprite noelleHappy:
    LiveComposite((1090, 818),(0,0), "sprite noelleDefault",(0,0), "sprite noelleHappy1")
image sideSprite1 noelleHappy:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((320, 50, sideImageWidth, sideImageHeight2), "sprite noelleHappy"))
image sideSprite2 noelleHappy:
    "sideSprite1 noelleHappy"

image sprite noelleAnnoyed:
       LiveComposite((1090, 818),(0,0), "sprite noelleDefault",(0,0), "sprite noelleAnnoyed1")
image sideSprite1 noelleAnnoyed:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((320, 50, sideImageWidth, sideImageHeight2), "sprite noelleAnnoyed"))
image sideSprite2 noelleAnnoyed:
    "sideSprite1 noelleAnnoyed"


image sprite noelleShocked:
    LiveComposite((1090, 818),(0,0), "sprite noelleDefault",(0,0), "sprite noelleShocked1")
image sideSprite1 noelleShocked:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((320, 50, sideImageWidth, sideImageHeight2), "sprite noelleShocked"))
image sideSprite2 noelleShocked:
    "sideSprite1 noelleShocked"


image sprite noelleSurprised:
       LiveComposite((1090, 818),(0,0), "sprite noelleDefault",(0,0), "sprite noelleSurprised1")
image sideSprite1 noelleSurprised:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((320, 50, sideImageWidth, sideImageHeight2), "sprite noelleSurprised"))
image sideSprite2 noelleSurprised:
    "sideSprite1 noelleSurprised"

image sprite noelleHm:
       LiveComposite((1090, 818),(0,0), "sprite noelleDefault",(0,0), "sprite noelleHm1")
image sideSprite1 noelleHm:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((320, 50, sideImageWidth, sideImageHeight2), "sprite noelleHm"))
image sideSprite2 noelleHm:
    "sideSprite1 noelleHm"

image sprite noelleWorried:
       LiveComposite((1090, 818),(0,0), "sprite noelleDefault",(0,0), "sprite noelleWorried1")
image sideSprite1 noelleWorried:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((320, 50, sideImageWidth, sideImageHeight2), "sprite noelleWorried"))
image sideSprite2 noelleWorried:
    "sideSprite1 noelleWorried"

image sprite noelleWorriedAway:
       LiveComposite((1090, 818),(0,0), "sprite noelleDefault",(0,0), "sprite noelleWorriedAway1")
image sideSprite1 noelleWorriedAway:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((320, 50, sideImageWidth, sideImageHeight2), "sprite noelleWorriedAway"))
image sideSprite2 noelleWorriedAway:
    "sideSprite1 noelleWorriedAway"


image sprite noelleNeutralB:
    LiveComposite((1090, 818),(0,0), "sprite noelleBaseball",(0,0), "sprite noelleNeutral1",(0,0), "sprite noelleHat" )
image sideSprite1 noelleNeutralB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((320, 50, sideImageWidth, sideImageHeight2), "sprite noelleNeutralB"))
image sideSprite2 noelleNeutralB:
    "sideSprite1 noelleNeutralB"

image sprite noelleUhB:
    LiveComposite((1090, 818),(0,0), "sprite noelleBaseball",(0,0), "sprite noelleUh1",(0,0), "sprite noelleHat" )
image sideSprite1 noelleUhB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((320, 50, sideImageWidth, sideImageHeight2), "sprite noelleUhB"))
image sideSprite2 noelleUhB:
    "sideSprite1 noelleUhB"

image sprite noelleBigSmileB:
    LiveComposite((1090, 818),(0,0), "sprite noelleBaseball",(0,0), "sprite noelleBigSmile1",(0,0), "sprite noelleHat" )
image sideSprite1 noelleBigSmileB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((320, 50, sideImageWidth, sideImageHeight2), "sprite noelleBigSmileB"))
image sideSprite2 noelleBigSmileB:
    "sideSprite1 noelleBigSmileB"

image sprite noelleTsunB:

    LiveComposite((1090, 818),(0,0), "sprite noelleBaseball",(0,0), "sprite noelleTsun1",(0,0), "sprite noelleHat" )
image sideSprite1 noelleTsunB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((320, 50, sideImageWidth, sideImageHeight2), "sprite noelleTsunB"))
image sideSprite2 noelleTsunB:
    "sideSprite1 noelleTsunB"

#image sprite noelleFacepalmB:
 #   "sprite noelleFacepalmB1"
image sideSprite1 noelleFacepalmB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((300, 50, sideImageWidth, sideImageHeight2), "sprite noelleFacepalmB"))
image sideSprite2 noelleFacepalmB:
    "sideSprite1 noelleFacepalmB"

image sprite noelleAwayB:
   LiveComposite((1090, 818),(0,0), "sprite noelleBaseball",(0,0), "sprite noelleAway1",(0,0), "sprite noelleHat" )
image sideSprite1 noelleAwayB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((320, 50, sideImageWidth, sideImageHeight2), "sprite noelleAwayB"))
image sideSprite2 noelleAwayB:
    "sideSprite1 noelleAwayB"

image sprite noelleHappyB:
    LiveComposite((1090, 818),(0,0), "sprite noelleBaseball",(0,0), "sprite noelleHappy1",(0,0), "sprite noelleHat" )
image sideSprite1 noelleHappyB:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((320, 50, sideImageWidth, sideImageHeight2), "sprite noelleHappyB"))
image sideSprite2 noelleHappyB:
    "sideSprite1 noelleHappyB"

image sprite noelleAnnoyedB:
       LiveComposite((1090, 818),(0,0), "sprite noelleBaseball",(0,0), "sprite noelleAnnoyed1",(0,0), "sprite noelleHat" )
image sideSprite1 noelleAnnoyedB:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((320, 50, sideImageWidth, sideImageHeight2), "sprite noelleAnnoyedB"))
image sideSprite2 noelleAnnoyedB:
    "sideSprite1 noelleAnnoyedB"


image sprite noelleShockedB:
    LiveComposite((1090, 818),(0,0), "sprite noelleBaseball",(0,0), "sprite noelleShocked1",(0,0), "sprite noelleHat" )
image sideSprite1 noelleShockedB:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((320, 50, sideImageWidth, sideImageHeight2), "sprite noelleShockedB"))
image sideSprite2 noelleShockedB:
    "sideSprite1 noelleShockedB"


image sprite noelleSurprisedB:
       LiveComposite((1090, 818),(0,0), "sprite noelleBaseball",(0,0), "sprite noelleSurprised1",(0,0), "sprite noelleHat" )
image sideSprite1 noelleSurprisedB:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((320, 50, sideImageWidth, sideImageHeight2), "sprite noelleSurprisedB"))
image sideSprite2 noelleSurprisedB:
    "sideSprite1 noelleSurprisedB"

image sprite noelleHmB:
       LiveComposite((1090, 818),(0,0), "sprite noelleBaseball",(0,0), "sprite noelleHm1",(0,0), "sprite noelleHat" )
image sideSprite1 noelleHmB:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((320, 50, sideImageWidth, sideImageHeight2), "sprite noelleHmB"))
image sideSprite2 noelleHmB:
    "sideSprite1 noelleHmB"

image sprite noelleWorriedB:
       LiveComposite((1090, 818),(0,0), "sprite noelleBaseball",(0,0), "sprite noelleWorried1",(0,0), "sprite noelleHat" )
image sideSprite1 noelleWorriedB:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((320, 50, sideImageWidth, sideImageHeight2), "sprite noelleWorriedB"))
image sideSprite2 noelleWorriedB:
    "sideSprite1 noelleWorriedB"
image sprite noelleWorriedAwayB:
       LiveComposite((1090, 818),(0,0), "sprite noelleBaseball",(0,0), "sprite noelleWorriedAway1",(0,0), "sprite noelleHat" )
image sideSprite1 noelleWorriedAwayB:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((320, 50, sideImageWidth, sideImageHeight2), "sprite noelleWorriedAwayB"))
image sideSprite2 noelleWorriedAwayB:
    "sideSprite1 noelleWorriedAwayB"



image sprite yNoelleNeutral:
    "sprite yNoelleNeutral1"
    zoom 1.05
image sideSprite1 yNoelleNeutral:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((345, 50, sideImageWidth, sideImageHeight2), "sprite yNoelleNeutral"))
image sideSprite2 yNoelleNeutral:
    "sideSprite1 yNoelleNeutral"


image sprite yNoelleUh:
    "sprite yNoelleUh1"
    zoom 1.05
image sideSprite1 yNoelleUh:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((345, 50, sideImageWidth, sideImageHeight2), "sprite yNoelleUh"))
image sideSprite2 yNoelleUh:
    "sideSprite1 yNoelleUh"

image sprite yNoelleWorried:
    "sprite yNoelleWorried1"
    zoom 1.05
image sideSprite1 yNoelleWorried:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((345, 50, sideImageWidth, sideImageHeight2), "sprite yNoelleWorried"))
image sideSprite2 yNoelleWorried:
    "sideSprite1 yNoelleWorried"

image sprite yNoelleWorriedAway:
    "sprite yNoelleWorriedAway1"
    zoom 1.05
image sideSprite1 yNoelleWorriedAway:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((345, 50, sideImageWidth, sideImageHeight2), "sprite yNoelleWorriedAway"))
image sideSprite2 yNoelleWorriedAway:
    "sideSprite1 yNoelleWorriedAway"

image sprite yNoelleShocked:
    "sprite yNoelleShocked1"
    zoom 1.05
image sideSprite1 yNoelleShocked:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((345, 50, sideImageWidth, sideImageHeight2), "sprite yNoelleShocked"))
image sideSprite2 yNoelleShocked:
    "sideSprite1 yNoelleShocked"

image sprite yNoelleHappy:
    "sprite yNoelleHappy1"
    zoom 1.05
image sideSprite1 yNoelleHappy:
    LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((345, 50, sideImageWidth, sideImageHeight2), "sprite yNoelleHappy"))
image sideSprite2 yNoelleHappy:
    "sideSprite1 yNoelleHappy"

image sprite yNoelleAnnoyed:
    "sprite yNoelleAnnoyed1"
    zoom 1.05
image sideSprite1 yNoelleAnnoyed:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((345, 50, sideImageWidth, sideImageHeight2), "sprite yNoelleAnnoyed"))
image sideSprite2 yNoelleAnnoyed:
    "sideSprite1 yNoelleAnnoyed"

image sprite yNoelleBigSmile:
    "sprite yNoelleBigSmile1"
    zoom 1.05
image sideSprite1 yNoelleBigSmile:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((345, 50, sideImageWidth, sideImageHeight2), "sprite yNoelleBigSmile"))
image sideSprite2 yNoelleBigSmile:
    "sideSprite1 yNoelleBigSmile"

image sprite yNoelleTsun:
    "sprite yNoelleTsun1"
    zoom 1.05
image sideSprite1 yNoelleTsun:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((345, 50, sideImageWidth, sideImageHeight2), "sprite yNoelleTsun"))
image sideSprite2 yNoelleTsun:
    "sideSprite1 yNoelleTsun"

image sprite yNoelleAway:
    "sprite yNoelleAway1"
    zoom 1.05
image sideSprite1 yNoelleAway:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((345, 50, sideImageWidth, sideImageHeight2), "sprite yNoelleAway"))
image sideSprite2 yNoelleAway:
    "sideSprite1 yNoelleAway"


image sprite yNoelleHm:
    "sprite yNoelleHm1"
    zoom 1.05
image sideSprite1 yNoelleHm:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((345, 50, sideImageWidth, sideImageHeight2), "sprite yNoelleHm"))
image sideSprite2 yNoelleHm:
    "sideSprite1 yNoelleHm"

image sprite chryssaNeutral:
    LiveComposite((898, 818),(0,0), "sprite chryssaDefault",(0,0), "sprite chryssaNeutral1")
image sideSprite1 chryssaNeutral:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((320, 50, sideImageWidth, sideImageHeight2), "sprite chryssaNeutral"))

image sideSprite2 chryssaNeutral:
    "sideSprite1 chryssaNeutral"

image sprite chryssaAnnoyedSmile:
    LiveComposite((898, 818),(0,0), "sprite chryssaDefault",(0,0), "sprite chryssaAnnoyedSmile1")
image sideSprite1 chryssaAnnoyedSmile:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((210, 0, sideImageWidth, sideImageHeight2), "sprite chryssaAnnoyedSmile"))
image sideSprite2 chryssaAnnoyedSmile:
    "sideSprite1 chryssaAnnoyedSmile"

image sprite chryssaHappy:
    LiveComposite((898, 818),(0,0), "sprite chryssaDefault",(0,0), "sprite chryssaHappy1")
image sideSprite1 chryssaHappy:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((210, 0, sideImageWidth, sideImageHeight2), "sprite chryssaHappy"))
image sideSprite2 chryssaHappy:
    "sideSprite1 chryssaHappy"

image sprite chryssaAnnoyed:
    LiveComposite((898, 818),(0,0), "sprite chryssaDefault",(0,0), "sprite chryssaAnnoyed1")
image sideSprite1 chryssaAnnoyed:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((210, 0, sideImageWidth, sideImageHeight2), "sprite chryssaAnnoyed"))
image sideSprite2 chryssaAnnoyed:
    "sideSprite1 chryssaAnnoyed"

image sprite chryssaShocked:
   LiveComposite((898, 818),(0,0), "sprite chryssaDefault",(0,0), "sprite chryssaShock1")
image sideSprite1 chryssaShocked:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((210, 0, sideImageWidth, sideImageHeight2), "sprite chryssaShocked"))
image sideSprite2 chryssaShocked:
    "sideSprite1 chryssaShocked"

image sprite chryssaNeutralB:
    LiveComposite((898, 818),(0,0), "sprite chryssaBaseball",(0,0), "sprite chryssaNeutral1")
image sideSprite1 chryssaNeutralB:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((210, 0, sideImageWidth, sideImageHeight2), "sprite chryssaNeutralB"))

image sideSprite2 chryssaNeutralB:
    "sideSprite1 chryssaNeutralB"

image sprite chryssaAnnoyedSmileB:
    LiveComposite((898, 818),(0,0), "sprite chryssaBaseball",(0,0), "sprite chryssaAnnoyedSmile1")
image sideSprite1 chryssaAnnoyedSmileB:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((210, 0, sideImageWidth, sideImageHeight2), "sprite chryssaAnnoyedSmileB"))
image sideSprite2 chryssaAnnoyedSmileB:
    "sideSprite1 chryssaAnnoyedSmileB"

image sprite chryssaHappyB:
    LiveComposite((898, 818),(0,0), "sprite chryssaBaseball",(0,0), "sprite chryssaHappy1")
image sideSprite1 chryssaHappyB:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((210, 0, sideImageWidth, sideImageHeight2), "sprite chryssaHappyB"))
image sideSprite2 chryssaHappyB:
    "sideSprite1 chryssaHappyB"

image sprite chryssaAnnoyedB:
    LiveComposite((898, 818),(0,0), "sprite chryssaBaseball",(0,0), "sprite chryssaAnnoyed1")
image sideSprite1 chryssaAnnoyedB:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((210, 0, sideImageWidth, sideImageHeight2), "sprite chryssaAnnoyedB"))
image sideSprite2 chryssaAnnoyedB:
    "sideSprite1 chryssaAnnoyedB"

image sprite chryssaShockedB:
   LiveComposite((898, 818),(0,0), "sprite chryssaBaseball",(0,0), "sprite chryssaShock1")
image sideSprite1 chryssaShockedB:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((210, 0, sideImageWidth, sideImageHeight2), "sprite chryssaShockedB"))
image sideSprite2 chryssaShockedB:
    "sideSprite1 chryssaShockedB"

image sprite esterNeutral:
    LiveComposite((898, 818),(0,0), "sprite esterDefault",(0,0), "sprite esterNeutral1")
image sideSprite1 esterNeutral:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((250, 50, sideImageWidth, sideImageHeight2), "sprite esterNeutral"))
image sideSprite2 esterNeutral:
    "sideSprite1 esterNeutral"

image sprite esterAnnoyed:
    LiveComposite((898, 818),(0,0), "sprite esterDefault",(0,0), "sprite esterAnnoyed1")
image sideSprite1 esterAnnoyed:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((250, 50, sideImageWidth, sideImageHeight2), "sprite esterAnnoyed"))
image sideSprite2 esterAnnoyed:
    "sideSprite1 esterAnnoyed"


image sprite esterNeutralB:
    LiveComposite((898, 818),(0,0), "sprite esterBaseball",(0,0), "sprite esterNeutral1")
image sideSprite1 esterNeutralB:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((250, 50, sideImageWidth, sideImageHeight2), "sprite esterNeutralB"))
image sideSprite2 esterNeutralB:
    "sideSprite1 esterNeutralB"

image sprite esterAnnoyedB:
    LiveComposite((898, 818),(0,0), "sprite esterBaseball",(0,0), "sprite esterAnnoyed1")
image sideSprite1 esterAnnoyedB:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((250, 50, sideImageWidth, sideImageHeight2), "sprite esterAnnoyedB"))
image sideSprite2 esterAnnoyedB:
    "sideSprite1 esterAnnoyedB"

image sprite graceNeutral:
    "sprite graceNeutral1"
image sideSprite1 graceNeutral:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((230, 50, sideImageWidth, sideImageHeight2), "sprite graceNeutral"))
image sideSprite2 graceNeutral:
    "sideSprite1 graceNeutral"

image sprite graceBaseball:
    "sprite graceBaseball1"
image sideSprite1 graceBaseball:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((230, 50, sideImageWidth, sideImageHeight2), "sprite graceBaseball"))
image sideSprite2 graceBaseball:
    "sideSprite1 graceBaseball"

image sprite sumiNeutral:
    "sprite sumiNeutral1"
image sideSprite1 sumiNeutral:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((240, 20, sideImageWidth, sideImageHeight2), "sprite sumiNeutral"))
image sideSprite2 sumiNeutral:
    "sideSprite1 sumiNeutral"

image sprite sumiBaseball:
    "sprite sumiBaseball1"
image sideSprite1 sumiBaseball:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((240, 20, sideImageWidth, sideImageHeight2), "sprite sumiBaseball"))
image sideSprite2 sumiBaseball:
    "sideSprite1 sumiBaseball"

image sideSprite1 dad:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((240, 20, sideImageWidth, sideImageHeight2), "sprite dad"))
image sideSprite2 dad:

    "sideSprite1 dad"
image sideSprite1 mom:
        LiveComposite((354, 205),(0, 96), "sidebox.png",(0,0), LiveCrop((220, 20, sideImageWidth, sideImageHeight2), "sprite mom"))
image sideSprite2 mom:
    "sideSprite1 mom"

init python:

#############Setting default bg pan to ON ###############
    if persistent.bgPan is None:
        persistent.bgPan=True

#############Setting default screenshake to ON ##############
    if persistent.screenshake is None:
        persistent.screenshake=True

##########Adding Multipersistent Variables for Butterfly Soup 2
    mp = MultiPersistent("butterflySoup.renpy.org")

    def rtlConfig(rtlState):
        if rtlState:
            renpy.config.rtl = True
        else:
            renpy.config.rtl = False

########Shows the version number)#########
#    versionNumber="Butterfly Soup Demo 1.0"
#    def showVersionNumber():
#        ui.vbox(xalign=0.90, yalign=0.96, clipping=False)
#        ui.text(versionNumber, size=16, color="#fff", font="arial.ttf")
#        ui.close()
#    config.overlay_functions.append(versionNumber)

 ########Shows the yellow subtitle text as UI Text (so it goes above everything else)#########
    subtitle=""
    def showSubtitle():
        ui.vbox(xalign=0.5, yalign=0.96, clipping=False)
        ui.text(subtitle, style = 'subtitle', size=33, color="#FFFF00", outlines = [(2, "#000000", 0, 0)])
        ui.close()
    config.overlay_functions.append(showSubtitle)

    #Shows the bar image that blocks the scrollbar until it's reached the point where you can actually use it
    blockBar=True
#    def showScrollbarBlock():
#        if blockBar==True:
#            ui.vbox(xalign=0.5, yalign=1.0, clipping=False)
#            ui.image("images/scrollbarBlock.png")
#            ui.close()
#    config.overlay_functions.append(showScrollbarBlock)

######ALLOWS > TO TRANSITION CORRECTLY###########
    ewc = Character(None)

    def my_empty_window():
         ewc("",interact=False)

    config.empty_window = my_empty_window




############SHAKER#################
    class Shaker(object):

        anchors = {
            'top' : 0.0,
            'center' : 0.5,
            'bottom' : 1.0,
            'left' : 0.0,
            'right' : 1.0,
            }

        def __init__(self, start, child, dist):
            if start is None:
                start = child.get_placement()
            #
            self.start = [ self.anchors.get(i, i) for i in start ]  # central position
            self.dist = dist    # maximum distance, in pixels, from the starting point
            self.child = child

        def __call__(self, t, sizes):
            # Float to integer...  turns floating point numbers to
            # integers.
            def fti(x, r):
                if x is None:
                    x = 0
                if isinstance(x, float):
                    return int(x * r)
                else:
                    return x

            xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

            xpos = xpos - xanchor
            ypos = ypos - yanchor

            nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

            return (int(nx), int(ny), 0, 0)

    def _Shake(start, time, child=None, dist=100.0, **properties):

        move = Shaker(start, child, dist=dist)
        if persistent.screenshake is False:
            move = Shaker(start, child, dist=0)

        return renpy.display.layout.Motion(move,
                      time,
                      child,
                      add_sizes=True,
                      **properties)

    Shake = renpy.curry(_Shake)

#############SPLASH SCREEN################
label splashscreen:
    if not persistent.language_selected:
        $renpy.change_language ("japanese") #This just makes the text align more neatly in the choice
        $menuStyle="language"
        scene black
        menu:
            "{font=YunusH.ttf}{size=36}English{/size}{/font}":
                $renpy.change_language (None)
            "{font=traditional_chinese.ttf}中文{/font}":
                $renpy.change_language ("traditional_chinese")
            "{font=myriad.OTF}Português{/font}":
                $renpy.change_language ("brazilian_portuguese")
            "{font=myriad.OTF}Česky{/font}":
                $renpy.change_language ("czech")
            "{font=japanese.ttc}日本語{/font}":
                $renpy.change_language ("japanese")
            "{font=Binggrae.otf}한국어{/font}":
                $renpy.change_language ("korean")
            "{font=myriad.OTF}Polski{/font}":
                $renpy.change_language ("polish")
            "{font=times.ttf}فارسی{/font}":
                $renpy.change_language ("farsi")
            "{font=myriad.OTF}bahasa Indonesia{/font}":
                $renpy.change_language ("indonesian")
            "{font=YunusH.ttf}{size=36}Français{/size}{/font}":
                $renpy.change_language ("french")
        $ persistent.language_selected = True
        $menuStyle="normal"

    $renpy.config.rtl = True

init:
    $ sshake = Shake((0, 0, 0, 0), 0.5, dist=15)
    $ bigShake = Shake ((0, 0, 0, 0), 0.75, dist=15)

    $menuStyle="normal"

    $diyaChatName=_("Diya")
    $minChatName=_("Min")
    $noelleChatName=_("Noelle")
    $akarshaChatName=_("YAOI SEME")
    $akarshaChatName2=_("NOELLEFUCKER69")
    $akarshaChatName3=_("albret einstong")
    $graceChatName=_("Yuki")
    $sumiChatName=_("Sakura")
    $chryssaChatName=_("Chryssa")
    $lizChatName=_("Liz")

    $textChoice=False
    $tt_ypos=0.9
    $blackScreen=True
    $newSpeaker=True
    $centeredMenu=False


    $ config.tag_layer = {'sprite' : 'back', 'bg' : 'farBack', 'prop' : 'farBack','sideSprite1' : 'screens', 'sideSprite2' : 'screens'}
    $ config.tag_transform = {'sprite' : spriteTransform, 'bg' : bgTransform, 'circle' : bgTransform,'screens' : bgTransform, 'prop' : bgTransform, 'sideSprite1' : sideSprite1, 'sideSprite2' : sideSprite2}


image chTitle = ParameterizedText(style='chTitle',xalign=0.5, yalign=0.5, color="#fff" )
image chTitleSmall = ParameterizedText(style='chTitle', xalign=0.5, yalign=0.5, color="#fff", size=90)
image credit = ParameterizedText(style='chTitle', xalign=0.5, yalign=0.5, color="#f89fe2", size=80)
image creditSmall = ParameterizedText(style='creditSmall', xanchor=0, yanchor=0, xpos=220, ypos=160, color="#f89fe2")
image creditSmall2 = ParameterizedText(style='creditSmall', xanchor=0, yanchor=0, xpos=320, ypos=260, color="#f89fe2")

image creditWhite = ParameterizedText(style='chTitle',xalign=0.5, yalign=0.5, color="#fff", size=80)

define persistent.ending1 = False

define narrator = Character(None,ctc="ctc_fixed",ctc_position="fixed"  )
define Diya = DynamicCharacter('diyaName', callback=clicks,cb_char=3 ,image="sprite", ctc="ctc_fixed",ctc_position="fixed")
define Min= DynamicCharacter('minName', callback=clicks,cb_char=2,image="sprite", ctc="ctc_fixed",ctc_position="fixed")


define DiyaT = DynamicCharacter('diyaName', image="sprite", callback=clicks,cb_char=3,ctc="ctc_fixed",what_prefix="{blue}(",what_suffix="){/blue}", ctc_position="fixed")
define NoelleT = DynamicCharacter('noelleName', callback=clicks,cb_char=4 ,image="sprite", ctc="ctc_fixed", what_prefix="{blue}(",what_suffix="){/blue}", ctc_position="fixed")
define AkarshaT = DynamicCharacter('akarshaName', callback=clicks,cb_char=1, image="sprite", ctc="ctc_fixed", what_prefix="{blue}(",what_suffix="){/blue}", ctc_position="fixed")
define MinT = DynamicCharacter('minName', callback=clicks,cb_char=2, image="sprite", ctc="ctc_fixed", what_prefix="{blue}(",what_suffix="){/blue}", ctc_position="fixed")

define Akarsha=DynamicCharacter('akarshaName',callback=clicks,cb_char=1, image="sprite", ctc="ctc_fixed",ctc_position="fixed")
define Noelle= DynamicCharacter('noelleName', callback=clicks,cb_char=4,image="sprite", ctc="ctc_fixed",ctc_position="fixed")

define Chryssa=DynamicCharacter('chryssaName', callback=clicks,cb_char=1,image="sprite", ctc="ctc_fixed",ctc_position="fixed")
define Liz= DynamicCharacter('lizName', callback=clicks,cb_char=2,image="sprite", ctc="ctc_fixed",ctc_position="fixed")
define Ester=DynamicCharacter('esterName', callback=clicks,cb_char=1,image="sprite", ctc="ctc_fixed",ctc_position="fixed")
define Grace= DynamicCharacter('graceName', callback=clicks,cb_char=2,image="sprite", ctc="ctc_fixed",ctc_position="fixed")
define Sumi = DynamicCharacter('sumiName', callback=clicks,cb_char=1,image="sprite", ctc="ctc_fixed",ctc_position="fixed")

define Mom=DynamicCharacter('momName', callback=clicks,cb_char=2,image="sprite", ctc="ctc_fixed",ctc_position="fixed")
define Dad=DynamicCharacter('dadName', callback=clicks,cb_char=4,image="sprite", ctc="ctc_fixed",ctc_position="fixed")

define NPC = DynamicCharacter('npcName', callback=clicks,cb_char=4,image="sprite", ctc="ctc_fixed",ctc_position="fixed")
define NPC2 = DynamicCharacter('npcName2',callback=clicks,cb_char=2, image="sprite", ctc="ctc_fixed",ctc_position="fixed")

define Jun = DynamicCharacter('junName',callback=clicks,cb_char=6, image="sprite", ctc="ctc_fixed",ctc_position="fixed")
define Hayden = DynamicCharacter('haydenName',callback=clicks,cb_char=4,image="sprite", ctc="ctc_fixed",ctc_position="fixed")
define Boy = DynamicCharacter('boyName',callback=clicks,cb_char=4,image="sprite", ctc="ctc_fixed",ctc_position="fixed")

define cDiya = DynamicCharacter('diyaChatName', kind=nvl, callback=gChat,what_suffix="{fast}",what_style="gChatBlack", who_style="gChatName")

define cMin =  DynamicCharacter('minChatName', kind=nvl, callback=gChat,what_suffix="{fast}",what_style="gChatBlack", who_style="gChatName")

define cNoelle =  DynamicCharacter('noelleChatName', kind=nvl, callback=gChat,what_suffix="{fast}",what_style="gChatBlack", who_style="gChatName")
define cAkarsha = DynamicCharacter('akarshaChatName', kind=nvl, callback=gChat, what_suffix="{fast}",what_style="gChatBlack", who_style="gChatName")
define cAkarsha2 = DynamicCharacter('akarshaChatName2', kind=nvl, callback=gChat, what_suffix="{fast}",what_style="gChatBlack", who_style="gChatName")

define cAkarsha3 = DynamicCharacter('akarshaChatName3', kind=nvl, callback=gChat, what_suffix="{fast}",what_style="gChatBlack", who_style="gChatName")


define cChryssa =  DynamicCharacter('chryssaChatName', kind=nvl, callback=gChat,what_suffix="{fast}",what_style="gChatBlack", who_style="gChatName")
define cLiz =  DynamicCharacter('lizChatName', kind=nvl, callback=gChat,what_suffix="{fast}",what_style="gChatBlack", who_style="gChatName")
define cGrace =  DynamicCharacter('graceChatName', kind=nvl, callback=gChat,what_suffix="{fast}",what_style="gChatBlack", who_style="gChatName")
define cSumi =  DynamicCharacter('sumiChatName', kind=nvl, callback=gChat,what_suffix="{fast}",what_style="gChatBlack", who_style="gChatName")


define cSame =  Character (None, kind=nvl, callback=gChat,what_suffix="{fast}",what_style="gChatBlack", who_style="gChatName")

define cNarrator = Character("", kind=nvl, what_style="gChatGrey", what_suffix="{fast}")
define cFirstLine = Character(None, kind=nvl, what_style="firstLine")
