import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")



BAN = int(os.environ.get("BAN", "498459845"))
DELETE_AFTER = int(os.environ.get("DELETE_AFTER", 86400)) #seconds
NOTIFICATION_TIME = int(os.environ.get('NOTIFICATION_TIME', 86400)) #seconds
AUTO_DELETE = os.environ.get("AUTO_DELETE", True) #ON/OFF
DELETE_INFORM = os.environ.get("INFORM" , "Successfully DELETED !!")
NOTIFICATION = os.environ.get("NOTIFICATION" ,f"𝚃𝚑𝚒𝚜 𝙵𝚒𝚕𝚎 𝚆𝚒𝚕𝚕 𝙱𝚎 𝚍𝚎𝚕𝚎𝚝𝚎𝚍 𝙸𝚗 {DELETE_AFTER}")
GET_INFORM = os.environ.get("GET_INFORM" , "File was deleted after {DELETE_AFTER} seconds. Use the button below to GET FILE AGAIN.")



#Your API ID & API HASH from my.telegram.org [https://youtu.be/gZQJ-yTMkEo?si=H4NlUUgjsIc5btzH]
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "14031130"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "e24c9b194237b7874ee602d782521a67")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002298431361"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7201053234"))

#Port
PORT = os.environ.get("PORT", "8585")

#Database 
#Database [https://youtu.be/qFB0cFqiyOM?si=fVicsCcRSmpuja1A]
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://ankushdeb91:WpbkXkwE0rL98h7q@cluster0.cpl3y.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#Shortner (token system) 
# check my discription to help by using my refer link of shareus.io
# 

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "shortxlinks.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "26c58ac6c7879cf25966a3f6fc999c9c1e3c9315")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID", "https://t.me/akmoviefile0/18") # shortxlink ka tut_vid he 

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "0"))
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "𝑯𝒆𝒍𝒍𝒐! <a href='tg://user?id={id}'><b>{first}</b></a>\n 𝑰 𝒂𝒎 𝒚𝒐𝒖𝒓 𝑴𝒐𝒗𝒊𝒆 𝑷𝒓𝒐𝒗𝒊𝒅𝒆𝒓 𝑭𝒊𝒍𝒆 𝑩𝒐𝒕. 𝑰 𝒂𝒎 𝒉𝒆𝒓𝒆 𝒕𝒐 𝒐𝒇𝒇𝒆𝒓 𝒚𝒐𝒖 𝒂 𝒗𝒂𝒔𝒕 𝒄𝒐𝒍𝒍𝒆𝒄𝒕𝒊𝒐𝒏 𝒐𝒇 𝒕𝒉𝒆 𝒍𝒂𝒕𝒆𝒔𝒕 𝒃𝒍𝒐𝒄𝒌𝒃𝒖𝒔𝒕𝒆𝒓𝒔, 𝒕𝒊𝒎𝒆𝒍𝒆𝒔𝒔 𝒄𝒍𝒂𝒔𝒔𝒊𝒄𝒔, 𝒂𝒏𝒅 𝒉𝒊𝒅𝒅𝒆𝒏 𝒈𝒆𝒎𝒔. 𝑮𝒆𝒕 𝒓𝒆𝒂𝒅𝒚 𝒕𝒐 𝒅𝒊𝒗𝒆 𝒊𝒏𝒕𝒐 𝒕𝒉𝒆 𝒘𝒐𝒓𝒍𝒅 𝒐𝒇 𝒄𝒊𝒏𝒆𝒎𝒂 𝒂𝒕 𝒚𝒐𝒖𝒓 𝒄𝒐𝒏𝒗𝒆𝒏𝒊𝒆𝒏𝒄𝒆.\n𝑻𝒉𝒂𝒏𝒌 𝒚𝒐𝒖 𝒇𝒐𝒓 𝒋𝒐𝒊𝒏𝒊𝒏𝒈 𝒐𝒖𝒓 𝒄𝒉𝒂𝒏𝒏𝒆𝒍, 𝒂𝒏𝒅 𝒆𝒏𝒋𝒐𝒚 𝒕𝒉𝒆 𝒔𝒉𝒐𝒘!")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7201053234").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "𝙹𝚘𝚒𝚗 𝙾𝚞𝚛 𝙼𝚘𝚟𝚒𝚎 𝙲𝚑𝚊𝚗𝚗𝚎𝚕!\n\n𝙴𝚡𝚙𝚎𝚛𝚒𝚎𝚗𝚌𝚎 𝚝𝚑𝚎 𝚋𝚎𝚜𝚝 𝚒𝚗 𝚌𝚒𝚗𝚎𝚖𝚊 𝚠𝚒𝚝𝚑 𝚘𝚞𝚛 𝚎𝚡𝚌𝚕𝚞𝚜𝚒𝚟𝚎 𝚖𝚘𝚟𝚒𝚎 𝚌𝚑𝚊𝚗𝚗𝚎𝚕. 𝙶𝚊𝚒𝚗 𝚊𝚌𝚌𝚎𝚜𝚜 𝚝𝚘 𝚝𝚑𝚎 𝚕𝚊𝚝𝚎𝚜𝚝 𝚋𝚕𝚘𝚌𝚔𝚋𝚞𝚜𝚝𝚎𝚛𝚜, 𝚝𝚒𝚖𝚎𝚕𝚎𝚜𝚜 𝚌𝚕𝚊𝚜𝚜𝚒𝚌𝚜, 𝚊𝚗𝚍 𝚑𝚒𝚍𝚍𝚎𝚗 𝚐𝚎𝚖𝚜. 𝚂𝚝𝚎𝚙 𝚒𝚗𝚝𝚘 𝚊 𝚠𝚘𝚛𝚕𝚍 𝚘𝚏 𝚎𝚗𝚍𝚕𝚎𝚜𝚜 𝚎𝚗𝚝𝚎𝚛𝚝𝚊𝚒𝚗𝚖𝚎𝚗𝚝.\n 𝙹𝚘𝚒𝚗 𝚝𝚑𝚎 𝙲𝚑𝚊𝚗𝚗𝚎𝚕 𝙽𝚘𝚠!")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "This video/Photo/anything is available on the internet. We LeakHubd or its subsidiary channel doesn't produce any of them.")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "𝙳𝚘𝚗𝚝 𝙳𝚘 𝙰𝚐𝚊𝚒𝚗 𝙸'𝚕𝚕 𝙺𝚒𝚕𝚕 𝚈𝚘𝚞 "

ADMINS.append(OWNER_ID)
ADMINS.append(7201053234)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
