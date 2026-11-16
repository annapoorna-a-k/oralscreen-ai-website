# OralScreen AI - Project Website

Project website (documentation portal) for **OralScreen AI**, an explainable oral cancer screening system built as an
M.Tech in Artificial Intelligence project at Amrita Vishwa Vidyapeetham, Coimbatore, under the guidance of Dr. Swapna T. R.

The site covers the problem statement, objectives, methodology, results, explainability, demonstration, project progress,
documentation, future improvements and team.

- Screening app: <https://oralscreen-ai-3nloatzwnkaypoqubwkfpy.streamlit.app/>
- Code and notebooks: <https://github.com/annapoorna-a-k/Oral-Cancer-Detection-and-Multiclass-Classification>
- Dataset: <https://zenodo.org/records/10664056>

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

The site opens at http://localhost:8501.

## Edit the content

Change the **CONFIG** block at the top of `app.py`:

- `TEAM`, `INSTITUTION`, `PROGRAMME`, `LAB` - team details
- `LIVE_APP_URL`, `GITHUB_URL`, `DATASET_URL` - links
- `DEMO_VIDEOS` - YouTube / Google Drive / .mp4 links

To add a demonstration video file, put an `.mp4` in `assets/videos/`; it appears automatically.
To replace a picture, save the new image in `assets/` with the same file name.
