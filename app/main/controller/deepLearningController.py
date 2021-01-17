import numpy as np
import torch
import matplotlib.pyplot as plt
from flask_restx import Namespace, Resource
from torchvision import transforms, datasets, utils
from app.main.batch_training.scratch import CNN

api = Namespace("dl", description="deeplearning related operations")


@api.route("/imgClassificationByCNN")
class file(Resource):
    @api.doc("imgClassificationByCNN")
    def post(self):
        classes = ('plane', 'car', 'bird', 'cat',
                   'deer', 'dog', 'frog', 'horse', 'ship', 'truck')
        BATCH_SIZE = 32
        CIFAR_NET_PATH = "./data/CIFAR_10/cifar_net_10.pth"

        data_transform = transforms.Compose([
            transforms.RandomSizedCrop(224),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225])
        ])

        test_dataset = datasets.ImageFolder(root='./uploads/car',
                                            transform=data_transform)

        test_loader = torch.utils.data.DataLoader(test_dataset,
                                                  batch_size=BATCH_SIZE, shuffle=True,
                                                  num_workers=4)

        dataiter = iter(test_loader)
        images, labels = dataiter.next()

        # 이미지를 출력합니다.
        test_images = utils.make_grid(images)
        test_images = test_images / 2 + 0.5     # unnormalize
        npimg = test_images.numpy()
        plt.imshow(np.transpose(npimg, (1, 2, 0)))
        plt.show()

        print('@@@@@@@@@ GroundTruth: ', ' '.join('%5s' %
                                                  classes[labels[j]] for j in range(1)))

        net = CNN()
        net.load_state_dict(torch.load(CIFAR_NET_PATH))
        outputs = net(images)

        _, predicted = torch.max(outputs, 1)

        print('@@@@@@@@@@ Predicted: ', ' '.join('%5s' % classes[predicted[j]]
                                                 for j in range(4)))

        return {"result": "success"}
