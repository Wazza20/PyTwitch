import subprocess
import sys

def start_twitch_stream(stream_key, rtmp_server, mp4_file):
    # Define the stream URL with the RTMP server and the stream key
    stream_url = f"rtmp://{rtmp_server}/app/{stream_key}"

    # Set the key frame interval (GOP size) in seconds
    gop_size = 2

    # Start the stream using FFmpeg with the specified GOP size and stream copy
    command = f"ffmpeg -stream_loop -1 -re -i {mp4_file} -c:v copy -x264opts keyint={gop_size*25}:no-scenecut -c:a copy -ar 44100 -b:a 128k -f flv {stream_url}"
    print("Starting the Twitch stream...")
    subprocess.call(command, shell=True)
    print("Twitch stream ended.")

def stop_twitch_stream():
    # Terminate the ffmpeg process
    subprocess.call("pkill -f ffmpeg", shell=True)
    print("Twitch stream stopped.")

# Set your Twitch stream key and RTMP server
twitch_stream_key = "YourTwitchKey"
rtmp_server = "YourTwitchServer"

# Set the MP4 file to loop in the stream
mp4_file = "YourMP$File"

# Check the command line arguments
if len(sys.argv) > 1:
    command = sys.argv[1]
    if command == "start":
        # Start the Twitch stream with the specified MP4 file
        start_twitch_stream(twitch_stream_key, rtmp_server, mp4_file)
    elif command == "stop":
        # Stop the Twitch stream
        stop_twitch_stream()
    else:
        print("Invalid command. Usage: python script.py [start|stop]")
else:
    print("No command specified. Usage: python script.py [start|stop]")
