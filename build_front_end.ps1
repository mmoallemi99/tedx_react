cd ted-react-version
BABEL_ENV=production webpack --config "config/webpack.config.dev.js"
Remove-Item –Path "../front_end/static/" -Recurse
New-Item -ItemType directory -Path "../front_end/static/"
Copy-Item -Path "dist/*" -Destination "../front_end/static/" -Recurse
