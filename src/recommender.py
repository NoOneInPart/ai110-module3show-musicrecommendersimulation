import csv
from typing import List, Dict, Tuple
from dataclasses import dataclass, asdict

# --- scoring weights (the "algorithm recipe" knobs) ---
# Heavy continuous backbone; light categorical bonuses on top.
W_ENERGY = 5.0    # heavy: energy similarity does most of the work
W_GENRE = 1.0     # slight boost for an exact genre match
W_MOOD = 1.0      # slight boost for an exact mood match
W_ACOUSTIC = 0.5  # slight boost when acoustic-ness agrees with the user

# A song is treated as "acoustic" at or above this acousticness value.
ACOUSTIC_THRESHOLD = 0.5

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # Reuse the shared scoring rule so OOP and functional paths agree.
        # asdict(user) yields the exact keys score_song expects.
        prefs = asdict(user)
        ranked = sorted(
            self.songs,
            key=lambda song: score_song(prefs, asdict(song))[0],
            reverse=True,
        )
        return ranked[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        score, reasons = score_song(asdict(user), asdict(song))
        detail = ", ".join(reasons) if reasons else "it didn't strongly match your preferences"
        return f"'{song.title}' by {song.artist} scored {score:.2f}: {detail}"

# Which CSV columns to convert to which numeric type. Anything not listed
# stays a str (title, artist, genre, mood).
_INT_FIELDS = {"id"}
_FLOAT_FIELDS = {
    "energy",
    "tempo_bpm",
    "valence",
    "danceability",
    "acousticness",
}


def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file into a list of dicts.

    Numeric columns are converted to the appropriate type: `id` becomes an
    int, the audio-feature columns (energy, tempo_bpm, valence,
    danceability, acousticness) become floats, and text columns (title,
    artist, genre, mood) stay as strings. Downstream scoring can therefore
    rely on numbers being real numbers, not strings.

    Required by src/main.py
    """
    songs: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            song: Dict = {}
            for key, value in row.items():
                if key in _INT_FIELDS:
                    song[key] = int(value)
                elif key in _FLOAT_FIELDS:
                    song[key] = float(value)
                else:
                    song[key] = value
            songs.append(song)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py

    Scoring recipe (see README):
      - Heavy continuous backbone: closeness of the song's energy to the
        user's preferred energy (weight W_ENERGY).
      - Slight categorical bonuses: +W_GENRE / +W_MOOD for an exact
        genre / mood match.
      - Slight acoustic bonus (pure bonus, never a penalty): +W_ACOUSTIC
        when the song's acoustic-ness agrees with the user's preference.

    Any preference the user hasn't supplied is simply skipped, so an
    unspecified taste never helps or hurts a song.

    Returns (score, reasons), where reasons explains which terms fired.
    """
    score = 0.0
    reasons: List[str] = []

    # HEAVY: energy closeness (both values are on a 0-1 scale)
    target_energy = user_prefs.get("target_energy")
    if target_energy is not None:
        song_energy = float(song["energy"])
        closeness = 1 - abs(song_energy - float(target_energy))
        score += W_ENERGY * closeness
        reasons.append(
            f"energy {song_energy:.2f} is close to your target {float(target_energy):.2f}"
        )

    # SLIGHT: exact genre match
    if user_prefs.get("favorite_genre") and song.get("genre") == user_prefs["favorite_genre"]:
        score += W_GENRE
        reasons.append(f"matches your favorite genre ({song['genre']})")

    # SLIGHT: exact mood match
    if user_prefs.get("favorite_mood") and song.get("mood") == user_prefs["favorite_mood"]:
        score += W_MOOD
        reasons.append(f"matches your mood ({song['mood']})")

    # SLIGHT: acoustic preference as a pure bonus (never subtracts)
    likes_acoustic = user_prefs.get("likes_acoustic")
    if likes_acoustic is not None:
        song_is_acoustic = float(song["acousticness"]) >= ACOUSTIC_THRESHOLD
        if song_is_acoustic == likes_acoustic:
            score += W_ACOUSTIC
            reasons.append(
                "it's acoustic like you prefer"
                if likes_acoustic
                else "it's not acoustic, matching your preference"
            )

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Ranks the catalog for a user and returns the top-k recommendations.

    Scoring (per song) and ranking (over the list) are kept as two steps:
    `score_song` judges one song, and this function orders those scores.

    Returns a list of (song, score, explanation) tuples, sorted from
    highest score to lowest and truncated to k items.

    Required by src/main.py
    """
    # Score every song. A list comprehension is the Pythonic way to build a
    # new list from an existing iterable in one clear expression.
    scored = [
        (song, *score_song(user_prefs, song))  # -> (song, score, reasons)
        for song in songs
    ]

    # Rank: sorted() returns a NEW list (leaving `songs` untouched); the key
    # picks the score, and reverse=True gives highest-to-lowest order.
    ranked = sorted(scored, key=lambda item: item[1], reverse=True)

    # Join reasons with newlines so callers can print one per line, then
    # keep only the top k.
    return [
        (song, score, "\n".join(reasons) if reasons else "no strong matches")
        for song, score, reasons in ranked[:k]
    ]
