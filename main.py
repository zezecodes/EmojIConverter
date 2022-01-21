print("Welcome to the Emoji Converter")
print("Please input any statement and include an emoji in the space below")

def emoji_converter(messageInput):
    messageOutput = messageInput.split(" ")
    emojis = {
    ":)": "😁",
	":(": "😞",
	":/": "😕",
	":|": "😐"  
    }
    output = ""
    for word in messageOutput:
        output += emojis.get(word, word) + " " 
    return output

message = input("Type your statement here - ")
print(emoji_converter(message))

