from datetime import datetime
import requests,os, random

class IG:
    def __init__(self, cookie):
        self.cookie = cookie
        self.csrftoken = cookie.split('csrftoken')[1].split(';')[0]
        self.headers = {
                'authority': 'i.instagram.com',
                'accept': '*/*',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'ig_did=7F9C005F-44C5-462B-9C83-C17F3C40C91B; ig_nrcb=1; mid=Y0TWXAALAAHVZ0CPiOlAvfTBQV2f; csrftoken=q555FDDIhmCzFFTqJg3Z9DPnn8dD0LaQ; sessionid=54844316525%3Aac8YPSzRPMLBmb%3A25%3AAYe8x5ueSQ39fNyyLrbQDcRczEqUdP_oXrUYFM8r0A; ds_user_id=54844316525; shbid="12403\\05454844316525\\0541696991721:01f7464e3e0d51e9caa8f881556afaf22f299ee78b6d75f59eaa8a9793a138fd5863227a"; shbts="1665455721\\05454844316525\\0541696991721:01f72034837bf1cc975c8dfdf150ba1787d3b8c1d827b00c83ba2d664d48df952a842a6a"; dpr=1.125; datr=p9ZEYyIh2rRWWQPZyqoE4-GZ; rur="EAG\\05454844316525\\0541696991796:01f71ecfa0c237bbb13cdc3bd7c1ef96d5743a0f9f90716826137625f2e29c2a3ca4b046"',
                'sec-gpc': '1',
                'user-agent': f"Mozilla/5.0 (Windows NT {random.choice(['7', '10', '11'])}.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90, 105)}.0.0.0 Safari/537.36",
                'x-csrftoken': self.csrftoken,
        }
        try:
            post = requests.get("https://www.instagram.com/", headers=self.headers).text
            self.idProfile = post.split('''"viewerId":"''')[1].split('"}')[0]
            self.ajax = post.split('''rollout_hash":"''')[1].split('",')[0]
            self.appId = post.split('''"appId":"''')[1].split('","')[0]
            self.headers = {
                'authority': 'i.instagram.com',
                'accept': '*/*',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'ig_did=7F9C005F-44C5-462B-9C83-C17F3C40C91B; ig_nrcb=1; mid=Y0TWXAALAAHVZ0CPiOlAvfTBQV2f; csrftoken=q555FDDIhmCzFFTqJg3Z9DPnn8dD0LaQ; sessionid=54844316525%3Aac8YPSzRPMLBmb%3A25%3AAYe8x5ueSQ39fNyyLrbQDcRczEqUdP_oXrUYFM8r0A; ds_user_id=54844316525; shbid="12403\\05454844316525\\0541696991721:01f7464e3e0d51e9caa8f881556afaf22f299ee78b6d75f59eaa8a9793a138fd5863227a"; shbts="1665455721\\05454844316525\\0541696991721:01f72034837bf1cc975c8dfdf150ba1787d3b8c1d827b00c83ba2d664d48df952a842a6a"; dpr=1.125; datr=p9ZEYyIh2rRWWQPZyqoE4-GZ; rur="EAG\\05454844316525\\0541696991796:01f71ecfa0c237bbb13cdc3bd7c1ef96d5743a0f9f90716826137625f2e29c2a3ca4b046"',
                'sec-gpc': '1',
                'x-requested-with': "XMLHttpRequest",
                'user-agent': f"Mozilla/5.0 (Windows NT {random.choice(['7', '10', '11'])}.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90, 105)}.0.0.0 Safari/537.36",
                'x-csrftoken': self.csrftoken,
                'x-ig-app-id': self.appId,
                'x-instagram-ajax': self.ajax,
        }
        except:
            exit()


    def followUser(self,id):
        try:
            fl = requests.post(f'https://i.instagram.com/api/v1/web/friendships/{id}/follow/', headers=self.headers).text
            if '{"result":"following","status":"ok"}' in fl:
                return True
            else:
                return False
        except:
            return False
    def unFollowUser(self,id):
        try:
            unfl = requests.post(f'https://i.instagram.com/api/v1/web/friendships/{id}/unfollow/', headers=self.headers).text
            if "ok" in unfl:
                return True
            else:
                return False
        except:
            return False
    def likePost(self,id): 
        try:
            react = requests.post(f'https://i.instagram.com/api/v1/web/likes/{id}/like/', headers=self.headers).text
            if "ok" in react:
                return True
            else:
                return False
        except:
            return False
    def likeCmt(self,id):
        try:
            reactCmt = requests.post(f'https://i.instagram.com/api/v1/web/comments/like/{id}/', headers=self.headers).text
            if "ok" in reactCmt:
                return True
            else:
                return False
        except:
            return False   
    def Cmt(self, id, noidung):
        try:
            cmt = requests.post(f'https://i.instagram.com/api/v1/web/comments/{id}/add/', headers=self.headers, data={'comment_text': noidung,}).text
            """ {"id":"17980054363665826",
                "from":{
                    "id":"54844316525",
                    "username":"lebaoduy_rabbit",
                    "full_name":"Lê Bảo Duy",},
                    "text":"hi",
                    "created_time":1665456940,
                    "status":"ok"} """
            if '"status":"ok"' in cmt:
                return True
            else:
                return False
        except:
            return False
    def UpPost_Profile(self,path):
        id = int(datetime.now().timestamp())
        upload_id = random.randint(10000, 50000) + id
        print(upload_id, id)
        url_loadImg = f"https://i.instagram.com/rupload_igphoto/fb_uploader_{upload_id}"
        hd = {
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'image/jpeg',
            'cookie': self.cookie,
            'offset': '0',
            'sec-gpc': '1',
            'user-agent': f"Mozilla/5.0 (Windows NT {random.choice(['7', '10', '11'])}.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90, 105)}.0.0.0 Safari/537.36",
            'x-requested-with': "XMLHttpRequest",
            'x-entity-length': str(os.path.getsize(path)),
            'x-entity-name': f'fb_uploader_{upload_id}',
            'x-entity-type': 'image/jpeg',
            'x-ig-app-id': self.appId,
            'x-instagram-ajax': self.ajax,
            'x-instagram-rupload-params': '{"media_type":1,"upload_id":"1665457485118","upload_media_height": 780,"upload_media_width":780}',
}   
        
        dataImg = open(path, "rb")
        requests.post(url=url_loadImg, headers=hd, data=dataImg).text