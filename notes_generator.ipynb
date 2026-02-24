{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPC2N7wkIlfUtSMnuv8+Kd0",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Padmasri-Nambi/GENERATIVE-AI-PROJECTS/blob/main/notes_generator.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QUTYde4wEZQv",
        "outputId": "66d4168b-4c8c-4887-a70e-2bb0ab2f905b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: transformers in /usr/local/lib/python3.12/dist-packages (5.0.0)\n",
            "Requirement already satisfied: filelock in /usr/local/lib/python3.12/dist-packages (from transformers) (3.24.2)\n",
            "Requirement already satisfied: huggingface-hub<2.0,>=1.3.0 in /usr/local/lib/python3.12/dist-packages (from transformers) (1.4.1)\n",
            "Requirement already satisfied: numpy>=1.17 in /usr/local/lib/python3.12/dist-packages (from transformers) (2.0.2)\n",
            "Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.12/dist-packages (from transformers) (26.0)\n",
            "Requirement already satisfied: pyyaml>=5.1 in /usr/local/lib/python3.12/dist-packages (from transformers) (6.0.3)\n",
            "Requirement already satisfied: regex!=2019.12.17 in /usr/local/lib/python3.12/dist-packages (from transformers) (2025.11.3)\n",
            "Requirement already satisfied: tokenizers<=0.23.0,>=0.22.0 in /usr/local/lib/python3.12/dist-packages (from transformers) (0.22.2)\n",
            "Requirement already satisfied: typer-slim in /usr/local/lib/python3.12/dist-packages (from transformers) (0.24.0)\n",
            "Requirement already satisfied: safetensors>=0.4.3 in /usr/local/lib/python3.12/dist-packages (from transformers) (0.7.0)\n",
            "Requirement already satisfied: tqdm>=4.27 in /usr/local/lib/python3.12/dist-packages (from transformers) (4.67.3)\n",
            "Requirement already satisfied: fsspec>=2023.5.0 in /usr/local/lib/python3.12/dist-packages (from huggingface-hub<2.0,>=1.3.0->transformers) (2025.3.0)\n",
            "Requirement already satisfied: hf-xet<2.0.0,>=1.2.0 in /usr/local/lib/python3.12/dist-packages (from huggingface-hub<2.0,>=1.3.0->transformers) (1.2.0)\n",
            "Requirement already satisfied: httpx<1,>=0.23.0 in /usr/local/lib/python3.12/dist-packages (from huggingface-hub<2.0,>=1.3.0->transformers) (0.28.1)\n",
            "Requirement already satisfied: shellingham in /usr/local/lib/python3.12/dist-packages (from huggingface-hub<2.0,>=1.3.0->transformers) (1.5.4)\n",
            "Requirement already satisfied: typing-extensions>=4.1.0 in /usr/local/lib/python3.12/dist-packages (from huggingface-hub<2.0,>=1.3.0->transformers) (4.15.0)\n",
            "Requirement already satisfied: typer>=0.24.0 in /usr/local/lib/python3.12/dist-packages (from typer-slim->transformers) (0.24.0)\n",
            "Requirement already satisfied: anyio in /usr/local/lib/python3.12/dist-packages (from httpx<1,>=0.23.0->huggingface-hub<2.0,>=1.3.0->transformers) (4.12.1)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.12/dist-packages (from httpx<1,>=0.23.0->huggingface-hub<2.0,>=1.3.0->transformers) (2026.1.4)\n",
            "Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.12/dist-packages (from httpx<1,>=0.23.0->huggingface-hub<2.0,>=1.3.0->transformers) (1.0.9)\n",
            "Requirement already satisfied: idna in /usr/local/lib/python3.12/dist-packages (from httpx<1,>=0.23.0->huggingface-hub<2.0,>=1.3.0->transformers) (3.11)\n",
            "Requirement already satisfied: h11>=0.16 in /usr/local/lib/python3.12/dist-packages (from httpcore==1.*->httpx<1,>=0.23.0->huggingface-hub<2.0,>=1.3.0->transformers) (0.16.0)\n",
            "Requirement already satisfied: click>=8.2.1 in /usr/local/lib/python3.12/dist-packages (from typer>=0.24.0->typer-slim->transformers) (8.3.1)\n",
            "Requirement already satisfied: rich>=12.3.0 in /usr/local/lib/python3.12/dist-packages (from typer>=0.24.0->typer-slim->transformers) (13.9.4)\n",
            "Requirement already satisfied: annotated-doc>=0.0.2 in /usr/local/lib/python3.12/dist-packages (from typer>=0.24.0->typer-slim->transformers) (0.0.4)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.12/dist-packages (from rich>=12.3.0->typer>=0.24.0->typer-slim->transformers) (4.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.12/dist-packages (from rich>=12.3.0->typer>=0.24.0->typer-slim->transformers) (2.19.2)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.12/dist-packages (from markdown-it-py>=2.2.0->rich>=12.3.0->typer>=0.24.0->typer-slim->transformers) (0.1.2)\n"
          ]
        }
      ],
      "source": [
        "!pip install transformers"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from transformers import pipeline\n",
        "notes_generator=pipeline('text-generation',model='gpt2')\n",
        "chapter=input(\"enter chapter name:\")\n",
        "\n",
        "prompt_notes = f\"\"\"\n",
        "write detailed study notes for {chapter}\n",
        "include explanation, example and key points\n",
        "\"\"\"\n",
        "detailed_notes=notes_generator(\n",
        "    prompt_notes,\n",
        "    max_length=300,\n",
        "    num_return_sequences=1\n",
        ")\n",
        "print(detailed_notes[0]['generated_text'])\n",
        "\n",
        "prompt_summary = f\"\"\"\n",
        "summarize the chapter: {chapter} in one page\n",
        "\"\"\"\n",
        "summary=notes_generator(\n",
        "    prompt_summary,\n",
        "    max_length=200,\n",
        "    num_return_sequences=1\n",
        ")\n",
        "print(\"\\n one-page summary \\n\")\n",
        "print(summary[0]['generated_text'])\n",
        "\n",
        "prompt_definition=f\"\"\"\n",
        "list important definitions and formulas from the chapter:{chapter}\n",
        "use bullet points\n",
        "\"\"\"\n",
        "definitions=notes_generator(\n",
        "    prompt_definition,\n",
        "    max_length=200,\n",
        "    num_return_sequences=1\n",
        ")\n",
        "print(\"\\n definitions and formulas:\")\n",
        "print(definitions[0]['generated_text'])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000,
          "referenced_widgets": [
            "ff947ee17f894958a3cc4bc5c534a1a9",
            "927e92f01b6a43a09ed93a05f253cbc2",
            "a5fa50afe7dc4afeb2328552a57b61c8",
            "a6e0d6260f544aec863bf0e304a692e7",
            "3dddd7887ce2464bbb74f5c69ce34ecd",
            "13103faddbc94056857a6953a4fccedc",
            "ed3971dcf042412d85fe39cd08efdd32",
            "aa47fa7f9711454586f60ee341a9323e",
            "be45e1e038b549c8a2a8641ecd160dfe",
            "dd5fd86e73984d419fb93ea04c3c21c0",
            "3d86446dae924d92a9eb01257fa6c758",
            "062415ead2a940689dc8886323d9ff50",
            "c7da4e14647b4fb186b9f964bc8fb9b4",
            "1122e978b0b7464f8d707aad42e850f7",
            "5390c8075f32431dbd8c36a4905533b1",
            "2e8e96bb70c246739727d6856e6f7446",
            "70fb13f7e2b64d0e96f701442d24e668",
            "1dd2cdd501f04173b3fc5e27a1820127",
            "14d61a703b8349ce9189bf59759f3714",
            "df958325ef3f4f078bf69f4c3d6309df",
            "6067693b133c48b2987d1077803a0ef7",
            "5a015a2ec010408d8b9e7d1eb613b1bd",
            "eceabb580cb849338619a7c3e919ac34",
            "142d8d3cd41d4b318c09ecf6b335dc28",
            "35de23dcb74b436aac1f8cffab298a1f",
            "896925a5d188414e87936617aab89638",
            "882a3fcbecdb4df8a2d2b8b5f59562cd",
            "41638e63e9234249bea53e957f97ab3d",
            "81d26f2d150c4ec0b96cc9442e464fde",
            "b0829da64c2146b98a561080a9aabc69",
            "3212e603228a4e019ec03d87c68190d3",
            "c9d67d3b68064ba8bb26789ae43cd76c",
            "9b3f83e929ed416599fec12087324b64",
            "d607d7994cf445dd9e2cffe0471ab669",
            "66ce85e83b954bceaa1b73dffb33949b",
            "aa554f490cf9481e940309390f61d47c",
            "2bc076b2c13c4b23b8f731d7c7dc4ed7",
            "f6b44b979e8f432ebd3f7bbb996b6979",
            "bb46368a3b4f43b099026f229c24b23e",
            "2735ef0e9d6f48bdb3b3dc6f748e45ca",
            "7443eab0fcba444587333bd9f7a163c2",
            "92acace19a4f418ab89996ef2cc64f7e",
            "bcd70953da064a1998d1cb279e57155e",
            "9b68a977061f4d2e876a180ae42292b4",
            "e978caf54e2140dd9cbffb5efb0583f6",
            "ae399acb29914dea91f91de6ea48620b",
            "6ac84886513e43acb4d3bd82187977aa",
            "440f3302713d45f192211f58fddfc6b9",
            "0a37061390fb4bfc8134762c9e0cc43e",
            "eab0f078894f47f5b3db5697d68cb3e9",
            "89ab1225b098465e890069787821e1bf",
            "85a8e06bca8245b7a9c5f7c1a98f8542",
            "f7aa0d649c1142b98c697b61030a43bc",
            "2264945c8d9d4dc1905e810f82eda7f4",
            "a57aa75f742648388b81ab1fc3f957c1",
            "675ea74ac5064f54aec7db06566837ff",
            "eb81dcb9d6214362a5750a58300e52df",
            "613ab20a181443cca1f97aacd03e8b8a",
            "f5239a1dec734849ab2c6b00beabe131",
            "0ed3fb17ae354d9f991bfbd31cc6673f",
            "9b017cbcbdd6481a88bf4ddb371803b6",
            "8072ce9b9bed459c869dce4c95a128bc",
            "20bccafdd16843dd9dd094d42aa819b1",
            "1adf9f445de640c4a0e9d777ca2969ac",
            "c8a0b730a5eb477a8e1f6e8827e47f96",
            "8351110a5c284ef09dba06a21d8df05f",
            "79f254639a404e11ae52d94164f35586",
            "164df66282ab4d50b1553ae8628b998a",
            "6333775ba8ce476eab6a407b0b756691",
            "43f09b48703d49d197744892075c7533",
            "004b0eda9ed04256873d86a72d76c9fa",
            "2069d11184fa458bad83780649eadf60",
            "293ee73ecc8a4c6d91d3db5087c9dc6e",
            "ffcff7045bb84d1187e85c74af34b3cf",
            "405a442778564dfaa8bd590315848df7",
            "d0b38eaf847444fca8547d2bc669ae52",
            "2e0bcb967bd54a66a6aacebe793a5ae5",
            "6bcf671a2416460d91240fb6fbb00c3e",
            "0ffa801cbb9e494294b01e50a15c3423",
            "59ac74dc042c424a82bed62f28a79a43",
            "3ab91e6f108c4bd5a0b90011f96f0845",
            "7844fcc937c84407968430ee10dea8fd",
            "7e59345741a54b0cbdd36ce1ab097f96",
            "d0172c9c27b0497ea924053bc6333df7",
            "2584cbbd1e7647ffb3c5d64dabe5052a",
            "798d29da9da14d2fad02e1bb92441553",
            "3cfa4bca8e204564972891ee1e09a68f",
            "395293cb6fb64397a2df12bd2f2835a1"
          ]
        },
        "id": "CI6XCWvEJ8nz",
        "outputId": "f6647035-250c-4a85-dd1d-1f074df07d9e"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.12/dist-packages/huggingface_hub/utils/_auth.py:94: UserWarning: \n",
            "The secret `HF_TOKEN` does not exist in your Colab secrets.\n",
            "To authenticate with the Hugging Face Hub, create a token in your settings tab (https://huggingface.co/settings/tokens), set it as secret in your Google Colab and restart your session.\n",
            "You will be able to reuse this secret in all of your notebooks.\n",
            "Please note that authentication is recommended but still optional to access public models or datasets.\n",
            "  warnings.warn(\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "config.json:   0%|          | 0.00/665 [00:00<?, ?B/s]"
            ],
            "application/vnd.jupyter.widget-view+json": {
              "version_major": 2,
              "version_minor": 0,
              "model_id": "ff947ee17f894958a3cc4bc5c534a1a9"
            }
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.\n",
            "WARNING:huggingface_hub.utils._http:Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "model.safetensors:   0%|          | 0.00/548M [00:00<?, ?B/s]"
            ],
            "application/vnd.jupyter.widget-view+json": {
              "version_major": 2,
              "version_minor": 0,
              "model_id": "062415ead2a940689dc8886323d9ff50"
            }
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "Loading weights:   0%|          | 0/148 [00:00<?, ?it/s]"
            ],
            "application/vnd.jupyter.widget-view+json": {
              "version_major": 2,
              "version_minor": 0,
              "model_id": "eceabb580cb849338619a7c3e919ac34"
            }
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "GPT2LMHeadModel LOAD REPORT from: gpt2\n",
            "Key                  | Status     |  | \n",
            "---------------------+------------+--+-\n",
            "h.{0...11}.attn.bias | UNEXPECTED |  | \n",
            "\n",
            "Notes:\n",
            "- UNEXPECTED\t:can be ignored when loading from different task/architecture; not ok if you expect identical arch.\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "generation_config.json:   0%|          | 0.00/124 [00:00<?, ?B/s]"
            ],
            "application/vnd.jupyter.widget-view+json": {
              "version_major": 2,
              "version_minor": 0,
              "model_id": "d607d7994cf445dd9e2cffe0471ab669"
            }
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "tokenizer_config.json:   0%|          | 0.00/26.0 [00:00<?, ?B/s]"
            ],
            "application/vnd.jupyter.widget-view+json": {
              "version_major": 2,
              "version_minor": 0,
              "model_id": "e978caf54e2140dd9cbffb5efb0583f6"
            }
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "vocab.json:   0%|          | 0.00/1.04M [00:00<?, ?B/s]"
            ],
            "application/vnd.jupyter.widget-view+json": {
              "version_major": 2,
              "version_minor": 0,
              "model_id": "675ea74ac5064f54aec7db06566837ff"
            }
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "merges.txt:   0%|          | 0.00/456k [00:00<?, ?B/s]"
            ],
            "application/vnd.jupyter.widget-view+json": {
              "version_major": 2,
              "version_minor": 0,
              "model_id": "79f254639a404e11ae52d94164f35586"
            }
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "tokenizer.json:   0%|          | 0.00/1.36M [00:00<?, ?B/s]"
            ],
            "application/vnd.jupyter.widget-view+json": {
              "version_major": 2,
              "version_minor": 0,
              "model_id": "6bcf671a2416460d91240fb6fbb00c3e"
            }
          },
          "metadata": {}
        },
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "enter chapter name:90\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "Passing `generation_config` together with generation-related arguments=({'num_return_sequences', 'max_length'}) is deprecated and will be removed in future versions. Please pass either a `generation_config` object OR all generation parameters explicitly, but not both.\n",
            "Setting `pad_token_id` to `eos_token_id`:50256 for open-end generation.\n",
            "Both `max_new_tokens` (=256) and `max_length`(=300) seem to have been set. `max_new_tokens` will take precedence. Please refer to the documentation for more information. (https://huggingface.co/docs/transformers/main/en/main_classes/text_generation)\n",
            "Setting `pad_token_id` to `eos_token_id`:50256 for open-end generation.\n",
            "Both `max_new_tokens` (=256) and `max_length`(=200) seem to have been set. `max_new_tokens` will take precedence. Please refer to the documentation for more information. (https://huggingface.co/docs/transformers/main/en/main_classes/text_generation)\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "write detailed study notes for 90\n",
            "include explanation, example and key points\n",
            "\n",
            "include explanation, example and key points write detailed study notes for 90 include explanation, example and key points\n",
            "\n",
            "include explanation, example and key points\n",
            "\n",
            "include explanation, example and key points\n",
            "\n",
            "include explanation, example and key points\n",
            "\n",
            "include explanation, example and key points\n",
            "\n",
            "include explanation, example and key points\n",
            "\n",
            "include explanation, example and key points\n",
            "\n",
            "include explanation, example and key points\n",
            "\n",
            "include explanation, example and key points\n",
            "\n",
            "include explanation, example and key points\n",
            "\n",
            "include explanation, example and key points\n",
            "\n",
            "include explanation, example and key points\n",
            "\n",
            "include explanation, example and key points\n",
            "\n",
            "include explanation, example and key points\n",
            "\n",
            "include explanation, example and key points\n",
            "\n",
            "include explanation, example and key points\n",
            "\n",
            "include explanation, example and key points\n",
            "\n",
            "include explanation, example and key points\n",
            "\n",
            "include explanation, example and key points\n",
            "\n",
            "include explanation, example and key points\n",
            "\n",
            "include explanation, example and key points\n",
            "\n",
            "include explanation, example and key points\n",
            "\n",
            "include explanation, example and key points\n",
            "\n",
            "include explanation, example and key points\n",
            "\n",
            "include explanation, example and key points\n",
            "\n",
            "include explanation, example and key points\n",
            "\n",
            "include explanation, example and key points\n",
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "Setting `pad_token_id` to `eos_token_id`:50256 for open-end generation.\n",
            "Both `max_new_tokens` (=256) and `max_length`(=200) seem to have been set. `max_new_tokens` will take precedence. Please refer to the documentation for more information. (https://huggingface.co/docs/transformers/main/en/main_classes/text_generation)\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            " one-page summary \n",
            "\n",
            "\n",
            "summarize the chapter: 90 in one page\n",
            "\n",
            "Chapter 1: \"Bondage\" by the two of them\n",
            "\n",
            "Chapter 2: \"Gangnam Style\" by the two of them\n",
            "\n",
            "Chapter 3: \"Bondage\" by the two of them\n",
            "\n",
            "Chapter 4: \"Bondage\" by the two of them\n",
            "\n",
            "Chapter 5: \"Bondage\" by the two of them\n",
            "\n",
            "Chapter 6: \"Bondage\" by the two of them\n",
            "\n",
            "Chapter 7: \"Bondage\" by the two of them\n",
            "\n",
            "Chapter 8: \"Bondage\" by the two of them\n",
            "\n",
            "Chapter 9: \"Bondage\" by the two of them\n",
            "\n",
            "Chapter 10: \"Bondage\" by the two of them\n",
            "\n",
            "Chapter 11: \"Bondage\" by the two of them\n",
            "\n",
            "Chapter 12: \"Bondage\" by the two of them\n",
            "\n",
            "Chapter 13: \"Bondage\" by the two of them\n",
            "\n",
            "Chapter 14: \"Bondage\" by the two of them\n",
            "\n",
            "Chapter 15: \"Bondage\" by the two of them\n",
            "\n",
            "Chapter 16: \"Bondage\" by the two of them\n",
            "\n",
            "Chapter 17: \"Bondage\" by the two of them\n",
            "\n",
            "\n",
            " definitions and formulas:\n",
            "\n",
            "list important definitions and formulas from the chapter:90\n",
            "use bullet points\n",
            "use bullet points to explain common problems with the definition\n",
            "use bullet points to list common problems with the definition\n",
            "use bullet points to explain common problems with the definition using bullet points to list common problems with the definition using bullet points to describe common problems with the definition using bullet points to describe common problems with the definition using bullet points to describe common problems with the definition using bullet points to describe common problems with the definition using bullet points to describe common problems with the definition using bullet points to describe common problems with the definition using bullet points to describe common problems with the definition using bullet points to describe common problems with the definition using bullet points to describe common problems with the definition using bullet points to describe common problems with the definition using bullet points to describe common problems with the definition using bullet points to describe common problems with the definition using bullet points to describe common problems with the definition using bullet points to describe common problems with the definition using bullet points to describe common problems with the definition using bullet points to describe common problems with the definition using bullet points to describe common problems with the definition using bullet points to describe common problems with the definition using bullet points to describe common problems with the definition using bullet points to describe common problems with the definition using bullet points to describe common problems with the definition using bullet points to\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "DI-YmsxtP1Ih"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
