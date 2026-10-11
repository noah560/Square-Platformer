import mido

mid = mido.MidiFile("song.mid")

data = []
for message in mid:
    if isinstance(message, mido.Message):
        if message.type == "note_on":
            data.append(["n", message.note, message.time])
        elif message.type == "note_off":
            data.append(["f", message.note, message.time])

# Format: type + milliseconds delay, note
data = [msg[0] + str(int(100*msg[2])) + "," + str(msg[1]) for msg in data]

print("|".join(data))
