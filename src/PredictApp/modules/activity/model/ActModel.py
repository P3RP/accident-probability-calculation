import torch.nn as nn


def ConvBlock(in_channels, out_channels):
    layers = [nn.Conv2d(in_channels, out_channels, kernel_size=2, padding="same"),
              nn.ReLU(),
              nn.Conv2d(out_channels, out_channels, kernel_size=3, padding=1),
              nn.BatchNorm2d(out_channels),
              nn.ReLU(inplace=True),
              nn.MaxPool2d(2),
              ]
    return nn.Sequential(*layers)


class ActModel(nn.Module):
    def __init__(self, input_size=3, num_classes=10):
        super(ActModel, self).__init__()
        self.model = nn.Sequential(
            ConvBlock(in_channels=input_size, out_channels=64),
            ConvBlock(in_channels=64, out_channels=128),
            ConvBlock(in_channels=128, out_channels=256),
            ConvBlock(in_channels=256, out_channels=512),
        )

        self.fully_connected_layer = nn.Sequential(
            nn.Dropout(0.5),
            nn.Flatten(),
            nn.Linear(512 * 4 * 4, 500),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(500, num_classes),
            nn.Softmax(1),
        )

    def forward(self, x):
        output = self.model(x)
        output = self.fully_connected_layer(output)
        return output
