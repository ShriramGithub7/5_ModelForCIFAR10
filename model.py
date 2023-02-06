{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPfNZPNLRhIz/5pAw/ytsod"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "id": "vUoBs-USLFgk"
      },
      "outputs": [],
      "source": [
        "import torch\n",
        "import torchvision\n",
        "from torchvision import datasets, transforms\n",
        "import albumentations as A\n",
        "import numpy as np\n",
        "import torch.nn as nn\n",
        "import torch.nn.functional as F\n",
        "\n",
        "class Net(nn.Module):\n",
        "    def __init__(self):\n",
        "        super(Net, self).__init__()\n",
        "\n",
        "        # Input block\n",
        "        self.convblock1 = nn.Sequential(\n",
        "            nn.Conv2d(3, 16, 3, padding=1),\n",
        "            nn.BatchNorm2d(16),\n",
        "            nn.ReLU(),\n",
        "            nn.Dropout(0.01)\n",
        "        )\n",
        "\n",
        "        # Convolution Block\n",
        "        self.convblock2 = nn.Sequential(\n",
        "            nn.Conv2d(16, 32, 3, padding=1),\n",
        "            nn.BatchNorm2d(32),\n",
        "            nn.ReLU(),\n",
        "            nn.Dropout(0.01)\n",
        "        )\n",
        "        self.convblock3 = nn.Sequential(\n",
        "            nn.Conv2d(32, 64, 3, stride=2),\n",
        "            nn.BatchNorm2d(64),\n",
        "            nn.ReLU(),\n",
        "            nn.Dropout(0.01)\n",
        "        )\n",
        "\n",
        "        # Convolution Block\n",
        "\n",
        "        self.convblock4 = nn.Sequential(\n",
        "            nn.Conv2d(64, 128, 3, stride=2, padding=1),\n",
        "            nn.BatchNorm2d(128),\n",
        "            nn.ReLU(),\n",
        "            nn.Dropout(0.01)\n",
        "        )\n",
        "\n",
        "        # Convolution Block with dilation\n",
        "        self.convblock5 = nn.Sequential(\n",
        "            nn.Conv2d(128, 64, 3, stride=2, dilation=1, padding=1),\n",
        "            nn.BatchNorm2d(64),\n",
        "            nn.ReLU(),\n",
        "            nn.Dropout(0.01)\n",
        "        )\n",
        "        self.convblock6 = nn.Sequential(\n",
        "            nn.Conv2d(64, 16, 3, padding=1),\n",
        "            nn.BatchNorm2d(16),\n",
        "            nn.ReLU(),\n",
        "            nn.Dropout(0.01)\n",
        "        )\n",
        "\n",
        "        self.convblock7 = nn.Sequential(\n",
        "            nn.Conv2d(16, 32, 3, padding=1),\n",
        "            nn.BatchNorm2d(32),\n",
        "            nn.ReLU(),\n",
        "            nn.Dropout(0.01)\n",
        "        )\n",
        "        self.gap = nn.Sequential(\n",
        "            nn.AvgPool2d(kernel_size=2, stride=2)\n",
        "        )\n",
        "        self.fc1 = nn.Linear(32 * 2 * 2, 64)\n",
        "        self.fc2 = nn.Linear(64, 10)\n",
        "\n",
        "    def forward(self, x):\n",
        "        x = self.convblock1(x)\n",
        "        x = self.convblock2(x)\n",
        "        x = self.convblock3(x)\n",
        "        x = self.convblock4(x)\n",
        "        x = self.convblock5(x)\n",
        "        x = self.convblock6(x)\n",
        "        x = self.convblock7(x)\n",
        "        x = self.gap(x)\n",
        "        x = x.view(-1, 32 * 2 * 2)\n",
        "        x = self.fc1(x)\n",
        "        x = self.fc2(x)\n",
        "\n",
        "        return F.log_softmax(x, dim=-1)\n"
      ]
    }
  ]
}