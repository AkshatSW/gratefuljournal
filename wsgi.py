# using render, server slows down on reactivation so restarting the server every hour

import os
import sys
from threading import Thread
import time
from app import app

def restart_server():
    print("Restarting server...")
    os.system("./restart_gunicorn.sh")

def keep_server_active():
    restart_interval = 3600  # Restart server every hour (3600 seconds)

    while True:
        print(f"Waiting for {restart_interval} seconds before restarting the server...")
        time.sleep(restart_interval)
        restart_server()

if __name__ == "__main__":
    # Start the keep_server_active thread
    keep_alive_thread = Thread(target=keep_server_active)
    keep_alive_thread.start()

    # Start the Flask app
    app.run()
