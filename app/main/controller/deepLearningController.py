from flask_restx import Namespace, Resource

import torch
import torch.nn as nn
import torch.nn.functional as F

import torchvision.transforms as transforms
from torchvision import transforms, datasets

import numpy as np

import matplotlib.pyplot as plt
from app.main.model.cnn import CNN


api = Namespace("dl", description="deeplearning related operations")


@api.route("/imgClassificationByCNN")
class file(Resource):
    @api.doc("imgClassificationByCNN")
    def post(self):
        ''' 딥러닝 모델을 설계할 때 활용하는 장비 확인 '''
        if torch.cuda.is_available():
            DEVICE = torch.device('cuda')
        else:
            DEVICE = torch.device('cpu')
        print('Using PyTorch version:',
              torch.__version__, ' Device:', DEVICE)

        BATCH_SIZE = 32
        EPOCHS = 10
        CIFAR_DATA_PATH = "./data/CIFAR_10"

        ''' CIFAR10 데이터 다운로드 (Train set, Test set 분리하기) '''
        train_dataset = datasets.CIFAR10(root=CIFAR_DATA_PATH,
                                         train=True,
                                         download=True,
                                         transform=transforms.ToTensor())

        # TODO: 데이터가 바이너리로 되있어서 내가 임의로 이미지를 추가해줄수가없음..내가 업로드한 이미지 텐서형식으로 변경해주는 로직 추가해야됨
        test_dataset = datasets.CIFAR10(root=CIFAR_DATA_PATH,
                                        train=False,
                                        transform=transforms.ToTensor())

        train_loader = torch.utils.data.DataLoader(dataset=train_dataset,
                                                   batch_size=BATCH_SIZE,
                                                   shuffle=True)

        test_loader = torch.utils.data.DataLoader(dataset=test_dataset,
                                                  batch_size=BATCH_SIZE,
                                                  shuffle=False)

        classes = ('plane', 'car', 'bird', 'cat',
                   'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

        ''' 데이터 확인하기 (1) '''
        for (X_train, y_train) in train_loader:
            print('X_train:', X_train.size(), 'type:', X_train.type())
            print('y_train:', y_train.size(), 'type:', y_train.type())
            break

        ''' 데이터 확인하기 (2)
        TODO: 메인쓰레드 외부에서 실행할경우 플로팅 실패할수있다고 경고뜸
            -> 메인쓰레드로 넘겨서 실행하도록 바꿔야될듯
        '''
        pltsize = 1
        plt.figure(figsize=(10 * pltsize, pltsize))

        for i in range(10):
            plt.subplot(1, 10, i + 1)
            plt.axis('off')
            plt.imshow(np.transpose(X_train[i], (1, 2, 0)))
            plt.title(str(classes[y_train[i]]))
        plt.show()

        # 테스트 이미지 저장 -> 이거가지고 다시 맞춰보라고 업로드하면서 테스트 할꺼임
        for i in range(10):
            plt.figure(figsize=(pltsize, pltsize))
            plt.axis('off')
            plt.imshow(np.transpose(X_train[i], (1, 2, 0)))
            plt.savefig(f'test{i}.png')

        ''' Optimizer, Objective Function 설정하기 '''
        model = CNN().to(DEVICE)
        optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
        criterion = nn.CrossEntropyLoss()

        print(model)

        ''' CNN 모델 학습을 진행하며 학습 데이터에 대한 모델 성능을 확인하는 함수 정의 '''
        # def train(model, train_loader, optimizer, log_interval):
        #     model.train()
        #     for batch_idx, (image, label) in enumerate(train_loader):
        #         image = image.to(DEVICE)
        #         label = label.to(DEVICE)
        #         optimizer.zero_grad()
        #         output = model(image)
        #         loss = criterion(output, label)
        #         loss.backward()
        #         optimizer.step()

        #         if batch_idx % log_interval == 0:
        #             print("Train Epoch: {} [{}/{} ({:.0f}%)]\tTrain Loss: {:.6f}".format(
        #                 epoch, batch_idx * len(image),
        #                 len(train_loader.dataset), 100. *
        #                 batch_idx / len(train_loader),
        #                 loss.item()))

        ''' 학습되는 과정 속에서 검증 데이터에 대한 모델 성능을 확인하는 함수 정의 '''
        # def evaluate(model, test_loader):
        #     model.eval()
        #     test_loss = 0
        #     correct = 0

        #     with torch.no_grad():
        #         for image, label in test_loader:
        #             image = image.to(DEVICE)
        #             label = label.to(DEVICE)
        #             output = model(image)
        #             test_loss += criterion(output, label).item()
        #             prediction = output.max(1, keepdim=True)[1]
        #             correct += prediction.eq(label.view_as(prediction)
        #                                      ).sum().item()

        #     test_loss /= len(test_loader.dataset)
        #     test_accuracy = 100. * correct / len(test_loader.dataset)
        #     return test_loss, test_accuracy

        ''' CNN 학습 실행하며 Train, Test set의 Loss 및 Test set Accuracy 확인하기 '''
        # for epoch in range(1, EPOCHS + 1):
        #     train(model, train_loader, optimizer, log_interval=200)
        #     test_loss, test_accuracy = evaluate(model, test_loader)
        #     print("\n[EPOCH: {}], \tTest Loss: {:.4f}, \tTest Accuracy: {:.2f} % \n".format(
        #         epoch, test_loss, test_accuracy))

        return {"result": "success"}
