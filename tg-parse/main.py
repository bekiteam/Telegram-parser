import random
import string
from telethon.sync import TelegramClient
from telethon.tl.types import InputMessagesFilterPhotos, InputMessagesFilterDocument

# set up the Telegram API client
api_id = 1 #REPLACE
api_hash = '###' #REPLACE 
client = TelegramClient('yoursession_file', api_id, api_hash)
client.start()


chat_id = -1001332389322 # Replace with your desired chat ID
num_posts = 1900 #number post dowload 1900

# fetch the last num_posts posts from the channel
posts = client.get_messages(chat_id, limit=num_posts)

# posts and download images to img folder and text to your txtname.txt
for post in posts:
    if post.media:
        # if the post has media (images, videos, etc.), download it to the img folder
        media = post.media
        if isinstance(media, list):
            # if there are multiple media items in the post download each one!
            for m in media:
                rand_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
                client.download_media(m, file=f'ex10/{post.id}_{rand_string}.jpg') #---REPLACE FOLDER
                if post.caption:
                    with open('te.txt', 'a', encoding='utf-8') as f: #---REPLACE FILE.TXT
                        f.write(post.caption + '\n')
        else:
            rand_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
            client.download_media(media, file=f'ex10/{post.id}_{rand_string}.jpg') #--REPLACE FOLDER