import requests
import os
import json
import time


def readImg(imgDirPath):
    print("开始添加图片...")
    images = []
    imgs = os.listdir(imgDirPath)
    i = 0
    for img in imgs:
        imgPath = imgDirPath+"/"+img
        i = i+1
        print(('images', ('image'+str(i)+'.jpg', open(imgPath, 'rb'), 'image/jpg')))
        images.append(
            ('images', ('image'+str(i)+'.jpg', open(imgPath, 'rb'), 'image/jpg')))

    return images


def autoWork():
    # 用户认证
    res = requests.post('http://localhost:8000/api/token-auth/',
                        data={'username': 'zj',
                              'password': 'zj.123'}).json()
    token = res['token']
    print(token)

    # 新建工程
    res = requests.post('http://localhost:8000/api/projects/',
                        headers={'Authorization': 'JWT {}'.format(token)},
                        data={'name': 'Hello WebODM!'}).json()
    project_id = res['id']

    print(project_id)

    # 新建一个task
    # images = [
    # ('images', ('image1.jpg', open('image1.jpg', 'rb'), 'image/jpg')),
    # ('images', ('image2.jpg', open('image2.jpg', 'rb'), 'image/jpg')),
    # # ...
    # ]
    images = readImg(r"D:\share\temp\test")
    options = json.dumps([
        {'name': "orthophoto-resolution", 'value': 24}
    ])

    res = requests.post('http://localhost:8000/api/projects/{}/tasks/'.format(project_id),
                        headers={'Authorization': 'JWT {}'.format(token)},
                        files=images,
                        data={
        'options': options
    }).json()

    task_id = res['id']

    # 启动task

    while True:
        res = requests.get('http://localhost:8000/api/projects/{}/tasks/{}/'.format(project_id, task_id),
                           headers={'Authorization': 'JWT {}'.format(token)}).json()

        # if res['status'] == status_codes.COMPLETED:
        #       print("Task has completed!")
        #       break
        # elif res['status'] == status_codes.FAILED:
        #       print("Task failed: {}".format(res))
        #       sys.exit(1)
        # else:
        #       print("Processing, hold on...")
        #       time.sleep(3)
        if (res['processing_node'] == None):
            print("没有可用节点")
            time.sleep(3)
        elif (res['status'] == 20):
            print("正在计算...")
            time.sleep(3)
        elif (res['status'] == 0):
            print("完成")
            break
        else:
            print(res)
            time.sleep(3)

    # 下载成果
    res = requests.get("http://localhost:8000/api/projects/{}/tasks/{}/download/orthophoto.tif".format(project_id, task_id),
                       headers={'Authorization': 'JWT {}'.format(token)},
                       stream=True)
    with open("orthophoto.tif", 'wb') as f:
        for chunk in res.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    print("Saved ./orthophoto.tif")


# readImg("/home/zj/桌面/img/test")
autoWork()
