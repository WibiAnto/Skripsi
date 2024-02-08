#Make Root Directory
import bing_image_downloader.downloader as tools
root_dir = 'Data'


#Make Categorical Directory
jenis = ["Monstera Adansonii", "Monstera Borsigiana", "Monstera Deliciosa Variegata"]
for item in jenis:
    tools.download(item, limit = 100, output_dir = root_dir, adult_filter_off = True, filter = "photo")