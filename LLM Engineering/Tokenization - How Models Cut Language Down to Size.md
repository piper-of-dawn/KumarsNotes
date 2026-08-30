# Tokenization: How Models Cut Language Down to Size

Take one sentence:

> **The car is running.**

To us, that is already meaningful language. The model is not so lucky. Underneath all the impressive conversation, it is still a neural network, and neural networks work with numbers. So before anything intelligent can happen, there is a boring plumbing problem: the sentence has to become numerical input.

Tokenization is where that conversion begins. It takes the open-ended mess of language and chops it into a finite box of reusable pieces.

But that immediately raises another question: **what exactly counts as one piece?**

## First: what is a token?

A **token** is one piece of text that a tokenizer decides to treat as a unit.

For our sentence, one tokenizer might produce:

```text
["The", " car", " is", " running", "."]
```

Another might produce:

```text
["The", " car", " is", " run", "ning", "."]
```

In the first version, `running` is one token. In the second, it is built from two. Neither version is *the* natural answer. Both are perfectly possible because:

> **Token does not mean word. Token means piece.**

Even the spaces can be part of those pieces. Many tokenizers distinguish between `"car"` and `" car"`, storing the space together with the word that follows it.

Which is a slightly annoying answer, because now we have to ask: who decides where those cuts go?

## What is the tokenizer?

The **tokenizer** is the system that applies the cutting rules. Roughly, it does this:

```text
The car is running.
        ↓
["The", " car", " is", " run", "ning", "."]
```

That still leaves us with text. The model needs numbers, so each piece is assigned a stored number:

```text
"The"      → 464
" car"     → 1097
" is"      → 318
" run"     → 1057
"ning"     → 278
"."        → 13
```

Our sentence can now travel into the model as:

```text
[464, 1097, 318, 1057, 278, 13]
```

The numbers here are illustrative. Different tokenizers have different vocabularies and therefore different IDs. There is no sacred international registry in which `car` has been assigned number 1097 for all time.

Fine—but **what is a token ID actually telling the model?**

## What is a token ID?

A **token ID** is the numerical label assigned to a token. The number itself usually has no semantic meaning. `1097` is not more car-like than `278`, just as locker 1097 is not more athletic than locker 278. It is an address. That is all.

The model uses that address to look up a learned list of numbers called an **embedding**. That embedding—not the bare ID—is what enters the neural network.

So the path is already longer than it first appeared:

```text
text → tokens → token IDs → embeddings
```

This is where a seemingly fussy question turns out not to be fussy at all. Our example ends with a full stop, but punctuation is not the same thing as an instruction to stop. **What token follows the sentence?**

## How does the model know the sentence is over?

Sometimes the final visible token is simply the punctuation mark. The surrounding system may then add a **special token**: a piece that carries structure rather than ordinary prose. It is stage direction, not dialogue.

A simplified sequence could look like:

```text
<BOS> | The | car | is | running | . | <EOS>
```

`<BOS>` means beginning of sequence and `<EOS>` means end of sequence. Those exact names are only conventions; real models use different control tokens. A chat model may mark the end of a user message rather than the end of a grammatical sentence. Padding, message roles, and separators can also have their own special tokens.

This distinction matters. The full stop belongs to the text. An end token belongs to the machinery wrapped around the text. What you typed and what the model receives are related, but they are not identical.

We now have the route from sentence to numbers. But we have quietly avoided the hardest part: **how should the tokenizer choose its vocabulary in the first place?**

## Why not simply make every word a token?

Because that is the obvious starting point. Split on spaces, keep every word whole, go home early:

```text
The | car | is | running | .
```

Easy. Then English shows up with a baseball bat.

Consider:

```text
run | ran | running
low | lower | lowest
```

With strict word-level tokenization, each form needs its own vocabulary entry. Do this across tens of thousands of base words, then add names, companies, technical terms, plurals, misspellings, slang, compound words, and other languages. The neat little vocabulary starts looking less like a toolbox and more like a warehouse whose owner has lost control of the inventory.

And after building that warehouse, an unfamiliar word can still arrive tomorrow.

Older word-level systems often replaced anything outside their vocabulary with `<UNK>`, the **unknown token**. This is the **out-of-vocabulary (OOV)** problem.

Once different unfamiliar words collapse into the same `<UNK>` token, the model effectively goes blind to the differences between them. `Kraków`, `PyTorch`, and a newly named drug become identical at the input. That is a brutal loss of information. The fixed vocabulary is a Procrustean bed: whatever does not fit gets hacked down to the same anonymous symbol.

Fine. If whole words are too rigid, **why not use individual characters?**

## Why not tokenize one character at a time?

Then almost nothing is unknown:

```text
running → r | u | n | n | i | n | g
```

A brand-new word can be assembled from characters the tokenizer already knows. Great. We have solved the coverage problem.

We have also created a length problem. `running` now occupies seven positions instead of one. Every familiar pattern has to be rebuilt character by character, and a fixed context window fills much faster. Individual characters are weak carriers of meaning: `r` tells us almost nothing; `run` is already getting somewhere.

Word-level tokenization is compact but brittle. Character-level tokenization is flexible but verbose.

So is there something between a whole word and a single character?

## Subwords: the missing middle

