# DEPLOYMENT on CleverCloud

## Dependencies

On Debian/Ubuntu, you are advised to install the following packages which will install, directly or by dependency, the required geospatial libraries:

```sh
sudo apt-get install binutils libproj-dev gdal-bin
```

Should we have to install it on CC

## Compilation with npm

We need to compile js file using `parcel`

```sh
npm run build
```

### Dev environment

We have to run 2 servers on development env : parcel & python -> to be investiate ([honcho](https://honcho.readthedocs.io/en/latest/index.html), makefile…)
