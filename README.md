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
  > As of this commit, the score is built around a base score (called the backbone) and some bonuses for categorical matches. The backbone (weight 5.0) rewards how closely a song's energy matches the user's preferred energy level, so a song that "sounds like" what the user wants ranks highly even if its labels don't match exactly. On top of that, small bonuses nudge the ranking: +1.0 if the song's genre matches the user's favorite, +1.0 if the mood matches, and up to +0.5 depending on how strongly the song's acoustic-ness agrees with the user's `likes_acoustic` preference. The acoustic term is a pure bonus that scales with how acoustic a song is (never a penalty), so a fully-acoustic song earns the whole +0.5 for an acoustic-lover while an electric one earns little or nothing, and a user who simply hasn't asked for acoustic tracks isn't punished for songs that happen to be acoustic. This setup prevents the algorithm from overwhelmingly recommending songs that fit into specific categories based on the specific genre name or mood, but it does mean most of the songs recommended have similar energy levels.
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
============================================================
  TOP RECOMMENDATIONS - high-energy pop
============================================================
  Profile: genre=pop, mood=happy, energy=0.95, likes_acoustic=False
------------------------------------------------------------
  1. Neon Echo - Sunrise City  (score: 6.76)
       [pop / happy]
       why:
         - energy 0.82 is close to your target 0.95
         - matches your favorite genre (pop)
         - matches your mood (happy)
         - acousticness 0.18 leans electric, matching your preference

  2. Max Pulse - Gym Hero  (score: 6.38)
       [pop / intense]
       why:
         - energy 0.93 is close to your target 0.95
         - matches your favorite genre (pop)
         - acousticness 0.05 leans electric, matching your preference

  3. Daft Punk - Get Lucky  (score: 5.78)
       [disco / happy]
       why:
         - energy 0.81 is close to your target 0.95
         - matches your mood (happy)
         - acousticness 0.04 leans electric, matching your preference

  4. Rammstein - Du Hast  (score: 5.45)
       [industrial metal / intense]
       why:
         - energy 0.96 is close to your target 0.95
         - acousticness 0.00 leans electric, matching your preference

  5. Indigo Parade - Rooftop Lights  (score: 5.38)
       [indie pop / happy]
       why:
         - energy 0.76 is close to your target 0.95
         - matches your mood (happy)
         - acousticness 0.35 leans electric, matching your preference


============================================================
  TOP RECOMMENDATIONS - chill lofi
============================================================
  Profile: genre=lofi, mood=chill, energy=0.4, likes_acoustic=True
------------------------------------------------------------
  1. LoRoom - Midnight Coding  (score: 7.26)
       [lofi / chill]
       why:
         - energy 0.42 is close to your target 0.40
         - matches your favorite genre (lofi)
         - matches your mood (chill)
         - acousticness 0.71 leans acoustic like you prefer

  2. Paper Lanterns - Library Rain  (score: 7.18)
       [lofi / chill]
       why:
         - energy 0.35 is close to your target 0.40
         - matches your favorite genre (lofi)
         - matches your mood (chill)
         - acousticness 0.86 leans acoustic like you prefer

  3. LoRoom - Focus Flow  (score: 6.39)
       [lofi / focused]
       why:
         - energy 0.40 is close to your target 0.40
         - matches your favorite genre (lofi)
         - acousticness 0.78 leans acoustic like you prefer

  4. Orbit Bloom - Spacewalk Thoughts  (score: 5.86)
       [ambient / chill]
       why:
         - energy 0.28 is close to your target 0.40
         - matches your mood (chill)
         - acousticness 0.92 leans acoustic like you prefer

  5. Slow Stereo - Coffee Shop Stories  (score: 5.29)
       [jazz / relaxed]
       why:
         - energy 0.37 is close to your target 0.40
         - acousticness 0.89 leans acoustic like you prefer


============================================================
  TOP RECOMMENDATIONS - deep intense rock
============================================================
  Profile: genre=rock, mood=intense, energy=0.95, likes_acoustic=False
