# 📘 DevOps Learning Notes

---

## 📅 Date: 2025-09-13  
**Topic: Git Branching & Merge Conflict**

### 🔹 Definition
- **Branch:** Git branch ek alag line of development hai. Matlab tum apna kaam main branch se alag rakh sakte ho bina dusron ko disturb kiye.  
- **Merge Conflict:** Jab ek hi file ke ek hi line ko do alag branches me alag tarike se badla jata hai, tab Git automatically merge nahi kar pata. Is situation ko "merge conflict" kehte hain.

### 🔹 Practice Steps
1. `git init` – new repo banaaya  
2. `git checkout -b feature/update-hello` – naya branch banaya  
3. `hello.txt` file banai aur alag updates kiye  
4. Wapas `main` branch pe alag update kiya  
5. `git merge feature/update-hello` – merge conflict aaya  
6. Conflict ko manually resolve karke commit kiya

### 🔹 Files
- `hello.txt` → merge conflict practice ke liye use ki

### 🔹 Key Commands
```bash
git branch
git checkout -b feature/update-hello
git add hello.txt
git commit -m "message"
git checkout main
git merge feature/update-hello
git status
git log --oneline --graph --all

