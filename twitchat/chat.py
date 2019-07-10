import os
import re
import socket


HOST = 'irc.twitch.tv'
PORT = 6667


def send_pong(con, msg):
    con.send(bytes('PONG %s\r\n' % msg, 'UTF-8'))


def send_nick(con, nick):
    con.send(bytes('NICK %s\r\n' % nick, 'UTF-8'))


def send_pass(con, password):
    con.send(bytes('PASS %s\r\n' % password, 'UTF-8'))


def join_channel(con, chan):
    con.send(bytes('JOIN %s\r\n' % chan, 'UTF-8'))


def get_sender(msg):
    result = ''
    for char in msg:
        if char == '!':
            break
        if char != ':':
            result += char
    return result


def get_message(msg):
    result = ''
    i = 3
    length = len(msg)
    while i < length:
        result += msg[i] + ' '
        i += 1
    result = result.lstrip(':')
    return result


def stream_channel(channel, nickname, token, callback):
    con = socket.socket()
    con.connect((HOST, PORT))

    send_pass(con, token)
    send_nick(con, nickname)
    join_channel(con, channel)

    data = ''

    while True:
        try:
            data = data + con.recv(1024).decode('UTF-8')
            data_split = re.split(r'[~\r\n]+', data)
            data = data_split.pop()

            for line in data_split:
                line = str.rstrip(line)
                line = str.split(line)

                if len(line) >= 1:
                    if line[0] == 'PING':
                        send_pong(con, line[1])

                    if line[1] == 'PRIVMSG':
                        sender = get_sender(line[0])
                        message = get_message(line)

                        callback(sender, message)

        except socket.error:
            print('Socket died')

        except socket.timeout:
            print('Socket timeout')
