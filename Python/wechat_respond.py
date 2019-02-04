import itchat
from itchat.content import *

who_send = None

# 注册发给小冰的函数, TEXT是itchat.content里的文本类型
@itchat.msg_register(TEXT, isFriendChat=True)
def send_ice(msg):
    global who_send
    msg_text = msg['Text']
    who_send = msg['FromUserName']
    itchat.send(msg_text, xiaoice)

# 注册发给小冰的函数, PICTURE是itchat.content里的图片类型
@itchat.msg_register(PICTURE, isFriendChat=True)
def send_ice(msg):
    global who_send
    msg['Text'](msg['FileName'])
    who_send = msg['FromUserName']
    itchat.send('@img@%s' % msg['FileName'], xiaoice)

# 注册发给小冰的函数, RECORDING是itchat.content里的语音类型
@itchat.msg_register(RECORDING, isFriendChat=True)
def send_ice(msg):
    global who_send
    msg['Text'](msg['FileName'])
    who_send = msg['FromUserName']
    itchat.send('@fil@%s' % msg['FileName'], xiaoice)

# 注册从小冰发回来的消息, TEXT是itchat.content里的文本类型
@itchat.msg_register(TEXT, isMpChat=True)
def get_ice(msg):
    ice_msg = msg['Text']
    itchat.send(ice_msg, who_send)

# 注册从小冰发回来的消息, PICTURE是itchat.content里的图片类型
@itchat.msg_register(PICTURE, isMpChat=True)
def get_ice(msg):
    msg['Text'](msg['FileName'])
    ice_msg = msg['Text']
    itchat.send('@img@%s' % msg['FileName'], who_send)

# 注册从小冰发回来的消息, RECORDING是itchat.content里的语音类型
@itchat.msg_register(RECORDING, isMpChat=True)
def get_ice(msg):
    msg['Text'](msg['FileName'])
    itchat.send('@fil@%s' % msg['FileName'], who_send)

# hotReload可以保证在一段时期内, 不需要重复扫码
itchat.auto_login(hotReload=True)
# 获得小冰的用户ID, 注意这个ID每次都是不一样的~
xiaoice = itchat.search_mps(name='小冰')[0]['UserName']


itchat.run()
