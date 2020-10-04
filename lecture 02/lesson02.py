{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 22\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Двадцать Два\n"
     ]
    }
   ],
   "source": [
    "number = input()\n",
    "dozens = number[0]   #Десятками у нас будет выступать 1-ый индекс number \n",
    "if len(number)==1:   #Проверим какой длины у нас число на входе, если Однозначное -> введем их\n",
    "    if dozens == \"0\":\n",
    "        print (\"Ноль\")\n",
    "    elif dozens == \"1\":\n",
    "        print (\"Один\")\n",
    "    elif dozens == \"2\":\n",
    "        print (\"Два\")\n",
    "    elif dozens == \"3\":\n",
    "        print (\"Три\")\n",
    "    elif dozens == \"4\":\n",
    "        print (\"Четыре\")\n",
    "    elif dozens == \"5\":\n",
    "        print (\"Пять\")\n",
    "    elif dozens == \"6\":\n",
    "        print (\"Шесть\")\n",
    "    elif dozens == \"7\":\n",
    "        print (\"Семь\")\n",
    "    elif dozens == \"8\":\n",
    "        print (\"Восемь\")\n",
    "    elif dozens == \"9\":\n",
    "        print (\"Девять\")\n",
    "    else:\n",
    "        print(\"Введите число от 0 до 99\")\n",
    "elif len(number)==2:       # Вторая проверка на длину, уже двузначные\n",
    "    units = number[1]\n",
    "    if units == \"0\":      #Зафиксируем значение единиц в двузначном числе\n",
    "        units=\"\"\n",
    "    elif units == \"1\": \n",
    "        units=\"Один\"\n",
    "    elif units==\"2\":\n",
    "         units=\"Два\"\n",
    "    elif units == \"3\":\n",
    "         units=\"Три\"\n",
    "    elif units ==\"4\":\n",
    "         units=\"Четыре\"\n",
    "    elif units==\"5\":\n",
    "         units=\"Пять\"\n",
    "    elif units==\"6\":\n",
    "         units=\"Шесть\"\n",
    "    elif units == \"7\":\n",
    "         units=\"Семь\"\n",
    "    elif units == \"8\":\n",
    "         units=\"Восемь\"\n",
    "    elif units == \"9\":\n",
    "         units=\"Девять\"\n",
    "    if dozens == \"2\":      #Зафиксируем десятки и просто будет прибавлять к ним строку с \"единицами\"\n",
    "        print(\"Двадцать \"+ \"\"+ units)\n",
    "    elif dozens == \"3\":\n",
    "        print(\"Тридцать \"+ \"\"+ units)\n",
    "    elif dozens == \"4\":\n",
    "        print(\"Сорок \"+ \"\"+ units)\n",
    "    elif dozens == \"5\":\n",
    "        print(\"Пятьдесят\"+ \"\"+ units)\n",
    "    elif dozens == \"6\":\n",
    "        print(\"Шестьдесят\"+ \"\"+ units)\n",
    "    elif dozens == \"7\":\n",
    "        print(\"Семдесят \"+ \"\"+ units)\n",
    "    elif dozens == \"8\":\n",
    "        print(\"Сорок \"+ \"\"+ units)\n",
    "    elif dozens ==\"9\":\n",
    "        print(\"Девяносто \"+ \"\"+ units)\n",
    "    else:\n",
    "        print (\"Введите число от 0 до 99\")\n",
    "        # Далее идут отбросы этой программы, вы поглядите на них...\n",
    "elif number==\"10\":\n",
    "    print (\"Десять\")\n",
    "elif number==\"11\":\n",
    "    print (\"Одиннадцать\")\n",
    "elif number==\"12\":\n",
    "    print (\"Двенадцать\")\n",
    "elif number==\"13\":\n",
    "    print (\"Тринадцать\")\n",
    "elif number==\"14\":\n",
    "    print (\"Четырнадцать\")\n",
    "elif number==\"15\":\n",
    "    print (\"Пятьнадцать\")\n",
    "elif number==\"16\":\n",
    "    print (\"Шестьнадцать\")\n",
    "elif number==\"17\":\n",
    "    print (\"Семьнадцать\")\n",
    "elif number==\"18\":\n",
    "    print (\"Восемьнадцать\")\n",
    "elif number==\"19\":\n",
    "    print (\"Девятьнадцать\")\n",
    "else:\n",
    "    print (\"ДА ВВЕДИ ТЫ УЖЕ ЧИСЛО\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
