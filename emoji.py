def emoji_convertor():
    words = message.split("\n")
 emoji = {
    "grinning": "😬",
    "laughing": "😂",
    "smiling": "😁",
    "sad": "😔",
    "angry": "😡",
    "frowning": "☹️",
    "winking": "😉",
    "heart": "❤️"
 }
 
 output =""
 for word in words:
    output += emoji.get(word, word) + " "
    return output


message = input("> ")
print(emoji_convertor(message))
