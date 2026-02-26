## Mon Gâteau

Mon Gâteau is a small Flask web app for browsing and managing cake recipes. It lets you search and filter cakes, view full recipes, save favourites, and add your own cakes (with images) backed by MongoDB.

### Features

- **Browse cakes**: Masonry-style card grid with images, names, and a detail modal for each cake.
- **Search & filter**:
  - Search by cake name.
  - Filter by difficulty level via a custom “All levels” dropdown.
- **Saved cakes**:
  - Heart icon on each card to save/unsave.
  - “♥ Saved” view shows only your saved cakes (saved in `localStorage`).
- **Add / edit / delete cakes**:
  - “+ Add Cake” opens a modal to create a new cake (name, category, difficulty, times, servings, description, ingredients, steps).
  - Upload an image from your device or paste an image URL.
  - Click a card → detail modal → **Edit** or **Delete** the cake.
  - Delete uses a custom confirmation dialog and shows an in‑page “Cake deleted” notice.
- **Seed data**:
  - `seed.py` can preload many example cakes into MongoDB.

### Tech stack

- **Backend**: Python 3, Flask, PyMongo.
- **Database**: MongoDB Atlas (collection `cakedb.cakes`).
- **Frontend**: HTML templates (`index.html`), vanilla JS (`static/script.js`), CSS (`static/style.css`).
- **Assets**: Images served from `static/images/...` and uploaded images saved under `static/images/uploads/`.

### Running the app

1. **Install dependencies**

   pip install -r requirements.txt

2. **Run locally**: `python app.py` (or `nohup python3 app.py > log.txt &` on a server)

### CI/CD (GitHub Actions)

- **CI** (on every push/PR): installs deps, runs `pytest tests/`.
- **Deploy** (after CI passes on `main`): SSHs to EC2, runs `git pull --rebase`, restarts the app with `nohup python3 app.py > log.txt &`.

**Required GitHub secrets** (Settings → Secrets and variables → Actions):

- `EC2_HOST`: EC2 public IP or hostname
- `EC2_SSH_KEY`: Private SSH key used to connect as `ec2-user` (entire PEM content, including `-----BEGIN` / `-----END`)
- `EC2_HOST_KEY`: EC2 host key so the runner can connect without "host key verification failed". On your machine run:  
  `ssh-keyscan -H YOUR_EC2_IP`  
  and paste the full output (one or more lines) into this secret.

Ensure the EC2 instance has `~/mon-gateau` cloned and can run `git pull --rebase` (e.g. deploy key or credentials configured). The EC2 security group must allow SSH (port 22) from the internet (or from [GitHub’s IP ranges](https://api.github.com/meta) if you restrict it).
