from pytube import YouTube

url = 'https://youtu.be/Eyx0Hvi1_Ng?list=TLPQMjgxMjIwMTk50FBhBFN9Og'
url = 'https://www.youtube.com/watch?v=9bZkp7q19f0'  #Gagnam Style
yt = YouTube(url)
print('Title: ' + yt.title)

res = yt.streams.all()
for i in res:
   print(i)


print('\n\n')
#print(yt.streams.filter(progressive=True).all())

#yt.streams[1].download()
#print(yt.streams.first())
print(type(res[1]))
#print('\n\n Downloading \n\n')
#res[1].download()

#down = <Stream: itag="137" mime_type="video/mp4" res="1080p" fps="30fps" vcodec="avc1.640028" acodec="mp4a.40.2">
#down = res[1]
#down.download()
#You can also specify a destination path:
#>>> stream.download('/tmp')