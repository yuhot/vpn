from GENERATOR import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from gtts import gTTS
from googletrans import Translator
from multiprocessing import Pool, Process
from ffmpy import FFmpeg
import time, random, asyncio, timeit, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, urllib, urllib.parse, ast, pytz, wikipedia, pafy, youtube_dl, atexit

cl = RIDEN()
#cl = RIDEN(authTokenRFU="EwBKIgTRxi6XboYagtR9.01eD1U2qXh8Zi0WWzaO7Yq.07GM1gYdN6itN5dsjOLCqDODoslXZf7ournf48ej/VA=")
cl.log("YOUR TOKEN : {}".format(str(cl.authToken)))
channel = RIDENChannel(cl,cl.server.CHANNEL_ID['LINE_TIMELINE'])
cl.log("CHANNEL TOKEN : " + str(channel.getChannelResult()))

riden1 = RIDEN()
#riden1 = RIDEN(authTokenRFU="EwuT4sRvmF3U6yLO8blf.a1QVT/QlosuRjiHwpVX5VW.H1Eu3ua4cA3DckQ7jp6Xk0bCL1E8HSfyKvauTJx4qSM=")
riden1.log("YOUR TOKEN : {}".format(str(riden1.authToken)))
channel = RIDENChannel(riden1,riden1.server.CHANNEL_ID['LINE_TIMELINE'])
riden1.log("CHANNEL TOKEN : " + str(channel.getChannelResult()))

#riden2 = RIDEN()
#riden2 = RIDEN(authTokenRFU="EwYRdytxSIqQYb1FuAN6.WKcub2t+uJueUYfdC1qAbG.kcuE5u3klvfwd1IYM+zs5xkxbo3+pIsLrjZ/Um1ti5U=")
#riden2.log("YOUR TOKEN : {}".format(str(riden2.authToken)))
#channel = RIDENChannel(riden2,riden2.server.CHANNEL_ID['LINE_TIMELINE'])
#riden2.log("CHANNEL TOKEN : " + str(channel.getChannelResult()))

#riden3 = RIDEN()
#riden3 = RIDEN(authTokenRFU="EwzQfNY5yaHg3Rs3OIy9.WrtAVyZDRBvprHExwvnXkq.5lj592fbau7e3dxelya1Ih8v9FHQpCe09CU7Jrf66xU=")
#riden3.log("YOUR TOKEN : {}".format(str(riden3.authToken)))
#channel = RIDENChannel(riden3,riden3.server.CHANNEL_ID['LINE_TIMELINE'])
#riden3.log("CHANNEL TOKEN : " + str(channel.getChannelResult()))

#riden4 = RIDEN()
#riden4 = RIDEN(authTokenRFU="EwPYN0FSJU0JDHi4hWl6.uEr21FsOaeuLSWAmhT6MLG.GUW49h6Z9j04PmS0EyEtIqOAFQkTkAwAcJ/DRgND10M=")
#riden4.log("YOUR TOKEN : {}".format(str(riden4.authToken)))
#channel = RIDENChannel(riden4,riden4.server.CHANNEL_ID['LINE_TIMELINE'])
#riden4.log("CHANNEL TOKEN : " + str(channel.getChannelResult()))

#riden5 = RIDEN()
#riden5 = RIDEN(authTokenRFU="EwbrWv7qWM8v94CdUyK5.Sz2c6sOTITJoE7jUS5iGXq.FDG0JGe4PkMZwquZtC2ht1esMg7CC++qcFyPlMYSr/Q=")
#riden5.log("YOUR TOKEN : {}".format(str(riden5.authToken)))
#channel = RIDENChannel(riden5,riden5.server.CHANNEL_ID['LINE_TIMELINE'])
#riden5.log("CHANNEL TOKEN : " + str(channel.getChannelResult()))

#riden6 = RIDEN()
#riden6 = RIDEN(authTokenRFU="EwzQtRP0ncBWcdjdpjg5.u+xXLFQSlbSB6sUpVT4zzq.772R8hojuD36MeWapgIUQnCMyOKAUEpCa7I5wcJQ6zE=")
#riden6.log("YOUR TOKEN : {}".format(str(riden6.authToken)))
#channel = RIDENChannel(riden6,riden6.server.CHANNEL_ID['LINE_TIMELINE'])
#riden6.log("CHANNEL TOKEN : " + str(channel.getChannelResult()))

#riden7 = RIDEN()
#riden7 = RIDEN(authTokenRFU="EwkYEgwbk6VUfHK5Tewf.SRsUzuDklMrk69jt3WvkhW.jigL8Rxr9t6I/fpBkf1cEjg1DolBqhezX8k8vpsPnQs=")
#riden7.log("YOUR TOKEN : {}".format(str(riden7.authToken)))
#channel = RIDENChannel(riden7,riden7.server.CHANNEL_ID['LINE_TIMELINE'])
#riden7.log("CHANNEL TOKEN : " + str(channel.getChannelResult()))

#riden8 = RIDEN()
#riden8 = RIDEN(authTokenRFU="Ew91coutN2nBG5cihRI3.NFnOcElHuDdTQG5zISlFKW.jiFt9BmKDxIShf6PHAtaRgJxLsawVmpLvLoCTggJZyw=")
#riden8.log("YOUR TOKEN : {}".format(str(riden8.authToken)))
#channel = RIDENChannel(riden8,riden8.server.CHANNEL_ID['LINE_TIMELINE'])
#riden8.log("CHANNEL TOKEN : " + str(channel.getChannelResult()))

#riden9 = RIDEN()
#riden9 = RIDEN(authTokenRFU="EwrFEPERf8My3Q9BdKac.XwGHfami0C6EGZ533rnqZa.3n1R+i5/pqpAFhMiHN52G0zxJ+9/Tlrtd0Zccz/K+Sc=")
#riden9.log("YOUR TOKEN : {}".format(str(riden9.authToken)))
#channel = RIDENChannel(riden9,riden9.server.CHANNEL_ID['LINE_TIMELINE'])
#riden9.log("CHANNEL TOKEN : " + str(channel.getChannelResult()))

#riden10 = RIDEN()
#riden10 = RIDEN(authTokenRFU="EwFZogXW3THy9KnwDRv5.4DANLenrmne5/CxD4zQP5q.pDWYzrGYkwh0ZakYaDNMdrUHm7iBrmLRNc1QPBl7Sbk=")
#riden10.log("YOUR TOKEN : {}".format(str(riden10.authToken)))
#channel = RIDENChannel(riden10,riden10.server.CHANNEL_ID['LINE_TIMELINE'])
#riden10.log("CHANNEL TOKEN : " + str(channel.getChannelResult()))

print ("BY:【YOU SELF BOT】")

clProfile = cl.getProfile()
clSettings = cl.getSettings()
RIDEN = RIDENPoll(cl)

Rfu = [cl,riden1]
mid = cl.profile.mid
JSMID1 = riden1.profile.mid
#JSMID2 = riden2.profile.mid
#JSMID3 = riden3.profile.mid
#JSMID4 = riden4.profile.mid
#JSMID5 = riden5.profile.mid
#JSMID6 = riden6.profile.mid
#JSMID7 = riden7.profile.mid
#JSMID8 = riden8.profile.mid
#JSMID9 = riden9.profile.mid
#JSMID10 = riden10.profile.mid
RfuBot=[mid,JSMID1]
Owner=["ud3511dd6ed90c47f33234c30640a3bc9"]
RfuSekawan = RfuBot + Rfu + Owner

contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

Squad = {
    "UnsendPesan":True,
    "SpamInvite":False,
    "Contact":False,
    "GName":"【YOU SELF BOT】",
    "AutoRespon":True,
    "KickRespon":False,
    "KillOn":False,
    "KickOn":True,
    "Upfoto":False,
    "UpfotoBot":False,
    "UpfotoGroup":False,
    "Steal":False,
    "Invite":False,
    "Copy":False,
    "autoAdd":True,
    "PesanAdd":"แอดทำไม มีไรว่ามา",
    "ContactAdd":{},
    "autoBlock":False,
    "autoJoin":True,
    "AutojoinTicket":True,
    "AutoReject":False,
    "autoRead":False,
    "IDSticker":False,
    "Timeline":False,
    "Welcome":True,
    "BackupBot":True,
    "WcText": "หวัดดีคร๊าบบ",
    "Leave":False,
    "WvText": "บายๆ บักหำ",
    "Mic":False,
    "MicDel":False,
    "Adminadd":False,
    "AdminDel":False,
    "Gift":False,
    "readMember":{},
    "readPoint":{},
    "readTime":{},
    "ROM":{},
    "Blacklist":{},
    "Ban":False,
    "Unban":False,
    "AddMention":True,
    "Admin": {
        "ud3511dd6ed90c47f33234c30640a3bc9","u035aafb7ea8b39252b2488563efc79bf":True,  #TARO MID ADMIN NYA DISINI
        "ud3511dd6ed90c47f33234c30640a3bc9":True
    },
}

Mozilla = {
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
    "mimic": {
        "copy": False,
        "conpp": False,
        "status": False,
        "target": {}
    }
}

setTime = {}
setTime = Squad['readTime']
mulai = time.time() 
msg_dict = {}

