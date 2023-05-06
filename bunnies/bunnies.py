def print_bunny_pyramid():
    word = "KITTY"
    word2 = "BUNNY"
    word3 = "SNAIL"
    word4 = "BIRD"
    for i in range(1, 11):
        spaces = " ~ " * (11 - i)
        layer_word = " ".join([word] * i)
        print(spaces + layer_word + spaces)
    sneak_kiss(3)

def sneak_kiss(count):
    for i in range(1,count):
        print("sneak kiss!")
    
sneak_kiss(3)
print_bunny_pyramid()

