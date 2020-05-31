import requests

link = 'https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/resnet50_coco_best_v2.0.1.h5'
file_name = 'resnet50_coco_best_v2.0.1.h5'

r = requests.get(link, stream = True)

count = 0
with open(file_name, 'wb') as f:
	for chunk in r.iter_content(chunk_size = 1024*1024):
		count=count+1
		if count%5 == 0: 
			print("In Progress..") 
		
		if chunk: 
			f.write(chunk)

print("%s downloaded!\n"%file_name)