def text_statistics_analyzer(txt_file):

    word_counts = {}
    max_count = 0

    status = {
        "total_lines": 0,
        "total_words": 0,
        "total_characters": 0,
        "most_repeated_word": ""
    }

    if txt_file.endswith(".txt"):
        try:
            with open(
                txt_file,
                "r",
                encoding="utf-8",
                errors="ignore"
            ) as file:

                for line in file:
                    status["total_lines"] += 1

                    words = line.split()
                    status["total_words"] += len(words)
                    status["total_characters"] += len(line)

                    for word in words:
                        if word in word_counts:
                            word_counts[word] += 1
                        else:
                            word_counts[word] = 1

            for word, count in word_counts.items():
                if max_count < count:
                    max_count = count
                    status["most_repeated_word"] = word

        except PermissionError:
            print("Access denied")

    return status


txt_file = input("Write a path: ")

result = text_statistics_analyzer(txt_file)

print(result)
