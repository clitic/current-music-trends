from typing import Any, Optional


class Create:
    
    def __init__(self, youtube: Any) -> None:
        """Create class creates new items on youtube account

        Args:
            youtube (Any): a resource object with methods for interacting with the service.
        """
        self._youtube = youtube
        self.cost = 0
        
    def playlist(self, title: str, desc: Optional[str] = "", status: Optional[str] = "private") -> str:
        """create a new playlist

        Args:
            title (str): title for playlist
            desc (Optional[str], optional): description for playlist. Defaults to "".
            status (Optional[str], optional): privacy status for playlist. Defaults to "private".

        Returns:
            str: created playlist id
        """
        request_body = {
            "kind": "youtube#playlist",
            "snippet": {
                "title": title,
                "description": desc
            },
            "status": {
                "privacyStatus": status
            }
        }
        
        request = self._youtube.playlists().insert(part="id,snippet,status", body=request_body)
        response = request.execute()
        self.cost += 50
        return response["id"]
