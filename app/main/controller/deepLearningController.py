import numpy as np
import torch
# import matplotlib.pyplot as plt
from flask_restx import Namespace, Resource
from torchvision import transforms, datasets, utils
from app.main.batch_training.cnn import CNN

api = Namespace("dl", description="deeplearning related operations")


@api.route("/imgClassificationByCNN")
class file(Resource):
    @api.doc("imgClassificationByCNN")
    def post(self):
        classes = ('plane', 'car', 'bird', 'cat',
                   'deer', 'dog', 'frog', 'horse', 'ship', 'truck')
        BATCH_SIZE = 32
        # CIFAR_NET_PATH = "./data/CIFAR_10/cifar_net_10.pth"
        CIFAR_NET_PATH = "./data/CIFAR_10/cifar_net_20.pth"

        data_transform = transforms.Compose([
            transforms.Resize((32, 32)),
            transforms.ToTensor()
        ])

        test_dataset = datasets.ImageFolder(root='./uploads/image_folder',
                                            transform=data_transform)

        test_loader = torch.utils.data.DataLoader(
            test_dataset, batch_size=BATCH_SIZE, shuffle=True)

        print('@@@@@ len = ', len(test_dataset),
              ', test_dataset = ', test_dataset)
        dataiter = iter(test_loader)
        images, label = dataiter.next()

        # 이미지를 출력합니다.
        # test_images = utils.make_grid(images)
        # test_images = test_images / 2 + 0.5     # unnormalize
        # npimg = test_images.numpy()
        # plt.imshow(np.transpose(npimg, (1, 2, 0)))
        # plt.show()

        net = CNN()
        net.load_state_dict(torch.load(CIFAR_NET_PATH))
        outputs = net(images)
        _, predicted = torch.max(outputs, 1)

        print('@@@@@@@@@@ Predicted: ', ' '.join('%5s' % classes[predicted[j]]
                                                 for j in range(1)))
        print(predicted)

        return {"result": classes[predicted[0]]}
