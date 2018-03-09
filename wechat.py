

from __future__ import unicode_literals

from wxpy import *
from wechat_sender import listen
bot = Bot(console_qr=True,cache_path=True)

my1 = bot.friends().search('吴震')[0]


listen(bot,receivers=my1,port=10003)
