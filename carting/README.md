# DEPLOYMENT on CleverCloud

## Dependencies

On Debian/Ubuntu, you are advised to install the following packages which will install, directly or by dependency, the required geospatial libraries:

```sh
sudo apt-get install binutils libproj-dev gdal-bin
```

```
brew install gdal
```

## Compilation with npm

We need to compile js file using `parcel`

```sh
npm install
npm run watch
```

```
./manage py migrate
```

```
./manage.py import_in_from_xml --ouvrage z99
```

### Dev environment

We have to run 2 servers on development env : parcel & python -> to be investiate ([honcho](https://honcho.readthedocs.io/en/latest/index.html), makefile…)

## Deployable on Clever Cloud

Is it deployable on Clever Cloud ?
