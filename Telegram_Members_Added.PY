import time
import json
from telethon.sync import TelegramClient
from telethon.errors import FloodWaitError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import ChannelParticipantsRecent
import colorama
from colorama import Fore
import asyncio
import random

# Initialize colorama
colorama.init(autoreset=True)

# Display the banner with colors and developer details
def display_banner():
    banner = f"""
{Fore.YELLOW} $$$$$$$$\        $$\            $$$$$$\  $$$$$$$\   $$$$$$\  $$\      $$\  
{Fore.CYAN} \__$$  __|       $$ |          $$  __$$\ $$  __$$\ $$  __$$\ $$$\    $$$ |  
{Fore.GREEN}     $$ | $$$$$$\  $$ | $$$$$$\  $$ /  \__|$$ |  $$ |$$ /  $$ |$$$$\  $$$$ |  
{Fore.BLUE}     $$ |$$  __$$\ $$ |$$  __$$\ $$ |$$$$\ $$$$$$$  |$$$$$$$$ |$$\$$\$$ $$ |  
{Fore.RED}     $$ |$$$$$$$$ |$$ |$$$$$$$$ |$$ |\_$$ |$$  __$$< $$  __$$ |$$ \$$$  $$ |  
{Fore.MAGENTA}     $$ |$$   ____|$$ |$$   ____|$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |\$  /$$ |  
{Fore.YELLOW}     $$ |\$$$$$$$\ $$ |\$$$$$$$\ \$$$$$$  |$$ |  $$ |$$ |  $$ |$$ | \_/ $$ |  
{Fore.CYAN}     \__| \_______|\__| \_______| \______/ \__|  \__|\__|  \__|\__|     \__|   

{Fore.YELLOW}  --- Developed By: Secure_Horizon --- 
{Fore.GREEN}  GitHub: https://github.com/chamidu200
{Fore.CYAN}  YouTube: https://www.youtube.com/@chamidunimsara20052
{Fore.RED}  Website: https://securehorizon.kesug.com/?i=1
"""
    print(banner)

# Configurations
API_ID = 29535298
API_HASH = '432c585b7173e5baaf0207ffb6535e8d'
SOURCE_GROUP = 'CyberTubeEthical'  # Replace with Source Group Username
TARGET_GROUP = 'xxxxxxxxxxxxghm'  # Replace with Target Group Username
DELAY_BETWEEN_ADDS = 30  # Increased delay between each user add

# Load or create approved members list
approved_members_file = 'approved_members.json'
try:
    with open(approved_members_file, 'r') as f:
        approved_members = json.load(f)
except FileNotFoundError:
    approved_members = []

def save_approved_members():
    with open(approved_members_file, 'w') as f:
        json.dump(approved_members, f)

# Progress bar function with improvement
def print_progress_bar(added, total):
    percentage = (added / total) * 100
    bar_length = 50
    block = int(round(bar_length * percentage / 100))
    progress = "#" * block + "-" * (bar_length - block)
    print(f"{Fore.CYAN}[{progress}] {percentage:.2f}% Complete", end='\r')

# Intelligent retry mechanism
async def add_member_with_retry(client, user, retries=5):
    for attempt in range(retries):
        try:
            await client(InviteToChannelRequest(TARGET_GROUP, [user]))
            approved_members.append(user.id)
            save_approved_members()
            print(f"{Fore.GREEN}➕ Successfully added {user.first_name} ({user.id})")
            return True
        except FloodWaitError as e:
            wait_time = e.seconds + random.randint(5, 30)  # Add a random delay to avoid bot-like behavior
            print(f"{Fore.RED}⏳ Rate limited! Waiting {wait_time} seconds...")
            time.sleep(wait_time)
        except UserPrivacyRestrictedError:
            print(f"{Fore.MAGENTA}🔒 Cannot add {user.first_name}, privacy settings restricted.")
            return False
        except Exception as e:
            print(f"{Fore.RED}❌ Error adding {user.first_name}: {str(e)}")
            return False
    print(f"{Fore.RED}❌ Failed to add {user.first_name} after {retries} attempts.")
    return False

async def fetch_members(client):
    print(f"{Fore.GREEN}🚀 Fetching members from source group...")
    members = []
    try:
        async for user in client.iter_participants(SOURCE_GROUP, filter=ChannelParticipantsRecent):
            if user.bot or user.deleted:
                continue
            members.append(user)
    except Exception as e:
        print(f"{Fore.RED}⚠️ Error fetching members: {e}")
    return members

async def add_members(client, members):
    total_members = len(members)
    added = 0

    for idx, user in enumerate(members):
        if user.id in approved_members:
            print(f"{Fore.YELLOW}✅ Skipping {user.first_name}, already added.")
            added += 1
            print_progress_bar(added, total_members)
            continue

        print(f"{Fore.GREEN}➕ Adding {user.first_name} ({user.id}) to {TARGET_GROUP}...")
        if await add_member_with_retry(client, user):
            added += 1
            print_progress_bar(added, total_members)
        else:
            print(f"{Fore.RED}Failed to add {user.first_name}, skipping.")
        time.sleep(DELAY_BETWEEN_ADDS)

async def send_group_message(client):
    try:
        message = "👋 Welcome new members! Be active & enjoy the community!"
        await client.send_message(TARGET_GROUP, message)
        print(f"{Fore.GREEN}✅ Group message sent successfully!")
    except Exception as e:
        print(f"{Fore.RED}⚠️ Error sending group message: {e}")

async def main():
    display_banner()  # Display the banner

    # User selection for mode
    print(f"{Fore.YELLOW}Select mode to add members:")
    print(f"{Fore.GREEN}1. Automatic Mode")
    print(f"{Fore.CYAN}2. Manual Mode")
    
    mode_choice = input(f"{Fore.YELLOW}Enter your choice (1/2): ").strip()

    if mode_choice == '1':
        mode = 'automatic'
        print(f"{Fore.GREEN}Automatic mode selected!")
    elif mode_choice == '2':
        mode = 'manual'
    else:
        print(f"{Fore.RED}Invalid input! Exiting...")
        return
    
    # Ask for phone number
    phone = input(f"{Fore.YELLOW}Please enter your phone number (with country code): ").strip()
    
    # Start client with the phone number
    async with TelegramClient('new_session', API_ID, API_HASH) as client:
        await client.start(phone=phone)  # Phone number or bot token
        members = await fetch_members(client)
        await add_members(client, members)
        await send_group_message(client)

if __name__ == '__main__':
    asyncio.run(main())
