# source: chatgpt
# Define the corpus
corpus = [
    "<s> I am Sam </s>",
    "<s> Sam I am </s>",
    "<s> I do not like green eggs and ham </s>"
]

# Tokenize the corpus into trigrams and bigrams
trigrams = {}
bigrams = {}

for sentence in corpus:
    words = ['<s>'] + sentence.split() + ['</s>']  # Adding start and end tokens
    for i in range(len(words) - 2):
        # Extract trigram and bigram
        trigram = (words[i], words[i + 1], words[i + 2])
        bigram = (words[i], words[i + 1])

        # Count trigrams
        if trigram not in trigrams:
            trigrams[trigram] = 0
        trigrams[trigram] += 1

        # Count bigrams
        if bigram not in bigrams:
            bigrams[bigram] = 0
        bigrams[bigram] += 1

# Calculate trigram probabilities
trigram_probabilities = {}
for trigram, trigram_count in trigrams.items():
    bigram = trigram[:2]
    trigram_probabilities[trigram] = trigram_count / bigrams[bigram]

# Print trigram probabilities
for trigram, probability in trigram_probabilities.items():
    print(f"P({trigram[2]}|{trigram[0]} {trigram[1]}) = {probability:.2f}")
