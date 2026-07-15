"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

#FIX: make importing relative so that it actually works
from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile (keys match the UserProfile fields)
    user_prefs = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.8,
        "likes_acoustic": False,
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print()
    print("=" * 60)
    print("  TOP RECOMMENDATIONS")
    print("=" * 60)
    print(
        f"  Profile: genre={user_prefs['favorite_genre']}, "
        f"mood={user_prefs['favorite_mood']}, "
        f"energy={user_prefs['target_energy']}, "
        f"likes_acoustic={user_prefs['likes_acoustic']}"
    )
    print("-" * 60)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"  {rank}. {song['title']} - {song['artist']}  (score: {score:.2f})")
        print(f"       [{song['genre']} / {song['mood']}]")
        print("       why:")
        for reason in explanation.split("\n"):
            print(f"         - {reason}")
        print()


if __name__ == "__main__":
    main()
