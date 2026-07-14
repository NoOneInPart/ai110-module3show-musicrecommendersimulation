from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

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
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    # TODO: Implement CSV loading logic
    print(f"Loading songs from {csv_path}...")
    return []

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
    target_energy = user_prefs.get("energy")
    if target_energy is not None:
        song_energy = float(song["energy"])
        closeness = 1 - abs(song_energy - float(target_energy))
        score += W_ENERGY * closeness
        reasons.append(
            f"energy {song_energy:.2f} is close to your target {float(target_energy):.2f}"
        )

    # SLIGHT: exact genre match
    if user_prefs.get("genre") and song.get("genre") == user_prefs["genre"]:
        score += W_GENRE
        reasons.append(f"matches your favorite genre ({song['genre']})")

    # SLIGHT: exact mood match
    if user_prefs.get("mood") and song.get("mood") == user_prefs["mood"]:
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
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    # TODO: Implement scoring and ranking logic
    # Expected return format: (song_dict, score, explanation)
    return []
