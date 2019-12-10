cd ted-react-version
BABEL_ENV=production webpack --config "config/webpack.config.dev.js"
rm -rf ../front_end/static/
mkdir -p ../front_end/static/
cp -rf dist/* ../front_end/static/