ProfileMe = {
    "displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
ProfileMe["displayName"] = clProfile.displayName
ProfileMe["statusMessage"] = clProfile.statusMessage
ProfileMe["pictureStatus"] = clProfile.pictureStatus

RfuProtect = {
    'protect':False,
    'linkprotect':False,
    'inviteprotect':False,
    'cancelprotect':False,
    'ProtectCancelled':False,
}

RfuCctv={
    "Point1":{},
    "Point2":{},
    "Point3":{}
}

Help ="""SELF BOT PYTHON 3 
╔════════════════╗
╠❂➣【YOU SELF BOT】 
╠════════════════╝
╠❂➣ คท
╠❂➣ ชื่อ
╠❂➣ ใครสร้างกลุ่ม
╠❂➣ คนในกลุ่ม
╠❂➣ เปิดจุด
╠❂➣ ปิดจุด
╠❂➣ สปีด
╠❂➣ เปิดแอบ
╠❂➣ ปิดแอบ
╠❂➣ แทค
╠❂➣ รีบอท
╠❂➣ ปิดบอท
╠❂➣ เตะ @
╠❂➣ เปิดมุดลิ้ง
╠❂➣ ปิดมุดลิ้ง
╠❂➣ มา
╠❂➣ ไป
╠❂➣ เตะเปิด
╠❂➣ เตะปิด
╠❂➣ เชคดำ
╠❂➣ ล้างดำ
╠❂➣ ลงดำคท
╠❂➣ เปิดลิ้ง
╠❂➣ ปิดลิ้ง
╚════════════════╝
By:【YOU SELF BOT】
""""________________________"

#------------------------------------------------ SCRIP DEF ----------------------------------------------------------#

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    month, days = divmod(days,30)
    year, month = divmod(month,12)
    century, year = divmod(year,100)
    return '\n%02d Abad\n%02d Tahun\n%02d Bulan\n%02d Hari\n%02d Jam\n%02d Menit\n%02d Detik' % (century, year, month, days, hours, mins, secs)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def RIDEN_FAST_USER(fast):
    try:
        if fast.type == 0:
            return
        if fast.type == 5:
            if Squad["autoAdd"] == True:
                if (Squad["PesanAdd"] in [""," ","\n",None]):
                    pass
                else:
                    Squad["ContactAdd"][fast.param2] = True
                    usr = cl.getContact(op.param2)
                    cl.sendMessage(fast.param1, "Haii {} " + str(Squad["PesanAdd"]).format(usr.displayName))
                    cl.sendMessage(fast.param1, None, contentMetadata={'mid':mid}, contentType=13)

        if fast.type == 5:
            if Squad['autoBlock'] == True:
                try:
                    usr = cl.getContact(op.param2)
                    cl.sendMessage(fast.param1, "Haii {} Sorry Auto Block , Komen di TL dulu ya kalo akun asli baru di unblock".format(usr.displayName))
                    cl.talk.blockContact(0, fast.param1)
                    Squad["Blacklist"][fast.param2] = True
                except Exception as e:
                	cl.log("[SEND_MESSAGE] ERROR : " + str(e))

#--------------------------------------------- PARAM SCRIP AUTO JOIN BOT & AUTO REJECT ------------------------------------------------#

        if fast.type == 13:
            if mid in fast.param3:
              if Squad['autoJoin'] == True:
                if fast.param2 in RfuSekawan and fast.param2 in Squad["Admin"]:
                    cl.acceptGroupInvitation(fast.param1)
                    print ("ANDA JOIN DI GRUP")
            if JSMID1 in fast.param3:
              if Squad['autoJoin'] == True:
                if fast.param2 in RfuSekawan and fast.param2 in Squad["Admin"]:
                    riden1.acceptGroupInvitation(fast.param1)
                    print ("BOT 1 JOIN GRUP")
            if JSMID2 in fast.param3:
              if Squad['autoJoin'] == True:
                if fast.param2 in RfuSekawan and fast.param2 in Squad["Admin"]:
                    riden2.acceptGroupInvitation(fast.param1)
                    print ("BOT 2 JOIN GRUP")
            if JSMID3 in fast.param3:
              if Squad['autoJoin'] == True:
                if fast.param2 in RfuSekawan and fast.param2 in Squad["Admin"]:
                    riden3.acceptGroupInvitation(fast.param1)
                    print ("BOT 3 JOIN GRUP")
            if JSMID4 in fast.param3:
              if Squad['autoJoin'] == True:
                if fast.param2 in RfuSekawan and fast.param2 in Squad["Admin"]:
                    riden4.acceptGroupInvitation(fast.param1)
                    print ("BOT 4 JOIN GRUP")
            if JSMID5 in fast.param3:
              if Squad['autoJoin'] == True:
                if fast.param2 in RfuSekawan and fast.param2 in Squad["Admin"]:
                    riden5.acceptGroupInvitation(fast.param1)
                    print ("BOT 5 JOIN GRUP")
            if JSMID6 in fast.param3:
              if Squad['autoJoin'] == True:
                if fast.param2 in RfuSekawan and fast.param2 in Squad["Admin"]:
                    riden6.acceptGroupInvitation(fast.param1)
                    print ("BOT 6 JOIN GRUP")
            if JSMID7 in fast.param3:
              if Squad['autoJoin'] == True:
                if fast.param2 in RfuSekawan and fast.param2 in Squad["Admin"]:
                    riden7.acceptGroupInvitation(fast.param1)
                    print ("BOT 7 JOIN GRUP")
            if JSMID8 in fast.param3:
              if Squad['autoJoin'] == True:
                if fast.param2 in RfuSekawan and fast.param2 in Squad["Admin"]:
                    riden8.acceptGroupInvitation(fast.param1)
                    print ("BOT 8 JOIN GRUP")
            if JSMID9 in fast.param3:
              if Squad['autoJoin'] == True:
                if fast.param2 in RfuSekawan and fast.param2 in Squad["Admin"]:
                    riden9.acceptGroupInvitation(fast.param1)
                    print ("BOT 9 JOIN GRUP")
            if JSMID10 in fast.param3:
              if Squad['autoJoin'] == True:
                if fast.param2 in RfuSekawan and fast.param2 in Squad["Admin"]:
                    riden10.acceptGroupInvitation(fast.param1)
                    print ("BOT 9 JOIN GRUP")
                    pass

        if fast.type == 13:
            if mid in fast.param3:
              if Squad['AutoReject'] == True:
                if fast.param2 not in RfuSekawan and fast.param2 not in Squad["Admin"]:
                    gid = cl.getGroupIdsInvited()
                    for i in gid:
                        cl.rejectGroupInvitation(i)
            if JSMID1 in fast.param3:
              if Squad["AutoReject"] == True:
                if fast.param2 not in RfuSekawan and fast.param2 not in Squad["Admin"]:
                    gid = riden1.getGroupIdsInvited()
                    for i in gid:
                        riden1.rejectGroupInvitation(i)
            if JSMID2 in fast.param3:
              if Squad["AutoReject"] == True:
                if fast.param2 not in RfuSekawan and fast.param2 not in Squad["Admin"]:
                    gid = riden2.getGroupIdsInvited()
                    for i in gid:
                        riden2.rejectGroupInvitation(i)
            if JSMID3 in fast.param3:
              if Squad["AutoReject"] == True:
                if fast.param2 not in RfuSekawan and fast.param2 not in Squad["Admin"]:
                    gid = riden3.getGroupIdsInvited()
                    for i in gid:
                        riden3.rejectGroupInvitation(i)
            if JSMID4 in fast.param3:
              if Squad["AutoReject"] == True:
                if fast.param2 not in RfuSekawan and fast.param2 not in Squad["Admin"]:
                    gid = riden4.getGroupIdsInvited()
                    for i in gid:
                        riden4.rejectGroupInvitation(i)
            if JSMID5 in fast.param3:
              if Squad["AutoReject"] == True:
                if fast.param2 not in RfuSekawan and fast.param2 not in Squad["Admin"]:
                    gid = riden5.getGroupIdsInvited()
                    for i in gid:
                        riden5.rejectGroupInvitation(i)
            if JSMID6 in fast.param3:
              if Squad["AutoReject"] == True:
                if fast.param2 not in RfuSekawan and fast.param2 not in Squad["Admin"]:
                    gid = riden6.getGroupIdsInvited()
                    for i in gid:
                        riden6.rejectGroupInvitation(i)
            if JSMID7 in fast.param3:
              if Squad["AutoReject"] == True:
                if fast.param2 not in RfuSekawan and fast.param2 not in Squad["Admin"]:
                    gid = riden7.getGroupIdsInvited()
                    for i in gid:
                        riden7.rejectGroupInvitation(i)
            if JSMID8 in fast.param3:
              if Squad["AutoReject"] == True:
                if fast.param2 not in RfuSekawan and fast.param2 not in Squad["Admin"]:
                    gid = riden8.getGroupIdsInvited()
                    for i in gid:
                        riden8.rejectGroupInvitation(i)
            if JSMID9 in fast.param3:
              if Squad["AutoReject"] == True:
                if fast.param2 not in RfuSekawan and fast.param2 not in Squad["Admin"]:
                    gid = riden9.getGroupIdsInvited()
                    for i in gid:
                        riden9.rejectGroupInvitation(i)
            if JSMID10 in fast.param3:
              if Squad["AutoReject"] == True:
                if fast.param2 not in RfuSekawan and fast.param2 not in Squad["Admin"]:
                    gid = riden10.getGroupIdsInvited()
                    for i in gid:
                        riden10.rejectGroupInvitation(i)
                        pass

#------------------- ( 1 ) ------------------------- PEMBATAS SCRIP SIDER & WC LV ------------------------------------------------#

        elif fast.type == 55:
            try:
                if RfuCctv['Point1'][fast.param1]==True:
                    if fast.param1 in RfuCctv['Point2']:  
                        Name = cl.getContact(fast.param2).displayName
                        if Name in RfuCctv['Point3'][fast.param1]:
                            pass
                        else:
                            RfuCctv['Point3'][fast.param1] += "\n~" + Name
                            if " " in Name:
                                nick = Name.split(' ')
                                if len(nick) == 2:
                                    cl.mentionWithRFU(fast.param1,fast.param2," Hii\n","" + "\n Nyimak yah kak?" )
                                else:
                                    cl.mentionWithRFU(fast.param1,fast.param2," Nah\n","" + "\n Nongol Sini Chat kak ??" )
                            else:
                                cl.mentionWithRFU(fast.param1,fast.param2," Hey\n","" + "\n What Are You Doing?" )
                    else:
                        pass
                else:
                    pass
            except:
                pass

        if fast.type == 55:
            try:
                if fast.param1 in Squad['readPoint']:
                    if fast.param2 in Squad['readMember'][fast.param1]:
                        pass
                    else:
                        Squad['readMember'][fast.param1] += fast.param2
                    Squad['ROM'][fast.param1][fast.param2] = fast.param2
                else:
                   pass
            except:
                pass   

        if fast.type == 17:
            if Squad["Welcome"] == True:
                if fast.param2 not in Rfu:
                    ginfo = cl.getGroup(fast.param1)
                    cl.mentionWithRFU(fast.param1,fast.param2," Hii","" + "\n " + str(Squad['WcText']))
                    cl.sendMessage(fast.param1, None, contentMetadata={'mid':fast.param2}, contentType=13)
                    print ("MEMBER HAS JOIN THE GROUP")

        if fast.type == 15:
            if Squad["Leave"] == True:
                if fast.param2 not in Rfu:
                    ginfo = cl.getGroup(fast.param1)
                    cl.mentionWithRFU(fast.param1,fast.param2," Hii","" + "\n " + str(Squad['LvText']))
                    cl.sendMessage(fast.param1, None, contentMetadata={'mid':fast.param2}, contentType=13)
                    print ("MEMBER HAS LEFT THE GROUP")

#--------------------------------------------- PARAM SCRIP FOR BACKUP BOT ------------------------------------------------#

        if fast.type == 19:
          if Squad["BackupBot"] == True:
            if mid in fast.param3:
              if fast.param2 in RfuBot:
                if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
                    pass
                else:
                    Squad["Blacklist"][fast.param2] = True
                    f=codecs.open('st2__b.json','w','utf-8')
                    json.dump(Squad, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        riden1.findAndAddContactsByMid(fast.param3)
                        riden1.kickoutFromGroup(fast.param1,[fast.param2])
                        riden1.inviteIntoGroup(fast.param1,[fast.param3])
                        cl.acceptGroupInvitation(fast.param1)
                    except:
                        try:
                            riden2.findAndAddContactsByMid(fast.param3)
                            riden2.kickoutFromGroup(fast.param1,[fast.param2])
                            riden2.inviteIntoGroup(fast.param1,[fast.param3])
                            cl.acceptGroupInvitation(fast.param1)
                        except:
                            try:
                                riden3.findAndAddContactsByMid(fast.param3)
                                riden3.kickoutFromGroup(fast.param1,[fast.param2])
                                riden3.inviteIntoGroup(fast.param1,[fast.param3])
                                cl.acceptGroupInvitation(fast.param1)
                            except:
                                try:
                                    x = riden1.getGroup(fast.param1)
                                    x.preventedJoinByTicket = False
                                    riden1.updateGroup(x)
                                    Riden = riden1.reissueGroupTicket(fast.param1)
                                    cl.acceptGroupInvitationByTicket(fast.param1,Riden)
                                    riden1.acceptGroupInvitationByTicket(fast.param1,Riden)
                                    riden2.acceptGroupInvitationByTicket(fast.param1,Riden)
                                    riden3.acceptGroupInvitationByTicket(fast.param1,Riden)
                                    x = cl.getGroup(fast.param1)
                                    x.preventedJoinByTicket = True
                                    cl.updateGroup(x)
                                    riden1.kickoutFromGroup(fast.param1,[fast.param2])
                                    Riden = cl.reissueGroupTicket(fast.param1)
                                except:
                                    pass
                return
            
            if JSMID1 in fast.param3:
              if fast.param2 in RfuBot:
                if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
                    pass
                else:
                    Squad["Blacklist"][fast.param2] = True
                    f=codecs.open('st2__b.json','w','utf-8')
                    json.dump(Squad, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        riden2.findAndAddContactsByMid(fast.param3)
                        riden2.kickoutFromGroup(fast.param1,[fast.param2])
                        riden2.inviteIntoGroup(fast.param1,[fast.param3])
                        riden1.acceptGroupInvitation(fast.param1)
                    except:
                        try:
                            riden3.findAndAddContactsByMid(fast.param3)
                            riden3.kickoutFromGroup(fast.param1,[fast.param2])
                            riden3.inviteIntoGroup(fast.param1,[fast.param3])
                            riden1.acceptGroupInvitation(fast.param1)
                        except:
                            try:
                                cl.findAndAddContactsByMid(fast.param3)
                                cl.kickoutFromGroup(fast.param1,[fast.param2])
                                cl.inviteIntoGroup(fast.param1,[fast.param3])
                                riden1.acceptGroupInvitation(fast.param1)
                            except:
                                try:
                                    x = riden2.getGroup(fast.param1)
                                    x.preventedJoinByTicket = False
                                    riden2.updateGroup(x)
                                    Riden = riden2.reissueGroupTicket(fast.param1)
                                    riden1.acceptGroupInvitationByTicket(fast.param1,Riden)
                                    x = riden1.getGroup(fast.param1)
                                    x.preventedJoinByTicket = True
                                    riden1.updateGroup(x)
                                    riden2.kickoutFromGroup(fast.param1,[fast.param2])
                                    Ticket = riden1.reissueGroupTicket(fast.param1)
                                except:
                                    pass
                return

            if JSMID2 in fast.param3:
              if fast.param2 in RfuBot:
                if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
                    pass
                else:
                    Squad["Blacklist"][fast.param2] = True
                    f=codecs.open('st2__b.json','w','utf-8')
                    json.dump(Squad, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        cl.findAndAddContactsByMid(fast.param3)
                        cl.kickoutFromGroup(fast.param1,[fast.param2])
                        cl.inviteIntoGroup(fast.param1,[fast.param3])
                        riden2.acceptGroupInvitation(fast.param1)
                    except:
                        try:
                            riden1.findAndAddContactsByMid(fast.param3)
                            riden1.kickoutFromGroup(fast.param1,[fast.param2])
                            riden1.inviteIntoGroup(fast.param1,[fast.param3])
                            riden2.acceptGroupInvitation(fast.param1)
                        except:
                            try:
                                riden3.findAndAddContactsByMid(fast.param3)
                                riden3.kickoutFromGroup(fast.param1,[fast.param2])
                                riden3.inviteIntoGroup(fast.param1,[fast.param3])
                                riden2.acceptGroupInvitation(fast.param1)
                            except:
                                try:
                                    x = cl.getGroup(fast.param1)
                                    x.preventedJoinByTicket = False
                                    cl.updateGroup(x)
                                    Riden = cl.reissueGroupTicket(fast.param1)
                                    riden2.acceptGroupInvitationByTicket(fast.param1,Riden)
                                    x = riden2.getGroup(fast.param1)
                                    x.preventedJoinByTicket = True
                                    riden2.updateGroup(x)
                                    riden3.kickoutFromGroup(fast.param1,[fast.param2])
                                    Ticket = riden2.reissueGroupTicket(fast.param1)
                                except:
                                    pass
                return

            if JSMID3 in fast.param3:
              if fast.param2 in RfuBot:
                if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
                    pass
                else:
                    Squad["Blacklist"][fast.param2] = True
                    f=codecs.open('st2__b.json','w','utf-8')
                    json.dump(Squad, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        cl.findAndAddContactsByMid(fast.param3)
                        cl.kickoutFromGroup(fast.param1,[fast.param2])
                        cl.inviteIntoGroup(fast.param1,[fast.param3])
                        riden3.acceptGroupInvitation(fast.param1)
                    except:
                        try:
                            riden1.findAndAddContactsByMid(fast.param3)
                            riden1.kickoutFromGroup(fast.param1,[fast.param2])
                            riden1.inviteIntoGroup(fast.param1,[fast.param3])
                            riden3.acceptGroupInvitation(fast.param1)
                        except:
                            try:
                                riden2.findAndAddContactsByMid(fast.param3)
                                riden2.kickoutFromGroup(fast.param1,[fast.param2])
                                riden2.inviteIntoGroup(fast.param1,[fast.param3])
                                riden3.acceptGroupInvitation(fast.param1)
                            except:
                                try:
                                    x = cl.getGroup(fast.param1)
                                    x.preventedJoinByTicket = False
                                    cl.updateGroup(x)
                                    Riden = cl.reissueGroupTicket(fast.param1)
                                    riden3.acceptGroupInvitationByTicket(fast.param1,Riden)
                                    x = riden3.getGroup(fast.param1)
                                    x.preventedJoinByTicket = True
                                    riden2.updateGroup(x)
                                    cl.kickoutFromGroup(fast.param1,[fast.param2])
                                    Ticket = riden3.reissueGroupTicket(fast.param1)
                                except:
                                    pass
                return

            if JSMID4 in fast.param3:
              if fast.param2 in RfuBot:
                if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
                    pass
                else:
                    Squad["Blacklist"][fast.param2] = True
                    f=codecs.open('st2__b.json','w','utf-8')
                    json.dump(Squad, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        riden5.findAndAddContactsByMid(fast.param3)
                        riden5.kickoutFromGroup(fast.param1,[fast.param2])
                        riden5.inviteIntoGroup(fast.param1,[fast.param3])
                        riden4.acceptGroupInvitation(fast.param1)
                    except:
                        try:
                            riden6.findAndAddContactsByMid(fast.param3)
                            riden6.kickoutFromGroup(fast.param1,[fast.param2])
                            riden6.inviteIntoGroup(fast.param1,[fast.param3])
                            riden4.acceptGroupInvitation(fast.param1)
                        except:
                            try:
                                riden7.findAndAddContactsByMid(fast.param3)
                                riden7.kickoutFromGroup(fast.param1,[fast.param2])
                                riden7.inviteIntoGroup(fast.param1,[fast.param3])
                                riden4.acceptGroupInvitation(fast.param1)
                            except:
                                try:
                                    x = riden8.getGroup(fast.param1)
                                    x.preventedJoinByTicket = False
                                    riden8.updateGroup(x)
                                    Riden = riden8.reissueGroupTicket(fast.param1)
                                    riden4.acceptGroupInvitationByTicket(fast.param1,Riden)
                                    x = riden4.getGroup(fast.param1)
                                    x.preventedJoinByTicket = True
                                    riden4.updateGroup(x)
                                    riden8.kickoutFromGroup(fast.param1,[fast.param2])
                                    Ticket = riden4.reissueGroupTicket(fast.param1)
                                except:
                                    pass
                return

            if JSMID5 in fast.param3:
              if fast.param2 in RfuBot:
                if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
                    pass
                else:
                    Squad["Blacklist"][fast.param2] = True
                    f=codecs.open('st2__b.json','w','utf-8')
                    json.dump(Squad, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        riden6.findAndAddContactsByMid(fast.param3)
                        riden6.kickoutFromGroup(fast.param1,[fast.param2])
                        riden6.inviteIntoGroup(fast.param1,[fast.param3])
                        riden5.acceptGroupInvitation(fast.param1)
                    except:
                        try:
                            riden7.findAndAddContactsByMid(fast.param3)
                            riden7.kickoutFromGroup(fast.param1,[fast.param2])
                            riden7.inviteIntoGroup(fast.param1,[fast.param3])
                            riden5.acceptGroupInvitation(fast.param1)
                        except:
                            try:
                                riden8.findAndAddContactsByMid(fast.param3)
                                riden8.kickoutFromGroup(fast.param1,[fast.param2])
                                riden8.inviteIntoGroup(fast.param1,[fast.param3])
                                riden5.acceptGroupInvitation(fast.param1)
                            except:
                                try:
                                    x = riden9.getGroup(fast.param1)
                                    x.preventedJoinByTicket = False
                                    riden9.updateGroup(x)
                                    Riden = riden9.reissueGroupTicket(fast.param1)
                                    riden5.acceptGroupInvitationByTicket(fast.param1,Riden)
                                    x = riden5.getGroup(fast.param1)
                                    x.preventedJoinByTicket = True
                                    riden5.updateGroup(x)
                                    riden9.kickoutFromGroup(fast.param1,[fast.param2])
                                    Ticket = riden5.reissueGroupTicket(fast.param1)
                                except:
                                    pass
                return

            if JSMID6 in fast.param3:
              if fast.param2 in RfuBot:
                if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
                    pass
                else:
                    Squad["Blacklist"][fast.param2] = True
                    f=codecs.open('st2__b.json','w','utf-8')
                    json.dump(Squad, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        riden7.findAndAddContactsByMid(fast.param3)
                        riden7.kickoutFromGroup(fast.param1,[fast.param2])
                        riden7.inviteIntoGroup(fast.param1,[fast.param3])
                        riden6.acceptGroupInvitation(fast.param1)
                    except:
                        try:
                            riden8.findAndAddContactsByMid(fast.param3)
                            riden8.kickoutFromGroup(fast.param1,[fast.param2])
                            riden8.inviteIntoGroup(fast.param1,[fast.param3])
                            riden6.acceptGroupInvitation(fast.param1)
                        except:
                            try:
                                riden9.findAndAddContactsByMid(fast.param3)
                                riden9.kickoutFromGroup(fast.param1,[fast.param2])
                                riden9.inviteIntoGroup(fast.param1,[fast.param3])
                                riden6.acceptGroupInvitation(fast.param1)
                            except:
                                try:
                                    x = riden10.getGroup(fast.param1)
                                    x.preventedJoinByTicket = False
                                    riden10.updateGroup(x)
                                    Riden = riden10.reissueGroupTicket(fast.param1)
                                    riden6.acceptGroupInvitationByTicket(fast.param1,Riden)
                                    x = riden6.getGroup(fast.param1)
                                    x.preventedJoinByTicket = True
                                    riden6.updateGroup(x)
                                    riden10.kickoutFromGroup(fast.param1,[fast.param2])
                                    Ticket = riden6.reissueGroupTicket(fast.param1)
                                except:
                                    pass
                return

            if JSMID7 in fast.param3:
              if fast.param2 in RfuBot:
                if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
                    pass
                else:
                    Squad["Blacklist"][fast.param2] = True
                    f=codecs.open('st2__b.json','w','utf-8')
                    json.dump(Squad, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        riden8.findAndAddContactsByMid(fast.param3)
                        riden8.kickoutFromGroup(fast.param1,[fast.param2])
                        riden8.inviteIntoGroup(fast.param1,[fast.param3])
                        riden7.acceptGroupInvitation(fast.param1)
                    except:
                        try:
                            riden9.findAndAddContactsByMid(fast.param3)
                            riden9.kickoutFromGroup(fast.param1,[fast.param2])
                            riden9.inviteIntoGroup(fast.param1,[fast.param3])
                            riden7.acceptGroupInvitation(fast.param1)
                        except:
                            try:
                                riden10.findAndAddContactsByMid(fast.param3)
                                riden10.kickoutFromGroup(fast.param1,[fast.param2])
                                riden10.inviteIntoGroup(fast.param1,[fast.param3])
                                riden7.acceptGroupInvitation(fast.param1)
                            except:
                                try:
                                    x = riden1.getGroup(fast.param1)
                                    x.preventedJoinByTicket = False
                                    riden1.updateGroup(x)
                                    Riden = riden1.reissueGroupTicket(fast.param1)
                                    riden7.acceptGroupInvitationByTicket(fast.param1,Riden)
                                    x = riden7.getGroup(fast.param1)
                                    x.preventedJoinByTicket = True
                                    riden7.updateGroup(x)
                                    riden1.kickoutFromGroup(fast.param1,[fast.param2])
                                    Ticket = riden7.reissueGroupTicket(fast.param1)
                                except:
                                    pass
                return

            if JSMID8 in fast.param3:
              if fast.param2 in RfuBot:
                if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
                    pass
                else:
                    Squad["Blacklist"][fast.param2] = True
                    f=codecs.open('st2__b.json','w','utf-8')
                    json.dump(Squad, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        riden9.findAndAddContactsByMid(fast.param3)
                        riden9.kickoutFromGroup(fast.param1,[fast.param2])
                        riden9.inviteIntoGroup(fast.param1,[fast.param3])
                        riden8.acceptGroupInvitation(fast.param1)
                    except:
                        try:
                            riden10.findAndAddContactsByMid(fast.param3)
                            riden10.kickoutFromGroup(fast.param1,[fast.param2])
                            riden10.inviteIntoGroup(fast.param1,[fast.param3])
                            riden8.acceptGroupInvitation(fast.param1)
                        except:
                            try:
                                riden2.findAndAddContactsByMid(fast.param3)
                                riden2.kickoutFromGroup(fast.param1,[fast.param2])
                                riden2.inviteIntoGroup(fast.param1,[fast.param3])
                                riden8.acceptGroupInvitation(fast.param1)
                            except:
                                try:
                                    x = riden3.getGroup(fast.param1)
                                    x.preventedJoinByTicket = False
                                    riden3.updateGroup(x)
                                    Riden = riden3.reissueGroupTicket(fast.param1)
                                    riden8.acceptGroupInvitationByTicket(fast.param1,Riden)
                                    x = riden8.getGroup(fast.param1)
                                    x.preventedJoinByTicket = True
                                    riden8.updateGroup(x)
                                    riden3.kickoutFromGroup(fast.param1,[fast.param2])
                                    Ticket = riden8.reissueGroupTicket(fast.param1)
                                except:
                                    pass
                return

            if JSMID9 in fast.param3:
              if fast.param2 in RfuBot:
                if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
                    pass
                else:
                    Squad["Blacklist"][fast.param2] = True
                    f=codecs.open('st2__b.json','w','utf-8')
                    json.dump(Squad, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        riden10.findAndAddContactsByMid(fast.param3)
                        riden10.kickoutFromGroup(fast.param1,[fast.param2])
                        riden10.inviteIntoGroup(fast.param1,[fast.param3])
                        riden9.acceptGroupInvitation(fast.param1)
                    except:
                        try:
                            riden1.findAndAddContactsByMid(fast.param3)
                            riden1.kickoutFromGroup(fast.param1,[fast.param2])
                            riden1.inviteIntoGroup(fast.param1,[fast.param3])
                            riden9.acceptGroupInvitation(fast.param1)
                        except:
                            try:
                                riden4.findAndAddContactsByMid(fast.param3)
                                riden4.kickoutFromGroup(fast.param1,[fast.param2])
                                riden4.inviteIntoGroup(fast.param1,[fast.param3])
                                riden9.acceptGroupInvitation(fast.param1)
                            except:
                                try:
                                    x = riden5.getGroup(fast.param1)
                                    x.preventedJoinByTicket = False
                                    riden5.updateGroup(x)
                                    Riden = riden5.reissueGroupTicket(fast.param1)
                                    riden9.acceptGroupInvitationByTicket(fast.param1,Riden)
                                    x = riden9.getGroup(fast.param1)
                                    x.preventedJoinByTicket = True
                                    riden9.updateGroup(x)
                                    riden5.kickoutFromGroup(fast.param1,[fast.param2])
                                    Ticket = riden9.reissueGroupTicket(fast.param1)
                                except:
                                    pass
                return

            if JSMID10 in fast.param3:
              if fast.param2 in RfuBot:
                if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
                    pass
                else:
                    Squad["Blacklist"][fast.param2] = True
                    f=codecs.open('st2__b.json','w','utf-8')
                    json.dump(Squad, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        riden7.findAndAddContactsByMid(fast.param3)
                        riden7.kickoutFromGroup(fast.param1,[fast.param2])
                        riden7.inviteIntoGroup(fast.param1,[fast.param3])
                        riden10.acceptGroupInvitation(fast.param1)
                    except:
                        try:
                            riden8.findAndAddContactsByMid(fast.param3)
                            riden8.kickoutFromGroup(fast.param1,[fast.param2])
                            riden8.inviteIntoGroup(fast.param1,[fast.param3])
                            riden10.acceptGroupInvitation(fast.param1)
                        except:
                            try:
                                riden6.findAndAddContactsByMid(fast.param3)
                                riden6.kickoutFromGroup(fast.param1,[fast.param2])
                                riden6.inviteIntoGroup(fast.param1,[fast.param3])
                                riden10.acceptGroupInvitation(fast.param1)
                            except:
                                try:
                                    x = riden9.getGroup(fast.param1)
                                    x.preventedJoinByTicket = False
                                    riden9.updateGroup(x)
                                    Riden = riden9.reissueGroupTicket(fast.param1)
                                    riden10.acceptGroupInvitationByTicket(fast.param1,Riden)
                                    x = riden10.getGroup(fast.param1)
                                    x.preventedJoinByTicket = True
                                    riden10.updateGroup(x)
                                    riden9.kickoutFromGroup(fast.param1,[fast.param2])
                                    Ticket = riden10.reissueGroupTicket(fast.param1)
                                except:
                                    pass
                return

        if fast.type == 13:
          if fast.param3 in Squad["Blacklist"]: # AUTO KICK JIKA YG DI BLACKLIST MASUK
            if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
                random.choice(Rfu).cancelGroupInvitation(fast.param1,[fast.param3])
                random.choice(Rfu).kickoutFromGroup(fast.param1,[fast.param2])
                random.choice(Rfu).kickoutFromGroup(fast.param1,[fast.param3])
                G = random.choice(Rfu).getGroup(fast.param1)
                G.preventedJoinByTicket = True
                random.choice(Rfu).updateGroup(G)
                random.choice(Rfu).sendMessage(fast.param1, None, contentMetadata={'mid': fast.param2}, contentType=13)
                random.choice(Rfu).sendMessage(fast.param1, "User Added Blacklist, Please to Unfollow blacklist first.\n")

#---------------------------------- SCRIP PROTECT GRUP -------------------------------------#

        if fast.type == 19:
            if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
                if fast.param2 in RfuBot:
                    pass
                elif RfuProtect["protect"] == True:
                    random.choice(Rfu).kickoutFromGroup(fast.param1,[fast.param2])
                    cl.findAndAddContactsByMid(fast.param3)
                    cl.inviteIntoGroup(fast.param1,[fast.param3])
                    Squad["Blacklist"][fast.param2] = True
                    random.choice(Rfu).sendMessage(fast.param1, None, contentMetadata={'mid': fast.param2}, contentType=13)
                    random.choice(Rfu).sendMessage(fast.param1, "User Added Blacklist (*-_-)/")

        if fast.type == 11:
            if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
                if fast.param2 in RfuBot:
                    pass
                elif RfuProtect["linkprotect"] == True:
                    Squad["Blacklist"][fast.param2] = True
                    G = random.choice(Rfu).getGroup(fast.param1)
                    G.preventedJoinByTicket = True
                    random.choice(Rfu).updateGroup(G)
                    random.choice(Rfu).kickoutFromGroup(fast.param1,[fast.param2])
                    Squad["Blacklist"][fast.param2] = True

        if fast.type == 13:
          if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
            if fast.param2 in RfuBot:
                pass
            elif RfuProtect["inviteprotect"] == True:
                Squad["Blacklist"][fast.param2] = True
                random.choice(Rfu).cancelGroupInvitation(fast.param1,[fast.param3])
                random.choice(Rfu).kickoutFromGroup(fast.param1,[fast.param2])
                random.choice(Rfu).kickoutFromGroup(fast.param1,[fast.param3])
                random.choice(Rfu).sendMessage(fast.param1, None, contentMetadata={'mid': fast.param2}, contentType=13)
                random.choice(Rfu).sendMessage(fast.param1, "User Added Blacklist (*-_-)/")
                G = random.choice(Rfu).getGroup(fast.param1)
                G.preventedJoinByTicket = True
                random.choice(Rfu).updateGroup(G)
                if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
                    if fast.param2 in RfuBot:
                        pass
                    elif RfuProtect["inviteprotect"] == True:
                        Squad["Blacklist"][fast.param2] = True
                        random.choice(Rfu).cancelGroupInvitation(fast.param1,[fast.param3])
                        random.choice(Rfu).kickoutFromGroup(fast.param1,[fast.param2])
                        random.choice(Rfu).kickoutFromGroup(fast.param1,[fast.param3])
                        random.choice(Rfu).sendMessage(fast.param1, None, contentMetadata={'mid': fast.param2}, contentType=13)
                        random.choice(Rfu).sendMessage(fast.param1, "User Added Blacklist (*-_-)/")
                        G = random.choice(Rfu).getGroup(fast.param1)
                        G.preventedJoinByTicket = True
                        random.choice(Rfu).updateGroup(G)
                        if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
                            if fast.param2 in RfuBot:
                                pass
                            elif RfuProtect["cancelprotect"] == True:
                                Squad["Blacklist"][fast.param2] = True
                                random.choice(Rfu).cancelGroupInvitation(fast.param1,[fast.param3])
                                random.choice(Rfu).kickoutFromGroup(fast.param1,[fast.param3])
                                random.choice(Rfu).sendMessage(fast.param1, None, contentMetadata={'mid': fast.param2}, contentType=13)
                                random.choice(Rfu).sendMessage(fast.param1, "User Added Blacklist (*-_-)/")
                                G = random.choice(Rfu).getGroup(fast.param1)
                                G.preventedJoinByTicket = True
                                random.choice(Rfu).updateGroup(G)

        if fast.type == 32:
            if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
                if fast.param2 in RfuBot:
                    pass
                elif RfuProtect["ProtectCancelled"] == True:
                    random.choice(Rfu).kickoutFromGroup(fast.param1,[fast.param2])
                    cl.findAndAddContactsByMid(fast.param3)
                    cl.inviteIntoGroup(fast.param1,[fast.param3])
                    Squad["Blacklist"][fast.param2] = True
                    random.choice(Rfu).sendMessage(fast.param1, None, contentMetadata={'mid': fast.param2}, contentType=13)
                    random.choice(Rfu).sendMessage(fast.param1, "User Added Blacklist (*-_-)/")

        if fast.type == 19:
            if fast.param3 in Squad["Admin"]:        # JIKA ADMIN KE KICK
              if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
                  random.choice(Rfu).kickoutFromGroup(fast.param1,[fast.param2])
                  riden1.findAndAddContactsByMid(fast.param3)
                  riden1.inviteIntoGroup(fast.param1,[fast.param3])
                  G = random.choice(Rfu).getGroup(fast.param1)
                  G.preventedJoinByTicket = True
                  random.choice(Rfu).updateGroup(G)
                  Squad["Blacklist"][fast.param2] = True
                  riden1.sendMessage(fast.param1, None, contentMetadata={'mid': fast.param2}, contentType=13)
                  riden1.sendMessage(fast.param1, "User Added Blacklist (*-_-)/")

        if fast.type == 13:
          if fast.param2 and fast.param3 in Squad["Blacklist"]: # AUTO KICK JIKA YG DI BLACKLIST MASUK
            if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
                random.choice(Rfu).cancelGroupInvitation(fast.param1,[fast.param3])
                random.choice(Rfu).kickoutFromGroup(fast.param1,[fast.param2])
                random.choice(Rfu).kickoutFromGroup(fast.param1,[fast.param3])
                G = random.choice(Rfu).getGroup(fast.param1)
                G.preventedJoinByTicket = True
                random.choice(Rfu).updateGroup(G)
                random.choice(Rfu).sendMessage(fast.param1, None, contentMetadata={'mid': fast.param2}, contentType=13)
                random.choice(Rfu).sendMessage(fast.param1, "User Added Blacklist, Please to Unfollow blacklist first.\n")

        if fast.type == 17:
          if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
            if fast.param2 in Squad["Blacklist"]: # AUTO KICK JIKA YG DI BLACKLIST MASUK
                random.choice(Rfu).kickoutFromGroup(fast.param1,[fast.param2])
                G = random.choice(Rfu).getGroup(fast.param1)
                G.preventedJoinByTicket = True
                random.choice(Rfu).updateGroup(G)
                Squad["Blacklist"][op.param2] = True
                random.choice(Rfu).sendMessage(fast.param1, None, contentMetadata={'mid': fast.param2}, contentType=13)
                random.choice(Rfu).sendMessage(fast.param1, "User Added Blacklist, Please to Unfollow blacklist first.\n")

        if fast.type == 55:
          if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
            if fast.param2 in Squad["Blacklist"]: # AUTO KICK JIKA YG DI BLACKLIST MASUK
                random.choice(Rfu).kickoutFromGroup(fast.param1,[fast.param2])
                G = random.choice(Rfu).getGroup(fast.param1)
                G.preventedJoinByTicket = True
                random.choice(Rfu).updateGroup(G)
                Squad["Blacklist"][op.param2] = True
                random.choice(Rfu).sendMessage(fast.param1, None, contentMetadata={'mid': fast.param2}, contentType=13)
                random.choice(Rfu).sendMessage(fast.param1, "User Added Blacklist, Please to Unfollow blacklist first.\n")

        if fast.type == 46:
            if fast.param2 in RfuBot:
                cl.removeAllMessages()
                riden1.removeAllMessages()
                riden2.removeAllMessages()
                riden3.removeAllMessages()
                riden4.removeAllMessages()
                riden5.removeAllMessages()
                riden6.removeAllMessages()
                riden7.removeAllMessages()
                riden8.removeAllMessages()
                riden9.removeAllMessages()
                riden10.removeAllMessages()

#------------------- ( 2 ) ------------------------- PEMBATAS SCRIP ------------------------------------------------#

        if fast.type == 26:
            msg = fast.message
            text = msg.text
            rfuText = msg.text
            msg_id = msg.id
            kirim = msg.to           
            user = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = kirim
                elif msg.toType == 2:
                    to = kirim
                if msg.contentType == 0:
                    if Squad["autoRead"] == True:
                        cl.sendChatChecked(kirim, msg_id)
                        riden1.sendChatChecked(kirim, msg_id)
                        riden2.sendChatChecked(kirim, msg_id)
                        riden3.sendChatChecked(kirim, msg_id)
                        riden4.sendChatChecked(kirim, msg_id)
                        riden5.sendChatChecked(kirim, msg_id)
                        riden6.sendChatChecked(kirim, msg_id)
                        riden7.sendChatChecked(kirim, msg_id)
                        riden8.sendChatChecked(kirim, msg_id)
                        riden9.sendChatChecked(kirim, msg_id)
                        riden10.sendChatChecked(kirim, msg_id)
                    if kirim in Squad["readPoint"]:
                        if user not in Squad["ROM"][kirim]:
                            Squad["ROM"][kirim][user] = True
                    if user in Mozilla["mimic"]["target"] and Mozilla["mimic"]["status"] == True and Mozilla["mimic"]["target"][user] == True:
                        text = msg.text
                        if text is not None:
                            cl.sendMessage(kirim,text)
                    if Squad["UnsendPesan"] == True:
                        msg = fast.message
                        if msg.toType == 0:
                            cl.log(" {} - {} ".format(str(user), str(rfuText)))
                        else:
                            cl.log(" {} - {} ".format(str(kirim), str(rfuText)))
                            msg_dict[msg.id] = {"rider": rfuText, "pelaku": user, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                    if Squad["Timeline"] == True:
                       if msg.contentType == 16:
                            ret_ = "Info Postingan\n"
                            if msg.contentMetadata["serviceType"] == "GB":
                                contact = cl.getContact(user)
                                auth = "\n Penulis : {}".format(str(contact.displayName))
                            else:
                                auth = "\n Penulis : {}".format(str(contact.displayName))
                                ret_ += auth
                            if "stickerId" in msg.contentMetadata:
                                stck = "\n Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                ret_ += stck
                            if "mediaOid" in msg.contentMetadata:
                                object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                if msg.contentMetadata["mediaType"] == "V":
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        murl = "\n Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        murl = "\n Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                    ret_ += murl
                                else:
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                ret_ += ourl
                            if "text" in msg.contentMetadata:
                                dia = cl.getContact(user)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan = 'Pengirim: '
                                xteam = str(dia.displayName)
                                pesan = ''
                                pesan2 = pesan+"@ARDIAN_GANTENG\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                                zx2.append(zx)
                                kata = "\n Tulisan : {}".format(str(msg.contentMetadata["text"]))
                                purl = "\n Post URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += purl
                                ret_ += kata
                                zxc += pesan2
                                pesan = xpesan + zxc + ret_ + ""
                                cl.sendMessage(kirim, pesan, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

        if fast.type == 65:
          if Squad['UnsendPesan'] == True:
              try:
                  you = fast.param1
                  msg.id = fast.param2
                  user = msg._from
                  if msg.id in msg_dict:
                    if msg_dict[msg.id]["pelaku"]:
                        pelaku = cl.getContact(msg_dict[msg.id]["pelaku"])
                        nama = pelaku.displayName
                        dia = "Detect Pesan Terhapus\n"
                        dia += "\n1. Name : " + nama
                        dia += "\n2. Taken : {}".format(str(msg_dict[msg.id]["createdTime"]))
                        dia += "\n3. Pesannya : {}".format(str(msg_dict[msg.id]["rider"]))
                        cl.mentionWithRFU(you,user," Nah","\n\n" +str(dia))
              except:
                  cl.sendMessage(you, "Return")

        if fast.type in [25,26]:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 7:
                if Squad['IDSticker'] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    filler = "STICKER CHECKS\nSTKID : %s\nSTKPKGID : %s\nSTKVER : %s\n\nTHIS IS LINK\n\nline://shop/detail/%s" % (stk_id,pkg_id,stk_ver,pkg_id)
                    cl.mentionWithRFU(kirim,user,"My Code Sticker\n","" + "\n\n" + str(filler))
                else:
                    pass

        if fast.type == 25 or fast.type == 26:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 1:
              if Squad['Upfoto'] == True:
                if user in Owner:
                    path = cl.downloadObjectMsg(msg.id)
                    cl.updateProfilePicture(path)
                    cl.mentionWithRFU(kirim,user," Update Picture Success ","")
                    Squad['Upfoto'] = False

        if fast.type == 25 or fast.type == 26:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 1:
              if Squad['UpfotoBot'] == True:
                if user in RfuSekawan or user in Squad["Admin"]:
                    path1 = riden1.downloadObjectMsg(msg.id)
                    path2 = riden2.downloadObjectMsg(msg.id)
                    path3 = riden3.downloadObjectMsg(msg.id)
                    path4 = riden4.downloadObjectMsg(msg.id)
                    path5 = riden5.downloadObjectMsg(msg.id)
                    path6 = riden6.downloadObjectMsg(msg.id)
                    path7 = riden7.downloadObjectMsg(msg.id)
                    path8 = riden8.downloadObjectMsg(msg.id)
                    path9 = riden9.downloadObjectMsg(msg.id)
                    path10 = riden10.downloadObjectMsg(msg.id)
                    riden1.updateProfilePicture(path1)
                    riden2.updateProfilePicture(path2)
                    riden3.updateProfilePicture(path3)                    
                    riden4.updateProfilePicture(path4)
                    riden5.updateProfilePicture(path5)
                    riden6.updateProfilePicture(path6)                    
                    riden7.updateProfilePicture(path7)
                    riden8.updateProfilePicture(path8)                    
                    riden9.updateProfilePicture(path9)
                    riden10.updateProfilePicture(path10)
                    riden1.mentionWithRFU(kirim,user," Update Picture Success ","")
                    riden2.mentionWithRFU(kirim,user," Update Picture Success ","")
                    riden3.mentionWithRFU(kirim,user," Update Picture Success ","")                    
                    riden4.mentionWithRFU(kirim,user," Update Picture Success ","")
                    riden5.mentionWithRFU(kirim,user," Update Picture Success ","")
                    riden6.mentionWithRFU(kirim,user," Update Picture Success ","")                    
                    riden7.mentionWithRFU(kirim,user," Update Picture Success ","")
                    riden8.mentionWithRFU(kirim,user," Update Picture Success ","")
                    riden9.mentionWithRFU(kirim,user," Update Picture Success ","")
                    riden10.mentionWithRFU(kirim,user," Update Picture Success ","")
                    Squad['UpfotoBot'] = False

        if fast.type == 25 or fast.type == 26:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 1:
              if Squad['UpfotoGroup'] == True:
                if user in RfuSekawan or user in Squad["Admin"]:
                    path = cl.downloadObjectMsg(msg.id)
                    cl.updateGroupPicture(kirim, path)
                    cl.mentionWithRFU(kirim,user," Update Picture Grup Success ","")
                    Squad['UpfotoGroup'] = False

        if fast.type in [25,26]:
          if Squad['Contact'] == True:
              msg = fast.message
              user = msg._from
              kirim = msg.to
              if msg.contentType == 13:
                if 'displayName' in msg.contentMetadata:
                    contact = cl.getContact(msg.contentMetadata["mid"])
                    try:
                        cover = cl.getProfileCoverURL(user)
                    except:
                        cover = ""
                    cl.sendMessage(kirim,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nBio:\n" + contact.statusMessage + "\n\nPicture URL:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\nCover URL:\n" + str(cover))
                else:
                    contact = cl.getContact(msg.contentMetadata["mid"])
                    try:
                        cover = cl.getProfileCoverURL(user)
                    except:
                        cover = ""
                    cl.sendText(kirim,"Nama:\n" + contact.displayName + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nBio:\n" + contact.statusMessage + "\n\nPicture URL\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\nCover URL:\n" + str(cover))

        if fast.type == 25 or fast.type == 26:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                try:
                    if user in RfuSekawan or user in Squad["Admin"]:
                      if Squad["Ban"] == True:
                        if msg.contentMetadata["mid"] in Squad["Blacklist"]:
                            name = msg.contentMetadata["displayName"]
                            cl.sendMessage(kirim, name + str(" Sudah di daftar Blacklist"))
                            Squad['Ban'] = False
                        else:
                            Squad["Blacklist"][msg.contentMetadata["mid"]] = True
                            name = msg.contentMetadata["displayName"]
                            cl.sendMessage(kirim, name + str(" Added in Blacklist"))
                            Squad['Ban'] = False
                      if Squad["Unban"] == True:
                        if msg.contentMetadata["mid"] in Squad["Blacklist"]:
                            del Squad["Blacklist"][msg.contentMetadata["mid"]]
                            name = msg.contentMetadata["displayName"]
                            cl.sendMessage(kirim, name + str(" Succes dellete in Blacklist"))
                            Squad['Unban'] = False
                        else:
                            name = msg.contentMetadata["displayName"]
                            cl.sendMessage(kirim, name + str(" Nothing in Blacklist"))
                            Squad['Unban'] = False
                      if Squad["Adminadd"] == True:
                        if msg.contentMetadata["mid"] in Squad["Admin"]:
                            name = msg.contentMetadata["displayName"]
                            cl.sendMessage(kirim, name + str(" Sudah di daftar Admin"))
                            Squad['Adminadd'] = False
                        else:
                            Squad["Admin"][msg.contentMetadata["mid"]] = True
                            name = msg.contentMetadata["displayName"]
                            cl.sendMessage(kirim, name + str(" Added in Admin"))
                            Squad['Adminadd'] = False
                      if Squad["AdminDel"] == True:
                        if msg.contentMetadata["mid"] in Squad["Admin"]:
                            del Squad["Admin"][msg.contentMetadata["mid"]]
                            name = msg.contentMetadata["displayName"]
                            cl.sendMessage(kirim, name + str(" Succes dellete in Admin"))
                            Squad['AdminDel'] = False
                        else:
                            name = msg.contentMetadata["displayName"]
                            cl.sendMessage(kirim, name + str(" Nothing in Admin"))
                            Squad['AdminDel'] = False
                except Exception as error:
                    cl.sendText(kirim, str(error))

        if fast.type == 25 or fast.type == 26:
          if Squad['Invite'] == True:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in RfuSekawan or user in Squad["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = cl.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            cl.sendText(msg.to, _name + " Sudah Berada DiGrup Ini")
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.findAndAddContactsByMid(target)
                                cl.inviteIntoGroup(kirim,[target])
                                cl.sendText(kirim,"Invite " + _name + "\nSUCCESS..")
                                Squad['Invite'] = False
                                break
                            except:             
                                 cl.sendText(kirim, 'Contact error')
                                 Squad['Invite'] = False
                                 break

        if fast.type == 25 or fast.type == 26:
          if Squad['Steal'] == True:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in RfuSekawan or user in Squad["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print ("[Target] Stealed")
                            break             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                contact = cl.getContact(target)
                                cl.sendText(kirim,"Nama :\n" + msg.contentMetadata["displayName"] + "\n\nBio :\n" + contact.statusMessage+ "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nSteal Succes..")
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                cl.sendImageWithURL(kirim,image)
                                cover = cl.getProfileCoverURL(target)
                                cl.sendImageWithURL(kirim, cover)
                                Squad['Steal'] = False
                                break                     
                            except:             
                                 cl.sendText(kirim, 'Contact error')
                                 Squad['Steal'] = False
                                 break

        if fast.type == 25 or fast.type == 26:
          if Squad['KillOn'] == True:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in RfuSekawan or user in Squad["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print ("[Target] Kick Via Contact")
                            break             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target not in RfuSekawan:
                                try:
                                    cl.kickoutFromGroup(kirim,[target])
                                    Squad['KillOn'] = False
                                    break
                                except:             
                                     cl.sendText(kirim, 'Target Not Found')
                                     Squad['KillOn'] = False
                                     break

        if fast.type == 25 or fast.type == 26:
          if Squad['Gift'] == True:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in RfuSekawan or user in Squad["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print ("[Target] Send Gift")
                            break             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.sendMessage(target, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58','PRDTYPE': 'THEME','MSGTPL': '12'}, contentType = 9)
                                riden1.sendMessage(target, None, contentMetadata={'PRDID': 'a99cbfdf-4672-45c5-b558-eb0d2e6ab777','PRDTYPE': 'THEME','MSGTPL': '12'}, contentType = 9)
                                riden2.sendMessage(target, None, contentMetadata={'PRDID': 'a99cbfdf-4672-45c5-b558-eb0d2e6ab777','PRDTYPE': 'THEME','MSGTPL': '12'}, contentType = 9)
                                riden3.sendMessage(target, None, contentMetadata={'PRDID': 'a99cbfdf-4672-45c5-b558-eb0d2e6ab777','PRDTYPE': 'THEME','MSGTPL': '12'}, contentType = 9)
                                Squad['Gift'] = False
                                break
                            except:             
                                 cl.sendText(kirim, 'Target Error')
                                 Squad['Gift'] = False
                                 break

        if fast.type == 25 or fast.type == 26:
          if Squad["Mic"] == True:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in RfuSekawan or user in Squad["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print ("[Target] Mimic Add")
                            break             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                Mozilla["mimic"]["target"][target] = True
                                cl.sendText(kirim,"Target ditambahkan!")
                                Squas['Mic'] = False
                                break
                            except:             
                                 cl.sendText(kirim, 'Silahkan untuk on kan kembali & Send Contact Again\nKami akan memuat ulang program')
                                 break

        if fast.type == 25 or fast.type == 26:
          if Squad["MicDel"] == True:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in RfuSekawan or user in Squad["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print ("[Target] Mimic Add")
                            break             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                del Mozilla["mimic"]["target"][target]
                                cl.sendText(kirim,"Target is Dellete!")
                                Squad['MicDel'] = False
                                break
                            except:             
                                 cl.sendText(kirim, 'Silahkan untuk on kan kembali & Send Contact Again\nKami akan memuat ulang program')
                                 break

        if fast.type == 25 or fast.type == 26:
          if Squad['Copy'] == True:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in RfuSekawan or user in Squad["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print ("[Target] Stealed")
                            break             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.cloneContactProfile(target)
                                cl.sendText(kirim, "Copy Contact Success")
                                Squad['Copy'] = False
                                break
                            except:             
                                 cl.sendText(kirim, "Contact Error")
                                 Squad['Copy'] = False
                                 break
                                 
                                 
#======= AUTO TAG & CHAT BATAS SCRIP ========
        if fast.type == 26:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 0 and user not in mid and msg.toType == 2:
                if "MENTION" in msg.contentMetadata.keys() != None:
                    if Squad['AutoRespon'] == True:
                        contact = cl.getContact(user)
                        cName = contact.displayName
                        balas = [cName + "\n" + str(Squad['MentionText'])]
                        ret_ = "" + random.choice(balas)
                        name = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                              if mention['M'] in mid:
                                  cl.mentionWithRFU(kirim,user,"","" +str(ret_))
                                  break

        if fast.type == 26:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 0 and user not in RfuSekawan or user not in Squad["Admin"]:
                if "MENTION" in msg.contentMetadata.keys() != None:
                    if Squad['KickRespon'] == True:
                        contact = cl.getContact(user)
                        cName = contact.displayName
                        balas = [cName + "Dont Tag Me","Sorry Dont Tag Me"]
                        ret_ = "" + random.choice(balas)
                        name = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                              if mention['M'] in mid:
                                  cl.mentionWithRFU(kirim,user,"","" +str(ret_))
                                  cl.kickoutFromGroup(kirim,[user])
                                  break

        if fast.type == 25 or fast.type == 26:
          if Squad['SpamInvite'] == True:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in RfuSekawan or user in Squad["Admin"]:
                    korban = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = cl.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for x in groups.members:
                        if korban in x.displayName:
                            cl.sendText(kirim, korban + " Sudah Berada DiGrup Ini")
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.findAndAddContactsByMid(target)
                                riden1.findAndAddContactsByMid(target)
                                riden2.findAndAddContactsByMid(target)
                                riden3.findAndAddContactsByMid(target)
                                cl.createGroup("【YOU SELF BOT】",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                cl.createGroup("【YOU SELF BOT】",[target]) # HANYA SPAM VIA CONTACT
                                cl.createGroup("【YOU SELF BOT】",[target])
                                riden1.createGroup("【YOU SELF BOT】",[target])
                                riden1.createGroup("【YOU SELF BOT】",[target])
                                riden1.createGroup("【YOU SELF BOT】",[target])
                                riden2.createGroup("【YOU SELF BOT】",[target])
                                riden2.createGroup("【YOU SELF BOT】",[target])
                                riden2.createGroup("【YOU SELF BOT】",[target])
                                riden3.createGroup("【YOU SELF BOT】",[target])
                                riden3.createGroup("【YOU SELF BOT】",[target])
                                riden3.createGroup("【YOU SELF BOT】",[target])
                                cl.sendText(kirim,"Spam Invite ke " + korban + "\nSUCCESS..")
                                Squad['SpamInvite'] = False
                            except:             
                                 cl.sendText(kirim, 'Contact error')
                                 Squad['SpamInvite'] = False
                                 break


#------------------- ( 3 ) ------------------------- PEMBATAS SCRIP ------------------------------------------------#

        if fast.type == 25 or fast.type == 26:
            msg = fast.message
            text = msg.text
            rfuText = msg.text
            msg_id = msg.id
            kirim = msg.to           
            user = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = kirim
                elif msg.toType == 2:
                    to = kirim
                if msg.contentType == 0:
                    if Squad["autoRead"] == True:
                        cl.sendChatChecked(0, msg_id)

                    elif rfuText is None:
                        return
                    else:               
                        if rfuText.lower() == 'PROSES TRANSISI':
                            cl.sendMessage(0, user)

                        elif rfuText.lower() == "คท":
                            if user in RfuSekawan or user in Squad["Admin"]:
                                cl.sendMessage(kirim, None, contentMetadata={'mid': mid}, contentType=13)
                                cl.mentionWithRFU(kirim,mid," Hi","")

                        elif rfuText.lower() == "คำสั่ง":
                            if user in RfuSekawan or user in Squad["Admin"]:
                                 cl.sendMessage(kirim, str(Help))

                        elif rfuText.lower() == "สปีด":
                            if user in RfuSekawan or user in Squad["Admin"]:
                                no = time.time()
                                cl.sendText("ud3511dd6ed90c47f33234c30640a3bc9", ' ')
                                elapsed_time = time.time() - no
                                cl.sendText(kirim, "%s" % (elapsed_time))
                                no1 = time.time()
                                riden1.sendText("ud3511dd6ed90c47f33234c30640a3bc9", ' ')
                                elapsed_time = time.time() - no1
                                riden1.sendText(kirim, "%s" % (elapsed_time))
                                no2 = time.time()
                                riden2.sendText("ud3511dd6ed90c47f33234c30640a3bc9", ' ')
                                elapsed_time = time.time() - no2
                                riden2.sendText(kirim, "%s" % (elapsed_time))
                                no3 = time.time()
                                riden3.sendText("ud3511dd6ed90c47f33234c30640a3bc9", ' ')
                                elapsed_time = time.time() - no3
                                riden3.sendText(kirim, "%s" % (elapsed_time))                                
                                no4 = time.time()
                                riden4.sendText("ud3511dd6ed90c47f33234c30640a3bc9", ' ')
                                elapsed_time = time.time() - no4
                                riden4.sendText(kirim, "%s" % (elapsed_time))
                                no5 = time.time()
                                riden5.sendText("ud3511dd6ed90c47f33234c30640a3bc9", ' ')
                                elapsed_time = time.time() - no5
                                riden5.sendText(kirim, "%s" % (elapsed_time))
                                no6 = time.time()
                                riden6.sendText("ud3511dd6ed90c47f33234c30640a3bc9", ' ')
                                elapsed_time = time.time() - no6
                                riden6.sendText(kirim, "%s" % (elapsed_time))                                
                                no7 = time.time()
                                riden7.sendText("ud3511dd6ed90c47f33234c30640a3bc9", ' ')
                                elapsed_time = time.time() - no7
                                riden7.sendText(kirim, "%s" % (elapsed_time))
                                no8 = time.time()
                                riden8.sendText("ud3511dd6ed90c47f33234c30640a3bc9", ' ')
                                elapsed_time = time.time() - no8
                                riden8.sendText(kirim, "%s" % (elapsed_time))
                                no9 = time.time()
                                riden9.sendText("ud3511dd6ed90c47f33234c30640a3bc9", ' ')
                                elapsed_time = time.time() - no9
                                riden9.sendText(kirim, "%s" % (elapsed_time))
                                no10 = time.time()
                                riden10.sendText("ud3511dd6ed90c47f33234c30640a3bc9", ' ')
                                elapsed_time = time.time() - no10
                                riden10.sendText(kirim, "%s" % (elapsed_time))

                        elif rfuText.lower() == "responsename":
                            if user in RfuSekawan or user in Squad["Admin"]:
                                team = cl.getContact(mid).displayName
                                team1 = riden1.getContact(JSMID1).displayName
                                team2 = riden2.getContact(JSMID2).displayName
                                team3 = riden3.getContact(JSMID3).displayName                                
                                team4 = riden4.getContact(JSMID4).displayName
                                team5 = riden5.getContact(JSMID5).displayName
                                team6 = riden6.getContact(JSMID6).displayName                                
                                team7 = riden7.getContact(JSMID7).displayName
                                team8 = riden8.getContact(JSMID8).displayName
                                team9 = riden9.getContact(JSMID9).displayName
                                team10 = riden10.getContact(JSMID10).displayName
                                owner = "ud3511dd6ed90c47f33234c30640a3bc9"
                                cl.mentionWithRFU(kirim,owner," Ready On ","" + str(" ("+team+")"))
                                riden1.mentionWithRFU(kirim,owner," Ready On ","" + str(" ("+team1+")"))
                                riden2.mentionWithRFU(kirim,owner," Ready On ","" + str(" ("+team2+")"))
                                riden3.mentionWithRFU(kirim,owner," Ready On ","" + str(" ("+team3+")"))                                
                                riden4.mentionWithRFU(kirim,owner," Ready On ","" + str(" ("+team4+")"))
                                riden5.mentionWithRFU(kirim,owner," Ready On ","" + str(" ("+team5+")"))
                                riden6.mentionWithRFU(kirim,owner," Ready On ","" + str(" ("+team6+")"))                                
                                riden7.mentionWithRFU(kirim,owner," Ready On ","" + str(" ("+team7+")"))
                                riden8.mentionWithRFU(kirim,owner," Ready On ","" + str(" ("+team8+")"))
                                riden9.mentionWithRFU(kirim,owner," Ready On ","" + str(" ("+team9+")"))
                                riden10.mentionWithRFU(kirim,owner," Ready On ","" + str(" ("+team10+")"))

                        elif rfuText.lower() == "mybot":
                            if user in RfuSekawan or user in Squad["Admin"]:
                               cl.sendMessage(kirim, None, contentMetadata={'mid': mid}, contentType=13)
                               cl.sendMessage(kirim, None, contentMetadata={'mid': JSMID1}, contentType=13)
                               cl.sendMessage(kirim, None, contentMetadata={'mid': JSMID2}, contentType=13)
                               cl.sendMessage(kirim, None, contentMetadata={'mid': JSMID3}, contentType=13)                             
                               cl.sendMessage(kirim, None, contentMetadata={'mid': JSMID4}, contentType=13)
                               cl.sendMessage(kirim, None, contentMetadata={'mid': JSMID5}, contentType=13)
                               cl.sendMessage(kirim, None, contentMetadata={'mid': JSMID6}, contentType=13)
                               cl.sendMessage(kirim, None, contentMetadata={'mid': JSMID7}, contentType=13)
                               cl.sendMessage(kirim, None, contentMetadata={'mid': JSMID8}, contentType=13)
                               cl.sendMessage(kirim, None, contentMetadata={'mid': JSMID9}, contentType=13)
                               cl.sendMessage(kirim, None, contentMetadata={'mid': JSMID10}, contentType=13)

                        elif rfuText.lower() == "my team":
                            if user in RfuSekawan or user in Squad["Admin"]:
                                rfu = ""
                                sekawan = ""
                                wa = 0
                                wi = 0
                                for m_id in Owner:
                                    wa = wa + 1
                                    end = '\n'
                                    rfu += str(wa) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in Squad["Admin"]:
                                    wi = wi + 1
                                    end = '\n'
                                    sekawan += str(wi) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendText(kirim,"【YOU】\n\nOwner:\n"+rfu+"\nAdmin:\n"+sekawan+"\n( %s ) 【YOU】" %(str(len(Owner)+len(Squad["Admin"]))))                                

                        elif rfuText.lower() == "มา":
                            if user in RfuSekawan or user in Squad["Admin"]:
                                X = cl.getGroup(kirim)
                                X.preventedJoinByTicket = False
                                cl.updateGroup(X)
                                invsend = 0
                                Riden = cl.reissueGroupTicket(kirim)
                                riden1.acceptGroupInvitationByTicket(kirim,Riden)
                             #   riden2.acceptGroupInvitationByTicket(kirim,Riden)
                               # riden3.acceptGroupInvitationByTicket(kirim,Riden)                             
                           #     riden4.acceptGroupInvitationByTicket(kirim,Riden)
                             #   riden5.acceptGroupInvitationByTicket(kirim,Riden)
                          #      riden6.acceptGroupInvitationByTicket(kirim,Riden)                           
                           #     riden7.acceptGroupInvitationByTicket(kirim,Riden)
                         #       riden8.acceptGroupInvitationByTicket(kirim,Riden)
                         #       riden9.acceptGroupInvitationByTicket(kirim,Riden)
                      #          riden10.acceptGroupInvitationByTicket(kirim,Riden)
                                X = cl.getGroup(kirim)
                                X.preventedJoinByTicket = True
                                cl.updateGroup(X)
                                X.preventedJoinByTicket(X)
                                cl.updateGroup(X)

                        elif rfuText.lower() == "ไป":
                            if user in RfuSekawan or user in Squad["Admin"]:
                                ginfo = cl.getGroup(kirim)
                                owner = "ud3511dd6ed90c47f33234c30640a3bc9"
                                riden1.mentionWithRFU(kirim,owner," บายๆ ","\n นายท่าน ยู" + str(" ("+ginfo.name+")"))
                               # riden10.leaveGroup(kirim)
                             #   riden9.leaveGroup(kirim)
                           #     riden8.leaveGroup(kirim)
                             #   riden7.leaveGroup(kirim)
                             #   riden6.leaveGroup(kirim)
                           #     riden5.leaveGroup(kirim)
                            #    riden4.leaveGroup(kirim)     
                            #    riden3.leaveGroup(kirim)
                            #    riden2.leaveGroup(kirim)
                                riden1.leaveGroup(kirim)
                             #   cl.leaveGroup(kirim)

                        elif rfuText.lower() == "leaveall grup":
                            if user in RfuSekawan or user in Squad["Admin"]:
                                gid = cl.getGroupIdsJoined()
                                gid = riden1.getGroupIdsJoined()
                              #  gid = riden2.getGroupIdsJoined()
                              #  gid = riden3.getGroupIdsJoined()                                
                              #  gid = riden4.getGroupIdsJoined()
                            #    gid = riden5.getGroupIdsJoined()
                            #    gid = riden6.getGroupIdsJoined()                                
                           #     gid = riden7.getGroupIdsJoined()
                            #    gid = riden8.getGroupIdsJoined()
                              #  gid = riden9.getGroupIdsJoined()                                
                             #   gid = riden10.getGroupIdsJoined()
                                for i in gid:
                                   # cl.leaveGroup(i)
                                    riden1.leaveGroup(i)
                                   # riden2.leaveGroup(i)
                                  #  riden3.leaveGroup(i)                                    
                                  #  riden4.leaveGroup(i)
                                   # riden5.leaveGroup(i)
                                   # riden6.leaveGroup(i)
                                  #  riden7.leaveGroup(i)                                    
                                    #riden8.leaveGroup(i)
                                   # riden9.leaveGroup(i)
                                   # riden10.leaveGroup(i)
                                    print ("Kicker Leave All group")

                        elif rfuText in ["เตะเปิด"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["KickOn"] = True
                                cl.sendText(kirim,"สถะนะ:\n{''ยกเลิก'':0,''เตะ'':1}")
                        elif rfuText in ["เตะปิด"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["KickOn"] = False
                                cl.sendText(kirim,"สถะนะ:\n{''ยกเลิก'':0,''เตะ'':0}")

                        elif rfuText.lower().startswith("ki"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                              if msg.toType == 2:
                                if Squad["KickOn"]:
                                    _name = msg.text.replace("Ki","")
                                    gs = cl.getGroup(kirim)
                                    targets = []
                                    for g in gs.members:
                                        if _name in g.displayName:
                                            targets.append(g.mid)
                                    if targets == []:
                                        cl.sendText(kirim,"ไม่พบเป้าหมาย.")
                                    else:
                                        for target in targets:
                                          if target not in RfuSekawan and target not in Squad["Admin"]:
                                            try:
                                                klist=[cl,riden1,riden2,riden3,riden4,riden5,riden6,riden7,riden8,riden9,riden10]
                                                kicker=random.choice(klist)
                                                kicker.kickoutFromGroup(kirim,[target])
                                                print (kirim,[g.mid])
                                            except Exception as error:
                                                cl.sendText(kirim, str(error))

                        elif rfuText.lower().startswith("spam "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                txt = rfuText.split(" ")
                                jmlh = int(txt[2])
                                teks = rfuText.replace("spam "+str(txt[1])+" "+str(jmlh)+" ","")
                                tulisan = jmlh * (teks+"\n")
                                if txt[1] == "on":
                                    if jmlh <= 500:
                                       for x in range(jmlh):
                                           cl.sendText(kirim, teks)
                                    else:
                                       cl.sendText(kirim, "Maksimal 500 SpamTeks!")
                                elif txt[1] == "off":
                                    if jmlh <= 500:
                                        cl.sendText(kirim, tulisan)
                                    else:
                                        cl.sendText(kirim, "Maksimal 500 SpamTeks!")

                        elif rfuText.lower().startswith("cekmid: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                ardian = rfuText.replace("cekmid: ","")
                                cl.sendMessage(kirim, None, contentMetadata={'mid': ardian}, contentType=13)
                                contact = cl.getContact(ardian)
                                ganteng = cl.getProfileCoverURL(ardian)
                                path = str(ganteng)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                try:
                                    cl.sendText(kirim,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                                    cl.sendText(kirim,"Profile Picture " + contact.displayName)
                                    cl.sendImageWithURL(kirim,image)
                                    cl.sendText(kirim,"Cover Picture " + contact.displayName)
                                    cl.sendImageWithURL(kirim,path)
                                except:
                                    pass

                        elif ("Banlock " in rfuText):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:
                                        Squad["Blacklist"][target] = True
                                        cl.sendText(kirim,"Succes Banned ")
                                    except:
                                        pass

                        elif rfuText.lower() == "เชคดำ":
                            if user in RfuSekawan or user in Squad["Admin"]:
                                if Squad["Blacklist"] == {}:
                                    cl.sendText(kirim,"ไม่มีคนติดดำ")
                                else:
                                    mc = "คำติดหำ เฮ้ย คนติดดำ "
                                    num=1
                                    ragets = cl.getContacts(Squad["Blacklist"])
                                    for mi_d in ragets:
                                        mc+="\n%i. %s" % (num, mi_d.displayName)
                                        num=(num+1)
                                    mc+="\n\n จำนวน %i คน " % len(ragets)
                                    cl.sendText(kirim, mc)

                        elif rfuText in ["Contact ban"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                              if Squad["Blacklist"] == {}:
                                  cl.sendText(kirim,"Tidak Ada Blacklist")
                              else:
                                  cl.sendText(kirim,"Contact Blacklist")
                                  h = ""
                                  for i in Squad["Blacklist"]:
                                      h = cl.getContact(i)
                                      cl.sendMessage(kirim, None, contentMetadata={'mid': i}, contentType=13)

                        elif rfuText in ["ล้างดำ"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["Blacklist"] = {}
                                cl.sendText(kirim,"ล้างหำ เฮ้ยๆ ล้างดำเรียบร้อย")
                                print ("Clear Ban")

                        elif rfuText in ["ลงดำคท"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["Ban"] = True
                                cl.sendText(kirim,"ลงดำเรียบร้อย..")
                        elif rfuText in ["Unban:on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["Unban"] = True
                                cl.sendText(kirim,"ส่งคท..คนที่จะลงดำ..")

                        elif rfuText.lower() == 'เปิดลิ้ง':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                if msg.toType == 2:
                                    group = cl.getGroup(kirim)
                                    group.preventedJoinByTicket = False
                                    cl.updateGroup(group)

                        elif rfuText.lower() == 'ปิดลิ้ง':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                if msg.toType == 2:
                                    group = cl.getGroup(kirim)
                                    group.preventedJoinByTicket = True
                                    cl.updateGroup(group)

                        elif rfuText.lower() == 'gurl':
                          if user in RfuSekawan or user in Squad["Admin"]:
                            if msg.toType == 2:
                                grup = cl.getGroup(kirim)
                                if grup.preventedJoinByTicket == False:
                                    set = cl.reissueGroupTicket(kirim)
                                    cl.sendMessage(kirim, "Group Ticket : \nhttps://line.me/R/ti/g/{}".format(str(set)))
                                else:
                                    cl.sendMessage(kirim, "Ketik Link on Dulu kaka")

                        elif rfuText.lower() == 'ใครสร้างกลุ่ม':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    group = cl.getGroup(kirim)
                                    GS = group.creator.mid
                                    cl.sendMessage(kirim, None, contentMetadata={'mid': GS}, contentType=13)
                                    cl.mentionWithRFU(kirim,GS,"ผู้สร้างกลุ่ม","")
                                    contact = cl.getContact(GS.mid)
                                except:
                                    W = group.members[0].mid
                                    cl.sendMessage(kirim, None, contentMetadata={'mid': W}, contentType=13)
                                    cl.mentionWithRFU(kirim,W,"ผู้สร้างกลุ่ม","")

                        elif "invite gcreator" == rfuText:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    group = cl.getGroup(kirim)
                                    GS = group.creator.mid
                                    cl.sendMessage(kirim, None, contentMetadata={'mid': GS}, contentType=13)
                                    cl.mentionWithRFU(kirim,GS,"Group Creator","")
                                    cl.findAndAddContactsByMid(GS)
                                    cl.inviteIntoGroup(kirim,[GS])
                                    cl.mentionWithRFU(kirim,user,"Invite Done","")
                                    contact = cl.getContact(GS.mid)
                                except:
                                    W = group.members[0].mid
                                    cl.sendMessage(kirim, None, contentMetadata={'mid': W}, contentType=13)
                                    cl.mentionWithRFU(kirim,W,"Group Creator","")
                                    cl.findAndAddContactsByMid(W)
                                    cl.inviteIntoGroup(kirim,[W])
                                    cl.mentionWithRFU(kirim,user,"Invite Done","")

                        elif rfuText.lower() == 'ginfo':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                group = cl.getGroup(kirim)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(line.reissueGroupTicket(group.id)))
                                cuki = "INFO GRUP"
                                cuki += "\nNama Group : {}".format(str(group.name))
                                cuki += "\nID Group :\n? {}".format(group.id)
                                cuki += "\nPembuat : {}".format(str(gCreator))
                                cuki += "\nJumlah Member : {}".format(str(len(group.members)))
                                cuki += "\nJumlah Pending : {}".format(gPending)
                                cuki += "\nGroup Qr : {}".format(gQr)
                                cuki += "\nGroup Ticket : {}".format(gTicket)
                                cl.sendMessage(kirim, str(cuki))

                        elif rfuText in ["คนในกลุ่ม"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                kontak = cl.getGroup(kirim)
                                group = kontak.members
                                num=1
                                msgs="สมาชิกทั้งหมด\n"
                                for ids in group:
                                    msgs+="\n%i. %s" % (num, ids.displayName)
                                    num=(num+1)
                                msgs+="\n\nว้าวๆ อยู่กันครบเลยนะ.. ( %i )" % len(group)
                                cl.sendText(kirim, msgs)

                        elif rfuText in ["Blocklist"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                blockedlist = cl.getBlockedContactIds()
                                kontak = cl.getContacts(blockedlist)
                                num=1
                                msgs="My Blocked\n"
                                for ids in kontak:
                                    msgs+="\n%i. %s" % (num, ids.displayName)
                                    num=(num+1)
                                msgs+="\n\nTotal Blocked : %i" % len(kontak)
                                cl.sendText(kirim, msgs)

                        elif rfuText in ["Friendlist mid"]: 
                            if user in RfuSekawan or user in Squad["Admin"]:
                                gruplist = cl.getAllContactIds()
                                kontak = cl.getContacts(gruplist)
                                num=1
                                msgs="List Mid Friend\n"
                                for ids in kontak:
                                    msgs+="\n%i. %s" % (num, ids.mid)
                                    num=(num+1)
                                msgs+="\n\nTotal Mid Friend : %i" % len(kontak)
                                cl.sendText(kirim, msgs)

                        elif "Grup id" in rfuText:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                saya = rfuText.replace('Grup id','')
                                gid = cl.getGroup(kirim)
                                cl.sendText(kirim, "ID Grup : \n" + gid.id + "\nName Grup : \n" + str(gid.name))

                        elif rfuText.lower().startswith("mid"):
                          if user in RfuSekawan or user in Squad["Admin"]:
                              try:
                                  key = eval(msg.contentMetadata["MENTION"])
                                  u = key["MENTIONEES"][0]["M"]
                                  cmid = cl.getContact(u).mid
                                  cl.sendText(kirim, str(cmid))
                              except Exception as e:
                                  cl.sendText(kirim, str(e))

                        elif rfuText.lower().startswith("profile"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                key = eval(msg.contentMetadata["MENTION"])
                                key1 = key["MENTIONEES"][0]["M"]
                                contact = cl.getContact(key1)
                                cover = cl.getProfileCoverURL(key1)
                                path = str(cover)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                try:
                                    cl.sendText(kirim,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                                    cl.sendImageWithURL(kirim,image)
                                    cl.sendImageWithURL(kirim,path)
                                except Exception as error:
                                    cl.sendMessage(kirim, str(error))

                        elif rfuText.lower() == 'เปิดจุด':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if kirim in Squad['readPoint']:
                                        try:
                                            del Squad['readPoint'][kirim]
                                            del Squad['readMember'][kirim]
                                            del Squad['readTime'][kirim]
                                        except:
                                            pass
                                        Squad['readPoint'][kirim] = msg.id
                                        Squad['readMember'][kirim] = ""
                                        Squad['readTime'][kirim] = datetime.now().strftime('%H:%M:%S')
                                        Squad['ROM'][kirim] = {}
                                        with open('sider.json', 'w') as fp:
                                            json.dump(Squad, fp, sort_keys=True, indent=4)
                                            cl.sendMessage(kirim,"Lurking already on")
                                else:
                                    try:
                                        del read['readPoint'][kirim]
                                        del read['readMember'][kirim]
                                        del read['readTime'][kirim]
                                    except:
                                        pass
                                    Squad['readPoint'][kirim] = msg.id
                                    Squad['readMember'][kirim] = ""
                                    Squad['readTime'][kirim] = datetime.now().strftime('%H:%M:%S')
                                    Squad['ROM'][kirim] = {}
                                    with open('sider.json', 'w') as fp:
                                        json.dump(Squad, fp, sort_keys=True, indent=4)
                                        cl.sendMessage(kirim, "Set reading point:\n" + readTime)
                                        
                        elif rfuText.lower() == 'ปิดจุด':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if kirim not in Squad['readPoint']:
                                    cl.sendMessage(kirim,"Lurking already off..")
                                else:
                                    try:
                                            del Squad['readPoint'][kirim]
                                            del Squad['readMember'][kirim]
                                            del Squad['readTime'][kirim]
                                    except:
                                          pass
                                    cl.sendMessage(kirim, "Delete reading point:\n" + readTime)
                
                        elif rfuText.lower() == 'lurking reset':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if kirim in Squad["readPoint"]:
                                    try:
                                        Squad["readPoint"][kirim] = True
                                        Squad["readMember"][kirim] = {}
                                        Squad["readTime"][kirim] = readTime
                                        Squad["ROM"][kirim] = {}
                                    except:
                                        pass
                                    cl.sendMessage(kirim, "Reset reading point:\n" + readTime)
                                else:
                                    cl.sendMessage(kirim, "Lurking on dulu kaka..")
                                    
                        elif rfuText.lower() == 'lurking read':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if kirim in Squad['readPoint']:
                                    if Squad["ROM"][kirim].items() == []:
                                        cl.sendMessage(kirim,"[ Reader ]:\nNone")
                                    else:
                                        chiya = []
                                        for rom in Squad["ROM"][kirim].items():
                                            chiya.append(rom[1])
                                        cmem = cl.getContacts(chiya) 
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = 'Pembaca Pesan:\n'
                                    for x in range(len(cmem)):
                                        xname = str(cmem[x].displayName)
                                        pesan = ''
                                        pesan2 = pesan+"@ARDIAN_GANTENG\n"
                                        xlen = str(len(zxc)+len(xpesan))
                                        xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                        zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    text = xpesan+ zxc + "\nLurking time: \n" + readTime
                                    try:
                                        cl.sendMessage(kirim, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    except Exception as error:
                                        print (error)
                                    pass
                                else:
                                    cl.sendMessage(kirim,"Lurking on dulu kaka ??")

                        elif rfuText.lower() == 'เปิดแอบ':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    del RfuCctv['Point2'][kirim]
                                    del RfuCctv['Point3'][kirim]
                                    del RfuCctv['Point1'][kirim]
                                except:
                                    pass
                                RfuCctv['Point2'][kirim] = msg.id
                                RfuCctv['Point3'][kirim] = ""
                                RfuCctv['Point1'][kirim]=True
                                cl.sendText(kirim,"Sider Set to On..")

                        elif rfuText.lower() == 'ปิดแอบ':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                if kirim in RfuCctv['Point2']:
                                    RfuCctv['Point1'][kirim]=False
                                    cl.sendText(kirim, RfuCctv['Point3'][kirim])
                                else:
                                    cl.sendText(kirim, "Off not Going")

                        elif rfuText.lower().startswith("แทค"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                gname = cl.getGroup(kirim)
                                local = [contact.mid for contact in gname.members]
                                try:
                                    lur = len(local)//20
                                    for fu in range(lur+1):
                                        hdc = u''
                                        sell=0
                                        com=[]
                                        for rid in gname.members[fu*20 : (fu+1)*20]:
                                            com.append({"S":str(sell), "E" :str(sell+6), "M":rid.mid})
                                            sell += 7
                                            hdc += u'@A_RFU\n'
                                            atas = '\n หวัดดี {} '.format(str(gname.name))
                                            atas += '\n หวัดดี {} หำ เฮ้ยๆ คน'.format(str(len(local)))
                                        cl.sendMessage(kirim, text=hdc + str(atas), contentMetadata={u'MENTION': json.dumps({'MENTIONEES':com})}, contentType=0)
                                except Exception as error:
                                    cl.sendMessage(kirim, str(error))

                        elif rfuText in ["Welcome on"]:
                          if user in RfuSekawan or user in Squad["Admin"]:
                            if user in RfuSekawan:
                                Squad['Welcome'] = True
                                cl.sendText(kirim,"Cek Welcome Already ON")
                        elif rfuText in ["Welcome off"]:
                          if user in RfuSekawan or user in Squad["Admin"]:
                            if user in RfuSekawan:
                                Squad['Welcome'] = False
                                cl.sendText(kirim,"Cek Welcome Already Off")

                        elif rfuText.lower().startswith("changewelcome: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                teks = rfuText.split(": ")
                                data = rfuText.replace(teks[0] + ": ","")
                                try:
                                    Squad["WcText"] = data
                                    cl.sendText(kirim,"Name Welcome Change to:\n" +str("(" +data+ ")"))
                                except:
                                    cl.sendText(kirim,"Name Error")

                        elif rfuText in ["Leave on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Leave'] = True
                                cl.sendText(kirim,"Cek Leave Already ON")
                        elif rfuText in ["Leave off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Leave'] = False
                                cl.sendText(kirim,"Cek Leave Already Off")

                        elif rfuText.lower().startswith("changeleave: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                teks = rfuText.split(": ")
                                data = rfuText.replace(teks[0] + ": ","")
                                try:
                                    Squad["LvText"] = data
                                    cl.sendText(kirim,"Name Leave Change to:\n" +str("(" +data+ ")"))
                                except:
                                    cl.sendText(kirim,"Name Error")

                        elif rfuText.lower() == "runtime":
                            if user in RfuSekawan or user in Squad["Admin"]:
                                eltime = time.time() - mulai                                
                                opn = " "+waktu(eltime)
                                cl.sendText(kirim,"Connect to RFU SEKAWAN\nBot Active\n" + opn)                

                        elif rfuText.lower().startswith("broadcast: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                bc = msg.text.replace("broadcast: ","")
                                gid = cl.getGroupIdsJoined()
                                owner = "uc721ad1f11fb7e128453ba5a27424998"
                                for i in gid:
                                    cl.mentionWithRFU(i,owner," BROADCAST BY:","\n" + str(" ("+bc+")"))

                        elif rfuText.lower().startswith("contactbc: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                bc = msg.text.replace("contactbc: ","")
                                gid = cl.getAllContactIds()
                                owner = "uc721ad1f11fb7e128453ba5a27424998"
                                for i in gid:
                                    cl.mentionWithRFU(i,owner," BROADCAST BY:","\n" + str(" ("+bc+")"))

                        elif rfuText.lower().startswith("adminadd"):
                            if user in RfuSekawan:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target in Squad["Admin"]:
                                        cl.sendText(kirim, "Sudah Terdaftar di Admin")
                                    else:
                                        try:
                                            Squad["Admin"][target] = True
                                            cl.sendText(kirim, "Terdaftar Menjadi Admin ")
                                        except Exception as e:
                                            cl.sendText(kirim, str(error))

                        elif rfuText.lower().startswith("admindell"):
                            if user in Owner:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target not in Squad["Admin"]:
                                        cl.sendText(kirim, "Belum Terdaftar di Admin")
                                    else:
                                        try:
                                            del Squad["Admin"][target]
                                            cl.sendText(kirim, "Succes Dihapus menjadi admin")
                                        except Exception as e:
                                            cl.sendText(kirim, str(error))

                        elif rfuText.lower().startswith("changename: "):
                            if user in RfuSekawan:
                                name = rfuText.split(": ")
                                change = rfuText.replace(name[0] + ": ","")
                                cll = cl.getProfile()
                                cll.displayName = change
                                cl.updateProfile(cll)
                                owner = "uc721ad1f11fb7e128453ba5a27424998"
                                cl.mentionWithRFU(kirim,owner," Update Name Success","\n Change to " + str(change))

                        elif rfuText.lower().startswith("changebio: "):
                            if user in RfuSekawan:
                                proses = rfuText.split(": ")
                                teks = rfuText.replace(proses[0] + ": ","")
                                no1 = cl.getProfile()
                                no1.statusMessage = teks
                                cl.updateProfile(no1)
                                cl.sendText(kirim,"My Bio Change To : " + teks)

                        elif rfuText.lower().startswith("changenameall: "):
                            if user in RfuSekawan:
                                name = rfuText.split(": ")
                                change = rfuText.replace(name[0] + ": ","")
                                cll = cl.getProfile()
                                cll1 = riden1.getProfile()
                                cll2 = riden2.getProfile()
                                cll3 = riden3.getProfile()                                
                                cll4 = riden4.getProfile()
                                cll5 = riden5.getProfile()
                                cll6 = riden6.getProfile()
                                cll7 = riden7.getProfile()
                                cll8 = riden8.getProfile()
                                cll9 = riden9.getProfile()
                                cll10 = riden10.getProfile()
                                cll.displayName = change
                                cll1.displayName = change
                                cll2.displayName = change
                                cll3.displayName = change                                
                                cll4.displayName = change
                                cll5.displayName = change
                                cll6.displayName = change
                                cll7.displayName = change                                
                                cll8.displayName = change
                                cll9.displayName = change
                                cll10.displayName = change
                                cl.updateProfile(cll)
                                riden1.updateProfile(cll1)
                                riden2.updateProfile(cll2)
                                riden3.updateProfile(cll3)                                
                                riden4.updateProfile(cll4)
                                riden5.updateProfile(cll5)
                                riden6.updateProfile(cll6)                                
                                riden7.updateProfile(cll7)
                                riden8.updateProfile(cll8)
                                riden9.updateProfile(cll9)
                                riden10.updateProfile(cll10)
                                cl.mentionWithRFU(kirim,user," Update Name Success","\n Change to " + str(change))
                                riden1.mentionWithRFU(kirim,user," Update Name Success","\n Change to " + str(change))
                                riden2.mentionWithRFU(kirim,user," Update Name Success","\n Change to " + str(change))
                                riden3.mentionWithRFU(kirim,user," Update Name Success","\n Change to " + str(change))                                
                                riden4.mentionWithRFU(kirim,user," Update Name Success","\n Change to " + str(change))
                                riden5.mentionWithRFU(kirim,user," Update Name Success","\n Change to " + str(change))
                                riden6.mentionWithRFU(kirim,user," Update Name Success","\n Change to " + str(change))                                
                                riden7.mentionWithRFU(kirim,user," Update Name Success","\n Change to " + str(change))
                                riden8.mentionWithRFU(kirim,user," Update Name Success","\n Change to " + str(change))
                                riden9.mentionWithRFU(kirim,user," Update Name Success","\n Change to " + str(change))
                                riden10.mentionWithRFU(kirim,user," Update Name Success","\n Change to " + str(change))

                        elif rfuText.lower().startswith("คิก"):
                            if user in RfuSekawan:
                                proses = rfuText.split(": ")
                                teks = rfuText.replace(proses[0] + ": ","")
                               # no = cl.getProfile()
                                no1 = riden1.getProfile()
                             #   no2 = riden2.getProfile()
                             #   no3 = riden3.getProfile()                                
                               # no4 = riden4.getProfile()
                              #  no5 = riden5.getProfile()
                                #no6 = riden6.getProfile()                                
                              #  no7 = riden7.getProfile()
                                #no8 = riden8.getProfile()
                              #  no9 = riden9.getProfile()
                                #no10 = riden10.getProfile()
                               # no.statusMessage = teks
                                no1.statusMessage = teks
                               # no2.statusMessage = teks
                               # no3.statusMessage = teks                                
                                #no4.statusMessage = teks
                               # no5.statusMessage = teks
                                #no6.statusMessage = teks
                               # no7.statusMessage = teks
                                #no8.statusMessage = teks
                               # no9.statusMessage = teks
                                #no10.statusMessage = teks
                                cl.updateProfile(no)
                                riden1.updateProfile(no1)
                             #   riden2.updateProfile(no2)
                             #   riden3.updateProfile(no3)                                
                               # riden4.updateProfile(no4)
                               # riden5.updateProfile(no5)
                                #riden6.updateProfile(no6)
                                #riden7.updateProfile(no7)
                                #riden8.updateProfile(no8)
                                #riden9.updateProfile(no9)
                                #riden10.updateProfile(no10)
                                cl.sendText(kirim,"My Bio Change To : " + teks)
                                riden1.sendText(kirim,"My Bio Change To : " + teks)
                                riden2.sendText(kirim,"My Bio Change To : " + teks)
                                riden3.sendText(kirim,"My Bio Change To : " + teks)                                
                                riden4.sendText(kirim,"My Bio Change To : " + teks)
                                riden5.sendText(kirim,"My Bio Change To : " + teks)
                                riden6.sendText(kirim,"My Bio Change To : " + teks)
                                riden7.sendText(kirim,"My Bio Change To : " + teks)
                                riden8.sendText(kirim,"My Bio Change To : " + teks)
                                riden9.sendText(kirim,"My Bio Change To : " + teks)
                                riden10.sendText(kirim,"My Bio Change To : " + teks)

                        elif rfuText.lower() == "remove pesan":
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    cl.removeAllMessages(fast.param2)
                                    riden1.removeAllMessages(fast.param2)
                                    riden2.removeAllMessages(fast.param2)
                                    riden3.removeAllMessages(fast.param2)                                    
                                    riden4.removeAllMessages(fast.param2)
                                    riden5.removeAllMessages(fast.param2)
                                    riden6.removeAllMessages(fast.param2)                                    
                                    riden7.removeAllMessages(fast.param2)
                                    riden8.removeAllMessages(fast.param2)
                                    riden9.removeAllMessages(fast.param2)
                                    riden10.removeAllMessages(fast.param2)
                                    ginfo = cl.getGroup(kirim)
                                    owner = "uc721ad1f11fb7e128453ba5a27424998"
                                    cl.mentionWithRFU(kirim,owner," Remove Message Success ","\n In Grup" + str(" ("+ginfo.name+")"))
                                    riden1.mentionWithRFU(kirim,owner," Remove Message Success ","\n In Grup" + str(" ("+ginfo.name+")"))
                                    riden2.mentionWithRFU(kirim,owner," Remove Message Success ","\n In Grup" + str(" ("+ginfo.name+")"))
                                    riden3.mentionWithRFU(kirim,owner," Remove Message Success ","\n In Grup" + str(" ("+ginfo.name+")"))                                    
                                    riden4.mentionWithRFU(kirim,owner," Remove Message Success ","\n In Grup" + str(" ("+ginfo.name+")"))
                                    riden5.mentionWithRFU(kirim,owner," Remove Message Success ","\n In Grup" + str(" ("+ginfo.name+")"))
                                    riden6.mentionWithRFU(kirim,owner," Remove Message Success ","\n In Grup" + str(" ("+ginfo.name+")"))
                                    riden7.mentionWithRFU(kirim,owner," Remove Message Success ","\n In Grup" + str(" ("+ginfo.name+")"))
                                    riden8.mentionWithRFU(kirim,owner," Remove Message Success ","\n In Grup" + str(" ("+ginfo.name+")"))
                                    riden9.mentionWithRFU(kirim,owner," Remove Message Success ","\n In Grup" + str(" ("+ginfo.name+")"))
                                    riden10.mentionWithRFU(kirim,owner," Remove Message Success ","\n In Grup" + str(" ("+ginfo.name+")"))
                                except:
                                    pass

                        elif rfuText.lower() == 'รีบอท':
                            if user in RfuSekawan:
                                cl.sendText(kirim, 'กำลังรีบอท ใจเย็ดๆนายท่าน..')
                                print ("Restarting Server")
                                restart_program()

                        elif rfuText.lower() == 'ปิดบอท':
                            if user in RfuSekawan:
                                cl.mentionWithRFU(kirim,user," Akses Off","")
                                print ("Selfbot Off")
                                exit(1)

                        elif rfuText.lower().startswith(" Kick","kick","เตะ"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target in Rfu:
                                        pass
                                    else:
                                        try:
                                            klist=[cl,riden1,riden2,riden3,riden4,riden5]
                                            kicker=random.choice(klist)
                                            kicker.kickoutFromGroup(kirim,[target])
                                            Squad["Blacklist"][target] = True
                                        except Exception as e:
                                            cl.sendText(kirim, str(error))

                        elif rfuText.lower() == 'my grup':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                groups = cl.groups
                                ret_ = "GRUP JOIN"
                                no = 0 + 1
                                for gid in groups:
                                    group = cl.getGroup(gid)
                                    ret_ += "\n\n{}. {} ".format(str(no), str(group.name))
                                    no += 1
                                ret_ += "\n\nTOTAL {} GRUP JOIN".format(str(len(groups)))
                                cl.sendText(kirim, str(ret_))

                        elif rfuText.lower() == 'm1 grup':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                groups = riden1.groups
                                ret_ = "GRUP JOIN"
                                no = 0 + 1
                                for gid in groups:
                                    group = riden1.getGroup(gid)
                                    ret_ += "\n\n{}. {} ".format(str(no), str(group.name))
                                    no += 1
                                ret_ += "\n\nTOTAL {} GRUP JOIN".format(str(len(groups)))
                                riden1.sendText(kirim, str(ret_))

                        elif rfuText.lower() == 'm2 grup':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                groups = riden2.groups
                                ret_ = "GRUP JOIN"
                                no = 0 + 1
                                for gid in groups:
                                    group = riden2.getGroup(gid)
                                    ret_ += "\n\n{}. {} ".format(str(no), str(group.name))
                                    no += 1
                                ret_ += "\n\nTOTAL {} GRUP JOIN".format(str(len(groups)))
                                riden2.sendText(kirim, str(ret_))

                        elif rfuText.lower() == 'm3 grup':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                groups = riden3.groups
                                ret_ = "GRUP JOIN"
                                no = 0 + 1
                                for gid in groups:
                                    group = riden3.getGroup(gid)
                                    ret_ += "\n\n{}. {} ".format(str(no), str(group.name))
                                    no += 1
                                ret_ += "\n\nTOTAL {} GRUP JOIN".format(str(len(groups)))
                                riden3.sendText(kirim, str(ret_))

                        elif rfuText.lower().startswith("ยกเชิญ"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                ginvited = cl.getGroupIdsInvited()
                                ginvited = riden1.getGroupIdsInvited()
                               # ginvited = riden2.getGroupIdsInvited()
                                #ginvited = riden3.getGroupIdsInvited()                                
                                #ginvited = riden4.getGroupIdsInvited()
                                #ginvited = riden5.getGroupIdsInvited()
                                #ginvited = riden6.getGroupIdsInvited()
                                #ginvited = riden7.getGroupIdsInvited()
                                #ginvited = riden8.getGroupIdsInvited()
                                #ginvited = riden9.getGroupIdsInvited()
                                #ginvited = riden10.getGroupIdsInvited()
                                if ginvited != [] and ginvited != None:
                                    for gid in ginvited:
                                        cl.rejectGroupInvitation(gid)
                                        riden1.rejectGroupInvitation(gid)
                                       # riden2.rejectGroupInvitation(gid)
                                       # riden3.rejectGroupInvitation(gid)
                                    cl.sendMessage(kirim, "Succes Cancell {} Invite Grup".format(str(len(ginvited))))
                                    riden1.sendMessage(kirim, "Succes Cancell {} Invite Grup".format(str(len(ginvited))))
                                    #riden2.sendMessage(kirim, "Succes Cancell {} Invite Grup".format(str(len(ginvited))))
                                    #riden3.sendMessage(kirim, "Succes Cancell {} Invite Grup".format(str(len(ginvited))))                                    
                                    #riden4.sendMessage(kirim, "Succes Cancell {} Invite Grup".format(str(len(ginvited))))
                                    #riden5.sendMessage(kirim, "Succes Cancell {} Invite Grup".format(str(len(ginvited))))
                                    #riden6.sendMessage(kirim, "Succes Cancell {} Invite Grup".format(str(len(ginvited))))
                                  #  riden7.sendMessage(kirim, "Succes Cancell {} Invite Grup".format(str(len(ginvited))))
                                #    riden8.sendMessage(kirim, "Succes Cancell {} Invite Grup".format(str(len(ginvited))))
                                    #riden9.sendMessage(kirim, "Succes Cancell {} Invite Grup".format(str(len(ginvited))))
                                    #riden10.sendMessage(kirim, "Succes Cancell {} Invite Grup".format(str(len(ginvited))))                                    
                                else:
                                    cl.sendMessage(kirim, "Nothing Invited")
#==============================================================================#
        if op.type == 19:
            print ("[ 19 ] บอทระบบคิก")
            try:
                if op.param3 in clMID:
                    if op.param2 in riden1MID:
                        G = riden1.getGroup(op.param1)
#                        ginfo = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        riden1.updateGroup(G)
                        invsend = 0
                        Ticket = riden1.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        riden1.acceptGroupInvitationByTicket(op.param1,Ticket)
                      #  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                      #  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = riden1.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        riden1.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        riden1.updateGroup(G)
                    else:
                        G = riden1.getGroup(op.param1)
#                        ginfo = ais.getGroup(op.param1)
                        riden1.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        riden1.updateGroup(G)
                        invsend = 0
                        Ticket = riden1.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        riden1.acceptGroupInvitationByTicket(op.param1,Ticket)
                       # kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = riden1.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        riden1.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        riden1.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#------- ban-nadya ----------------------------------------------------------------------[kiMID ki2MID]
                elif op.param3 in riden1MID:
                    if op.param2 in clMID:
                        G = cl.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        riden1.acceptGroupInvitationByTicket(op.param1,Ticket)
                     #   kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                       # kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = cl.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        cl.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        cl.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)
#                        ginfo = gye.getGroup(op.param1)
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        riden1.acceptGroupInvitationByTicket(op.param1,Ticket)
                       # kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = cl.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        cl.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        cl.updateGroup(G)
                        settings["blacklist"][op.param2] = True              
#------- nadya - can ----------------------------------------------------------------------[kiMID ki2MID]
                        elif rfuText.lower().startswith("status"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    hasil = "Status Bot\n"
                                    if Squad["autoAdd"] == True: hasil += "\nAuto Add 🔵 "
                                    else: hasil += "\nAuto Add 🔴 "
                                    if Squad["autoJoin"] == True: hasil += "\nAuto Join 🔵 "
                                    else: hasil += "\nAuto Join 🔴 "
                                    if Squad["AutoReject"] == True: hasil += "\nAuto Reject Room 🔵 "
                                    else: hasil += "\nAuto Reject Room 🔴 "
                                    if Squad["AutojoinTicket"] == True: hasil += "\nAuto Join Ticket 🔵 "
                                    else: hasil += "\nAuto Join Ticket 🔴 "
                                    if Squad["autoRead"] == True: hasil += "\nAuto Read  🔵 "
                                    else: hasil += "\nAuto Read 🔴 "
                                    if Squad["AutoRespon"] == True: hasil += "\nDetect Mention 🔵 "
                                    else: hasil += "\nDetect Mention 🔴 "
                                    if Squad["KickRespon"] == True: hasil += "\nDetect Mention 🔵 "
                                    else: hasil += "\nDetect Kick Mention 🔴 "
                                    if Squad["Contact"] == True: hasil += "\nCheck Contact 🔵 "
                                    else: hasil += "\nCheck Contact 🔴 "
                                    if Squad["Timeline"] == True: hasil += "\nCheck Post Timeline 🔵 "
                                    else: hasil += "\nCheck Post 🔴 "
                                    if Squad["IDSticker"] == True: hasil += "\nCheck Sticker 🔵 "
                                    else: hasil += "\nCheck Sticker 🔴 "
                                    if Squad["UnsendPesan"] == True: hasil += "\nUnsend Message 🔵 "
                                    else: hasil += "\nUnsend Message 🔴 "
                                    if RfuProtect["protect"] == True: hasil += "\nProtect Grup 🔵 "
                                    else: hasil += "\nProtect Grup 🔴 "
                                    if RfuProtect["linkprotect"] == True: hasil += "\nProtect Link Grup 🔵 "
                                    else: hasil += "\nProtect Link Grup 🔴 "
                                    if RfuProtect["inviteprotect"] == True: hasil += "\nProtect Invite Grup 🔵 "
                                    else: hasil += "\nProtect Invite Grup 🔴 "
                                    if RfuProtect["cancelprotect"] == True: hasil += "\nProtect Cancel Grup 🔵 "
                                    else: hasil += "\nProtect Cancel Grup 🔴 "
                                    if RfuProtect["ProtectCancelled"] == True: hasil += "\nProtect Cancel Member 🔵 "
                                    else: hasil += "\nProtect Cancel Member 🔴 "
                                    if Squad["BackupBot"] == True: hasil += "\nBackup Bot 🔵 "
                                    else: hasil += "\nBackup Bot 🔴 "
                                    if Squad["KickOn"] == True: hasil += "\nKick All Member 🔵 "
                                    else: hasil += "\nKick All Member 🔴 "
                                    if Squad["SpamInvite"] == True: hasil += "\nSpam invite via contact 🔵 "
                                    else: hasil += "\nSpam invite Via Contact 🔴 "
                                    hasil += "\n\nStatus Bot"
                                    cl.sendMessage(kirim, str(hasil))
                                except Exception as error:
                                    cl.sendMessage(kirim, str(error))

                        elif rfuText in ["Allprotect on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    RfuProtect['protect'] = True
                                    RfuProtect['linkprotect'] = True
                                    RfuProtect['inviteprotect'] = True
                                    RfuProtect['cancelprotect'] = True
                                    RfuProtect['ProtectCancelled'] = True
                                    grup = cl.getGroup(kirim)
                                    cl.sendText(kirim,"AllProtect Already On in Grup : " +str(grup.name))
                                except Exception as e:
                                    cl.sendText(kirim, str(error))
                        elif rfuText in ["Allprotect off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    RfuProtect['protect'] = False
                                    RfuProtect['linkprotect'] = False
                                    RfuProtect['inviteprotect'] = False
                                    RfuProtect['cancelprotect'] = False
                                    RfuProtect['ProtectCancelled'] = False
                                    grup = cl.getGroup(kirim)
                                    cl.sendText(kirim,"AllProtect Already Off in Grup : " +str(grup.name))
                                except Exception as e:
                                    cl.sendText(kirim, str(error))

                        elif rfuText in ["Backup on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['BackupBot'] = True
                                cl.sendText(kirim,"Backup Bot Ready On")
                        elif rfuText in ["Backup off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['BackupBot'] = False
                                cl.sendText(kirim,"Backup Bot Nonactive")

                        elif rfuText in ["Unsend on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['UnsendPesan'] = True
                                cl.sendText(kirim,"Cek UnsendMessage Set to on..")
                        elif rfuText in ["Unsend off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['UnsendPesan'] = False
                                cl.sendText(kirim,"Cek UnsendMessage Set to off..")

                        elif rfuText in ["Changepp on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Upfoto'] = True
                                cl.sendText(kirim,"Send Pict For UpPict")
                        elif rfuText in ["Changepp off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Upfoto'] = False
                                cl.sendText(kirim,"Send Pict Already Off")

                        elif rfuText in ["Changeppbot on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['UpfotoBot'] = True
                                riden1.sendText(kirim,"Send Pict For UpPict")
                                riden2.sendText(kirim,"Send Pict For UpPict")
                                riden3.sendText(kirim,"Send Pict For UpPict")
                        elif rfuText in ["Changeppbot off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['UpfotoBot'] = False
                                riden1.sendText(kirim,"Send Pict Already Off")
                                riden2.sendText(kirim,"Send Pict Already Off")
                                riden3.sendText(kirim,"Send Pict Already Off")

                        elif rfuText in ["Cfotogrup on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['UpfotoGrup'] = True
                                cl.sendText(kirim,"Send Pict For Change Foto Grup")
                        elif rfuText in ["Cfotogrup off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['UpfotoGrup'] = False
                                cl.sendText(kirim,"Send Pict Already Off")

                        elif rfuText in ["Timeline on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Timeline'] = True
                                cl.sendText(kirim,"Cek Post Set to on..")
                        elif rfuText in ["Timeline off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Timeline'] = False
                                cl.sendText(kirim,"Cek Post Set to off..")

                        elif rfuText in ["เปิดมุดลิ้ง"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['autoJoin'] = True
                                cl.sendText(kirim,"เปิดแล้วท่านยู..")
                        elif rfuText in ["ปิดมุดลิ้ง"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['autoJoin'] = False
                                cl.sendText(kirim,"ปิดแล้วท่านยู..")

                        elif rfuText in ["Autoreject on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['AutoReject'] = True
                                cl.sendText(msg.to,"Reject Set To On..")
                        elif rfuText in ["Autoreject off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['AutoReject'] = False
                                cl.sendText(msg.to,"Reject Set To Off..")

                        elif rfuText in ["Admin:add-on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["Adminadd"] = True
                                cl.sendText(kirim,"Send Contact to added Admin..")
                        elif rfuText in ["Admin:add-off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["Adminadd"] = False
                                cl.sendText(kirim,"Send Contact to added Admin in Off..")

                        elif rfuText in ["Admin:del-on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["AdminDel"] = True
                                cl.sendText(kirim,"Send Contact to Dellete Admin..")
                        elif rfuText in ["Admin:del-off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["AdminDel"] = False
                                cl.sendText(kirim,"Send Contact to Dellete Admin in Off..")

                        elif rfuText in ["Gift:on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["Gift"] = True
                                cl.sendText(kirim,"Send Contact to send Gift..")
                        elif rfuText in ["Gift:off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["Gift"] = False
                                cl.sendText(kirim,"Send Contact to Gift in Off..")

                        elif rfuText in ["Spaminvite on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["SpamInvite"] = True
                                cl.sendText(kirim,"Send Contact to spam grup..")
                        elif rfuText in ["Spaminvite off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["Gift"] = False
                                cl.sendText(kirim,"Send Contact to send grup Off..")

                        elif rfuText in ["Auto jointicket on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["AutojoinTicket"] = True
                                cl.sendText(kirim,"Join Ticket Set To On")
                        elif rfuText in ["Auto jointicket off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["AutojoinTicket"] = False
                                cl.sendText(kirim,"Join Ticket Set To Off")
                        elif '/ti/g/' in rfuText.lower():
                            if user in RfuSekawan or user in Squad["Admin"]:
                                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(msg.text)
                                n_links=[]
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    if Squad["AutojoinTicket"] == True:
                                        group=cl.findGroupByTicket(ticket_id)
                                        cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                        cl.sendText(kirim,"Success Masuk %s" % str(group.name))

                        elif rfuText in ["Copy on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Copy'] = True
                                cl.sendText(kirim,"Send Contact For Copy User")
                        elif rfuText in ["Copy off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Copy'] = False
                                cl.sendText(kirim,"Send Contact Already Off")

                        elif rfuText.lower().startswith("clone "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = cl.getContact(ls)
                                        cl.cloneContactProfile(ls)
                                        cl.sendMessage(kirim, "Berhasil mengclone profile {}".format(contact.displayName))

                        elif rfuText.lower() == 'comeback':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    clProfile.displayName = str(ProfileMe["displayName"])
                                    clProfile.statusMessage = str(ProfileMe["statusMessage"])
                                    clProfile.pictureStatus = str(ProfileMe["pictureStatus"])
                                    cl.updateProfileAttribute(8, clProfile.pictureStatus)
                                    cl.updateProfile(clProfile)
                                    cl.sendMessage(kirim, "Already back to my account")
                                except:
                                    cl.sendMessage(kirim, "Error Come Back")

                        elif rfuText in ["Steal on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Steal'] = True
                                cl.sendText(kirim,"Send Contact For Cek Contact")
                        elif rfuText in ["Steal off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Steal'] = False
                                cl.sendText(kirim,"Send Contact Already Off")

                        elif rfuText in ["Contact on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Contact'] = True
                                cl.sendText(kirim,"Contact Set to on")
                        elif rfuText in ["Contact off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Contact'] = False
                                cl.sendText(kirim,"Contact Already Off")

                        elif rfuText in ["Invite on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Invite'] = True
                                cl.sendText(kirim,"Send Contact For Invite Target")
                        elif rfuText in ["Invite off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Invite'] = False
                                cl.sendText(kirim,"Send Contact Set Off")

                        elif rfuText.lower().startswith("kill on"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["KillOn"] = True
                                cl.sendMessage(kirim, "SendContact For Kick Taget")
                        elif rfuText.lower().startswith("kill off"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["KillOn"] = False
                                cl.sendMessage(kirim, "SendContact For Kick Taget in Off")

                        elif rfuText in ["Mic:add-on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Target["Mic"] = True
                                cl.sendText(kirim,"Send Contact To Clone Message User")
                        elif rfuText in ["Mic:del-on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Target["MicDel"] = True
                                cl.sendText(kirim,"Send Contact Dellete Clone Message User")
                        elif "mimic" in rfuText.lower():
                            if user in RfuSekawan or user in Squad["Admin"]:
                                sep = rfuText.split(" ")
                                mic = rfuText.replace(sep[0] + " ","")
                                if mic == "on":
                                    if Mozilla["mimic"]["status"] == False:
                                        Mozilla["mimic"]["status"] = True
                                        cl.sendText(kirim,"Mimic Set to on")
                                elif mic == "off":
                                    if Mozilla["mimic"]["status"] == True:
                                        Mozilla["mimic"]["status"] = False
                                        cl.sendText(kirim,"Mimic Message off")

                        elif rfuText.lower() == 'mimiclist':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                if Mozilla["mimic"]["target"] == {}:
                                    cl.sendText(kirim,"Tidak Ada Target")
                                else:
                                    mc = "Mimic List"
                                    for mi_d in Mozilla["mimic"]["target"]:
                                        mc += "\n? "+cl.getContact(mi_d).displayName
                                    cl.sendText(kirim,mc + "\nFinish")

                        elif rfuText.lower().startswith("refresh"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    Squad['Mic'] = False
                                    Squad['MicDel'] = False
                                    Squad['Gift'] = False
                                    Squad['Steal'] = False
                                    Squad['Invite'] = False
                                    Squad['Contact'] = False
                                    Squad['Copy'] = False
                                    Squad['autoJoin'] = False
                                    Squad['autoAdd'] = False
                                    Squad['AutojoinTicket'] = False
                                    Squad['UnsendPesan'] = False
                                    Squad['AutoReject'] = False
                                    Squad['Timeline'] = False
                                    Squad['Upfoto'] = False
                                    Squad['UpfotoBot'] = False
                                    Squad['UpfotoGrup'] = False
                                    Squad['Adminadd'] = False
                                    Squad['AdminDel'] = False
                                    Squad['Welcome'] = False
                                    Squad['Leave'] = False
                                    Squad['Ban'] = False
                                    Squad['Unban'] = False
                                    Squad['KillOn'] = False
                                    Squad['KickOn'] = False
                                    Squad['SpamInvite'] = False
                                    cl.sendText(kirim,"Refresh Success")
                                except Exception as e:
                                    cl.sendText(kirim, str(error))

                        elif rfuText.lower().startswith("my name"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                contact = cl.getContact(user)
                                cl.sendMessage(kirim, "MyName : {}".format(contact.displayName))
                        elif rfuText.lower().startswith("my bio"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                contact = cl.getContact(user)
                                cl.sendMessage(kirim, "My Status : \n{}".format(contact.statusMessage))
                        elif rfuText.lower().startswith("my picture"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                contact = cl.getContact(user)
                                cl.sendImageWithURL(kirim,"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                        elif rfuText.lower().startswith("my video"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                contact = cl.getContact(user)
                                cl.sendVideoWithURL(kirim,"http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))
                        elif rfuText.lower().startswith("my cover"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                channel = cl.getProfileCoverURL(user)          
                                path = str(channel)
                                cl.sendImageWithURL(kirim, path)

#------------------------------------------ SOCIAL MEDIA ----------------------------------------------------#

                        elif rfuText.lower().startswith("topnews"):
                              if user in RfuSekawan or user in Squad["Admin"]:
                                  rfu=requests.get("https://newsapi.org/v2/top-headlines?country=id&apiKey=1214d6480f6848e18e01ba6985e2008d")
                                  data=rfu.text
                                  data=json.loads(data)
                                  hasil = "Top News\n\n"
                                  hasil += "(1) " + str(data["articles"][0]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][0]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][0]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][0]["url"])
                                  hasil += "\n\n(2) " + str(data["articles"][1]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][1]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][1]["author"])   
                                  hasil += "\n     Link : " + str(data["articles"][1]["url"])
                                  hasil += "\n\n(3) " + str(data["articles"][2]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][2]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][2]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][2]["url"])
                                  hasil += "\n\n(4) " + str(data["articles"][3]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][3]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][3]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][3]["url"])
                                  hasil += "\n\n(5) " + str(data["articles"][4]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][4]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][4]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][4]["url"])
                                  hasil += "\n\n(6) " + str(data["articles"][5]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][5]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][5]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][5]["url"])
                                  path = data["articles"][3]["urlToImage"]
                                  cl.sendText(kirim, str(hasil))
                                  cl.sendImageWithURL(kirim, str(path))

                        elif rfuText.lower().startswith("data birth: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                tanggal = rfuText.replace("data birth: ","")
                                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                                data=r.text
                                data=json.loads(data)
                                lahir = data["data"]["lahir"]
                                usia = data["data"]["usia"]
                                ultah = data["data"]["ultah"]
                                zodiak = data["data"]["zodiak"]
                                cl.sendText(kirim," I N F O R M A S I \n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n  I N F O R M A S I ")

                        elif rfuText.lower().startswith("urban: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                sep = rfuText.split(" ")
                                judul = rfuText.replace(sep[0] + " ","")
                                url = "http://api.urbandictionary.com/v0/define?term="+str(judul)
                                with requests.session() as s:
                                    s.headers["User-Agent"] = random.choice(Mozilla["userAgent"])
                                    r = s.get(url)
                                    data = r.text
                                    data = json.loads(data)
                                    cu = "Urban Result\n\n"
                                    cu += "\nText: "+ data["tags"][0]
                                    cu += ","+ data["tags"][1]
                                    cu += ","+ data["tags"][2]
                                    cu += ","+ data["tags"][3]
                                    cu += ","+ data["tags"][4]
                                    cu += ","+ data["tags"][5]
                                    cu += ","+ data["tags"][6]
                                    cu += ","+ data["tags"][7]
                                    cu += "\n[1]\nAuthor: "+str(data["list"][0]["author"])+"\n"
                                    cu += "\nWord: "+str(data["list"][0]["word"])+"\n"
                                    cu += "\nLink: "+str(data["list"][0]["permalink"])+"\n"
                                    cu += "\nDefinition: "+str(data["list"][0]["definition"])+"\n"
                                    cu += "\nExample: "+str(data["list"][0]["example"])+"\n"
                                    cl.sendText(kirim, str(cu))

                        elif rfuText.lower().startswith("sslink: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                 website = msg.text.replace("sslink: ","")
                                 response = requests.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link="+website+"")
                                 data = response.json()
                                 pictweb = data['result']
                                 cl.sendImageWithURL(kirim, pictweb)

                        elif rfuText.lower().startswith("maps: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                location = rfuText.lower().replace("maps: ","")
                                with requests.session() as web:
                                    web.headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                    rfu = web.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(urllib.parse.quote(location)))
                                    data = rfu.text
                                    data = json.loads(data)
                                    if data[0] != "" and data[1] != "" and data[2] != "":
                                        link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                        ret_ = "Check Location\n"
                                        ret_ += "\n Lokasi : " + data[0]
                                        ret_ += "\n Google Maps : " + link
                                        ret_ += "\n\nSearch Location Success"
                                    else:
                                        ret_ = "Searching Location Error or Location Tidak Ditemukan"
                                    cl.sendText(kirim,str(ret_))

                        elif rfuText.lower().startswith("cekcuaca: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                weather = rfuText.lower().replace("cekcuaca: ","")
                                with requests.session() as web:
                                    web.headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                    rfu = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(weather)))
                                    data = rfu.text
                                    data = json.loads(data)
                                    if "result" not in data:
                                        ret_ = "Cheking Weather\n"
                                        ret_ += "\nSuhu : " + data[1].replace("Suhu : ","")
                                        ret_ += "\nLokasi : " + data[0].replace("Temperatur di kota ","")
                                        ret_ += "\nKelembaban : " + data[2].replace("Kelembaban : ","")
                                        ret_ += "\nTekanan Udara : " + data[3].replace("Tekanan udara : ","")
                                        ret_ += "\nKecepatan Angin : " + data[4].replace("Kecepatan angin : ","")
                                        ret_ += "\n\nSearching Weather Success"
                                    else:
                                        ret_ = "Checking Weather Error or Not Found Location"
                                    cl.sendText(kirim, str(ret_))

                        elif rfuText.lower().startswith("jadwalshalat: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                shalat = rfuText.lower().replace("jadwalshalat: ","")
                                with requests.session() as web:
                                    web.headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                    rfu = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(shalat)))
                                    data = rfu.text
                                    data = json.loads(data)
                                    if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashar : " and data[4] != "Maghrib : " and data[5] != "Isha : ":
                                        ret_ = "Jadwal Shalat\n"
                                        ret_ += "\nLocation : " + data[0]
                                        ret_ += "\n " + data[1]
                                        ret_ += "\n " + data[2]
                                        ret_ += "\n " + data[3]
                                        ret_ += "\n " + data[4]
                                        ret_ += "\n " + data[5]
                                        ret_ += "\n\nJadwal Shalat Wilayah"
                                    else:
                                        ret_ = "Jadwa Shalat Wilayah Error or Not Found Location" 
                                    cl.sendText(kirim, str(ret_))

                        elif rfuText.lower().startswith("idline: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                 msgg = rfuText.replace('idline: ','')
                                 conn = cl.findContactsByUserid(msgg)
                                 if True:
                                    cl.sendText(kirim,"Link User : https://line.me/ti/p/~" + msgg)
                                    cl.sendMessage(kirim, None, contentMetadata={'mid': conn.mid}, contentType=13)
                                    contact = cl.getContact(conn.mid)
                                    cl.sendImageWithURL(kirim,"http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                                    cover = cl.getProfileCoverURL(conn.mid)
                                    cl.sendImageWithURL(kirim, cover)
                                    cl.mentionWithRFU(kirim,conn.mid,"Tag User\n","")

                        elif rfuText.lower().startswith("say-id: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    isi = rfuText.lower().replace('say-id: ','')
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp.mp3')
                                    cl.sendAudio(kirim, 'temp.mp3')
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

                        elif rfuText.lower().startswith("say-en: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    isi = rfuText.lower().replace('say-en: ','')
                                    tts = gTTS(text=isi, lang='en', slow=False)
                                    tts.save('temp.mp3')
                                    cl.sendAudio(kirim, 'temp.mp3')
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

                        elif rfuText.lower().startswith("say-jp: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    isi = rfuText.lower().replace('say-jp: ','')
                                    tts = gTTS(text=isi, lang='ja', slow=False)
                                    tts.save('temp.mp3')
                                    cl.sendAudio(kirim, 'temp.mp3')
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

                        elif rfuText.lower().startswith("say-ar: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    isi = rfuText.lower().replace('say-ar: ','')
                                    tts = gTTS(text=isi, lang='ar', slow=False)
                                    tts.save('temp.mp3')
                                    cl.sendAudio(kirim, 'temp.mp3')
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

                        elif rfuText.lower().startswith("say-ko: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    isi = rfuText.lower().replace('say-ko: ','')
                                    tts = gTTS(text=isi, lang='ko', slow=False)
                                    tts.save('temp.mp3')
                                    cl.sendAudio(kirim, 'temp.mp3')
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

                        elif rfuText.lower().startswith("apakah: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    txt = ['iya','tidak','bisa jadi','mungkin saja','tidak mungkin','au ah gelap']
                                    isi = random.choice(txt)
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp2.mp3')
                                    cl.sendAudio(kirim, 'temp2.mp3')
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

                        elif rfuText.lower().startswith("kapan: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    txt = ['kapan kapan','besok','satu abad lagi','Hari ini','Tahun depan','Minggu depan','Bulan depan','Sebentar lagi']
                                    isi = random.choice(txt)
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp2.mp3')
                                    cl.sendAudio(kirim, 'temp2.mp3')
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

                        elif rfuText.lower().startswith("wikipedia: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    wiki = rfuText.lower().replace("wikipedia: ","")
                                    wikipedia.set_lang("id")
                                    pesan="Title ("
                                    pesan+=wikipedia.page(wiki).title
                                    pesan+=")\n\n"
                                    pesan+=wikipedia.summary(wiki, sentences=1)
                                    pesan+="\n"
                                    pesan+=wikipedia.page(wiki).url
                                    cl.sendText(kirim, pesan)
                                except:
                                    try:
                                        pesan="Over Text Limit! Please Click link\n"
                                        pesan+=wikipedia.page(wiki).url
                                        cl.sendText(kirim, pesan)
                                    except Exception as e:
                                        cl.sendText(kirim, str(e))

                        elif rfuText.lower().startswith("kalender"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                cl.sendMessage(kirim, readTime)

                        elif rfuText.lower().startswith("gambar: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    query = rfuText.replace("gambar: ", "")
                                    query = query.replace(" ", "+")
                                    gambar = cl.download_image(query)
                                    cl.sendImageWithURL(kirim, gambar)
                                except Exception as e:
                                    cl.sendText(kirim, str(e))                                    

                        elif rfuText.lower().startswith("youtube: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    query = rfuText.replace("youtube: ", "")
                                    query = query.replace(" ", "+")
                                    x = cl.youtube(query)
                                    cl.sendText(kirim, x)
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

#--------------------------------- TRANSLATOR -------------------------------------------------#

                        elif rfuText.lower().startswith("indonesian: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                sep = rfuText.split(" ")
                                isi = rfuText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='id')
                                text = hasil.text
                                cl.sendMessage(kirim, "Translator Indonesian\n\n" + str(text))

                        elif rfuText.lower().startswith("english: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                sep = rfuText.split(" ")
                                isi = rfuText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='en')
                                text = hasil.text
                                cl.sendMessage(kirim, "Translator English\n\n" + str(text))

                        elif rfuText.lower().startswith("korea: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                    sep = rfuText.split(" ")
                                    isi = rfuText.replace(sep[0] + " ","")
                                    translator = Translator()
                                    hasil = translator.translate(isi, dest='ko')
                                    text = hasil.text
                                    cl.sendMessage(kirim, "Translator Korea\n\n" + str(text))

                        elif rfuText.lower().startswith("japan: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                sep = rfuText.split(" ")
                                isi = rfuText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='ja')
                                text = hasil.text
                                cl.sendMessage(kirim, "Translator Japan\n\n" + str(text))

                        elif rfuText.lower().startswith("thailand: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                sep = rfuText.split(" ")
                                isi = rfuText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='th')
                                text = hasil.text
                                cl.sendMessage(kirim, "Translator Thailand\n\n" + str(text))

                        elif rfuText.lower().startswith("arab: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                sep = rfuText.split(" ")
                                isi = rfuText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='ar')
                                text = hasil.text
                                cl.sendMessage(kirim, "Translator Saudi Arabia\n\n" + str(text))

                        elif rfuText.lower().startswith("malaysia: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                sep = rfuText.split(" ")
                                isi = rfuText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='ms')
                                text = hasil.text
                                cl.sendMessage(kirim, "Translator Malaysia\n\n" + str(text))

                        elif rfuText.lower().startswith("jawa: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                sep = rfuText.split(" ")
                                isi = rfuText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='jw')
                                text = hasil.text
                                cl.sendMessage(kirim, "Translator Jawa\n\n" + str(text))

    except Exception as error:
        print (error)

#-------------------------------------------- FINNISHING SCRIP ------------------------------------------------#

while True:
    try:
        Operation = RIDEN.singleTrace(count=50)
        if Operation is not None:
            for fast in Operation:
                RIDEN.setRevision(fast.revision)
                thread1 = threading.Thread(target=RIDEN_FAST_USER, args=(fast,))#self.OpInterrupt[fast.type], args=(fast,)
                thread1.start()
                thread1.join()
    except Exception as error:
        print (error)
