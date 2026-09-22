# Publishing this snapshot to GitHub

This folder is already initialized as a Git repository on branch `main` with one snapshot commit.

Create an empty repository on GitHub, then from this directory run:

```bash
git remote add origin https://github.com/YOUR-ACCOUNT/YOUR-REPO.git
git push -u origin main
```

Or use SSH:

```bash
git remote add origin git@github.com:YOUR-ACCOUNT/YOUR-REPO.git
git push -u origin main
```

The generated `outputs/` directory is ignored except for `.gitkeep`. Historical outputs used for the research record are already versioned under `data/` and `results/`.

Before choosing an open-source license, review the repository and add the license you actually want. This export intentionally does not choose one for you.
