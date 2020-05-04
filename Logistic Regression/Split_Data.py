{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Split Data.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMhm7ggJmsMJiWDMxJliaSA",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
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
        "<a href=\"https://colab.research.google.com/github/Gauravhulmukh/All_ml_algorithm_from_scratch/blob/master/Logistic%20Regression/Split_Data.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Sq8FhSVSf5qH",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n",
        "from sklearn.model_selection import train_test_split"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "p4-pLHdzghsv",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "data = pd.read_csv('data.csv',header=None,names=['x1','x2','y'])\n",
        "train_data , test_data = train_test_split(data,test_size=0.2,shuffle=True)\n",
        "train_data.to_csv('train_dataset.csv',index=False)\n",
        "test_data.to_csv('test_dataset.csv',index=False)"
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}