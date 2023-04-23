from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent, ConnectEvent
import requests
from PIL import ImageTk, Image
import tkinter as tk

# GUI

# Create a new window
window = tk.Tk()

# Set the window title
window.title("My GUI")

# Set the window size
window.geometry("400x400")

# Add a label to the window
label = tk.Label(text="Hello, World!")
label.pack()

# Add a canvas to the window to display the user's profile picture and comment
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# Instantiate the client with the user's username
client: TikTokLiveClient = TikTokLiveClient(unique_id="@")

# Define how you want to handle specific events via decorator
@client.on("connect")
async def on_connect(_: ConnectEvent):
    print("✅✅✅Connected to Room ID:", client.room_id)

# Notice no decorator?
async def on_comment(event: CommentEvent):
    print(f"{event.user.nickname} -> {event.comment}")
    
    # Download the user's profile picture from the URL
    response = requests.get(event.user.avatar_url)
    img_data = response.content

    # Convert the image data to a PIL Image object
    img = Image.open(io.BytesIO(img_data))
    
    # Resize the image to a smaller size
    img = img.resize((50, 50))
    
    # Create a Tkinter-compatible image object
    img_tk = ImageTk.PhotoImage(img)
    
    # Clear the canvas
    canvas.delete("all")
    
    # Add the user's profile picture and comment to the canvas
    canvas.create_image(25, 25, anchor="nw", image=img_tk)