------------------------------------------------------------
  1. Voltline - Storm Runner  (score: 7.25)
       [rock / intense]
       why:
         - energy 0.91 is close to your target 0.95
         - matches your favorite genre (rock)
         - matches your mood (intense)
         - acousticness 0.10 leans electric, matching your preference

  2. Rammstein - Du Hast  (score: 6.45)
       [industrial metal / intense]
       why:
         - energy 0.96 is close to your target 0.95
         - matches your mood (intense)
         - acousticness 0.00 leans electric, matching your preference

  3. Max Pulse - Gym Hero  (score: 6.38)
       [pop / intense]
       why:
         - energy 0.93 is close to your target 0.95
         - matches your mood (intense)
         - acousticness 0.05 leans electric, matching your preference

  4. Pulsewave - Neon Tide  (score: 5.14)
       [house / energetic]
       why:
         - energy 0.88 is close to your target 0.95
         - acousticness 0.02 leans electric, matching your preference

  5. Daft Punk - Get Lucky  (score: 4.78)
       [disco / happy]
       why:
         - energy 0.81 is close to your target 0.95
         - acousticness 0.04 leans electric, matching your preference


============================================================
  TOP RECOMMENDATIONS - edge: acoustic headbanger
============================================================
  Profile: genre=rock, mood=intense, energy=0.95, likes_acoustic=True
------------------------------------------------------------
  1. Voltline - Storm Runner  (score: 6.85)
       [rock / intense]
       why:
         - energy 0.91 is close to your target 0.95
         - matches your favorite genre (rock)
         - matches your mood (intense)
         - acousticness 0.10 leans acoustic like you prefer

  2. Rammstein - Du Hast  (score: 5.95)
       [industrial metal / intense]
       why:
         - energy 0.96 is close to your target 0.95
         - matches your mood (intense)
         - acousticness 0.00 leans acoustic like you prefer

  3. Max Pulse - Gym Hero  (score: 5.93)
       [pop / intense]
       why:
         - energy 0.93 is close to your target 0.95
         - matches your mood (intense)
         - acousticness 0.05 leans acoustic like you prefer

  4. Pulsewave - Neon Tide  (score: 4.66)
       [house / energetic]
       why:
         - energy 0.88 is close to your target 0.95
         - acousticness 0.02 leans acoustic like you prefer

  5. Neon Echo - Sunrise City  (score: 4.44)
       [pop / happy]
       why:
         - energy 0.82 is close to your target 0.95
         - acousticness 0.18 leans acoustic like you prefer


============================================================
  TOP RECOMMENDATIONS - edge: happy classical
============================================================
  Profile: genre=classical, mood=happy, energy=0.5, likes_acoustic=True
------------------------------------------------------------
  1. E. Marchetti - Nocturne in Blue  (score: 4.97)
       [classical / calm]
       why:
         - energy 0.20 is close to your target 0.50
         - matches your favorite genre (classical)
         - acousticness 0.95 leans acoustic like you prefer

  2. LoRoom - Midnight Coding  (score: 4.96)
       [lofi / chill]
       why:
         - energy 0.42 is close to your target 0.50
         - acousticness 0.71 leans acoustic like you prefer

  3. Mara Silk - Velvet Hours  (score: 4.90)
       [r&b / romantic]
       why:
         - energy 0.45 is close to your target 0.50
         - acousticness 0.30 leans acoustic like you prefer

  4. LoRoom - Focus Flow  (score: 4.89)
       [lofi / focused]
       why:
         - energy 0.40 is close to your target 0.50
         - acousticness 0.78 leans acoustic like you prefer

  5. Indigo Parade - Rooftop Lights  (score: 4.88)
       [indie pop / happy]
       why:
         - energy 0.76 is close to your target 0.50
         - matches your mood (happy)
         - acousticness 0.35 leans acoustic like you prefer
```

---

## Experiments You Tried

Use this section to document the experiments you ran.
> I picked the weighting shift experiment where the weighting of energy is doubled while the weighting of genre is halved. For user profiles like "chill lofi" and "acoustic headbanger" the results remained identical because song energy was the defining factor in these ranking choices, but "high-energy pop" experienced a large change as high energy songs were prioritized more heavily over songs within the pop genre.

---

## Limitations and Risks

Summarize some limitations of your recommender.

> This model prioritizes recommending based on energy, this is by design to reduce the effects of locking in on a particular genre or mood but this does mean all recommended songs are roughly the same energy level. Categories like genre are matched by exact-string, so a user that prefers "pop" would miss "indie pop" songs. Tempo, valence, and danceability are also not used in scoring as the current user profile does not contain preference info for those categories.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



