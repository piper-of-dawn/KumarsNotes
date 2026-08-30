# Tokenization: How Models Cut Language Down to Size

Before a language model can do anything with a sentence, it has to solve an awkward mismatch. Language is open-ended: we invent names, misspell words, borrow from other languages, write code, and attach prefixes to things that did not exist yesterday. A neural network, meanwhile, expects numbers drawn from a fixed system.

Tokenization is the compromise between those two worlds.

Take a simple sentence:

> **The car is running.**

A tokenizer might split it into:

```text
["The", " car", " is", " running", "."]
```

Another might produce:

```text
["The", " car", " is", " run", "ning", "."]
```

Both are valid. A **token** is not necessarily a word; it is one piece of text that a particular tokenizer treats as a unit. The leading spaces above are deliberate too. Many tokenizers store a space together with the text that follows it, so `"car"` and `" car"` can be different tokens.

Each token is then mapped to a **token ID**:

```text
"The"      → 464
" car"     → 1097
" is"      → 318
" run"     → 1057
"ning"     → 278
"."        → 13
```

The resulting sequence might be:

```text
[464, 1097, 318, 1057, 278, 13]
```

These numbers are illustrative. An ID is only an address in the tokenizer's vocabulary: `1097` is not intrinsically more car-like than `278`. The model uses the ID to look up a learned vector called an **embedding**, and that vector—not the ID itself—is what enters the neural network.

This explains the mechanics. It does not yet explain the real design problem: **how large should each piece be?**

## The Two Bad Extremes

The most obvious approach is to make every word a token. Then our sentence becomes:

```text
The | car | is | running | .
```

This is compact and readable, but it quietly assumes that we can list every word the model will ever encounter. We cannot. Even closely related forms would occupy separate places:

```text
run | ran | running
low | lower | lowest
```

Now multiply that across technical terms, product names, spelling variants, compound words, and many languages. The vocabulary swells, yet it still fails the first time an unseen word appears. Older word-level systems often replaced such an **out-of-vocabulary (OOV)** word with a generic `<UNK>` token.

That is a Procrustean bed: language is forced into a fixed list, and whatever does not fit is cut down to the same anonymous symbol. `Kraków`, `PyTorch`, and a new drug name may be completely different, but once all three become `<UNK>`, those differences are gone.

So why not go to the other extreme and use individual characters?

```text
r | u | n | n | i | n | g
```

The unknown-word problem nearly disappears because new words can be assembled from familiar characters. The price is sequence length. A word that could have been one useful unit now takes seven steps. Longer sequences consume more context and give the model more positions over which it must reconstruct patterns such as `run`, `-ing`, or `running`.

Word tokenization is efficient but brittle. Character tokenization is robust but verbose. The useful answer lies between them.

## Subwords: The Missing Middle

Modern language models generally use **subword tokenization**. Common words or fragments stay intact, while rarer words are assembled from smaller reusable pieces.

For example, a tokenizer might know `run` and `ning` but not store `running` as a single token:

```text
running → run | ning
```

It might keep a frequent word such as `the` whole:

```text
the → the
```

And it could break an unusual term into several parts:

```text
tokenization → token | ization
```

The exact cuts vary by tokenizer because they are learned from different text and built with different rules. The important idea is stable: frequent patterns earn larger pieces; uncommon patterns fall back to smaller ones.

This gives the vocabulary a kind of compositional reach. It does not need a separate entry for every possible word, only enough reusable pieces to construct them. Related forms can also share parts: `walk`, `walking`, and `walked` may reuse `walk` rather than occupying three completely unrelated entries.

Subwords therefore balance three competing demands:

1. **Coverage:** represent text the tokenizer has never seen before.
2. **Vocabulary size:** keep the set of stored pieces finite and manageable.
3. **Sequence length:** avoid spelling every sentence one character at a time.

