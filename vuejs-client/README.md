# Kodi RemoteControl Client

RemoteControl for Kodi Server. This frontend must be used with
the [Websocket/UDP gateway](https://github.com/dmachard/kodi_remotecontrol-gateway)

![web interface](/vuejs-client/images/webinterface_v1.png)

## Installation

```
npm install
```

## Compile for development

```
npm run serve
```

## Build for production 

```
npm run build
```

## Build docker images

```
docker build . --build-arg VUE_APP_KODI="ws://kodi-rc.home:10000" --file Dockerfile-client -t kodi-remotecontrol-client
```

## Run docker image

```
docker run -d -p 8080:8080 --name=kodirc_client kodi-remotecontrol-client --restart=always
```


## License

This project is available under the MIT license.
