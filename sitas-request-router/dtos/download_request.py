import json



class DownloadRequest:
    def __init__(self, userId, downloadId, songName, spotify, youtube, soundcloud, direct):
        self.userId = userId
        self.downloadId = downloadId
        self.songName = songName
        self.spotify = spotify
        self.youtube = youtube
        self.soundcloud = soundcloud
        self.direct = direct
    
    def from_json(json_dict):
        return DownloadRequest(
            json_dict['userId'],
            json_dict['downloadId'],
            json_dict['songName'],
            json_dict['spotify'],
            json_dict['youtube'],
            json_dict['soundcloud'],
            json_dict['direct']
        )
    
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def __str__(self):
        return f'DownloadRequest: [downloadId: {self.downloadId}, songName: {self.songName}, soundcloud: {self.soundcloud}]\n'

    def __eq__(self, other):
        return self.__dict__ == other.__dict__