git filter-branch -f --commit-filter '
        if [ "$GIT_COMMITTER_NAME" = "relh" ] || [ "$GIT_COMMITTER_NAME" = "Richard Higgins" ] || [ "$GIT_COMMITTER_NAME" = "Ubuntu" ];
        then
                GIT_COMMITTER_NAME="relh";
                GIT_AUTHOR_NAME="relh";
                GIT_COMMITTER_EMAIL="richard@relh.net";
                GIT_AUTHOR_EMAIL="richard@relh.net";
                git commit-tree "$@";
        else
                git commit-tree "$@";
        fi' HEAD
