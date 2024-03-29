# Current Music Trends 🎵

Current Music Trends is custom youtube metrics for trending music videos. There is also a youtube playlist which lists outs the trending music videos from youtube, across its all regions.

- [Website](https://clitic.github.io/current-music-trends/home)
- [Stream Youtube Playlist](https://www.youtube.com/playlist?list=PLv5KLCzERve6UI32k8kvAcUY077i3VWE6)

The only criteria to add videos to playlist is that, the music video should trend in at least 2 regions.

## Usage

First install all dependecies by running the below command.

```bash
pip install -r requirements.txt
```

Now enable and generate a [youtube v3](https://console.cloud.google.com/apis/library/youtube.googleapis.com) api key from [cloud project](https://console.cloud.google.com/). Set the api key as envoirnment variable if you want. To generate playlist data just run the below command.

```bash
python generate.py $YT_API_KEY
```

Optionally you can serve site too.

```bash
$ pip install mkdocs-material
$ mkdocs serve
```

Visit [localhost](http://127.0.0.1:8000) to view site.

## Creating A Youtube Playlist

To create a youtube playlist you need to create [OAuth](https://developers.google.com/youtube/v3/guides/authentication) client in your [cloud project](https://console.cloud.google.com). Also setup a [installed app flow](https://developers.google.com/youtube/v3/guides/auth/installed-apps) and add one redirect urls as http://localhost:8080/ . After creating OAuth client download client_secrets.json file and save it in safe/client_secrets.json . Finally run this command.

```bash
python update.py -p <playlist id>
```

Or

```bash
python update.py -h
```

## Credits

- [millify](https://github.com/azaitsev/millify)'s module script

## License

&copy; 2021-22 clitic

This repository is licensed under the MIT license. See LICENSE for details.
