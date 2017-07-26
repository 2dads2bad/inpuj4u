import wget
url='http://eerikinpujsound.com/legacy/releases_zipped/inpuj%r.zip'
for i in range(101):
    print(url % str(i).zfill(3))
