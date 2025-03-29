{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNTzYL4pjb2rcFzF11t0RXm",
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
        "<a href=\"https://colab.research.google.com/github/Rajath-R-Prasad/Python-DSA/blob/main/PDSA_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#timer function\n",
        "import time\n",
        "class Timer:\n",
        "  def __init__(self):\n",
        "    self.start_time=None\n",
        "    self.elapsed_time=None\n",
        "  def start(self):\n",
        "    if self.start_time is not None:\n",
        "      raise TimerError(\"timer is running . use .stop()\")\n",
        "    self.start_time=time.perf_counter()\n",
        "\n",
        "  def stop(self):\n",
        "    if self.start_time is None:\n",
        "      raise TimerError(\"Timer has not started,use .start()\")\n",
        "    self.elapsed_time=time.perf_counter()-self.start_time\n",
        "    self.start_time=None\n",
        "\n",
        "  def elapsed(self):\n",
        "    if self.elapsed_time is None:\n",
        "      raise TimerError(\"timer has not yet started. use .start()\")\n",
        "    return(self.elapsed_time)\n",
        "  def __str__(self):\n",
        "    return (str(self.elapsed_time))"
      ],
      "metadata": {
        "id": "zhX6axHg5pMz"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "#BINARY SEARCH\n"
      ],
      "metadata": {
        "id": "trt5K1D685hu"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#binary search implementation\n",
        "def binarysearch(v,l):\n",
        "  if l==[]:\n",
        "    return False\n",
        "  m=len(l)//2\n",
        "  if v==l[m]:\n",
        "    return True\n",
        "  elif v<l[m]:\n",
        "    return binarysearch(v,l[:m])\n",
        "  else:\n",
        "    return binarysearch(v,l[m+1:])"
      ],
      "metadata": {
        "id": "h1KtWzus2ZeT"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "t=Timer()\n",
        "t.start()\n",
        "print(binarysearch(890,[1,4,9,11,14,15,17,18,23,24,25,27,28,29,31,32,34,36,37,40,56,78,79,80,81,82,85,86,89,90,92,100,112,344,456,678,689,711,723,724,768,890]))\n",
        "t.stop()\n",
        "print(t)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KsRoqIbF3S3z",
        "outputId": "39f4f1aa-eccb-450c-ed0c-f6e5197c0c66"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n",
            "0.0002014770002460864\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# SORTING ALGORITHMS"
      ],
      "metadata": {
        "id": "jIIBErys9D27"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "- Selection Sort"
      ],
      "metadata": {
        "id": "IRumcUS8BXch"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#SELECTION SORT\n",
        "def selectionsort(l):\n",
        "  n=len(l)\n",
        "  if n<1:\n",
        "    return l\n",
        "  for i in range(n):\n",
        "    mpos=i\n",
        "    for j in range(i+1,n):\n",
        "      if l[j]<l[mpos]:\n",
        "        mpos=j\n",
        "    (l[i],l[mpos])=(l[mpos],l[i])\n",
        "  return l\n"
      ],
      "metadata": {
        "id": "LT4MHnzp9Ifo"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "t=Timer()\n",
        "t.start()\n",
        "print(selectionsort([34,67,12,35,56,90,44,567,23,89,32,67,46,222,33,987,56,788,445,2,335]))\n",
        "t.stop()\n",
        "print(t)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EWZYjteA-mti",
        "outputId": "c211bf7d-6df8-40cb-be94-bd8d350a92fa"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[2, 12, 23, 32, 33, 34, 35, 44, 46, 56, 56, 67, 67, 89, 90, 222, 335, 445, 567, 788, 987]\n",
            "0.00017694000007395516\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "- Insertion Sort"
      ],
      "metadata": {
        "id": "ZQ7lFtnpBcyM"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def insertionsort(l):\n",
        "  n=len(l)\n",
        "  if n<1:\n",
        "    return l\n",
        "  for i in range(n):\n",
        "    j=i\n",
        "    while(j>0 and l[j]<l[j-1]):\n",
        "      (l[j],l[j-1])=(l[j-1],l[j])\n",
        "      j-=1\n",
        "  return l"
      ],
      "metadata": {
        "id": "SXQgtIfBBgxR"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "t=Timer()\n",
        "t.start()\n",
        "print(insertionsort([34,67,12,35,56,90,44,567,23,89,32,67,46,222,33,987,56,788,445,2,335]))\n",
        "t.stop()\n",
        "print(t)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VswpSTG3CsMC",
        "outputId": "5064a757-9490-4aa6-9a3e-34035ff0052f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[2, 12, 23, 32, 33, 34, 35, 44, 46, 56, 56, 67, 67, 89, 90, 222, 335, 445, 567, 788, 987]\n",
            "0.0016889130001800368\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Linked-lists\n"
      ],
      "metadata": {
        "id": "TViJeash03LY"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#Implementation of Linked-lists\n",
        "class Node:\n",
        "  def __init__(self,data=None,next=None):\n",
        "    self.data=data\n",
        "    self.next=next"
      ],
      "metadata": {
        "id": "KpganmtS1I3f"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "class LinkedList():\n",
        "  def __init__(self):\n",
        "    self.head=None\n",
        "\n",
        "  def print(self):\n",
        "      if self.head is None:\n",
        "          print(\"Linked list is empty\")\n",
        "          return\n",
        "      itr = self.head\n",
        "      llstr = ''\n",
        "      while itr:\n",
        "          llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)\n",
        "          itr = itr.next\n",
        "      print(llstr)\n",
        "\n",
        "  def get_length(self):\n",
        "    count=0\n",
        "    itr=self.head\n",
        "    while itr:\n",
        "      count+=1\n",
        "      itr=itr.next\n",
        "    return count\n",
        "\n",
        "  def insert_at_beg(self,data):\n",
        "    node=Node(data,self.head)\n",
        "    self.head=node\n",
        "\n",
        "  def insert_at_end(self,data):\n",
        "    if self.head is None:\n",
        "      self.head=Node(data,None)\n",
        "      return\n",
        "    itr=self.head\n",
        "    while itr.next:\n",
        "      itr=itr.next\n",
        "    itr.next=Node(data,None)\n",
        "\n",
        "  def insert_at(self,index,data):\n",
        "    if index<0 or index>self.get_length():\n",
        "      raise Exception (\"Invalid Index\")\n",
        "    if index==0:\n",
        "      self.insert_at_beg(data)\n",
        "      return\n",
        "\n",
        "    count=0\n",
        "    itr=self.head\n",
        "    while itr:\n",
        "\n",
        "      if count==index-1:\n",
        "        node=Node(data,itr.next)\n",
        "        itr.next=node\n",
        "        break\n",
        "      itr=itr.next\n",
        "      count+=1\n",
        "  def remove_at(self,index):\n",
        "    if index<0 or index>self.get_length():\n",
        "      print(\"invalid syntax\")\n",
        "\n",
        "    if index==0:\n",
        "      self.head=self.head.next\n",
        "      return\n",
        "\n",
        "    count=0\n",
        "    itr=self.head\n",
        "    while itr:\n",
        "      if count==index-1:\n",
        "          itr.next=itr.next.next\n",
        "          break\n",
        "      itr=itr.next\n",
        "      count+=1\n",
        "\n",
        "  def insert_values(self,data_list):\n",
        "    self.head=None\n",
        "    for data in data_list:\n",
        "      self.insert_at_end(data)"
      ],
      "metadata": {
        "id": "I3Lk_d625PY5"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "ll=LinkedList()\n",
        "ll.insert_at_beg(3)\n",
        "ll.insert_at_end(4)\n",
        "ll.insert_at_end(2)\n",
        "ll.insert_at_end(6)\n",
        "ll.insert_at(2,7)\n",
        "ll.insert_at(0,5)\n",
        "ll.insert_at(4,\"hello\")\n",
        "ll.insert_at(1,\"hi\")\n",
        "ll.insert_at(3,8)\n",
        "ll.insert_at(5,78)\n",
        "ll.print()\n",
        "ll.get_length()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kqT6eUVR5087",
        "outputId": "e982d31d-c197-47aa-9796-29fe3bc7dba1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5 --> hi --> 3 --> 8 --> 4 --> 78 --> 7 --> hello --> 2 --> 6\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "10"
            ]
          },
          "metadata": {},
          "execution_count": 142
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "ll1=LinkedList()\n",
        "ll1.insert_values([3,5,6,8,9])\n",
        "ll1.insert_at_beg(7)\n",
        "ll1.insert_at(5,1)\n",
        "ll1.insert_at(3,89)\n",
        "ll1.insert_at(4,\"linkedlist\")\n",
        "ll1.print()\n",
        "ll1.get_length()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qiDYwh3XQN9z",
        "outputId": "7f68a3d2-806f-48f8-88ab-69d4b68893cf"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "7 --> 3 --> 5 --> 89 --> linkedlist --> 6 --> 8 --> 1 --> 9\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "9"
            ]
          },
          "metadata": {},
          "execution_count": 146
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Graph and Trees"
      ],
      "metadata": {
        "id": "TRoo06AeDVG4"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "3BUQnM71xrMK"
      },
      "outputs": [],
      "source": [
        "#queue implementation\n",
        "class queue():\n",
        "  def __init__(self):\n",
        "    self.queue=[]\n",
        "  def isempty(self):\n",
        "    return self.queue==[]\n",
        "  def enqueue(self,v):\n",
        "    self.queue.append(v)\n",
        "  def dequeue(self):\n",
        "    v=None\n",
        "    if not self.isempty():\n",
        "      v=self.queue[0]\n",
        "      self.queue=self.queue[1:]\n",
        "    return v\n",
        "  def __str__(self):\n",
        "    return (self.queue==[])"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#stack implementation\n",
        "class stack:\n",
        "  def ___init__(self):\n",
        "    self.stack=[]\n",
        "    def issempty(self):\n",
        "      return (self.stack==[])\n",
        "    def push(self,v):\n",
        "      self.stack.append(v)\n",
        "    def pop(self):\n",
        "      v=None\n",
        "      if not self.isempty():\n",
        "        v=self.stack.pop()\n",
        "      return v"
      ],
      "metadata": {
        "id": "qa7gOKFWzt3N"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Adjacency List Implementation\n",
        "\n",
        "def adjlist(V,E):\n",
        "  size=len(V)\n",
        "  Alist={}\n",
        "  for i in range(size):\n",
        "    Alist[i]=[]\n",
        "  for (i,j) in E:\n",
        "    Alist[i].append(j)\n",
        "  return (Alist)"
      ],
      "metadata": {
        "id": "AkKXlRHDDyDX"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "- BFS Implementation"
      ],
      "metadata": {
        "id": "cVqztuJDFBMT"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#BFS implementation\n",
        "def BFS(Alist,v):\n",
        "  (level,parent)=({},{})\n",
        "  for each_vertex in Alist.keys():\n",
        "    parent[each_vertex]=-1\n",
        "    level[each_vertex]=-1\n",
        "  q=queue()\n",
        "  level[v]=0\n",
        "  q.enqueue(v)\n",
        "  while not q.isempty():\n",
        "    curr_vertex=q.dequeue()\n",
        "    for adj_vertex in Alist[curr_vertex]:\n",
        "      if level[adj_vertex]==-1:\n",
        "        parent[adj_vertex]=curr_vertex\n",
        "        level[adj_vertex]=level[curr_vertex]+1\n",
        "  return (level,parent)\n"
      ],
      "metadata": {
        "id": "jtywPRfHE0Mz"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "AList ={0: [1, 2], 1: [3, 4], 2: [4, 3], 3: [4], 4: []}\n",
        "print(BFS(AList,0))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2lGYYmqOi_Tf",
        "outputId": "842fe3c2-ab87-4aa1-9a60-d60f4d33ed7e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "({0: 0, 1: 1, 2: 1, 3: -1, 4: -1}, {0: -1, 1: 0, 2: 0, 3: -1, 4: -1})\n"
          ]
        }
      ]
    }
  ]
}