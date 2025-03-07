import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000";

export const fetchSongs = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/songs?limit=10`);
    return response.data.songs;
  } catch (error) {
    console.error("Error fetching songs:", error);
    return [];
  }
};

export const fetchRecommendedSongIds = async (selectedSongIds) => {
  try {
    const response = await fetch(`${API_BASE_URL}/predict`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ profile: selectedSongIds, limit: 10 }),
    });

    if (!response.ok) throw new Error("Failed to fetch recommendations");

    const data = await response.json();

    if (typeof data !== "object" || data === null) {
      throw new Error("Invalid API response format");
    }

    return Object.keys(data); // Extracts song IDs
  } catch (error) {
    console.error("Error fetching recommended song IDs:", error);
    return [];
  }
};

export const fetchSongDetails = async (songId) => {
  try {
    const response = await fetch(`${API_BASE_URL}/song/${songId}`);
    if (!response.ok)
      throw new Error(`Failed to fetch details for song ID: ${songId}`);

    const song = await response.json();

    return {
      id: song.song_id,
      title: song.title,
      artist: song.artist_name,
      release: song.release,
    };
  } catch (error) {
    console.error("Error fetching song details:", error);
    return null;
  }
};
