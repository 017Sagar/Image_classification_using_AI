from simple_image_download import simple_image_download as sim

my_downloader = sim.Downloader()

my_downloader.directory = 'my_dir/'
# Change File extension type
my_downloader.extensions = '.jpg'
print(my_downloader.extensions)

my_downloader.download('Ktm', limit=20)
my_downloader.download('Royal Enfield', limit=20)
my_downloader.download('yamaha', limit=20)
my_downloader.download('TVS',limit=20)