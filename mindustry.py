#Source :https://github.com/RCR-OOP/pydustry.py
from socket import socket, create_connection, AF_INET, SOCK_DGRAM
from struct import unpack
from time import time
from dataclasses import dataclass

class Server:
    def __init__(
        self,
        server_host: str,
        server_port: int=6567):
        self.server = (server_host, server_port)
    def get_status(self, timeout: float=10.0):
        # * Инициализация сервера
        s = socket(AF_INET, SOCK_DGRAM)
        s.connect(self.server)
        s.settimeout(timeout)

        # * Создание и так понятно чего для чего
        info = {}

        # * Получение данных и замер
        s_time = time()
        s.send(b"\xfe\x01")
        data = s.recv(1024)
        e_time = time()

        # * Парсинг
        info["name"] = data[1:data[0]+1].decode("utf-8")
        data = data[data[0]+1:]
        info["map"] = data[1:data[0]+1].decode("utf-8")
        data = data[data[0]+1:]
        info["players"] = unpack(">i", data[:4])[0]
        data = data[4:]
        info["wave"] = unpack(">i", data[:4])[0]
        data = data[4:]
        info["version"] = unpack(">i", data[:4])[0]
        data = data[4:]
        info["vertype"] = data[1:data[0]+1].decode("utf-8")
        info["ping"] = round((e_time - s_time) * 1000)

        return info
