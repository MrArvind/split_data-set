import os, random

def create_dir(dir_path):
    if not os.path.isfile(dir_path):
        os.makedirs(dir_path)

def image_files(image_dir):
    create_dir('images')
    create_dir('images/train')
    create_dir('images/test')
    file_size = 200
    loop_index = 1
    file_data = int(0.1 * file_size)
    test_array_sample = random.sample(range(file_size),k = file_data)
    
    for root, dir, files in os.walk(image_dir):
        for name in files:
            for f in os.listdir(image_dir):
                if (f.split('.')[1]=='jpg'):
                    loop_index += 1
                    print(loop_index,f)
                    if loop_index in test_array_sample:
                        new_path = os.path.join(name , image_dir)
                        os.rename(image_dir, 'images/train/'+ name + f)
                       
                    else:
                        print('print')
image_files(Path)
