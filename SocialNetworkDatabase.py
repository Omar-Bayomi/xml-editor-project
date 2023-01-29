import re
import numpy as np


class Topic:

    def __init__(self):
        self.name = ""

    @property
    def Name(self):
        return self.name

    @Name.setter
    def Name(self, value):
        self.name = value


class Post:
    def __init__(self):
        self.topics = []
        self.body = None

    @property
    def Body(self):
        return self.body

    @Body.setter
    def Body(self, value):
        self.body = value

    @property
    def Topics(self):
        return self.topics

    @Topics.setter
    def Topics(self, value):
        self.topics.append(value)


class User:
    def __init__(self):
        self.posts = []
        self.name = ""
        self.id = 0
        self.followers = []

    @property
    def Posts(self):
        return self.posts

    @Posts.setter
    def Posts(self, value):
        self.posts.append(value)

    @property
    def Followers(self):
        return self.followers

    @Followers.setter
    def Followers(self, value):
        self.followers.append(value)

    @property
    def Name(self):
        return self.name

    @Name.setter
    def Name(self, value):
        self.name = value

    @property
    def Id(self):
        return self.id

    @Id.setter
    def Id(self, value):
        self.id = value


class SocialNetwork:
    def __init__(self, FilePath):
        self.__users = SocialNetwork.ParseXml(FilePath)

    @property
    def Graph(self):
        return self.__users

    @staticmethod
    def ParseXml(FilePath):
        xmlstring = ""
        tags = {}
        UsersDictionary = {}

        with open(FilePath, 'r') as f:
            xmlstring = f.read()
            for tag in re.finditer("(<.[^(><.)]+>)", xmlstring):
                if tags is None:
                    break
                if tag.group() not in tags.keys():
                    tags.update({tag.group(): [tag.span()]})
                else:
                    tags[tag.group()].append(tag.span())
        f.close()

        # print(tags)
        user_id = -1
        user_name = -1
        user_posts = 0
        user_topics = 0
        user_followers = 0
        for _ in tags["<user>"]:
            user_id += 1
            user_name += 1

            (_, start) = tags["<id>"][user_id]
            (end, _) = tags["</id>"][user_id]
            (userEnd, _) = tags["</user>"][user_name]
            Id = xmlstring[start:end]
            user = None
            if Id in UsersDictionary:
                user = UsersDictionary[Id]
            else:
                user = User()
                user.id = Id
                UsersDictionary.update({user.id: user})

            (_, start) = tags["<name>"][user_name]
            (end, _) = tags["</name>"][user_name]
            name = xmlstring[start:end]
            user.name = name

            while user_posts < len(tags["<post>"]):
                (_, start) = tags["<post>"][user_posts]
                (postEnd, _) = tags["</post>"][user_posts]

                if start >= userEnd:
                    break
                (_, start) = tags["<body>"][user_posts]
                (end, _) = tags["</body>"][user_posts]
                post = Post()
                user.posts.append(post)
                post.body = xmlstring[start:end]
                while user_topics < len(tags["<post>"]):
                    (_, start) = tags["<topic>"][user_topics]
                    (end, _) = tags["</topic>"][user_topics]
                    if start >= postEnd:
                        break
                    post.topics.append(xmlstring[start:end])
                    user_topics += 1

                user_posts += 1

            while user_followers < len(tags["<follower>"]):
                (_, start) = tags["<follower>"][user_followers]
                (end, _) = tags["</follower>"][user_followers]
                if start >= userEnd:
                    break
                user_id += 1
                (_, start) = tags["<id>"][user_id]
                (end, _) = tags["</id>"][user_id]
                Id = xmlstring[start:end]
                follower = None
                if Id in UsersDictionary:
                    follower = UsersDictionary[Id]
                else:
                    follower = User()
                    follower.id = Id
                    UsersDictionary.update({follower.id: follower})
                user.followers.append(follower)
                user_followers += 1
        return UsersDictionary