Yes. And this is the part that makes the whole story click.

Modern language models generally use **subword tokenization**. A common word may remain whole. A less common word can be assembled from fragments. A very unusual sequence can fall back to still smaller pieces.

For example:

```text
the          → the
running      → run | ning
tokenization → token | ization
```

The exact cuts are not universal. One tokenizer may store `running` whole; another may split it into `run` and `ning`; another may do something uglier. Each tokenizer learned from a different body of text and made a different trade-off. Language does not arrive with dotted lines showing us where to cut.

The important idea is that the vocabulary no longer needs a separate entry for every possible word. It needs a set of pieces from which words can be built. `walk`, `walking`, and `walked` may reuse `walk`. A name the tokenizer has never seen can still survive as several smaller tokens rather than disappearing into `<UNK>`.

Subwords sit in the middle because they balance three competing pressures:

1. Can the tokenizer represent unfamiliar text?
2. Can it keep the vocabulary to a manageable size?
3. Can it avoid turning every sentence into a very long sequence?

There is no free lunch hiding here. Larger pieces shorten the sequence but enlarge the vocabulary. Smaller pieces improve coverage but consume more positions. Tokenizer design is mostly the art of deciding which bill you would rather receive.

But where do these subwords come from? Does somebody sit down and write a list of useful fragments?

## How does BPE learn the pieces?

Usually, the pieces are learned from a large collection of text. **Byte Pair Encoding (BPE)** is one widely used method.

Its basic move is almost suspiciously simple: start with small units, find the neighboring pair that appears most often, mash it into one piece, and repeat.

Imagine a tiny corpus containing many examples of:

```text
low
lower
lowest
```

At first, each word is broken into small pieces:

```text
l | o | w
l | o | w | e | r
l | o | w | e | s | t
```

The pair `l | o` appears repeatedly, so BPE may merge it:

```text
lo | w
lo | w | e | r
lo | w | e | s | t
```

If `lo | w` remains frequent, the next merge produces `low`:

```text
low
low | e | r
low | e | s | t
```

Repeat this across a much larger corpus and frequent sequences gradually earn their own tokens. Rare sequences remain combinations of smaller pieces.

Notice what BPE has and has not learned. It has discovered that keeping `low` together is useful for compressing the training text. It has not sat there contemplating the meaning of low. Meaning is learned later by the language model from how tokens occur in context.

That produces another distinction I initially found easy to blur: **training a tokenizer is not the same as using one.** They sound like adjacent details. They are different events.

During tokenizer training, the system examines a corpus and builds its vocabulary and merge rules. During ordinary encoding, it applies those frozen rules to new text. The model does not normally invent a new token because you typed a word it has never seen.

BPE is not the only subword method. **WordPiece**, associated especially with BERT, chooses pieces using a different scoring rule. **Unigram tokenization** begins with many candidate pieces and removes the less useful ones. The machinery differs, but the question is the same: which finite collection of fragments can cover an effectively unlimited stream of language?

And what happens if even the smallest learned fragment is not enough?

## What sits below a character?

A byte. There is always another floor in the basement.

Computers ultimately store text as bytes, and many modern tokenizers use bytes either as their starting units or as a fallback. A familiar word may be one token, an unusual word may become several subwords, and a truly unfamiliar symbol may fall all the way down to its bytes.

That is how byte-level BPE can represent almost any input without resorting to `<UNK>`. The tokenizer does not need to understand something new. It just keeps cutting until it reaches units already present in its vocabulary.

Coverage, however, is not the same as efficiency. A language or notation poorly represented in the training corpus may take many more tokens than familiar English text. The model can read it, but the same thought occupies more of its context window.

Meta's **Byte Latent Transformer (BLT)** takes this further. It works directly with bytes and dynamically groups them rather than relying on a conventional fixed subword vocabulary. It is an interesting research direction, but it makes more sense once the subword compromise is clear: tokenization is still an engineering choice, not a solved one-size-fits-all problem.

Which brings us to the practical question: **why should any of this matter to the person using the model?**

## Why do the cuts matter after tokenization?

Because the model's context window is measured in tokens, not words. The meter is running on the cuts.

If one tokenizer represents a passage in 700 tokens and another needs 1,100, the second version consumes more of the available context. API usage is also commonly metered in tokens. The cuts influence how much text fits, how much it costs to process, and how far apart related pieces sit inside the sequence.

They can also explain some model oddities. A model may stumble over the spelling of a name because that name arrives as a strange collection of fragments. Arithmetic can be awkward when numbers are split inconsistently. The same paragraph can cost more tokens in one language than another.

So tokenization is not the intern tidying up text before the real work begins. It decides what the pieces of the real work will be.

The complete path is:

```text
raw text
   ↓
ordinary tokens + any special tokens
   ↓
token IDs
   ↓
embeddings
   ↓
language model
```

On the way out, generated token IDs are mapped back to text pieces and joined into readable text.

And that returns us to the first sentence. The model never receives **The car is running.** in the form in which we see it. It receives a sequence of addresses, probably wrapped in bits of stage direction, each pointing to a learned embedding.

That is the entire bargain. Do not store every possible word. Do not make the model crawl through every character. Give it a finite vocabulary of reusable subwords, then let those pieces stretch far enough to handle language they have never met before.
