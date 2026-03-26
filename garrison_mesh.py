# Cassaiglobal Genesis - Garrison Mesh
# Function: Decentralized P2P Communication

class MeshNode:
    def __init__(self, user_id):
        self.user_id = user_id
        self.peers = []

    def broadcast_emergency(self, signal):
        """Hopping the signal from phone to phone without a central server."""
        for peer in self.peers:
            print(f"Propagating {signal} to {peer}...")
        return "Signal Distributed across the Garrison."

node = MeshNode("GARRISON_HERO_7")
