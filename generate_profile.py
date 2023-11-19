from profile import AlAreefProfile

def generate_profile():
    # Create an instance of the class
    alareef_profile = AlAreefProfile(username="nuccasjnr")

    # Generate dynamic content
    profile_content = f"""
    # Al-Areef's Profile

    ## Skills
    {', '.join(alareef_profile.skills)}

    ## GitHub Stats
    - Followers: {alareef_profile.github_stats.get('followers', 0)}
    - Following: {alareef_profile.github_stats.get('following', 0)}
    - Public Repositories: {alareef_profile.github_stats.get('public_repos', 0)}

    ## Top Languages
    {', '.join(alareef_profile.languages)}
    """

    return profile_content

if __name__ == "__main__":
    # Generate content and write it to the README.md file
    generated_content = generate_profile()

    # Read existing README content
    with open("README.md", "r") as readme_file:
        existing_content = readme_file.read()

    # Replace the dynamic content placeholder with the generated content
    updated_content = existing_content.replace("<!-- Dynamic Content Placeholder -->", generated_content)

    # Write the updated content back to the README.md file
    with open("README.md", "w") as readme_file:
        readme_file.write(updated_content)