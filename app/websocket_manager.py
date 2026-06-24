from fastapi import WebSocket
from typing import Dict, Set
from redis import Redis

class ConnectionManager:
    def __init__(self, redis: Redis):
        self.active_connections: Dict[str, Set[WebSocket]] = {}
        self.redis = redis

    async def connect(self, websocket: WebSocket, room: str):
        await websocket.accept()
        if room not in self.active_connections:
            self.active_connections[room] = set()
        self.active_connections[room].add(websocket)

    async def disconnect(self, websocket: WebSocket, room: str):
        self.active_connections[room].remove(websocket)

    async def send_message(self, message: str, room: str):
        for connection in self.active_connections[room]:
            await connection.send_text(message)