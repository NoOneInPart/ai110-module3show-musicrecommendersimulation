# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
  > In this setup, each song contains metadata about the id, artist, genre, mood, energy, tempo, valence, danceability, and acousticness.
- What information does your `UserProfile` store
  > The UserProfile stores a user's favorite genre, mood, their preferred energy level, and whether they like acoustic tracks (people don't?).
- How does your `Recommender` compute a score for each song
  > As of this commit, the score is built around a base score (called the backbone) and some bonuses for categorical matches. The backbone (weight 5.0) rewards how closely a song's energy matches the user's preferred energy level, so a song that "sounds like" what the user wants ranks highly even if its labels don't match exactly. On top of that, small fixed bonuses nudge the ranking: +1.0 if the song's genre matches the user's favorite, +1.0 if the mood matches, and +0.5 if the song's acoustic-ness agrees with the user's `likes_acoustic` preference. The acoustic term is a pure bonus (never a penalty), so a user who simply hasn't asked for acoustic tracks isn't punished for songs that happen to be acoustic. This setup prevents the algorithm from overwhelmingly recommending songs that fit into specific categories based on the specific genre name or mood, but it does mean most of the songs recommended have similar energy levels.
- How do you choose which songs to recommend
  > Every song in the catalog is scored with the formula above, then the list is ranked from highest to lowest score and the top `k` songs (default 5) are returned. The scoring rule judges one song at a time; the ranking rule turns those scores into an ordered shortlist.

You can include a simple diagram or bullet list if helpful.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



