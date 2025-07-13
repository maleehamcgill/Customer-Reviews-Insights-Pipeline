{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPlvQHhWrMhYqGX9wBOHr82",
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
        "<a href=\"https://colab.research.google.com/github/maleehamcgill/Customer-Reviews-Insights-Pipeline/blob/etl/process_reviews.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "cCfl6a8xnkG6"
      },
      "outputs": [],
      "source": [
        "import openai\n",
        "import os\n",
        "from dotenv import load_dotenv\n",
        "\n",
        "load_dotenv()\n",
        "openai.api_key = os.getenv(\"OPENAI_API_KEY\")\n",
        "\n",
        "def analyze_review(text):\n",
        "    prompt = f\"Review: \\\"{text}\\\"\\nReturn sentiment (Positive, Neutral, Negative) and key topics as comma-separated list.\"\n",
        "    response = openai.ChatCompletion.create(\n",
        "        model=\"gpt-3.5-turbo\",\n",
        "        messages=[{\"role\": \"user\", \"content\": prompt}]\n",
        "    )\n",
        "    return response.choices[0].message.content\n"
      ]
    }
  ]
}