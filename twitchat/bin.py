import os
from twitchat.chat import stream_channel
from twitchat.colors import colors


CHAN = '#{}'.format(os.environ.get('TWITCH_CHANNEL') or input('Channel: '))
NICK = os.environ.get('TWITCH_NICK') or input('Nickname: ')
PASS = os.environ.get('TWITCH_TOKEN') or input('Token: ')


def on_message(sender, message):
    print('{}: {}'.format(
        colors.OKGREEN + sender + colors.ENDC,
        message
    ))


def run():
    stream_channel(CHAN, NICK, PASS, on_message)
