from urllib.request import urlopen
from random import choices, randint
import matplotlib.pyplot as plt



def generate_name(data: list[str]) -> dict:
	bigram_count = {}
	for name in data:
		# Берет первую букву
		if name[0] in bigram_count:
			bigram_count[name[0]] += 1
		else:
			bigram_count[name[0]] = 1

		# Берет последнюю букву
		if name[-1] in bigram_count:
			bigram_count[name[-1]] += 1
		else:
			bigram_count[name[-1]] = 1

		# Берет буквы с шагом 2, начиная с 0, но заканчивая на len - 1, \
		# так как без минуса последним элементом будет самая последняя буква, что уже есть в словаре
		for bi in range(len(name) - 1):
			if name[bi:bi+2] in bigram_count:
				bigram_count[name[bi:bi+2]] += 1
			else:
				bigram_count[name[bi:bi+2]] = 1

	return bigram_count


def visualization(bigrams: list[str], weights: list[int]) -> None:
	figure, axis = plt.subplots(figsize = (30,8))
	axis.grid()
	plt.plot(bigrams, weights)
	plt.xticks(ha="right", fontsize=8, rotation=75)
	# Вывожу только первые 30 биграмм, так как значения оси "x" лезут друг на друга
	plt.xlim(0, 30)
	plt.show()


if __name__ == '__main__':
	# Читает данные из URL-а в бинарном виде, преобразует в ASCII и создает список (сепарация по переносу строки)
	url = "https://file.notion.so/f/s/fbbe6c40-a3f2-4a58-a90b-d8004f62fdcc/names.txt?id=27b23c03-0edc-4e08-8751-77f02aaac186&table=block&spaceId=7c849ae7-f9f9-4efe-9968-3fab523bf9e5&expirationTimestamp=1683316405266&signature=kHkIY9IOYGRQq1Et5QWKn9photCJ3-PyMwfTDk_12yU&downloadName=names.txt"
	data = urlopen(url).read()
	data = data.decode('ascii').split("\n")

	# Убирает последний элемент, являющийся пустой строкой
	del data[-1]


	bigrams_with_weights = generate_name(data=data)
	bigrams = list(bigrams_with_weights.keys())
	weights = list(bigrams_with_weights.values())


	# Генерирует 5 имен. \
	# Функция choices выбирает на рандом биграмму (используя веса) и для 1 имени может сделать это от 2 до 3 раз.
	for x in range(5):
		generated_name = choices(bigrams, weights, k = randint(2, 4))
		print('GENERATED NAME ->', ''.join(generated_name))


	visualization(bigrams=bigrams, weights=weights)


	# Хоть и непонятно выводит, но блин как же красиво в терминале)). Оставлю так
	for k, v in bigrams_with_weights.items():
		print(k, '->', v, end = " || ")