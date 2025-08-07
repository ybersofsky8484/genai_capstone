import subprocess
import sys

'''
Usage: python git_auto_push.py "Description of changes applied"
'''
def git_commit_and_push(commit_message="Update project files"):
    try:
        # Stage all changes
        subprocess.run(["git", "add", "."], check=True)

        # Commit changes
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        # Push to remote (main branch)
        subprocess.run(["git", "push", "origin", "main"], check=True)

        print("Changes committed and pushed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    msg = sys.argv[1] if len(sys.argv) > 1 else "Update project files"
    git_commit_and_push(msg)

