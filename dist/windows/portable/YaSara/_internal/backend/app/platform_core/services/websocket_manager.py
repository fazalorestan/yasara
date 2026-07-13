class WebSocketManager:
    def __init__(self): self.connections=[]
    def register(self,c): self.connections.append(c)
    def count(self): return len(self.connections)
websocket_manager=WebSocketManager()
