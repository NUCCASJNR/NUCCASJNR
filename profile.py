import requests  # Import necessary modules

class AlAreefProfile:
    def __init__(self, username):
        self.username = username
        self.github_stats = self.get_github_stats()
        self.languages = self.get_top_languages()
        self.skills = [
            "Python",
            "Flask",
            "JavaScript",
            "Node.js",
            "MySQL",
            "Git",
            "Bash scripting",
            "DevOps",
            "Linux",
        ]

    def get_github_stats(self):
        # Make a request to the GitHub API to fetch user stats
        response = requests.get(f"https://api.github.com/users/{self.username}")
        if response.status_code == 200:
            user_data = response.json()
            return {
                "followers": user_data["followers"],
                "following": user_data["following"],
                "public_repos": user_data["public_repos"],
            }
        else:
            print(f"Failed to fetch GitHub stats. Status code: {response.status_code}")
            return {}

    def get_top_languages(self):
        # Make a request to the GitHub API to fetch user repositories
        response = requests.get(f"https://api.github.com/users/{self.username}/repos")
        if response.status_code == 200:
            repos = response.json()
            languages = {}
            for repo in repos:
                lang = repo["language"]
                if lang:
                    languages[lang] = languages.get(lang, 0) + 1

            # Sort languages by usage count and take the top 5
            top_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)[:5]
            return [lang[0] for lang in top_languages]
        else:
            print(f"Failed to fetch GitHub repositories. Status code: {response.status_code}")
            return []


    def greet(self):
        print(f"Hello, I'm {self.username}!")

    def display_skills(self):
        print("My skills include:")
        for skill in self.skills:
            print(f"- {skill}")

    def display_github_stats(self):
        print("My GitHub stats:")
        # Display GitHub stats here using self.github_stats

    def display_top_languages(self):
        print("My top programming languages:")
        for language in self.languages:
            print(f"- {language}")
