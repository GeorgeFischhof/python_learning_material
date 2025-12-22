
# GitHub authentication with SSH keys (most common on Linux - easy and secure)

## 1. Generate the SSH key on Linux (bash)

1. Generate an SSH key, answer the questions (enter is enough)
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

2. Start SSH agent
```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

3. Get public key
```bash
cat ~/.ssh/id_ed25519.pub
```

## 1. Generate the SSH key on Windows - use powershell 

1. Generate key
```powershell
ssh-keygen -t ed25519 -C "your_email@example.com"
```

2. Start SSH agent
```powershell
Start-Service ssh-agent
```

3. Enable auto-start (recommended)
```powershell
Set-Service ssh-agent -StartupType Automatic
```

4. Add key
```powershell
ssh-add $env:USERPROFILE\.ssh\id_ed25519
```

5. Get public key
```powershell
type $env:USERPROFILE\.ssh\id_ed25519.pub
```

## 2. Use the generated key

1. Copy the key output form your terminal -> <br/>
paste to 
[GitHub (profile) -> Settings -> SSH and GPG keys -> New SSH key](https://github.com/settings/ssh/new)

2. Use SSH URLs for repos
Clone like this:
```bash
git clone git@github.com:USERNAME/REPO.git
```
code -> clone (SSH tab) 
