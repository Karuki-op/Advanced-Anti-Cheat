import time
from minecraft.networking.connection import Connection
from minecraft.networking.packets import clientbound

class AntiCheat:
    def __init__(self, server_ip, server_port, username):
        self.connection = Connection(server_ip, server_port, username=username)
        self.players = {}
        self.max_speed = 10  # Set maximum allowed speed

    def handle_player_position(self, packet):
        player_uuid = packet.data["player_uuid"]
        x, y, z = packet.data["position"]

        if player_uuid not in self.players:
            self.players[player_uuid] = {"last_pos": (x, y, z), "last_time": time.time()}
            return

        last_pos = self.players[player_uuid]["last_pos"]
        last_time = self.players[player_uuid]["last_time"]
        current_time = time.time()
        distance = ((x - last_pos[0]) ** 2 + (y - last_pos[
