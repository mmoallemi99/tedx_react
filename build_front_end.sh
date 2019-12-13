cd ted-react-version

rm -rf dist/
rm -rf ../front_end/static/

mkdir -p ../front_end/static/

BABEL_ENV=production webpack --config "config/webpack.config.dev.js"
cp -rf dist/* ../front_end/static/