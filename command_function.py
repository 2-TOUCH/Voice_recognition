
import ctypes
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import webbrowser
import urllib.parse

def mute_unmute_device_sound():
   """
   Mutes the system sound on a Windows computer by simulating a key press
   of the 'mute' multimedia key.
   """
   print("Running...mute_device_sound")
   VK_VOLUME_MUTE = 0xAD
   KEYEVENTF_EXTENDEDKEY = 0x1
   KEYEVENTF_KEYUP = 0x2

   # Simulate the key press
   ctypes.windll.user32.keybd_event(VK_VOLUME_MUTE, 0, KEYEVENTF_EXTENDEDKEY, 0)

   # Simulate the key release
   ctypes.windll.user32.keybd_event(VK_VOLUME_MUTE, 0, KEYEVENTF_EXTENDEDKEY | KEYEVENTF_KEYUP, 0)


def unmute_device_sound():
    """
    Unmutes the system sound on a Windows computer by simulating a key press
    of the 'mute' multimedia key. This assumes the key acts as a toggle.
    """

    print("Running...unmute_device_sound")

    VK_VOLUME_MUTE = 0xAD
    KEYEVENTF_EXTENDEDKEY = 0x1
    KEYEVENTF_KEYUP = 0x2

    # Check if currently muted, then unmute
    if ctypes.windll.user32.GetKeyState(VK_VOLUME_MUTE) < 0:
        # Simulate the key press
        ctypes.windll.user32.keybd_event(VK_VOLUME_MUTE, 0, KEYEVENTF_EXTENDEDKEY, 0)

        # Simulate the key release
        ctypes.windll.user32.keybd_event(VK_VOLUME_MUTE, 0, KEYEVENTF_EXTENDEDKEY | KEYEVENTF_KEYUP, 0)


def change_volume(change_percent):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    
    # Get current volume
    current_volume = volume.GetMasterVolumeLevelScalar()
    # Calculate new volume
    new_volume = max(0, min(1, current_volume + change_percent))
    # Set new volume
    volume.SetMasterVolumeLevelScalar(new_volume, None)

def increase_volume():
    change_volume(0.20)  # Increase by 20%

def decrease_volume():
    change_volume(-0.20)  # Decrease by 20%


driver = None


def open_google():
    # Opens Google in a new tab of the default browser
    webbrowser.open_new_tab("https://www.google.com")


def search_google(query):
    # URL encode the query and open it in a new browser tab
    encoded_query = urllib.parse.quote(query)
    webbrowser.open_new_tab(f"https://www.google.com/search?q={encoded_query}")
