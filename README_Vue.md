# AOC_Vue

This template should help get you started developing with Vue 3 in Vite.

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

## Customize configuration

See [Vite Configuration Reference](https://vitejs.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```

Etape pour deployer le site

```sh

npm run build

git add dist -f
git commit -m "message"
git checkout main
git pull origin main
git fetch origin gh-pages
git subtree split --prefix dist -b gh-pages-split
git push origin gh-pages-split:gh-pages --force
git checkout main
git branch -D gh-pages-split
```