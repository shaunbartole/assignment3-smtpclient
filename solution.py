import socket
from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"
    # mailserver = ('127.0.0.1', 1025)

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    clientSocket = socket(AF_INET, socket.SOCK_STREAM)
    clientSocket.connect(1025, '127.0.0.1')

    recv = clientSocket.recv(1024).decode()
    # print(recv) #You can use these print statement to validate return codes from the server.
    # if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Shaun\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print(recv1)
    # if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    messageFromCommand = "MAIL FROM:<test.test.com>\r\n"
    clientSocket.send(messageFromCommand.encode())
    recv2 = clientSocket.recv(1024).decode()

    # Send RCPT TO command and handle server response.
    RCPTToCommand = "RCPT TO:<shaun.test.com>\r\n"
    clientSocket.send(RCPTToCommand.encode())
    recv3 = clientSocket.recv(1024).decode()

    # Send DATA command and handle server response.
    data = "DATA\r\n"
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024).decode()

    # Send message data.
    sendData = "Subject: Hope This Works\r\n"
    clientSocket.send(sendData.encode())
    clientSocket.send(msg.encode())
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()

    # Message ends with a single period, send message end and handle server response.
    clientSocket.send(endmsg.encode())
    recv6 = clientSocket.recv(1024).decode()

    # Send QUIT command and handle server response.
    quit = "QUIT\r\n"
    clientSocket.send(quit.encode())
    recv7 = clientSocket.recv(1024).decode()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
