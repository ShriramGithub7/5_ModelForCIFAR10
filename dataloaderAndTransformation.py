{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO79rMxeCiCURQKtiUn7rgt",
      "include_colab_link": true
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ShriramGithub7/5_ModelForCIFAR10/blob/main/dataloaderAndTransformation.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Apply Albumentation and transformation on dataset"
      ],
      "metadata": {
        "id": "iCyoTuFO6gwB"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "_tX5OkcW6UTD"
      },
      "outputs": [],
      "source": [
        "class DataTransform():\n",
        "    mean=(0.4914, 0.4822, 0.4465)\n",
        "    std=(0.2023, 0.1994, 0.2010)\n",
        "\n",
        "    def albumentations_transform(image):\n",
        "        image = np.array(image)\n",
        "        augmented = A.Compose(\n",
        "                    [A.HorizontalFlip(),\n",
        "                    A.ShiftScaleRotate(shift_limit=0.0625, scale_limit=0.1,rotate_limit=45),\n",
        "                    A.CoarseDropout(max_holes=1, max_height=16, max_width=16, min_holes=1,min_height=16, min_width=16,\n",
        "                              fill_value=np.mean(mean), mask_fill_value=None),\n",
        "            ])(image=image)[\"image\"]\n",
        "        return transforms.ToTensor()(augmented)\n",
        "\n",
        "    transform = transforms.Compose([\n",
        "        transforms.Lambda(albumentations_transform),\n",
        "        transforms.Normalize(mean, std),\n",
        "    ])\n",
        "\n",
        "    trainset = torchvision.datasets.CIFAR10(root='./data', train=True,\n",
        "                                            download=True, transform=transform)\n",
        "\n",
        "    batch_size = 4\n",
        "\n",
        "    trainloader = torch.utils.data.DataLoader(trainset, batch_size=batch_size,\n",
        "    shuffle=True, num_workers=2)\n",
        "\n",
        "    testset = torchvision.datasets.CIFAR10(root='./data', train=False, \n",
        "                                          download=True, transform=transform)\n",
        "\n",
        "    testloader = torch.utils.data.DataLoader(testset, batch_size=batch_size,\n",
        "    shuffle=False, num_workers=2)\n",
        "\n",
        "    classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog','frog', 'horse', 'ship', 'truck')"
      ]
    }
  ]
}