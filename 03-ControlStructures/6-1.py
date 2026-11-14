text = "This is a sample text."
vowels = "aeiouAEIOU"
vowel_count = 0
i = 0 # w pętli while sam muszę pilnować indeksu znaku, zaczynam od zera

while i < len(text):
    if text[i] in vowels: # sprawdzam czy znak na pozycji 'i' znajduje się w zestawie samogłosek
        vowel_count += 1
    i += 1 # przesuwam się do następnego znaku w tekście

print(f"The number of vowels in the text is: {vowel_count}")