There is no perfect cut. Larger pieces shorten sequences but require a bigger vocabulary. Smaller pieces improve coverage but lengthen sequences. Tokenizer design is the act of choosing where to pay.

## How BPE Learns the Pieces

**Byte Pair Encoding (BPE)** is one widely used way to build a subword vocabulary. Its central move is simple: begin with small units, count which adjacent pair occurs most often, merge that pair, and repeat.

Imagine a tiny training corpus containing many instances of:

```text
low
lower
lowest
```

At first, the words are split into small pieces:

```text
l | o | w
l | o | w | e | r
l | o | w | e | s | t
```

Because `l` followed by `o` appears frequently, the tokenizer may merge them:

```text
lo | w
lo | w | e | r
lo | w | e | s | t
```

If `lo` followed by `w` remains frequent, another merge creates `low`:

```text
low
low | e | r
low | e | s | t
```

With enough merges, frequent sequences become tokens. Rare sequences remain compositions of smaller ones. The tokenizer is not being taught that `low` has a particular meaning; it is discovering that keeping those characters together compresses the training text efficiently.

This distinction matters because a tokenizer has two different lives:

- During **tokenizer training**, it examines a corpus and decides which pieces belong in the vocabulary.
- During **encoding**, it applies those already-learned pieces and rules to new text.

The language model does not usually invent new tokens while you chat with it. It works with the tokenizer and vocabulary chosen before the model was trained.

Other subword methods make the choice differently. **WordPiece**, associated with models such as BERT, scores candidate pieces rather than following exactly the same merge rule as BPE. **Unigram tokenization** begins with many possible pieces and removes less useful ones until it reaches the desired vocabulary. The algorithms differ, but they are answering the same question: which finite set of fragments can represent an effectively unbounded stream of text?

## Bytes Close the Last Gap

Characters are not quite the bottom of the stack. Computers ultimately store text as **bytes**, and several modern tokenizers use bytes as their fallback units.

This is why a byte-level BPE tokenizer can represent almost any input without resorting to `<UNK>`. A familiar word may be one token, an unusual word may become several subwords, and an unfamiliar symbol may fall all the way back to bytes. Nothing magical happens when the tokenizer meets new text; it simply uses smaller pieces.

Byte-level fallbacks solve coverage, but not for free. Text that is poorly represented in the training corpus—some languages, niche notation, or unusual character sequences—may require many more tokens than familiar English text. The model can still read it, but less efficiently.

Research systems such as Meta's **Byte Latent Transformer (BLT)** push this idea further by operating on bytes and dynamically grouping them instead of relying on a conventional fixed subword vocabulary. That is an active research direction, not a reason to skip subwords: subword tokenization remains the clearest foundation for understanding how most current language models bridge text and numbers.

## Tokenization Shapes What the Model Can See

Tokenization can look like preprocessing plumbing, but its choices reach into the model itself.

A model's context window is measured in tokens, not words. If one tokenizer represents a passage in 700 tokens and another needs 1,100, the second passage consumes more of the available context. API usage is also commonly metered in tokens. Even apparent oddities—why a name is hard to spell, why arithmetic fragments strangely, or why one language costs more tokens than another—can begin at this boundary.

Tokenizers also add **special tokens** that are not ordinary pieces of prose. Depending on the model, these may mark the beginning or end of text, separate messages, identify roles such as user and assistant, or stand for padding. They let a plain sequence of IDs carry some structure alongside its content.

The full path is therefore:

```text
raw text
   ↓
tokens, including any special tokens
   ↓
token IDs
   ↓
embedding vectors
   ↓
language model
```

On the way out, the process runs in reverse: generated token IDs are mapped back to their text pieces and joined into readable text.

Tokenization does not understand the sentence, and token IDs do not contain its meaning. Tokenization performs the quieter but essential job that makes understanding possible: it turns open-ended language into a finite set of reusable pieces without forcing every word into `<UNK>` or making the model read everything one character at a time. Subwords are the compromise that holds that system together.
