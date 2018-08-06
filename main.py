from braille import braille_dict

def converter(text):
	word_list = []
	for word in text:
		word_list.append(braille_dict[word])
	result = '\n\n'.join(word_list)
	return result


def main():
	text = input("Text：")
	print(converter(text))

if __name__ == '__main__':
	main()

