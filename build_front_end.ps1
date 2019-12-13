cd ted-react-version

$env:BABEL_ENV = "production"
Remove-Item –Path "../front_end/static/" -Recurse
Remove-Item –Path "dist/" -Recurse

New-Item -ItemType directory -Path "../front_end/static/"

webpack --config "config/webpack.config.dev.js"
Copy-Item -Path "dist/*" -Destination "../front_end/static/" -Recurse
